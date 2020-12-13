class Instruction:
    type: str
    number: int
    executed: bool

    def __init__(self, line):
        self.type = line.split(" ")[0]
        self.number = int(line.split(" ")[1])
        self.executed = False

    def next(self):
        return self.number if self.type == 'jmp' else 1

    def execute(self):
        return self.number if self.type == 'acc' else 0


def load_input():
    return list(map(lambda x: Instruction(x), [str(x.strip()) for x in open("input.txt")]))


def execute_instructions(instructions):
    i = 0
    counter = 0
    while True:
        if i >= len(instructions):
            print('Ran to Completion: ' + str(counter))
            return counter
        if not instructions[i].executed:
            instructions[i].executed = True
            counter += instructions[i].execute()
            i += instructions[i].next()
        else:
            return counter


instruction_list = load_input()
print(execute_instructions(instruction_list))

