---
title: "Phenotype Analysis"
author: "Nicolas Matentzoglu"
date: "12/01/2018"
output: html_document
editor_options:
  chunk_output_type: console
---




```r
df_ec<-read.csv(entity_count_file)
#df_p<-read.csv(pattern_file)

df_ec<-df_ec[order(-df_ec$mentioned),]
kable(head(df_ec,20),row.names = FALSE)
```



|oid     |entity                                             |entity_class   |entity_label                               | mentioned|X  |
|:-------|:--------------------------------------------------|:--------------|:------------------------------------------|---------:|:--|
|nbo.owl |http://purl.obolibrary.org/obo/uberon#has_quality  |ObjectProperty |has_quality                                |        77|NA |
|nbo.owl |http://purl.obolibrary.org/obo/BFO_0000056         |ObjectProperty |BFO_0000056                                |        73|NA |
|nbo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |Class          |quality                                    |        47|NA |
|dpo.owl |http://purl.obolibrary.org/obo/RO_0000052          |ObjectProperty |inheres_in                                 |        22|NA |
|dpo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |Class          |quality                                    |        21|NA |
|dpo.owl |http://purl.obolibrary.org/obo/PATO_0000460        |Class          |abnormal                                   |        21|NA |
|dpo.owl |http://purl.obolibrary.org/obo/fbcv#qualifier      |ObjectProperty |qualifier                                  |        21|NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#is_about        |ObjectProperty |is_about                                   |        21|NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#in_response_to  |ObjectProperty |in_response_to                             |        20|NA |
|nbo.owl |http://purl.obolibrary.org/obo/RO_0002211          |ObjectProperty |regulates                                  |        19|NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000130         |Class          |liquid consumption                         |        14|NA |
|nbo.owl |http://purl.obolibrary.org/obo/pato#towards        |ObjectProperty |towards                                    |        13|NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#has_participant |ObjectProperty |has_participant                            |        12|NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000064         |Class          |regulation of drinking behavior            |        10|NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#by_means        |ObjectProperty |by_means                                   |         8|NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000308         |Class          |sensation behavior                         |         6|NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000134         |Class          |food consumption                           |         5|NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000331         |Class          |nociceptive behavior                       |         5|NA |
|nbo.owl |http://purl.obolibrary.org/obo/PATO_0000912        |Class          |increased rate                             |         5|NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0001728         |Class          |behavioral response to addictive substance |         5|NA |
