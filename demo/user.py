from pycgm import *
import time 

# Demonstrates basic case with no customization

if __name__ == "__main__":
    for x in range(1,9):
        subject0 = CGM(trial=0, ncores=x)
        start = time.time()
        subject0.run()
        end = time.time()

        print(f"Time elapsed using {x} core(s): {end-start}")
