import unittest
import pyCGM_Single.pycgmKinetics as pycgmKinetics
import numpy as np

rounding_precision = 8

class TestKinetics(unittest.TestCase):
    def testf(self):
        accuracyTests=[
            ([0,0],0),
            ([1,2],10),
            ([1,2,3,4,5],10),
            (np.array([1,2,3,4,5]),10),
            (np.array([142.10231243,23.40231521]),10),
            (np.array([-142.10231243,-23.40231521]),-10.421312),
            (np.array([0.10231243,3.40231521]),0.421312),
            (np.array([0.10231243,-3.40231521]),-0.421312),
            (np.array([-0.10231243,3.40231521]),-0.421312),
            (np.array([-0.10231243,-3.40231521]),-0.421312),
            (np.array([-0.10231243,-3.40231521,-8.10231243,-5.40231521,1]),-0.421312)
        ]
        accuracyResults=[
            0,
            12,
            12,
            12,
            1444.42543951,
            1457.49021854,
            3.44542066,
            -3.44542066,
            3.44542066,
            -3.35920975,
            -3.35920975
        ]
        for i in range(len(accuracyTests)):
            result = pycgmKinetics.f(accuracyTests[i][0],accuracyTests[i][1])
            expected = accuracyResults[i]
            np.testing.assert_almost_equal(result, expected, rounding_precision)

        self.assertFalse(pycgmKinetics.f([1,2], 2) == 10)
        
        exceptionTests=[([1],2), ([],2), ([1,2]), (2), ([]), ([1,2], "a"), (["a","b"], "c")]
        for e in exceptionTests:
            with self.assertRaises(Exception):
                pycgmKinetics.f(e[0],e[1])

    def testDot(self):
        accuracyTests=[
            ([0,0,0],[3,4,5]),
            ([1,2,3],[4,5,6]),
            ([1,2,3],[-4,-5,-6]),
            (np.array([1,2,3]),np.array([4,5,6])),
            (np.array([0.1,0.2,0.3]),np.array([4,5,6])),
            (np.array([240.92318213,160.32949124,429.2941023]),np.array([204.2931024,20.20142134,1.4293544])),
            ([366.87249488, 972.25566446, 519.54469762], [318.87916021, 624.44837115, 173.28031049]),
            ([143.73405485, 253.65432719, 497.53480618], [607.58442024, -836.1222914, 747.91240563]),
            ([918.86076151, 92.04884656, 568.38140393], [-186.24219938, -724.27298992, -155.58515366]),
            ([467.7365042, -788.74773579, 500.33205429], [649.06495926, 310.14934252, 853.05203014])
        ]
        accuracyResults=[
            0,
            32,
            -32,
            32,
            3.2,
            53071.44133720,
            814138.32560191,
            247356.98888589,
            -326230.85053223,
            485771.05802978
        ]
        for i in range(len(accuracyTests)):
            result = pycgmKinetics.dot(accuracyTests[i][0],accuracyTests[i][1])
            expected = accuracyResults[i]
            np.testing.assert_almost_equal(result, expected, rounding_precision)
        
        self.assertFalse(pycgmKinetics.dot([0,0,0],[3,4,5]) != 0)

        exceptionTests=[([]), ([1,2,3],[4,5]), ([],[]), ([1,2],[4,5,6]), ([1,2,"c"],[4,5,6]), (["a","b","c"], ["e","f","g"])]
        for e in exceptionTests:
            with self.assertRaises(Exception):
                pycgmKinetics.dot(e[0],e[1])

    def testLength(self):
        accuracyTests=[
            ([0,0,0]),
            ([1,2,3]),
            ([1.1,2.2,3.3]),
            (np.array([1.1,2.2,3.3])),
            (np.array([-1.1,-2.2,-3.3])),
            (np.array([4.1,-5.2,6.3])),
            (np.array([20.1,-0.2,0])),
            (np.array([477.96370143, -997.67255536, 400.99490597])),
            (np.array([330.80492334, 608.46071522, 451.3237226])),
            (np.array([-256.41091237, 391.85451166, 679.8028365])),
            (np.array([197.08510663, 319.00331132, -195.89839035])),
            (np.array([910.42721331, 184.76837848, -67.24503815])),
            (np.array([313.91884245, -703.86347965, -831.19994848])),
            (np.array([710.57698646, 991.83524562, 781.3712082]))
        ]
        accuracyResults=[
            0.0,
            3.74165738,
            4.11582312,
            4.11582312,
            4.11582312,
            9.14002188,
            20.10099500,
            1176.68888930,
            826.64952782,
            825.486772034,
            423.06244365,
            931.41771487,
            1133.51761873,
            1448.86085361
        ]
        for i in range(len(accuracyTests)):
            result = pycgmKinetics.length(accuracyTests[i])
            expected = accuracyResults[i]
            np.testing.assert_almost_equal(result, expected, rounding_precision)
        
        self.assertFalse(pycgmKinetics.length([0,0,0]) != 0.0)

        exceptionTests=[([]), ([1]), ([1,2]), ([1,2,"c"]), (["a","b",3])]
        for e in exceptionTests:
            with self.assertRaises(Exception):
                pycgmKinetics.length(e[0])
    
    def testVector(self):
        accuracyTests=[
            ([0,0,0],[1,2,3]),
            ([1,2,3],[1,2,3]),
            ([1,2,3],[4,5,6]),
            ([-1,-2,-3],[4,5,6]),
            ([-1.1,-2.2,-3.3],[4.4,5.5,6]),
            (np.array([-1,-2,-3]),np.array([4,5,6])),
            (np.array([871.13796878, 80.07048505, 81.7226316]), np.array([150.60899971, 439.55690306, -746.27742664])),
            (np.array([109.96296398, 278.68529143, 224.18342906]), np.array([28.90044238, -332.38141918, 625.15884162])),
            (np.array([261.89862662, 635.64883561, 335.23199233]), np.array([462.68440338, 329.95040901, 260.75626459])),
            (np.array([-822.76892296, -457.04755227, 64.67044766]), np.array([883.37510574, 599.45910665, 94.24813625])),
            (np.array([-723.03974742, -913.26790889, 95.50575378]), np.array([-322.89139623, 175.08781892, -954.38748492])),
            (np.array([602.28250216, 868.53946449, 666.82151334]), np.array([741.07723854, -37.57504097, 321.13189537])),
            (np.array([646.40999378, -633.96507365, -33.52275607]), np.array([479.73019807, 923.99114103, 2.18614984])),
            (np.array([647.8991296, 223.85365454, 954.78426745]), np.array([-547.48178332, 93.92166408, -809.79295556]))
        ]
        accuracyResults=[
            ([1,2,3]),
            ([0,0,0]),
            ([3,3,3]),
            ([5,7,9]),
            ([5.5, 7.7, 9.3]),
            ([5,7,9]),
            ([-720.52896907,  359.48641801, -828.00005824]),
            ([-81.0625216 , -611.06671061,  400.97541256]),
            ([200.78577676, -305.6984266 ,  -74.47572774]),
            ([1706.1440287 , 1056.50665892, 29.57768859]),
            ([400.14835119,  1088.35572781, -1049.8932387 ]),
            ([138.79473638, -906.11450546, -345.68961797]),
            ([-166.67979571, 1557.95621468, 35.70890591]),
            ([-1195.38091292, -129.93199046, -1764.57722301])
        ]
        for i in range(len(accuracyTests)):
            result = pycgmKinetics.vector(accuracyTests[i][0],accuracyTests[i][1])
            expected = accuracyResults[i]
            np.testing.assert_almost_equal(result, expected, rounding_precision)

        self.assertFalse(pycgmKinetics.vector([1,2,3],[4,5,6]) != (3,3,3))

        exceptionTests=[([]), ([],[]), ([1,2,3],[4,5]), ([1,2],[4,5,6]), (["a",2,3],[4,5,6])]
        for e in exceptionTests:
            with self.assertRaises(Exception):
                pycgmKinetics.vector(e[0])

    def testUnit(self):
        accuracyTests=[
            ([1,1,1]),
            ([1,2,3]),
            ([1.1,2.2,3.3]),
            (np.array([1.1,2.2,3.3])),
            (np.array([-1.1,-2.2,-3.3])),
            (np.array([4.1,-5.2,6.3])),
            (np.array([20.1,-0.2,0])),
            (np.array([477.96370143, -997.67255536, 400.99490597])),
            (np.array([330.80492334, 608.46071522, 451.3237226])),
            (np.array([-256.41091237, 391.85451166, 679.8028365])),
            (np.array([197.08510663, 319.00331132, -195.89839035])),
            (np.array([910.42721331, 184.76837848, -67.24503815])),
            (np.array([313.91884245, -703.86347965, -831.19994848])),
            (np.array([710.57698646, 991.83524562, 781.3712082]))
        ]
        accuracyResults=[
            ([0.57735027, 0.57735027, 0.57735027]),
            ([0.26726124, 0.53452248, 0.80178373]),
            ([0.26726124, 0.53452248, 0.80178373]),
            ([0.26726124, 0.53452248, 0.80178373]),
            ([-0.26726124, -0.53452248, -0.80178373]),
            ([ 0.44857661, -0.56892643,  0.68927625]),
            ([ 0.9999505 , -0.00994976,  0.00000001]),
            ([ 0.40619377, -0.84786435,  0.34078244]),
            ([0.40017554, 0.73605645, 0.54596744]),
            ([-0.31061783,  0.47469508,  0.82351754]),
            ([ 0.46585347,  0.75403363, -0.46304841]),
            ([ 0.97746392,  0.19837327, -0.07219643]),
            ([ 0.27694218, -0.62095504, -0.73329248]),
            ([0.49043839, 0.68456211, 0.53930038])
        ]
        for i in range(len(accuracyTests)):
            result = pycgmKinetics.unit(accuracyTests[i])
            expected = accuracyResults[i]
            np.testing.assert_almost_equal(result, expected, rounding_precision)

        exceptionTests=[([]), ([1]), ([1,2]), ([1,2,"c"]), (["a","b",3])]
        for e in exceptionTests:
            with self.assertRaises(Exception):
                pycgmKinetics.unit(e[0])
