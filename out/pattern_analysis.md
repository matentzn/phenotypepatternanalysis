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



|entity_class   |oid     |entity_label                               | mentioned|entity                                             |X  |
|:--------------|:-------|:------------------------------------------|---------:|:--------------------------------------------------|:--|
|ObjectProperty |nbo.owl |has_quality                                |        77|http://purl.obolibrary.org/obo/uberon#has_quality  |NA |
|ObjectProperty |nbo.owl |BFO_0000056                                |        73|http://purl.obolibrary.org/obo/BFO_0000056         |NA |
|Class          |nbo.owl |quality                                    |        47|http://purl.obolibrary.org/obo/PATO_0000001        |NA |
|ObjectProperty |dpo.owl |inheres_in                                 |        22|http://purl.obolibrary.org/obo/RO_0000052          |NA |
|Class          |dpo.owl |quality                                    |        21|http://purl.obolibrary.org/obo/PATO_0000001        |NA |
|Class          |dpo.owl |abnormal                                   |        21|http://purl.obolibrary.org/obo/PATO_0000460        |NA |
|ObjectProperty |dpo.owl |qualifier                                  |        21|http://purl.obolibrary.org/obo/fbcv#qualifier      |NA |
|ObjectProperty |nbo.owl |is_about                                   |        21|http://purl.obolibrary.org/obo/nbo#is_about        |NA |
|ObjectProperty |nbo.owl |in_response_to                             |        20|http://purl.obolibrary.org/obo/nbo#in_response_to  |NA |
|ObjectProperty |nbo.owl |regulates                                  |        19|http://purl.obolibrary.org/obo/RO_0002211          |NA |
|Class          |nbo.owl |liquid consumption                         |        14|http://purl.obolibrary.org/obo/NBO_0000130         |NA |
|ObjectProperty |nbo.owl |towards                                    |        13|http://purl.obolibrary.org/obo/pato#towards        |NA |
|ObjectProperty |nbo.owl |has_participant                            |        12|http://purl.obolibrary.org/obo/nbo#has_participant |NA |
|Class          |nbo.owl |regulation of drinking behavior            |        10|http://purl.obolibrary.org/obo/NBO_0000064         |NA |
|ObjectProperty |nbo.owl |by_means                                   |         8|http://purl.obolibrary.org/obo/nbo#by_means        |NA |
|Class          |nbo.owl |sensation behavior                         |         6|http://purl.obolibrary.org/obo/NBO_0000308         |NA |
|Class          |nbo.owl |food consumption                           |         5|http://purl.obolibrary.org/obo/NBO_0000134         |NA |
|Class          |nbo.owl |nociceptive behavior                       |         5|http://purl.obolibrary.org/obo/NBO_0000331         |NA |
|Class          |nbo.owl |increased rate                             |         5|http://purl.obolibrary.org/obo/PATO_0000912        |NA |
|Class          |nbo.owl |behavioral response to addictive substance |         5|http://purl.obolibrary.org/obo/NBO_0001728         |NA |
