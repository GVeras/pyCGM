import numpy as np


# default amount of markers (5)
example0 = np.array([[[0, 1, 2], [10, 10, 10], [8, 8, 8], [5, 5, 5], [5, 5, 5]],
                     [[3, 4, 5], [9, 9, 9], [7, 7, 7], [4, 4, 4], [4, 4, 4]],
                     [[6, 7, 8], [8, 8, 8], [6, 6, 6], [3, 3, 3], [3, 3, 3]],
                     [[5, 6, 7], [8, 8, 8], [4, 4, 4], [2, 2, 2], [2, 2, 2]],
                     [[4, 5, 6], [8, 8, 8], [2, 2, 2], [0, 0, 0], [0, 0, 0]]])
ex0markers = "PELV RHIP LHIP RKNE LKNE".split()

# one more marker
# mechanism that changes number of markers stored is responsibility of IO
example1 = np.array([[[0, 1, 2], [10, 10, 10], [8, 8, 8], [5, 5, 5], [5, 5, 5], [0, 0, 0]],
                     [[3, 4, 5], [9, 9, 9], [7, 7, 7], [4, 4, 4], [4, 4, 4], [2, 2, 2]],
                     [[6, 7, 8], [8, 8, 8], [6, 6, 6], [3, 3, 3], [3, 3, 3], [4, 4, 4]],
                     [[5, 6, 7], [8, 8, 8], [4, 4, 4], [2, 2, 2], [2, 2, 2], [7, 7, 7]],
                     [[4, 5, 6], [8, 8, 8], [2, 2, 2], [0, 0, 0], [0, 0, 0], [9, 9, 9]]])
ex1markers = "PELV RHIP LHIP RKNE LKNE RANK".split()

# multiple different marker names
example2 = example0
ex2markers = "PELVIS RIGHTHIP LEFTHIP RIGHTKNEE LEFTKNEE".split()

# extra marker with partial renames
example3 = example1
ex3markers = "PELVIS RHIP LHIP RKNEE LKNEE RANK".split()

trials = [(example0, ex0markers), (example1, ex1markers), (example2, ex2markers), (example3, ex3markers),
          (example0, ex0markers), (example0, ex0markers)]
