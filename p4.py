import csv

sample = 1
with open(("d4_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

# print(lines)

def p1(lines : str):
    ins = 0
    for line in lines:
        r1,r2 = [ [ int(i) for i in p.split("-")] for p in line.split(",")]
        n = len(set(range(r1[0],r1[1]+1)).intersection(set(range(r2[0],r2[1]+1))))
        if  n >= r1[1]-r1[0]+1 or n >= r2[1]-r2[0]+1:
            ins += 1
    return ins




def p2(lines : str):
    ins = 0
    for line in lines:
        r1,r2 = [ [ int(i) for i in p.split("-")] for p in line.split(",")]
        n = len(set(range(r1[0],r1[1]+1)).intersection(set(range(r2[0],r2[1]+1))))
        if  n > 0:
            ins += 1
    return ins
            


# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))