from collections import Counter


if __name__ == '__main__':
    
    # Open file
    f = open('day2/input.txt', 'r')
    goodOnesP1 = 0
    goodOnesP2 = 0

    # part 1
    for x in f:
        tmp = x.split()
        tmp[0] = tmp[0].split('-')
        tmp[1] = tmp[1].strip(':')
        
        # Part 1
        cntr = Counter(tmp[2])

        min = int(tmp[0][0])
        max = int(tmp[0][1])
        print("min = ", min , " and max = ", max)
        print(tmp[1], " appears ", Counter(tmp[2])[tmp[1]], " times")
        if cntr[tmp[1]] <= max and cntr[tmp[1]] >= min:
            print("Found a good one ", tmp)
            goodOnesP1 += 1
        
        # Part 2
        if bool(tmp[2][int(tmp[0][0]) - 1] == tmp[1]) ^ bool(tmp[2][int(tmp[0][1]) - 1] == tmp[1]):
            goodOnesP2 += 1

    print("Part 1 Good ones = ", goodOnesP1)
    print("Part 2 Good ones = ", goodOnesP2)