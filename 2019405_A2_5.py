pro_dict ={
    "UUU": "F","UUC":"F",
    "UUA": "L","UUG":"L",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
    "UAU":"Y","UAC":"Y",
    "UGU":"C","UGC":"C",
    "UGG":"W",
    "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAU":"H","CAC":"H",
    "CAA":"E","CAG":"E",
    "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
    "AUU":"I","AUC":"I","AUA":"I",
    "AUG":"M",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAU":"N","AAC":"N",
    "AAA":"K","AAG":"K",
    "AGU":"S","AGC":"S",
    "AGA":"R","AGG":"R",
    "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAU":"D","GAC":"D",
    "GAA":"Q","GAG":"Q",
    "GGU":"G","GGC":"G","GGA":"G","GGG":"G"
}

amino_mass={
    "A":89,"R":174,"N":132,"D":133,"C":121,"E":146,"Q":147,"G":75,"H":155,
    "I":131,"L":131,"K":146,"M":149,"F":165,"P":115,"S":105,"T":119,"W":204,
    "Y":181,"V":117
}
def rna_to_protein(s):
    l1 = []
    l2 = []
    ans = []
    p_list = []
    i=0
    while i+3<=len(s):
        c=1
        if s[i:i+3] == "AUG":
            l1.append(i)
    
        elif s[i:i+3]=="UAA" or s[i:i+3]=="UGA" or s[i:i+3]=="UAG":
            l2.append(i+3)
            c=3
        i+=c
    
    '''for i in l1:
        print(i,end=" ")
    print()
    for i in l2:
        print(i,end=" ")'''

    for i in l1:
        for j in l2:
            if j>i and (j-i)%3==0 :
                ans.append(s[i:j])
    
    #ans = [i for i in ans if not("UGA" in i[3:len(i)-3] or "UAA" in i[3:len(i)-3] or "UAG" in i[3:len(i)-3]) ]
    for i in range(len(ans)):
        prot = ""
        j=0
        while j+3<=len(ans[i]):
            if ans[i][j:j+3]!="UAA" and ans[i][j:j+3]!="UGA" and ans[i][j:j+3]!="UAG" :
                prot += pro_dict[ans[i][j:j+3]]
            else:
                if 0<j<len(ans[i])-3:
                    break
            j+=3
        if prot not in p_list:
            p_list.append(prot)
    
    for i in range(len(p_list)):
        sum=0
        for j in p_list[i]:
            sum+=amino_mass[j]
        print("-".join(list(p_list[i])))
        print(sum)
        print()

def q5_input():
    with open("Input4.txt") as f:
        lines = [line.rstrip() for line in f]
    i=0
    RNA = ""
    while (i<len(lines)):
        RNA+=lines[i]
        i+=1
    rna_to_protein(RNA)

q5_input()
