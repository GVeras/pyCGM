import numpy as np
import IO
import multiprocessing as mp
import mmap
import json
import tempfile 
import errno 
import os 
import math 



class CGM:

    def __init__(self, static_path=None, dynamic_path=None, vsk_path=None, trial=0, ncores = 1):
        self.static_path = static_path
        self.dynamic_path = dynamic_path
        self.vsk_path = vsk_path
        self.trial = trial
        self.ncores = ncores
        self.all_angles = None
        self.all_axes = None
        self.offsets = None
        self.mapping = {"PELV": "PELV", "RHIP": "RHIP", "LHIP": "LHIP", "RKNE": "RKNE", "LKNE": "LKNE"}
        self.marker_index = {}
        self.output_index = {"Pelvis": 0, "Hip": 1, "Knee": 2}

    def run(self, static=None):
        data, markers = IO.trials[self.trial]  # Substitute for loading in data from c3d

        # Associate each marker name with its index
        for i, marker in enumerate(markers):
            self.marker_index[marker] = i

        if not static:
            static = StaticCGM(self.static_path, self.vsk_path)

        result = self.multiCalc(data,
                           (self.pelvis_calc, self.hip_calc, self.knee_calc),
                           (self.mapping, self.marker_index, self.output_index),
                           self.ncores)
        self.all_angles = result

    def map(self, old=None, new=None, dic=None):
        if dic and type(dic) == dict:  # Entire dictionary given
            self.mapping.update(dic)
            return
        # TODO: Potential issue if 'new' is an existing marker that CGM expects, unless all
        # instances that use it are overridden
        if old and new:  # Old and new marker name provided
            self.mapping[old] = new
            self.mapping[new] = new
        elif old and not new:  # Only one marker name provided
            self.mapping[old] = old  # Interpret it as adding a new marker

    @property
    def pelvis_angles(self):
        return self.all_angles[0:, self.output_index["Pelvis"]]

    @property
    def hip_angles(self):
        return self.all_angles[0:, self.output_index["Hip"]]

    @property
    def knee_angles(self):
        return self.all_angles[0:, self.output_index["Knee"]]

    @staticmethod
    def pelvis_calc(pelv):
        return pelv

    @staticmethod
    def hip_calc(rhip, lhip):
        return np.mean(np.array([rhip, lhip]), axis=0)

    @staticmethod
    def knee_calc(rkne, lkne):
        return rkne - lkne
    
    @staticmethod
    def calc(data, result):
        info = IO.readMem()
        pel, hip, kne = info['methods']
        mmap, mi, oi = info['mappings']

        for i, frame in enumerate(data):
            pelv = frame[mi[mmap["PELV"]]]
            result[i][oi["Pelvis"]] = pel(pelv)
            rhip = frame[mi[mmap["RHIP"]]]
            lhip = frame[mi[mmap["LHIP"]]]
            result[i][oi["Hip"]] = hip(rhip, lhip)
            rkne = frame[mi[mmap["RKNE"]]]
            lkne = frame[mi[mmap["LKNE"]]]
            result[i][oi["Knee"]] = kne(rkne, lkne)

    @staticmethod
    #Could also have VSK, offset, start, and end here. 
    def multiCalc(data, methods, mappings, ncores):
        # mechanism responsible for changing size of output array
        result = np.zeros((len(data), len(mappings[2]), 3), dtype=int)

        # Data in this case would be changed upon furhter implementation.
        print(len(data))
        length = int(len(data)/ncores)

        # Hold all the processes together for asynchronize running and joining
        processes = []
        IO.writeMem(methods, mappings)

        for c in range(ncores):
            first = c * length
            last = (c+1) * length

            if c == ncores - 1:
                last = len(data)

            proc = mp.Process(target=CGM.calc, args=[data, result])
            proc.start()
            processes.append(proc)

        for process in processes:
            process.join()
        
        return result
            


class StaticCGM:

    def __init__(self, static_path, vsk_path):
        self.static_path = static_path
        self.vsk_path = vsk_path
        # In reality, measurements would be determined with appropriate functions
        self._measurements = {"MeanLegLength": 940.0, "RightKneeWidth": 105.0, "LeftKneeWidth": 105.0}

    @property
    def measurements(self):
        # Equivalent of getStatic
        return self._measurements

    @staticmethod
    def pelvis_calc_static(pelv):
        return pelv

    @staticmethod
    def hip_calc_static(rhip, lhip):
        return np.mean(np.array([rhip, lhip]), axis=0)

    @staticmethod
    def knee_calc_static(rkne, lkne):
        return rkne - lkne
