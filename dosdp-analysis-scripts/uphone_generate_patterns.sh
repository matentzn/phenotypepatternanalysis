#!/bin/bash

PATTERNS='/ws/upheno/src/patterns_rewritten'
OUT='/ws/upheno/src/out'
DOSDP='/ws/dosdp-tools/target/universal/stage/bin/'

cd $PATTERNS
for i in *.yaml; do
    [ -f "$i" ] || break
    #tsv=$(basename $i)".tsv"
    tsv="${i%.*}.tsv"
    echo $tsv
    /ws/dosdp-tools/target/universal/stage/bin/dosdp-tools generate --obo-prefixes=true --template=$i --infile=$tsv --outfile=$OUT/$i.owl
done
