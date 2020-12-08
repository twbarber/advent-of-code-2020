class Bag:
    color: str
    content: dict

    def __init__(self, color, content):
        self.color = color
        self.content = content


def load_input():
    return list(str(x.strip().replace('.', '')) for x in open("input.txt"))


def build_bags(data):
    sewn_bags = {}
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
            sewn_bags[outside] = bag
        else:
            bag = Bag(outside, {})
            sewn_bags[outside] = bag
    return sewn_bags


def count_bags_inside_color(bag_of_bags, color, count):
    bag = bag_of_bags[color]
    for b in bag.content:
        count += int(bag.content[b]) * (1 + count_bags_inside_color(bag_of_bags, b, 0))
    return count


bag_list = load_input()
bags = build_bags(bag_list)
print(count_bags_inside_color(bags, 'shiny gold', 0))
