
sample = 1
with open(("d8_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]

def p1(lines : str):
    lines = [ [ int(val) for val in line] for line in lines]

    isVisible= set()
    # isVisible = [ [ 0 for i in range(len(lines[0]))] for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            # print(lines[i][j], [lines[x][j] for x in range(0, i)])
            if lines[i][:j] == []:
                isVisible.add((i,j))
            elif lines[i][j] > max(lines[i][:j]):
                isVisible.add((i,j))
            
            if lines[i][j+1:] == []:
                isVisible.add((i,j))
            elif lines[i][j] > max(lines[i][j+1:]):
                isVisible.add((i,j))
                
            if [lines[x][j] for x in range(i+1, len(lines))] == []:
                isVisible.add((i,j))
            elif lines[i][j] > max([lines[x][j] for x in range(i+1, len(lines))]):
                isVisible.add((i,j))

            if [lines[x][j] for x in range(0, i)] == []:
                isVisible.add((i,j))
            elif lines[i][j]> max([lines[x][j] for x in range(0, i)]):
                isVisible.add((i,j))
    return len(isVisible)

def viewDist(tree, view):
    v = 0
    for t in view:
        if t < tree:
            v += 1
        else:
            v += 1
            return v
    return v

def p2(lines : str):
    lines = [ [ int(val) for val in line] for line in lines]

    isVisible= set()
    max_tv = -1e10
    max_id = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            # print(lines[i][j], [lines[x][j] for x in range(0, i)])
            lv = viewDist(lines[i][j], lines[i][:j][::-1])
            rv = viewDist(lines[i][j], lines[i][j+1:])
            dv = viewDist(lines[i][j], [lines[x][j] for x in range(i+1, len(lines))])
            uv = viewDist(lines[i][j], [lines[x][j] for x in range(0, i)][::-1])
            tv = lv*rv*dv*uv
            if tv > max_tv:
                max_tv = tv
                # print(lines[i][j],lines[i][:j][::-1],lines[i][j+1:],[lines[x][j] for x in range(i+1, len(lines))],[lines[x][j] for x in range(0, i)][::-1])
                # print(lv,rv,dv,uv)

    return max_tv

    # print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))
print("ans: ",viewDist(5, [4,9]))