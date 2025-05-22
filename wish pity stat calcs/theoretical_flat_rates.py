import numba
import numpy as np
import time

GREEN = "\033[42m"
RESET = "\033[0m"
MIN_THRESHOLD = 70
MAX_THRESHOLD = 80
MIN_RATE = 20
MAX_RATE = 40
TABLE_WIDTH = 7

@numba.njit
def test_rates(threshold: int, rate = .3, cycles = 200_000, base = 0.006) -> float:
    pity_sum = 0
    for _ in range(cycles):
        for pity in range(1, 90):
            roll = np.random.rand()
            if pity >= threshold:
                if roll <= rate:
                    pity_sum += pity
                    break
            if roll <= base:
                pity_sum += pity
                break
        else:
            pity_sum += 90
     # pity_sum / cycles = average_pity.
     # 1/average_pity = average_rate.
     # 1/pity_sum/cycles -> cycles/pity_sum
    return np.round(cycles/pity_sum, 4)

test_rates(1, 1) # numba compiilation

def data_row(rate: int) -> list[float]:
    return [test_rates(x, rate/100) for x in range(MIN_THRESHOLD, MAX_THRESHOLD+1)]

def table_header() -> None:
    header = ' '*7
    for pity in range(MIN_THRESHOLD, MAX_THRESHOLD+1):
        header += f"{pity:^{TABLE_WIDTH}}"
    print(header)
    print('-'*7*(MAX_THRESHOLD-MIN_THRESHOLD+2))

def table_entry(rate: float) -> str:
    flag = False
    output = round(rate*100, 2)
    if 1.59 <= output <= 1.61: flag = True

    output = str(output)+'%'
    center_delta = TABLE_WIDTH-len(output)
    if flag: output = GREEN+output+RESET
    
    return f"{output:^{len(output)+center_delta}}"

def make_table(data: list[list[float]]) -> None:
    table_header()
    for row_num in range(len(data)):
        row = f"{str(row_num+MIN_RATE)+'% |':^{TABLE_WIDTH}}"
        for rate in data[row_num]:
            row += table_entry(rate)
        print(row)

if __name__ == "__main__":
    start = time.time()
    rate_array = [data_row(x) for x in range(MIN_RATE, MAX_RATE+1)]
    end = time.time()
    print(f"data generated in {round(end-start, 2)}s")
    make_table(rate_array)
