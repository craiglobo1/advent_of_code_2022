

sample = 0

with open(("d1_input.txt" if not sample else "sample.txt"),"r+") as rf:
    lines = rf.read()
    lines = lines.split("\n\n")
    lines = [ list(map(int, val.split())) for val in lines]

print("lines:",lines)

def p1(lines : str):
    sums = list(map(sum, lines))
    return max(sums)

def p2(lines : str):    
    sums = list(map(sum, lines))
    sums.sort(reverse=True)
    return sum(sums[:3])

print("part 1:",p1(lines))
print("part 2:",p2(lines))