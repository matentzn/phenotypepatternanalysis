#!/bin/bash

# Settings
repo=/ws/phenotypepatternanalysis
corpus=corpus_mphpdpo.zip
data=/data/dockerdata

# Pipeline
results=$repo/out
corpus_archive=$repo/in/$corpus

rm -r $results
mkdir $results

rm -r $data
mkdir $data
mkdir $data/out

cp $corpus_archive $data/corpus.zip
cd $data
unzip corpus.zip
docker pull matentzn/ebi-patternanalysis-pipeline
docker pull matentzn/r-knitr
docker run -v $data:/data -e XMS='4G' -e XMX='10G' -e SAMPLESIZE='100' -p 4000:80 matentzn/ebi-patternanalysis-pipeline
docker run -v $data/out:/data -p 4000:80 matentzn/r-knitr
cp $data/out/*.md $results
cp $data/out/*.csv $results
zip -r $results/ontologies.zip $data/out/*.owl
