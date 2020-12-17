from os import truncate
import re

class Day4:

    def __init__(self, p):
        self.puzzle = p

    def solve(self):
        num = 0
        passports_p1 = []
        passports_p2 = []
        passport = Passport()
        for x in self.puzzle:
            # Blank line
            if x == "\n":
                if passport.check_if_valid_p1():
                    passports_p1.append(passport)
                    if passport.check_if_valid_p2():
                        passports_p2.append(passport)
                passport = Passport()
                continue
            else:
                line = x.strip().split(" ")
                for a in line:
                    attr = a.split(":")
                    setattr(passport, attr[0], attr[1])
        # Check total in passports which are the valid ones
        return len(passports_p1), len(passports_p2)

class Passport:
    byr, iyr, eyr, hgt, hcl, ecl, pid, cid = "", "", "", "", "", "", "", ""
    
    def check_if_valid_p1(self):
        for x in [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]:
            if getattr(self, x) == "" and x != "cid":
                return False
        return True

    def check_if_valid_p2(self):
        if (len(self.byr) != 4 or (int(self.byr) < 1920 or int(self.byr) > 2002)):
            return False
        if ( len(self.iyr) != 4 or (int(self.iyr) < 2010 or int(self.iyr) > 2020)):
            return False
        if (len(self.eyr) != 4 or (int(self.eyr) < 2020 or int(self.eyr) > 2030)):
            return False
        if not self.check_hgt():
            return False
        if not self.check_hcl():
            return False
        if not self.check_ecl():
            return False
        if not self.check_pid():
            return False

        # else return True
        return True

    def check_hgt(self):
        # Determine if cm or in
        if self.hgt.find("cm") > 0:
            index = self.hgt.find("cm")
            if int(self.hgt[0:index]) > 193 or int(self.hgt[0:index]) < 150:
                return False
            else:
                return True
        else:
            index = self.hgt.find('in')
            if int(self.hgt[0:index]) < 59 or int(self.hgt[0:index]) > 76:
                return False
            else:
                return True

    def check_hcl(self):
        return re.search("^#[0-9a-f]{6}$", self.hcl)

    def check_ecl(self):
        valid_eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.ecl in valid_eye_color

    def check_pid(self):
        return re.search(r'^\d{9}$', self.pid)

if __name__ == '__main__':
    
    # Open file
    f = open('day4/input.txt', 'r')

    run = Day4(f)
    ret = run.solve()
    print("Part 1 = ", ret[0], "\nPart 2 = ", ret[1])