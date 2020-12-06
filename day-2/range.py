class Password:
    text: str
    rule_min: int
    rule_max: int
    rule_letter: str

    def __init__(self, raw):
        self.rule_min = int(raw.split(":")[0].split(" ")[0].split("-")[0])
        self.rule_max = int(raw.split(":")[0].split(" ")[0].split("-")[1])
        self.rule_letter = list(raw.split(":")[0].split(" ")[1])[0]
        self.text = raw.split(":")[1].strip()

    def valid(self):
        return int(self.rule_min) <= self.text.count(self.rule_letter) <= int(self.rule_max)


def solve():
    valid = 0
    for x in open("input.txt"):
        valid = valid + 1 if Password(x).valid() else valid
    return valid


print(solve())
