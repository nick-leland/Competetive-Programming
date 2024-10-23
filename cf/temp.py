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

test_cases = int(lines[0])
cases = lines[1:]

result = []
    
for iterations in range(0, len(cases)-1, 2):
    line1 = (cases[iterations])
    line1 = line1.split(" ")


    line2 = (cases[iterations + 1])
    line2 = line2.split(" ")
    
    print()
