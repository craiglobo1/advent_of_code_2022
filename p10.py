import csv

sample = 1
with open(("d10_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

def get_task(line):
    if " " in line:
        cmd, amt = line.split(" ")
        amt = int(amt)
    else:
        cmd = line
    if cmd == "noop":
        return (cmd, 1)
    elif cmd == "addx":
        return ((cmd, amt), 2)

def p1(lines : str):
    cycle = 1
    tasks = []
    s = True
    x= 1
    sumx = 0
    while len(lines):
        line = lines.pop(0)
        if " " in line:
            cmd, amt = line.split(" ")
            amt = int(amt)
        else:
            cmd = line
        if cmd == "noop":
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ss = cycle*x
                sumx += ss
        if cmd == "addx":
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                ss = cycle*x
                sumx += ss
            cycle += 1
            x += amt
            if cycle in [20, 60, 100, 140, 180, 220]:
                ss = cycle*x
                sumx += ss
    return sumx

def print_pixel(cycle, x):
    x = (cycle//40)*40 + x
    cycle -= 1
    if cycle >= x-1 and cycle <= x+1:
        print("#", end="")
    else:
        print(".", end="")
    if cycle % 40 == 0:
        print()

def p2(lines : str):
    cycle = 1
    x= 1
    while len(lines):
        line = lines.pop(0)
        if " " in line:
            cmd, amt = line.split(" ")
            amt = int(amt)
        else:
            cmd = line
        if cmd == "noop":
            cycle += 1
            print_pixel(cycle,x)
        if cmd == "addx":
            cycle += 1
            print_pixel(cycle,x)
            cycle += 1
            x += amt
            print_pixel(cycle,x)
            
    

print("part 1:",p1(lines.copy()))
print("part 2:",p2(lines))