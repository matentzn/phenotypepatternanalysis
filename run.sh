#!/bin/bash

docker run -v ${DATA}:/data  -p 4000:80 matentzn/ebi-patternanalysis-pipeline
docker run -v ${DATAOUT}:/data  -p 4000:80 matentzn/r-knitr
