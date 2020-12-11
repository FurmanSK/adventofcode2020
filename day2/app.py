from collections import Counter


if __name__ == '__main__':
    
    # Open file
    f = open('day2/input.txt', 'r')
    goodOnes = 0

    for x in f:
        tmp = x.split()
        tmp[0] = tmp[0].split('-')
        tmp[1] = tmp[1].strip(':')
        
        cntr = Counter(tmp[2])

        min = int(tmp[0][0])
        max = int(tmp[0][1])
        print("min = ", min , " and max = ", max)
        print(tmp[1], " appears ", Counter(tmp[2])[tmp[1]], " times")
        if cntr[tmp[1]] <= max and cntr[tmp[1]] >= min:
            print("Found a good one ", tmp)
            goodOnes += 1

    print("Good ones = ", goodOnes)