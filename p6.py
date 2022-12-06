
sample = 1
with open(("d6_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line for line in rf.readlines()]

def p1(lines : str):
    n = 4
    line = lines[0]
    for i in range(0,len(line)-n):
        if len(set(line[i:i+n])) == n:
            return i+n

def p2(lines : str):
    n = 14
    line = lines[0]
    for i in range(0,len(line)-n):
        if len(set(line[i:i+n])) == n:
            return i+n

# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))