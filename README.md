# barcodeSpliter

"barcodeSpliter" is a simple command-line tool that can split the mix-sampled sequencing by the barcode label, that is, demultiplex the sample. Currently at version V1.6, I have implemented this functionality most directly due to optimization issues that may require you to run more memory than the sequenced files. 

## Installation

```
# simple run
pip install barcodeSpliter

# if need upgrade

pip install -U barcodeSpliter
```

## E.g.:

```
barcodeSpliter ./example_data/test_r1.fastq.gz ./example_data/test_r2.fastq.gz ./example_data/barcode.tsv
```

## TO DO LIST:

1. support large sequencing files.
2. support muti-threads
3. add function: statistic barcode.

## Usage

```
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
```