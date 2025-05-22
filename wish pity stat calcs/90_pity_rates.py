import time
import numba
import numpy as np

charRates = [0.0, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.066, 0.126, 0.186, 0.246, 0.306, 0.366, 0.426, 0.486, 0.546, 0.606, 0.666, 0.726, 0.786, 0.846, 0.906, 0.966, 1.026]
weapRates = [0.0, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.077, 0.147, 0.217, 0.287, 0.357, 0.427, 0.497, 0.567, 0.637, 0.707, 0.777, 0.847, 0.917, 0.987, 1.057, 1.127, 1.197, 1.267]
rates = np.array(charRates)
hardPityPlusOne = 91

@numba.njit
def main(wishCount: int, debug: bool = False) -> np.array:
    tenPercent = wishCount // 10
    pityCounts: np.ndarray[int] = np.full(hardPityPlusOne, 0, dtype=numba.types.int64)
    timesCounted: np.ndarray[int] = np.full(hardPityPlusOne, 0, dtype=numba.types.int64)
    
    pity = 0
    if not debug: print("0%")
    for i in range(1, wishCount+1):
        if (i%tenPercent == 0 and not debug): print(f"{i//tenPercent*10}%")
        pity += 1
        timesCounted[pity] += 1
        if np.random.rand() < rates[pity]:
            pityCounts[pity] += 1
            pity = 0
            
    return pityCounts, timesCounted

def analyze(pulls, counts, timeTaken):
    for i in range(hardPityPlusOne):
        print(f"{i:<2}: {pulls[i]:<8} | rate: {pulls[i]/counts[i]*100:.2f}%")
    print(f"\nTime taken: {timeTaken}s")
    print(f"Total 5* pulls: {sum(pulls)}")
    print("5* pulls:")
    print(pulls)
    print("Rolls per pity:")
    print(counts)

def runMain(wishCount: int) -> None:
    startTime: float = time.perf_counter()
    pulls, counts = main(wishCount)
    endTime: float = time.perf_counter()
    timeTaken = f"{endTime-startTime:.3f}"
    analyze(pulls, counts, timeTaken)

if __name__ == "__main__":
    main(10, True) # trivially small calc just to compile the function
    # runMain(5000)
    runMain(50*10**9)
