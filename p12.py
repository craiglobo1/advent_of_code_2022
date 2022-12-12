from heapq import *
sample = 1
with open(("d12_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = [line.strip() for line in rf.readlines()]


def getVertices(lines, cur, height, width):
    off = [(0,1),(0,-1),(1,0),(-1,0)]
    ans = []
    for of in off:
        if cur[0]+of[0] >= 0 and cur[0]+of[0] < height and cur[1]+of[1] >= 0 and cur[1]+of[1] < width:
            ans.append((cur[0]+of[0], cur[1]+of[1]))
    
    ans = [val for val in ans if lines[cur[0]][cur[1]] <= lines[val[0]][val[1]]+1]
    assert (0,-1) not in ans, f"{ans}"
    return ans

def p1(lines : str):
    s = [ char for line in lines for char in line].index("S")
    e = [ char for line in lines for char in line].index("E")

    s = (s//len(lines[0]),  s%len(lines[0]))
    e = (e//len(lines[0]),  e%len(lines[0]))

    lines = [ [ord(char)-ord("a")  if char not in ["S", "E"] else (0 if char == "S" else 25) for char in line ] for line in lines]
    
    dist  = { (i, j): 1e100 for i in range(len(lines)) for j in range(len(lines[0]))}
    dist[e] = 0

    q = [e]
    visted = set()
    while q:
        cur = q.pop(0)
        visted.add(cur)
        for ver in getVertices(lines, cur, len(lines), len(lines[0])):
            dist[ver] = min(dist[ver], dist[cur] + 1)
            if ver not in visted and ver not in q:
                q.append(ver)
        if cur == s:
            return dist[cur]


def p2(lines : str):
    s = [ char for line in lines for char in line].index("S")
    e = [ char for line in lines for char in line].index("E")

    s = (s//len(lines[0]),  s%len(lines[0]))
    e = (e//len(lines[0]),  e%len(lines[0]))

    lines = [ [ord(char)-ord("a")  if char not in ["S", "E"] else (0 if char == "S" else 25) for char in line ] for line in lines]
    
    dist  = { (i, j): 1e100 for i in range(len(lines)) for j in range(len(lines[0]))}
    dist[e] = 0

    q = [e]
    visted = set()
    while q:
        cur = q.pop(0)
        visted.add(cur)
        for ver in getVertices(lines, cur, len(lines), len(lines[0])):
            dist[ver] = min(dist[ver], dist[cur] + 1)
            if ver not in visted and ver not in q:
                q.append(ver)
        if lines[cur[0]][cur[1]] == 0:
            return dist[cur]

# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))