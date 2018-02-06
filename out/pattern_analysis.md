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



|oid     |entity                                             |entity_label                               | mentioned|entity_class   |X  |
|:-------|:--------------------------------------------------|:------------------------------------------|---------:|:--------------|:--|
|nbo.owl |http://purl.obolibrary.org/obo/uberon#has_quality  |has_quality                                |        77|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/BFO_0000056         |BFO_0000056                                |        73|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |quality                                    |        47|Class          |NA |
|dpo.owl |http://purl.obolibrary.org/obo/RO_0000052          |inheres_in                                 |        22|ObjectProperty |NA |
|dpo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |quality                                    |        21|Class          |NA |
|dpo.owl |http://purl.obolibrary.org/obo/PATO_0000460        |abnormal                                   |        21|Class          |NA |
|dpo.owl |http://purl.obolibrary.org/obo/fbcv#qualifier      |qualifier                                  |        21|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#is_about        |is_about                                   |        21|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#in_response_to  |in_response_to                             |        20|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/RO_0002211          |regulates                                  |        19|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000130         |liquid consumption                         |        14|Class          |NA |
|nbo.owl |http://purl.obolibrary.org/obo/pato#towards        |towards                                    |        13|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#has_participant |has_participant                            |        12|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000064         |regulation of drinking behavior            |        10|Class          |NA |
|nbo.owl |http://purl.obolibrary.org/obo/nbo#by_means        |by_means                                   |         8|ObjectProperty |NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000308         |sensation behavior                         |         6|Class          |NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000134         |food consumption                           |         5|Class          |NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000331         |nociceptive behavior                       |         5|Class          |NA |
|nbo.owl |http://purl.obolibrary.org/obo/PATO_0000912        |increased rate                             |         5|Class          |NA |
|nbo.owl |http://purl.obolibrary.org/obo/NBO_0001728         |behavioral response to addictive substance |         5|Class          |NA |
