#! /bin/bash
# Author: Pablo Baeyens
# Usage: $0 name.pdf
# Splits pdf into individual pages
# Needs pdftk

# Gets number of pages in pdf
n=$(pdftk $1.pdf dump_data|grep NumberOfPages| awk '{print $2}')

for i in $(seq 1 $n); do
 pdftk A="$1.pdf" cat A$i output "$1$i.pdf"
done
