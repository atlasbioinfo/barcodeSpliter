# splitByBarcode

usage: barcodeSpliter [-h] [-sr SEARCHREGION] [-o OUTFOLDER] r1.fastq.gz r2.fastq.gz barcode.csv

This software can use barcode label to separate different samples in mixed-sample sequencing.

positional arguments:
  r1.fastq.gz           Sequencing reads, R1. Also support uncompressed format, like: r1.fastq
  r2.fastq.gz           Sequencing reads, R2. Also support uncompressed format, like: r2.fastq
  barcode.csv           csv file contains barcode info. eg:Barcode01,TAACTCGG,TAACAGTT

optional arguments:
  -h, --help            show this help message and exit
  -sr SEARCHREGION, --searchRegion SEARCHREGION
                        Barcode search region.Default is 20, means the first 20nt of reads.
  -o OUTFOLDER, --outfolder OUTFOLDER
                        The name of output folder can be customized. Default: ./Output/