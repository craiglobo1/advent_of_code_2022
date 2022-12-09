from math import dist
from copy import deepcopy

sample = 1
with open(("d9_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]



def p1(lines : str):
    phpos =[0,0]
    hpos = [0, 0]

    tpos = [0, 0]
    visted = set()
    for line in lines:
        dir, amt = line.split(" ")
        amt = int(amt)
        for i in range(amt):
            phpos[0],phpos[1] = hpos[0], hpos[1]
            if dir == "R":
                hpos[0] += 1
            if dir == "L":
                hpos[0] -= 1
            if dir == "U":
                hpos[1] += 1
            if dir == "D":
                hpos[1] -= 1
            if dist(hpos, tpos) >= 2:
                tpos[0],tpos[1] = phpos[0],phpos[1]
            visted.add((tpos[0], tpos[1]))
    return len(visted)

move_side = lambda h,t,s : h[s]-1 if t[s]<h[s] else h[s]+1  


def print_g(h, ropes):
    max_x = 6
    max_y = 6
    g = [ [ "." for _ in range(max_x)] for _ in range(max_y)]
    for i in range(len(ropes)-1,-1,-1):
        g[(max_x-1)-ropes[i][1]][ropes[i][0]] = str(i+1)
    g[(max_x-1)-h[1]][h[0]] = "H"
    print( "\n".join(["".join(r) for r in g]))
    print("--------------------------------------")


def move(h,t):
    dx = h[0]-t[0]
    dy = h[1]-t[1]

    if abs(dx) >= 2 and abs(dy) >= 2:
        t = (move_side(h,t,0), move_side(h,t,1))
    elif abs(dx) >= 2:
        t = (move_side(h,t,0), h[1])
    elif abs(dy) >= 2:
        t = (h[0], move_side(h,t,1))
    return t

def p2(lines : str):
    h = (0, 0)
    ropes = [(0, 0) for i in range(9)]
    visted = set()
    for line in lines:
        dir, amt = line.split(" ")
        amt = int(amt)
        for i in range(amt):
            visted.add(ropes[-1])
            if dir == "R":
                h = (h[0]+1, h[1])
            if dir == "L":
                h = (h[0]-1, h[1])
            if dir == "U":
                h = (h[0], h[1]+1)
            if dir == "D":
                h = (h[0], h[1]-1)
            
            ropes[0] = move(h, ropes[0])
            for i in range(1,9):
                ropes[i] = move(ropes[i-1], ropes[i])
            # print_g(h,ropes)
            visted.add(ropes[-1])
    return len(visted)

print("part 1:",p1(lines))
print("part 2:",p2(lines))