import re


class Document:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str

    def __init__(self, d):
        self.byr = int(d.get('byr')) if 'byr' in d.keys() else 0
        self.iyr = int(d.get('iyr')) if 'iyr' in d.keys() else 0
        self.eyr = int(d.get('eyr')) if 'eyr' in d.keys() else 0
        self.hgt = d.get('hgt')
        self.hcl = d.get('hcl')
        self.ecl = d.get('ecl')
        self.pid = d.get('pid')

    def __str__(self):
        return '{byr},{iyr},{eyr},{hgt},{hcl},{ecl},{pid}'.format(byr=self.byr, iyr=self.iyr, eyr=self.eyr, hgt=self.hgt, hcl=self.hcl, ecl=self.ecl, pid=self.pid)

    def valid(self):
        return self.valid_byr() and self.valid_iyr() and self.valid_eyr() and self.valid_hgt() \
               and self.valid_hcl() and self.valid_ecl() and self.valid_pid()

    def valid_byr(self):
        return 1920 <= self.byr <= 2002

    def valid_iyr(self):
        return 2010 <= self.iyr <= 2020

    def valid_eyr(self):
        return 2020 <= self.eyr <= 2030

    def valid_hgt(self):
        if self.hgt is None:
            return False
        match = re.match(r"([0-9]{2,3})(cm|in)", self.hgt)
        if match:
            items = match.groups()
            if items[1] == 'cm':
                return 150 <= int(items[0]) <= 193
            if items[1] == 'in':
                return 59 <= int(items[0]) <= 76

    def valid_hcl(self):
        if self.hcl is None:
            return False
        return re.match(r"#[a-f0-9]{6}", self.hcl)

    def valid_ecl(self):
        if self.ecl is None:
            return False
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def valid_pid(self):
        if self.pid is None:
            return False
        return re.match(r"[0-9]{9}$", self.pid)


def load_input():
    data = list(str(x) for x in open("input.txt").read().split("\n\n"))
    for d in range(len(data)):
        data[d] = data[d].strip().replace('\n', ',').replace(' ', ',')
    doc_list = []
    for d in data:
        doc_props = []
        for e in d.split(','):
            doc_props.append(tuple(e.split(':')))
        doc_list.append(Document(dict(doc_props)))
    return doc_list


def solve(docs):
    valid = 0
    for d in docs:
        if d.valid():
            print(d)
            valid += 1
    return valid


documents = load_input()
print(solve(documents))

