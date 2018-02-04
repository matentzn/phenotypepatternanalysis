FROM maven:3-jdk-8
FROM rocker/hadleyverse

ENV WORKSPACE=/opt/phenotypeanalysis
ENV DATA=/data

ENV JAVA_OPTS='-Xmx20g -Xms12g'

VOLUME ${DATA}

RUN echo Building OLS && \
mkdir -p ${WORKSPACE} && \
cd ${WORKSPACE} && \
git clone https://github.com/matentzn/ontologyinferenceanalysis && \
git clone https://github.com/matentzn/patternextract && \
git clone https://github.com/matentzn/corpusdebugger && \
git clone https://github.com/matentzn/ebi.utilities && \
cd ${WORKSPACE}/ebi.utilities && \
mvn clean install && \
cd ${WORKSPACE}/patternextract && \
mvn clean compiler:compile package && \
cd ${WORKSPACE}/corpusdebugger && \
mvn clean compiler:compile package && \
cd ${WORKSPACE}/ontologyinferenceanalysis && \
mvn clean compiler:compile package

COPY run.sh ${WORKSPACE}/run.sh
COPY pattern_analysis.Rmd ${DATA}/pattern_analysis.Rmd

RUN chmod +x ${WORKSPACE}/run.sh

ENTRYPOINT ["/opt/phenotypeanalysis/run.sh"]
