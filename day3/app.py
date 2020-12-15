from collections import deque
import math
# Create queue (deck) global
d = deque()


def calcTreesInSlope(x, y):
    # calculates based on x and y slope passed in

    # x, y coord for current position
    currentPos = [0, 0]
    # tree count found
    treeCount = 0
    xoff = 0
    while currentPos[1] < len(d):
        # start at y = 0 and increment x by 3 total looking for #'s
        currentPos[0] += x
        xoff = currentPos[0] % 31
        currentPos[1] += y
        if currentPos[1] >= len(d):
            break
        if d[currentPos[1]][xoff] == '#':
            treeCount += 1

    return treeCount


if __name__ == '__main__':
    
    # Open file
    f = open('day3/input.txt', 'r')

    # build 2D map using deque for faster appends
    for x in f:
        d.append(list(x.strip()))
    
    # Part 1
    print("Part 1 answer = ", calcTreesInSlope(3, 1))

    # Part 2
    p2 = []
    p2.append(calcTreesInSlope(1, 1))
    p2.append(223) # from part 1
    p2.append(calcTreesInSlope(5, 1))
    p2.append(calcTreesInSlope(7, 1))
    p2.append(calcTreesInSlope(1, 2))

    print("Part 2 answer is = ", math.prod(p2))