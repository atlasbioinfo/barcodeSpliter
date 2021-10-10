import sys,gzip,argparse,os,time

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

def findBarcode(seq,barcodeInfo,sr):
    resDict={}
    for b in barcodeInfo:
        resDict[b]=[findRes(seq[:sr].find(barcodeInfo[b][0])),
                   findRes(seq[:sr].find(barcodeInfo[b][1]))]
    return resDict

def judgeIfBarcode(seq1,seq2,barcodeInfo,sr):
    resDict1=findBarcode(seq1,barcodeInfo,sr)
    resDict2=findBarcode(seq2,barcodeInfo,sr)
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
    parser.add_argument("-sr","--searchRegion",default=20, help="Barcode search region.Default is 20, means the first 20nt of reads. ", type=str)
    parser.add_argument("-o","--outfolder",default="./Output/",help="The name of output folder can be customized. Default: ./Output/", type=str)
    args = parser.parse_args()
    return args

def main():
    args=getArg()
    if (not os.path.isdir(args.outfolder)):
        os.mkdir(args.outfolder)
    if (len(os.listdir(args.outfolder))!=0):
        inp=input("The output folder: "+args.outfolder+" is not empty! \
            \n\"barcodeSpliter\" may overwrite the exists files. \nDo you want to continue? Y/N : ")
        if (inp != "Y" and inp != "y"):
            showError(["May overwrite the following files:",", ".join(os.listdir(args.outfolder))])
            exit()

    # # Initial dict
    barcodeInfo=getBarcodeInfo(args.b)
    # statBarcode功能待完善
    statBarcode,readsInfoR1,readsInfoR2=initalDict(barcodeInfo)
    if (args.r1.split(".")[-1]=="gz"):
        r1f=gzip.open(args.r1,"r")
    else:
        r1f=open(args.r1,"r")
    if (args.r2.split(".")[-1]=="gz"):
        r2f=gzip.open(args.r2,"r")
    else:
        r2f=open(args.r2,"r")
    count=0
    loading="."
    while (True):
        count+=1
        if (count % 20000 == 0):
            print("Processed "+ str(count)+" reads"+loading,end="\r")
            if (len(loading)==1):
                loading=".."
                continue
            if (len(loading)==2):
                loading="..."
                continue
            if (len(loading)==3):
                loading="."
                continue
        header1=str(r1f.readline().strip(),encoding="utf8")
        seq1=str(r1f.readline().strip(),encoding="utf8")
        quaHeader1=str(r1f.readline().strip(),encoding="utf8")
        quality1=str(r1f.readline().strip(),encoding="utf8")

        header2=str(r2f.readline().strip(),encoding="utf8")
        seq2=str(r2f.readline().strip(),encoding="utf8")
        quaHeader2=str(r2f.readline().strip(),encoding="utf8")
        quality2=str(r2f.readline().strip(),encoding="utf8")

        if (not header1):
            break
        barcodeLabel=judgeIfBarcode(seq1,seq2,barcodeInfo,int(args.searchRegion))
        for b in barcodeLabel:
            if (barcodeLabel[b]):
                readsInfoR1[b].append(header1)
                readsInfoR1[b].append(seq1)
                readsInfoR1[b].append(quaHeader1)
                readsInfoR1[b].append(quality1)

                readsInfoR2[b].append(header2)
                readsInfoR2[b].append(seq2)
                readsInfoR2[b].append(quaHeader2)
                readsInfoR2[b].append(quality2)

                statBarcode[b]
    print("Write fastq files into the folder....")            
    for b in readsInfoR1:
        with gzip.open(os.path.join(args.outfolder,b+".R1.fastq.gz"),"w") as out1:
            with gzip.open(os.path.join(args.outfolder,b+".R2.fastq.gz"),"w") as out2:
                out1.write(str("\n".join(readsInfoR1[b])+"\n").encode())
                out2.write(str("\n".join(readsInfoR2[b])+"\n").encode())
    print("Success!")
    r1f.close()
    r2f.close()

if __name__ == "__main__":
    main()         

