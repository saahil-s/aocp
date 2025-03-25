# Algorithm to find the greatest common divisor between two numbers

# The process is as follows:

#   E0: [Ensure that m >= n.]   If m < n, then exchange m and n.
#   E1: [Find remainder]        Divide m by n and let r be the remainder.
#   E2: [Is it zero?]           If r = 0, the algorithm terminates and n is the answer.
#   E3: [Reduce]                Set m <-- n, n <-- r, and go back to step E1.

def swap(m, n):
    temp = m
    m = n
    n = temp
    return m, n


def findGCD(m, n):
    # E0
    if (m < n):
        swap(m, n)
    # E1
    r = m % n

    # E2 and E3
    while(r != 0):    
        m = n
        n = r
        r = m % n
    return n

print(findGCD(300, 400))