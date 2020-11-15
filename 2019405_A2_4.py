dinu={
    "AA":0,"AC":0,"AG":0,"AT":0,
    "CA":0,"CC":0,"CG":0,"CT":0,
    "GA":0,"GC":0,"GG":0,"GT":0,
    "TA":0,"TC":0,"TG":0,"TT":0
}

def d_freq(s):
    for i in range(len(s)-1):
        dinu[s[i]+s[i+1]]+=1
    for i,j in dinu.items():
        print(i+" : "+str(j))


def q4_input():
    l = []
    with open("Input3.txt") as f:
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
    for i in range(len(l)):
        d_freq(l[i])

q4_input()
