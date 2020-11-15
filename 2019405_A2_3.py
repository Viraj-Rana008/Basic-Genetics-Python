def h_dist(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count

def q3_input():
    l = []
    with open("Input2.txt") as f:
        lines = [line.rstrip() for line in f]
    i=0
    sample = 0
    while (i<len(lines)):
        if lines[i][0]=='>':
            DNA=""
            i+=1
            sample+=1
            while i<len(lines) and lines[i][0]!=">":
                DNA+=lines[i]
                i+=1
        l.append(DNA)
    ham_dis = h_dist(l[0],l[1])
    print("Hamming Distance to two sequence is :"+str(ham_dis))

q3_input()
