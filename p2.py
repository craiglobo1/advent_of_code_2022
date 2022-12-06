

sample = 1
with open(("d2_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = rf.readlines()



def p1(lines : str):
    score = 0
    prs = {"X":1, "Y":2, "Z":3}
    for line in lines:
        p1,p2 = line.split()
        score += prs[p2]
        if p1 == "A":
            if p2 == "X":
                score += 3
            if p2 == "Y":
                score += 6
            if p2 == "Z":
                score += 0
        if p1 == "B":
            if p2 == "X":
                score += 0
            if p2 == "Y":
                score += 3
            if p2 == "Z":
                score += 6
        if p1 == "C":
            if p2 == "X":
                score += 6
            if p2 == "Y":
                score += 0
            if p2 == "Z":
                score += 3
    return score

def p2v2(lines : str):
    prs = {"X":0,"Y":3,"Z":6}
    prss = {"X":1,"Y":2,"Z":3}
    d = {"A": "X", "B":"Y", "C":"Z"}
    w = {"A": "Y", "B":"Z", "C":"X"}
    l = {"A": "Z", "B":"X", "C":"Y"}
    r = {"X":l,"Y":d,"Z":w}
    score = 0
    for line in lines:
        p1,p2 = line.split()
        score += prs[p2]
        score += prss[r[p2][p1]]
    return score


def p2(lines : str):    
    prs = {"X":0, "Y":3, "Z":6}
    score = 0
    for line in lines:
        p1,p2 = line.split()
        score += prs[p2]
        if p1 == "A":
            if p2 == "X":
                score += 3 
            if p2 == "Y":
                score += 1
            if p2 == "Z":
                score += 2
        if p1 == "B":
            if p2 == "X":
                score += 1
            if p2 == "Y":
                score += 2
            if p2 == "Z":
                score += 3
        if p1 == "C":
            if p2 == "X":
                score += 2
            if p2 == "Y":
                score += 3
            if p2 == "Z":
                score += 1
    return score


print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2v2(lines))