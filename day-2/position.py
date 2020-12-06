class Password:
    text: str
    first: int
    second: int
    char: str

    def __init__(self, raw):
        self.first = int(raw.split(":")[0].split(" ")[0].split("-")[0]) - 1
        self.second = int(raw.split(":")[0].split(" ")[0].split("-")[1]) - 1
        self.char = list(raw.split(":")[0].split(" ")[1])[0]
        self.text = raw.split(":")[1].strip()

    def valid(self):
        return True if (self.text[self.first] == self.char or self.text[self.second] == self.char) \
                       and self.text[self.first] != self.text[self.second] else False


def solve():
    valid = 0
    for x in open("input.txt"):
        valid = valid + 1 if Password(x.strip()).valid() else valid
    return valid


print(solve())
