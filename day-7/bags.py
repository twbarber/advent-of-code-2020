class Bag:
    color: str
    content: dict

    def __init__(self, color, content):
        self.color = color
        self.content = content


def load_input():
    return list(str(x.strip().replace('.', '')) for x in open("input.txt"))


def build_bags(data):
    sewn_bags = set()
    for x in data:
        outside = x.split(' bags contain')[0]
        inside = x.split(' bags contain')[1].strip().split(',')
        if inside[0] != 'no other bags':
            content = {}
            for b in inside:
                num_color = b.split('bag')[0].strip()
                bag_color = b.split('bag')[0].strip()[1:len(num_color)].strip()
                number = num_color[0]
                content[bag_color] = number
            bag = Bag(outside, content)
            sewn_bags.add(bag)
        else:
            bag = Bag(outside, {})
            sewn_bags.add(bag)
    return sewn_bags


def find_bags_containing_color(bag_of_bags, color, known_bags):
    for b in bag_of_bags:
        if color in b.content and b not in known_bags:
            known_bags.add(b)
            known_bags.union(find_bags_containing_color(bag_of_bags, b.color, known_bags))
    return known_bags


bag_list = load_input()
bags = build_bags(bag_list)
print(len(find_bags_containing_color(bags, 'shiny gold', set())))
