from math import lcm

sample = 1
with open(("d11_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line for line in rf.readlines()]

def oper(old, operand):
    amt,op = operand
    if amt == "old":
        return old*old
    
    amt = int(amt)
    if op == "+":
        return old + amt
    if op == "*":
        return old * amt
    
    assert False, f"the pair {amt} and {op} are invalid"


def p1(lines : str):
    st = filter(lambda x: "Starting items:" in x,lines)
    st = [ list(map(int, it.split(":")[1].strip().split(","))) for it in st]
    ift = filter(lambda x: "If true:" in x, lines)
    ift = [ int(it.split(":")[1].strip().split(" ")[-1]) for it in ift]

    iff = filter(lambda x: "If false:" in x, lines)
    iff = [ int(it.split(":")[1].strip().split(" ")[-1]) for it in iff]

    div = filter(lambda x: "Test:" in x, lines)
    div = [ int(it.split(" ")[-1].strip()) for it in div]

    op = filter(lambda x: "Operation:" in x, lines)
    op = [ (it.split(" ")[-1].strip(), it.split(" ")[-2].strip())  for it in op]

    ins = [0 for i in range(len(st))]
    for round in range(20):
        for i in range(len(st)):
            rem_i = set()
            for j in range(len(st[i])):
                ins[i] += 1
                new = oper(st[i][j], op[i])
                new //= 3
                if new % div[i] == 0:
                    rem_i.add((i,j))
                    st[ift[i]].append(new)
                else:
                    rem_i.add((i,j))
                    st[iff[i]].append(new)
            st = [  [ st[i][j] for j in range(len(st[i])) if (i,j) not in rem_i] for i in range(len(st))]
    mon1  = max(ins)
    ins.remove(mon1)
    mon2  = max(ins)
    return mon1*mon2

def p2(lines : str):
    st = filter(lambda x: "Starting items:" in x,lines)
    st = [ list(map(int, it.split(":")[1].strip().split(","))) for it in st]
    ift = filter(lambda x: "If true:" in x, lines)
    ift = [ int(it.split(":")[1].strip().split(" ")[-1]) for it in ift]

    iff = filter(lambda x: "If false:" in x, lines)
    iff = [ int(it.split(":")[1].strip().split(" ")[-1]) for it in iff]

    div = filter(lambda x: "Test:" in x, lines)
    div = [ int(it.split(" ")[-1].strip()) for it in div]

    op = filter(lambda x: "Operation:" in x, lines)
    op = [ (it.split(" ")[-1].strip(), it.split(" ")[-2].strip())  for it in op]

    ins = [0 for i in range(len(st))]

    max_lim = lcm(*div)
    for _ in range(10000):
        for i in range(len(st)):
            for j in range(len(st[i])):
                ins[i] += 1
                new = oper(st[i][j], op[i])
                # new //= 3
                new %= max_lim

                if new % div[i] == 0:
                    st[ift[i]].append(new)
                else:
                    st[iff[i]].append(new)
            st[i] = []
    
    mon1  = max(ins)
    ins.remove(mon1)
    mon2  = max(ins)
    # print(st)
    return mon1*mon2


# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))
