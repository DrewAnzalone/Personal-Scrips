import time

# VERSION 1 -----------------------------
# def make_min(string):
#     rotations = [string]
#     rotations += [string[i:]+string[:i] for i in range(1, 4)]
#     return min(rotations)

# def make_min(string):
#     minn = string
#     for i in range(1, 4):
#         if (newMin := string[i:]+string[:i]) < minn:
#             minn = newMin
#     return minn

# def make_min(string):
#     minn = string
#     for i in range(1, 4):
#         newMin = string[i:]+string[:i]
#         if newMin < minn:
#             minn = newMin
#     return minn

# def make_min(s):
#     """Booth's algorithm to find the lexicographically smallest string rotation."""
#     s = s + s  # Concatenate string to itself to avoid modular arithmetic
#     f = [-1] * len(s)  # Failure function
#     k = 0  # Least rotation of string found so far

#     for j in range(1, len(s)):
#         sj = s[j]
#         i = f[j - k - 1]
#         while i != -1 and sj != s[k + i + 1]:
#             if sj < s[k + i + 1]:
#                 k = j - i - 1
#             i = f[i]
#         if sj != s[k + i + 1]:  # if sj != s[k+i+1], then i == -1
#             if sj < s[k]:  # k+i+1 = k
#                 k = j
#             f[j - k] = -1
#         else:
#             f[j - k] = i + 1

#     return s[k:k + len(s) // 2]

def make_min(string):
    rotations = [string, None, None, None]
    for i in range(1, 4):
        rotations[i] = string[i:]+string[:i]
    return min(rotations)

if __name__ == "__main__":
    result = set()
    b41 = ")*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQ"
    
    timeStart = time.time()
    for a in b41:
      for b in b41:
        for c in b41:
          for d in b41:
            combo = a+b+c+d
            result.add(make_min(combo))
    timeEnd = time.time()

    print(len(result)-1)
    print(f"Time: {timeEnd-timeStart:.2f}s") # 4.3 to 2.4s of calc time

#Version 1 End -------------------------
#Version 2 -----------------------------

N = 41
L = 4
shifter = pow(N, L-1)
total = pow(N, L)

def o_result_mem():
    def rot(val):
        values = [None] * L
        values[0] = val
        for i in range(1, L): 
            res = (values[i-1]%N) * shifter
            values[i] = int(values[i-1]/N + res)
        return min(values)

    found = set()
    for i in range(total):
        found.add(rot(i))
    return len(found) - 1

if __name__ == "__main__":
    timeStart = time.time()
    t = o_result_mem()
    timeEnd = time.time()
    print(t)
    print(f"Time: {timeEnd-timeStart:.2f}s") # 2.3s of calc time

#Version 2 End -------------------------
#Version 3 -----------------------------

def o_total_mem():
    def rot(val):
        res = (val%N) * shifter
        return int(val/N + res)

    found = [False] * total
    count = -1
    for i in range(total):
        if found[i]:
            continue
        count += 1
        found[i] = True
        j = i
        while (j := rot(j)) != i:
            found[j] = True

    return count

if __name__ == "__main__":
    timeStart = time.time()
    t = o_total_mem()
    timeEnd = time.time()
    print(t)
    print(f"Time: {timeEnd-timeStart:.2f}s") # 0.7s of calc time

#Version 3 End -------------------------
