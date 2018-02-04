#!/bin/bash

data=/data/dockerdata
results=/ws/phenotypepatternanalysis/out

rm -r $results
mkdir $results
docker build --no-cache -t ppa .
docker run -v $data:/data  -p 4000:80 ppa
cp $data/*.txt $results
cp $data/*.md $results
cp $data/*.csv $results
cd /ws/phenotypepatternanalysis
Rscript -e "library(knitr); knit('pattern_analysis.Rmd')"

zip -r $results/ontologies.zip $data/*.owl
