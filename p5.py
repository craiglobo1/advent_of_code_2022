
sample = 1
with open(("d5_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line for line in rf.readlines()]

# print(lines)

def p1(lines : str):
    crane, ins = ("".join(lines)).split("\n\n")
    crane = crane.split("\n")
    rcrane = list(zip(*crane[::-1]))
    rcrane = ["".join(r)[1:] for r in rcrane]
    rcrane = list(filter(lambda x : x.strip().isalpha(),rcrane))
    rcrane = [ list(line.strip()) for line in rcrane]

    for line in ins.split("\n"):
        s,move = line.split(" from ")
        move = list(map(int, move.split(" to ")))
        s = s.replace("move ", "")
        s = int(s)
        added = rcrane[move[0]-1][-s:]

        rcrane[move[0]-1] = rcrane[move[0]-1][:-s]
        rcrane[move[1]-1] += added[::-1]
    
    return "".join([l[-1] for l in rcrane])

def p2(lines : str):
    crane, ins = ("".join(lines)).split("\n\n")
    crane = crane.split("\n")
    rcrane = list(zip(*crane[::-1]))
    rcrane = ["".join(r)[1:] for r in rcrane]
    rcrane = list(filter(lambda x : x.strip().isalpha(),rcrane))
    rcrane = [ list(line.strip()) for line in rcrane]
    
    for line in ins.split("\n"):
        s,move = line.split(" from ")
        move = list(map(int, move.split(" to ")))
        s = s.replace("move ", "")
        s = int(s)
        added = rcrane[move[0]-1][-s:]
        rcrane[move[0]-1] = rcrane[move[0]-1][:-s]
        rcrane[move[1]-1] += added
    
    return "".join([l[-1] for l in rcrane])



# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))