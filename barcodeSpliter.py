import sys,gzip,argparse

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
    
def getBarcodeInfo(file):
    barcodeInfo={}
    with open(file,"r")as bf:
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

def initalDict(barcodeInfo):
    statBarcode={}
    readsInfoR1={}
    readsInfoR2={}
    
    for barName in barcodeInfo:
        statBarcode[barName]=[0 for i in range(16)]
        readsInfoR1[barName]=[]
        readsInfoR2[barName]=[]
    return [statBarcode,readsInfoR1,readsInfoR2]

def findRes(num):
    if (num==-1):
        return 0
    return 1

def findBarcode(seq,barcodeInfo):
    resDict={}
    for b in barcodeInfo:
        resDict[b]=[findRes(seq[:20].find(barcodeInfo[b][0])),
                   findRes(seq[:20].find(barcodeInfo[b][1]))]
    return resDict

def judgeIfBarcode(seq1,seq2,barcodeInfo):
    resDict1=findBarcode(seq1,barcodeInfo)
    resDict2=findBarcode(seq2,barcodeInfo)
    barcodeLabel={}
    for b in resDict1:
        if ((resDict1[b][0] or resDict1[b][1]) and 
            (resDict2[b][0] or resDict2[b][1])):
            barcodeLabel[b]=1
            continue
        barcodeLabel[b]=0
        
    return barcodeLabel

def getArg():
    parser = argparse.ArgumentParser(description='This software can use barcode label to \
        separate different samples in mixed-sample sequencing.')
    parser.add_argument("r1",metavar='r1.fastq.gz',help="Sequencing reads, R1. Also support uncompressed format, like: r1.fastq",type=str)
    parser.add_argument("r2",metavar='r2.fastq.gz',help="Sequencing reads, R2. Also support uncompressed format, like: r2.fastq",type=str)
    parser.add_argument("b",metavar='barcode.csv',help="csv file contains barcode info. eg:Barcode01,TAACTCGG,TAACAGTT",type=str)
    parser.add_argument("-o","--outfolder",help="The name of output folder can be customized. Default: ./Output/", type=str)
    args = parser.parse_args()
    return args

def main():
    args=getArg()
    print(args)

    # # Initial dict
    # barcodeInfo=getBarcodeInfo("./barcode.tsv")
    # statBarcode,readsInfoR1,readsInfoR2=initalDict(barcodeInfo)
    
    # with gzip.open("./test_r1.fastq.gz","r") as r1f:
    #     with gzip.open("test_r2.fastq.gz","r") as r2f:
    #         while (True):
    #             header1=str(r1f.readline().strip(),encoding="utf8")
    #             seq1=str(r1f.readline().strip(),encoding="utf8")
    #             quaHeader1=str(r1f.readline().strip(),encoding="utf8")
    #             quality1=str(r1f.readline().strip(),encoding="utf8")

    #             header2=str(r2f.readline().strip(),encoding="utf8")
    #             seq2=str(r2f.readline().strip(),encoding="utf8")
    #             quaHeader2=str(r2f.readline().strip(),encoding="utf8")
    #             quality2=str(r2f.readline().strip(),encoding="utf8")

    #             if (not header1):
    #                 break
    #             barcodeLabel=judgeIfBarcode(seq1,seq2,barcodeInfo)
    #             for b in barcodeLabel:
    #                 if (barcodeLabel[b]):
    #                     readsInfoR1[b].append(header1)
    #                     readsInfoR1[b].append(seq1)
    #                     readsInfoR1[b].append(quaHeader1)
    #                     readsInfoR1[b].append(quality1)

    #                     readsInfoR2[b].append(header2)
    #                     readsInfoR2[b].append(seq2)
    #                     readsInfoR2[b].append(quaHeader2)
    #                     readsInfoR2[b].append(quality2)
                        
    #         for b in readsInfoR1:
    #             with open("./Output/test_"+b+"_R1.fastq","w") as out1:
    #                 with open("./Output/test_"+b+"_R2.fastq","w") as out2:
    #                     out1.write("\n".join(readsInfoR1[b])+"\n")
    #                     out2.write("\n".join(readsInfoR2[b])+"\n")
    
main()
