#!/bin/bash

# Settings
repo=/ws/phenotypepatternanalysis
corpus=corpus_small.zip
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
docker run -v $data:/data  -p 4000:80 matentzn/ebi-patternanalysis-pipeline "-Xms1G -Xmx8G"
docker run -v $data/out:/data  -p 4000:80 matentzn/r-knitr
cp $data/out/*.md $results
cp $data/out/*.csv $results
zip -r $results/ontologies.zip $data/out/*.owl
