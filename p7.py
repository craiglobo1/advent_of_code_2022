
sample = 0
with open(("d7_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

def p1(lines : str):
    i = 0
    curdir = []
    dir = {}
    while i < len(lines):
        line = lines[i]
        if "$" == line[0]:
            cmd = line[2:4]
            if "cd" == cmd:
                path = line[5:]
                if path == "..":
                    curdir.pop()
                elif path == "/":
                    curdir = []
                else:
                    curdir.append(path)
            if "ls" == cmd:
                i += 1
                ls_lines = []
                while i < len(lines):
                    if "$"  == lines[i][0]:
                        break
                    ls_lines.append(lines[i])
                    i += 1
                i -= 1
                dir_size = 0
                for lsl in ls_lines:
                    if lsl[:3] != "dir":
                        size, file = lsl.split(" ")
                        dir_size += int(size)
                dir["/".join(curdir)] = dir_size
        i += 1

    for d1,s1 in dir.items():
        for d2,s2 in dir.items():
            if d1 == d2[:len(d1)] and d1 != d2:
                dir[d1] += s2
    tsum = 0
    for d,s in dir.items():
        if s <= 100000:
            tsum += s
    return tsum
        

def p2(lines : str):
    i = 0
    curdir = []
    dir = {}
    while i < len(lines):
        line = lines[i]
        if "$" == line[0]:
            cmd = line[2:4]
            if "cd" == cmd:
                path = line[5:]
                if path == "..":
                    curdir.pop()
                elif path == "/":
                    curdir = []
                else:
                    curdir.append(path)
            if "ls" == cmd:
                i += 1
                ls_lines = []
                while i < len(lines):
                    if "$"  == lines[i][0]:
                        break
                    ls_lines.append(lines[i])
                    i += 1
                i -= 1
                dir_size = 0
                for lsl in ls_lines:
                    if lsl[:3] != "dir":
                        size, file = lsl.split(" ")
                        dir_size += int(size)
                dir["/".join(curdir)] = dir_size
        i += 1
    # print(dir)

    for d1,s1 in dir.items():
        for d2,s2 in dir.items():
            if d1 == d2[:len(d1)] and d1 != d2:
                dir[d1] += s2

    ts = 30000000-(70000000-dir[""])
    ms = 1e10
    for d,s in dir.items():
        # print(d,s,s >= ts)
        if s >= ts:
            if s < ms:
                ms = s
    return ms
        

# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))