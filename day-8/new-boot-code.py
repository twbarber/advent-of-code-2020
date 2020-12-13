import copy


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

    def flip(self):
        if self.type == 'jmp':
            self.type = 'nop'
            return self
        elif self.type == 'nop':
            self.type = 'jmp'
            return self


def load_input():
    return list(map(lambda x: Instruction(x), [str(x.strip()) for x in open("input.txt")]))


def execute_instructions(instructions):
    attempt = build_new_instructions(instructions, 0)
    new_instructions = attempt[0]
    last_flipped_index = attempt[1]
    i = 0
    counter = 0
    while i < len(new_instructions):
        if not new_instructions[i].executed:
            new_instructions[i].executed = True
            counter += new_instructions[i].execute()
            i += new_instructions[i].next()
        else:
            print('Loop found: ' + str(last_flipped_index))
            retry = build_new_instructions(instructions, last_flipped_index)
            new_instructions = retry[0]
            last_flipped_index = retry[1]
            i = 0
            counter = 0
    print('Ran to Completion: ' + str(counter))
    return counter


def build_new_instructions(instructions, last_flipped_index):
    new_instructions = copy.deepcopy(instructions)
    for i in range(last_flipped_index + 1, len(instructions)):
        if new_instructions[i].type in ['nop', 'jmp']:
            new_instructions[i].flip()
            return new_instructions, i


instruction_list = load_input()
print(execute_instructions(instruction_list))

