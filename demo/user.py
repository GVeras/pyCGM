from pycgm import *
import time 

# Demonstrates basic case with no customization

if __name__ == "__main__":
    subject0 = CGM(trial=0)
    subject0.run()
    print("Trial 0 pelvis angles at each frame with no modification\n", subject0.pelvis_angles, "\n")

