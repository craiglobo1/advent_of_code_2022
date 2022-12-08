
sample = 1
with open(("d9_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]


def p1(lines : str):
    pass

def p2(lines : str):
    pass

print("part 1:",p1(lines))
print("part 2:",p2(lines))