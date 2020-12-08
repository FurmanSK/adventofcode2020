from collections import deque

# Create queue (deck)
d = deque()

def part1():
    q = d.copy()
    while len(d) > 0:
        testnum = d.pop()
        for num in q:
            # print(testnum, "+", num, " = ", testnum + num)
            if ( testnum + num == 2020):
                print('Part 1 Answer = ', testnum * num)
                return

def part2():
    q1 = dim.copy()
    q2 = dim.copy()
    while len(q1):
        num1 = q1.pop()
        for i in q2:
            num2 = i;
            for j in dim:
                if (num1 + num2 + j == 2020):
                    print("Part 2 Answer = ", num1 * num2 * j)
                    return


if __name__ == '__main__':

    # Open file
    f = open('day1/input.txt', 'r')
    # Add to queue and convert to ints
    for x in f:
        d.append(int(x.rstrip()))
    # immutible
    dim = d.copy()
    part1()
    part2()