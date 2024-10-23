import sys
lines = [line.strip() for line in sys.stdin.readlines()]

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

    
for iterations in range(int(lines[0])):
    print(lines[1 + iterations])
    print(lines[2 + iterations])
    print()
