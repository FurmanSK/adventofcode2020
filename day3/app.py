from collections import deque

# Create queue (deck)
d = deque()

if __name__ == '__main__':
    
    # Open file
    f = open('day3/input.txt', 'r')

    # build 2D map using deque for faster appends
    for x in f:
        d.append(list(x.strip()))

    # x, y coord for current position
    currentPos = [0, 0]
    # tree count found
    treeCount = 0
    xoff = 0
    while currentPos[1] < len(d):
        # start at y = 0 and increment x by 3 total looking for #'s
        currentPos[0] += 3
        xoff = currentPos[0] % 31
        currentPos[1] += 1
        if currentPos[1] == len(d):
            break
        if d[currentPos[1]][xoff] == '#':
            treeCount += 1
    
    print("Part 1 tree's found = ", treeCount)