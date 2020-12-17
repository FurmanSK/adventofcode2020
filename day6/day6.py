from collections import Counter
class Day6:

    def __init__(self, f):
        self.customs_file = f

    def parse_customs_forms(self):
        ans = []
        ans2 = []
        cnt = Counter()
        grps = 0
        for line in self.customs_file:
            if line == "\n":
                ans.append(len(cnt))
                # get total for part 2
                ans2.append(Counter(cnt.values())[grps])
                grps = 0
                cnt.clear()
            else:
                cnt.update(line.strip())
                grps += 1
        return sum(ans), sum(ans2)
  

if __name__ == '__main__':
    
    # Open file
    f = open('day6/input.txt', 'r').readlines()

    run = Day6(f)
    ret = run.parse_customs_forms()
    print("Part 1",ret[0], "\nPart 2 = ", ret[1])