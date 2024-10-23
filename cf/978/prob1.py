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
    n = int(line1[0])
    r = int(line1[1])
    # print(f"Number of families = {n}")
    # print(f"Number of rows = {r}")
    # print([n, r])


    family = (cases[iterations + 1])
    family = family.split(" ")
    # print(family)
    # All members will fit on the bus

    # Output the total number of happy people

    happy = 0
    counter = 0
    odd = []
    # print("Starting people")
    for people in family:
        # print(int(people))
        people = int(people)

        # If Even
        if people % 2 == 0: 
            happy += int(people)
            r -= int(people / 2)
            # print(f"Happy is now {happy}, {r} rows remain")

        # If Odd
        else:
            if people > 1:
                happy += int(people - (people // 2))
                r -= int(people // 2)
                odd.append(int(people - (people // 2)))
                # print(f"Happy is now {happy}, {r} rows remain")
            else:
                odd.append(people)

        # print()
    # print("Beginning leftover")
    # print(odd, len(odd))
    # print(r)

    if len(odd) > r:
        # print("Have to reduce")
        # print("Old Odd")
        # print(odd)

        while len(odd) > r:
            odd = odd[:-2]

        # New Odd
        # print("New Odd")
        # print(odd)
    happy += len(odd)

    # print("End of people")
    # print("Result is", happy)
    # print()
    result.append(happy)
for item in result:
    print(item)

