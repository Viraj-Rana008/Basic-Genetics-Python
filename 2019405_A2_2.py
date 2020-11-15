def dna_to_rna(s):
    rna = ""
    for i in range(len(s)):
        if s[i]=="T":
            rna = rna+"U"
        else:
            rna = rna+s[i]
    return rna

def q2_input():
    ans_list = []
    with open("Input1.txt") as f:
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
        RNA = dna_to_rna(DNA)
        ans_list.append([RNA,sample])
    for i  in ans_list:
        print("Sample-"+str(i[1])+" : "+i[0])

q2_input()
