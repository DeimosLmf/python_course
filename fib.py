import sys

def recurtion(a):
    #print(a)
    if a > 2:
        return recurtion(a - 1) + recurtion(a - 2)
    else:
        return 1

n = int(sys.argv[1])
print(recurtion(n))