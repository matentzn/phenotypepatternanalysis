FROM docker

ENV WORKSPACE=/opt/pheno_patterns

ENV DATA=/data
ENV CORPUS=${DATA}/corpus
ENV DATAOUT=${DATA}/out

VOLUME ${DATA}

RUN echo Run Complete Pattern Analysis Pipeline && \
mkdir -p ${WORKSPACE} && \
cd ${WORKSPACE} && \
docker pull matentzn/ebi-patternanalysis-pipeline && \
docker pull matentzn/r-knitr 

COPY run.sh ${WORKSPACE}/run.sh
COPY pattern_analysis.Rmd ${WORKSPACE}/pattern_analysis.Rmd
COPY in/corpus_small.zip ${WORKSPACE}/corpus.zip

RUN unzip corpus

RUN chmod +x ${WORKSPACE}/run.sh

ENTRYPOINT ["/opt/pheno_patterns/run.sh"]
