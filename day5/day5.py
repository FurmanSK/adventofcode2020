import re

class Day5:

    def __init__(self, p):
        self.boardingpasses = p

    def solve(self):
        ans = []
        for bp in self.boardingpasses:
            ans.append(self.parse_boarding_pass(bp))
        print("Part 1 = ", max(ans))
        ans.sort()
        print("Part 2 = ", sorted(set(range(ans[0], ans[-1])) - set(ans))[0])

    def parse_boarding_pass(self, bp):
        row = bp[0:7]
        col = bp[7:]

        rows = list(range(128))
        for x in row:
            # take the lower half so divide the upper num by 2
            if x == "F":
                rows = rows[0:int(len(rows)/2)]
            # take the upper half so set the lower num to half betwee
            elif x == "B":
                rows = rows[int(len(rows)/2):]
        ans_r = rows[0]

        cols = list(range(8))
        for y in col:
            if y == "L":
                cols = cols[0:int(len(cols)/2)]
            elif y == "R":
                cols = cols[int(len(cols)/2):]
        ans_c = cols[0]

        return ans_r * 8 + ans_c
        

if __name__ == '__main__':
    
    # Open file
    f = open('day5/input.txt', 'r')

    run = Day5(f)
    run.solve()