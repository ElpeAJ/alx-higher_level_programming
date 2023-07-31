#!/usr/bin/python3

def magic_calculation(a, b):
    answer = 0
    for i in range(1, 3, 1):
        try:
            if (i <= a):
                answer += (a ** b) / i
            else:
                raise Exception("Too far")
        except Exception:
            answer = b + a
    return (answer)
