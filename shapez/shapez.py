import time
import numba
import numpy as np
import math

@numba.njit
def make_all_rotations(num: int, N: int, L: int) -> np.ndarray[int]:
    ans: np.ndarray[int] = np.zeros(L, dtype=numba.types.int64)
    ans[0] = num
    splitter: int = N**(L-1)
    for i in range(1, L):
        div, mod = divmod(ans[i-1], splitter)
        ans[i] = mod * N + div
    
    return ans

@numba.njit
def main(N: int, L: int) -> int:
    length = N**L
    checkAll: np.ndarray[bool] = np.full(length, False, dtype=bool)
    total: int = -1
    
    for i in range(length):
        if checkAll[i]: continue
        for j in make_all_rotations(i, N, L):
            checkAll[j] = True
        total += 1
    
    return total

def runMain(N: int, L: int) -> int:
    print(f"Calculating how many unique 1-layer shapes there are with {N} shapes and {L} quadrants in the layer.")
    startTime: float = time.perf_counter()
    t = main(N, L)
    endTime: float = time.perf_counter()
    print("Total unique shapes:", t)
    print(f"Time taken: {endTime-startTime:.3f}s")

# The pure math solution finishes in 5e-6 seconds
def pureMath(N: int, L: int):
    count = -1
    for i in range(L):
        gcd = math.gcd(i, L)
        count += pow(N, gcd)
    return count // L

if __name__ == "__main__":
    main(1, 1) # trivially small calc just to compile the function
    runMain(41, 4) # 0.07s of calc time
