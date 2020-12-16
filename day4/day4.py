class Day4:

    def __init__(self, p):
        self.puzzle = p

    def solve(self):
        num = 0
        passports = []
        passport = Passport()
        for x in self.puzzle:
            # Blank line
            num += 1
            if num == 998:
                print("Stop here and check")
            if x == "\n":
                if passport.check_if_valid():
                    passports.append(passport)
                passport = Passport()
                continue
            else:
                line = x.strip().split(" ")
                for a in line:
                    attr = a.split(":")
                    setattr(passport, attr[0], attr[1])
        # Check total in passports which are the valid ones
        return len(passports)

class Passport:
    byr, iyr, eyr, hgt, hcl, ecl, pid, cid = "", "", "", "", "", "", "", ""
    
    def check_if_valid(self):
        for x in [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]:
            if getattr(self, x) == "" and x != "cid":
                return False
        return True




if __name__ == '__main__':
    
    # Open file
    f = open('day4/input.txt', 'r')

    run = Day4(f)
    print("Part 1 = ", run.solve())