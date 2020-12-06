def load_input():
    data = list(str(x) for x in open("input.txt").read().split("\n\n"))
    for d in range(len(data)):
        data[d] = data[d].strip().replace('\n', ',').replace(' ', ',')
    doc_list = []
    for d in data:
        doc_props = []
        for e in d.split(','):
            doc_props.append(tuple(e.split(':')))
        doc_list.append(dict(doc_props))
    return doc_list


def solve(docs):
    valid = 0
    for d in docs:
        if len(d.keys()) == 8 or (len(d.keys()) == 7 and 'cid' not in d.keys()):
            valid += 1
    return valid


documents = load_input()
print(solve(documents))
