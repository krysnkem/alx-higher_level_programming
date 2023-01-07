#!/usr/bin/python3
for M in range(0, 8):
    for N in range(0, 10):
        if N <= M:
            continue
        print("{}{}".format(M, N), end=", ")
print(89)
