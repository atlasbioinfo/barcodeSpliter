import sys
def showError(Mes):
    print("-"*20)
    print("Exception:\n\t",end="")
    print("\n\t".join(Mes))
    print("-"*20)
    print("Exit...")
    sys.exit()
    
def trans(seq):
    seq=seq[::-1]
    nt={
        "A":"T","T":"A","C":"G","G":"C","N":"N",
        "a":"t","t":"a","c":"g","g":"c","n":"n"
    }
    nseq=""
    for s in seq:
        if (s not in nt):
            return "Error"
        nseq+=nt[s]
    return nseq

def codeBeak():
    print("\nExit...")
    sys.exit(0)
    
def getBarcodeInfo(file):
    barcodeInfo={}
    with open(file,"r")as bf:
        title=bf.readline()
        for line in bf:
            if (line[0]=="#"):
                continue
            tmp=line.strip().split(",")
            if (len(tmp)!=3):
                showError(['The barcode ['+line.strip()+'] may incomplete.',
                           'It should contain Name,i5,i7 and seperate with \",\"',
                          ])
            barcodeInfo[tmp[0]]=[tmp[1],tmp[2],trans(tmp[1]),trans(tmp[2])]
    return barcodeInfo

res=getBarcodeInfo("./barcode.tsv")

# statBarcode={}
# readsInfoR1={}
# readsInfoR2={}
# with open(,"r")as bf:
#     title=bf.readline()
#     for line in bf:
#         if (line[0]=="#"):
#             continue
#         tmp=line.strip().split(",")
#         barcodeInfo[tmp[0]]=[tmp[1],tmp[2],trans(tmp[1]),trans(tmp[2])]
#         statBarcode[tmp[0]]=[0 for i in range(16)]
#         readsInfoR1[tmp[0]]=[]
#         readsInfoR2[tmp[0]]=[]