from unittest import TestCase
import pytest
import pyCGM_Single.pycgmStatic as pycgmStatic
import numpy as np
import os

rounding_precision = 8

class Test_pycgmStatic_UpperBody(TestCase):
    """
    This class tests the coverage of all the lower body functions in pycgmStatic.py.
    """
    def test_headoffCalc(self):
        """
        This test provides coverage of the headoffCalc function in pycgmStatic.py,
        defined as headoffCalc(axisP, axisD), where axisP represents the 
        position of the proximal axis and axisD represents the position of the distal
        axis. Both are 3x3 lists.

        Each index in accuracyTests is used as parameters for the function headoffCalc 
        and the result is then checked to be equal with the same index in 
        accuracyResults using 8 decimal point precision comparison.
        """
        # Test the following cases: lists, numpy arrays, floats, and negative values.
        accuracyTests=[]

        axisP = [[0.18560279, 0.0315192, 0.09194304], np.array([-0.1651286, 0.48197341, -0.89334102]), [0.42118631, 0.44566058, 0.3685976]]
        axisD = [np.array([0.93833978, 0.53494403, 0.28153401]), [0.5948737, 0.45679797, 0.59007101], [0.41493765, -0.31543255, 0.53007426]]
        accuracyTests.append((axisP,axisD))

        axisP = [[-0.55032734, 0.25267946, 0.82540112], [0.84009478, 0.73715195, 0.20206328], [0.77226627, -0.76252519, 0.67441226]]
        axisD = [np.array([0.97433339, 0.73549566, -0.94843216]), np.array([0.01288564, 0.06751503, 0.09013066]), np.array([0.2225316, -0.62467846, 0.06837276])]
        accuracyTests.append((axisP,axisD))

        axisP = [[-0.30408101, 0.70062712, -0.42611435], np.array([0.54387147, -0.05276455, 0.1003203]), [0.85617289, -0.29502885, 0.62815308]]
        axisD = [[-0.91401951, 0.23435732, -0.58043682], [0.07793386, 0.94936247, 0.2530925], [0.83692574, 0.35039923, 0.32052456]]
        accuracyTests.append((axisP,axisD))

        axisP = [[8.32917259, 9.58920789, -3.13295098], [8.3806542, 6.39064471, 1.30397279], [5.2825194, 3.53266395, 2.29415691]]
        axisD = [[-0.71052732, 3.59469381, 9.54697609], [-4.60401137, -3.59406754, 0.47846057], [8.47980655, 2.0503102, 5.73192244]]
        accuracyTests.append((axisP,axisD))

        axisP = [[7.21963359, 9.20287597, 0.07500897], np.array([6.88917649, 9.76746551, 1.79033317]), [9.0332691, 3.5445209, 2.28758474]]
        axisD = [[14.70068748, -37.01360567, 62.95212593], [35.31793645, 44.96281688, 58.23024786], [48.30129467, -35.1597873, 18.06703122]]
        accuracyTests.append((axisP,axisD))

        axisP = [[59.52660864, 71.77247382, -3.76175508], [53.75640621, 15.84017578, 79.9918092], [-47.81776965, 88.44436408, 99.19775002]]
        axisD = [[7.2812784, 44.01016741, 77.01874928], [97.52423496, 78.17944915, 95.5606174], np.array([23.14115906, 41.90092584, -50.58812772])]
        accuracyTests.append((axisP,axisD))
        
        axisP = [np.array([-0.67932973, -0.14011356, -0.27340921]), np.array([-0.22042642, 0.07653077, 0.46128554]), [0.12396834, 0.0391548, 0.5067273]]
        axisD = [[-0.19601928, -0.30645399, 0.40226696], [-0.23806927, 0.69430281, -0.17296611], [0.20712497, 0.63414787, 0.16593221]]
        accuracyTests.append((axisP,axisD))

        axisP = [[86.14908044, 46.21168176, 34.87558559], [-18.93240546, 44.42916607, 12.48682341], [43.48770525, 17.98549489, 4.78518285]]
        axisD = [[49.97178315, 23.06136542, 87.12541747], [4.75745064, 3.91045307, -41.8781886], [-47.25427441, 93.55474812, 6.13684817]]
        accuracyTests.append((axisP,axisD))

        axisP = [np.array([-30.02589893, -58.74691723, -46.59534683]), np.array([-61.59201266, 96.76266307, 0.48738339]), [63.98728033, 93.11965068, 60.87770796]]
        axisD = [[406.95480187, 872.74236975, 245.30758801], [598.03316806, 292.36367673, 292.4500129], [692.53856323, 291.79167259, 688.90009713]]
        accuracyTests.append((axisP,axisD))

        axisP = [[429.72833747, 819.91705305, -739.55124153], [734.65227412, -11.15110022, 7.91987428], [263.7479073, 124.5058704, 67.08837605]]
        axisD = [np.array([-464.41470532, -291.71959629, 847.81720649]), [99.1311952, -27.47766766, 514.44507114], [223.75267828, -215.4478294, 712.133009]]
        accuracyTests.append((axisP,axisD))

        accuracyResults=[
            -0.96092622,
            -0.75923143,
            -0.68703969,
            -1.46490390,
            0.70984326,
            -1.38886056,
            -0.57665209,
            -1.30443978,
            -1.37275643,
            0.84429843
        ]

        for i in range(len(accuracyTests)):
            # Call headoffCalc(axisP, axisD) with the variables given from each accuracyTests index.
            result = pycgmStatic.headoffCalc(accuracyTests[i][0],accuracyTests[i][1])
            expected = accuracyResults[i]
            np.testing.assert_almost_equal(result, expected, rounding_precision)