import numpy as np
from demo.IO import trials


class CGM:

    def __init__(self):
        self.all_angles = None
        self.all_axes = None
        self.mapping = {"PELV": "PELV", "RHIP": "RHIP", "LHIP": "LHIP", "RKNE": "RKNE", "LKNE": "LKNE"}
        self.marker_index = {}
        self.output_index = {"Pelvis": 0, "Hip": 1, "Knee": 2}

    def run(self, trial):
        data, markers = trials[trial]  # Substitute for loading in data from c3d

        # Associate each marker name with its index
        for i, marker in enumerate(markers):
            self.marker_index[marker] = i

        result = calc(data,
                      (self.pelvis_calc, self.hip_calc, self.knee_calc),
                      (self.mapping, self.marker_index, self.output_index))
        self.all_angles = result

    def map(self, old=None, new=None, dic=None):
        if dic and type(dic) == dict:  # Entire dictionary given
            self.mapping.update(dic)
            return
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
    def pelvis_calc(frame, mapping, mi):
        return frame[mi[mapping["PELV"]]]

    @staticmethod
    def hip_calc(frame, mapping, mi):
        return np.mean(np.array([frame[mi[mapping["RHIP"]]], frame[mi[mapping["LHIP"]]]]), axis=0)

    @staticmethod
    def knee_calc(frame, mapping, mi, i, oi, result):
        result[i][oi["Knee"]] = frame[mi[mapping["RKNE"]]] - frame[mi[mapping["LKNE"]]]


def calc(data, methods, mappings):
    pel, hip, kne = methods
    mmap, mi, oi = mappings

    result = np.zeros((len(data), len(mi), 3), dtype=int)

    # TODO: Current issue - no way for user to modify what is written to output
    for i, frame in enumerate(data):
        result[i][oi["Pelvis"]] = pel(frame, mmap, mi)
        result[i][oi["Hip"]] = hip(frame, mmap, mi)
        kne(frame, mmap, mi, i, oi, result)
    return result
