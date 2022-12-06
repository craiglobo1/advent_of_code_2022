import csv

sample = 1
with open(("d3_input.txt" if sample else "sample.txt"),"r+") as rf:
    lines = rf.readlines()



def p1(lines : str):
    com = []
    for line in lines:
        line = line[:-1]
        f,s = line[:len(line)//2], line[len(line)//2:]
        item = list(set(f).intersection(set(s)))[0]
        if item >= "a" and item <= "z":
            com.append(ord(list(item)[0])-ord("a") + 1) 
        if item >= "A" and item <= "Z":
            com.append(ord(list(item)[0])-ord("A") + 27) 
            

    return sum(com)




def p2(lines : str):
    com =[]
    for i in range(0,len(lines),3):
        item = list(set(lines[i][:-1]).intersection(set(lines[i+1][:-1])).intersection(set(lines[i+2][:-1])))[0]
        if item >= "a" and item <= "z":
            com.append(ord(list(item)[0])-ord("a") + 1) 
        if item >= "A" and item <= "Z":
            com.append(ord(list(item)[0])-ord("A") + 27) 

    return sum(com)
            


        

# print("lines:",lines)
print("part 1:",p1(lines))
print("part 2:",p2(lines))