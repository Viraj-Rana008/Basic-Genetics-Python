def cal_gc(fasta):
    length = len(fasta)
    count = 0
    for i in range(len(fasta)):
        if fasta[i]=="G" or fasta[i]=="C":
            count+=1
    GC_content = count/length*100
    return GC_content



def q1_input():
    ans_list = []
    with open("Input1.txt") as f:
        lines = [line.rstrip() for line in f]
    i=0
    sample=0
    while (i<len(lines)):
        if lines[i][0]=='>':
            DNA=""
            i+=1
            sample+=1
            while i<len(lines) and lines[i][0]!=">":
                DNA+=lines[i]
                i+=1
        GC_content = cal_gc(DNA)   
        ans_list.append([GC_content,sample])
    ans_list.sort()
    for i in ans_list[::-1]:
        print("Sample-"+str(i[1])+" : "+str(i[0])+" %")

q1_input()
