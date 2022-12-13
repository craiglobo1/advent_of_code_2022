sample = 1
with open(("d13_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

def compare(l,r, i=[]):
    if isinstance(l,int) and isinstance(r, int):
        if l == r:
            return 
        return l < r     
    
    if isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            ans =  compare(l[i],r[i])
            if isinstance(ans, bool):
                return ans

        if len(l) < len(r):
            return True
        if len(r) < len(l):
            return False
    
    if isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])

    if isinstance(l, int) and isinstance(r, list):
        return compare([l], r)

def p1(lines : str):
    lines = ("\n".join(lines)).split("\n\n")
    indices = [ i+1 for i, line in enumerate(lines) if compare(eval(line.split("\n")[0]), eval(line.split("\n")[1]))]
    return sum(indices)

def p2(lines : str):
    lines = [ eval(line) for line in lines if line.strip() != ""]
    lines += [[[2]], [[6]]]
    for i in range(len(lines)):
        for j in range(len(lines)):
            if compare(lines[i], lines[j]):
                lines[i], lines[j] = lines[j], lines[i]

    return (lines.index([[2]])+1)*(lines.index([[6]])+1)

# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))