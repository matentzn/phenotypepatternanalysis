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



|oid     |entity_label                               |entity                                             | mentioned|entity_class   |X  |
|:-------|:------------------------------------------|:--------------------------------------------------|---------:|:--------------|:--|
|nbo.owl |has_quality                                |http://purl.obolibrary.org/obo/uberon#has_quality  |        77|ObjectProperty |NA |
|nbo.owl |BFO_0000056                                |http://purl.obolibrary.org/obo/BFO_0000056         |        73|ObjectProperty |NA |
|nbo.owl |quality                                    |http://purl.obolibrary.org/obo/PATO_0000001        |        47|Class          |NA |
|dpo.owl |inheres_in                                 |http://purl.obolibrary.org/obo/RO_0000052          |        22|ObjectProperty |NA |
|dpo.owl |quality                                    |http://purl.obolibrary.org/obo/PATO_0000001        |        21|Class          |NA |
|dpo.owl |abnormal                                   |http://purl.obolibrary.org/obo/PATO_0000460        |        21|Class          |NA |
|dpo.owl |qualifier                                  |http://purl.obolibrary.org/obo/fbcv#qualifier      |        21|ObjectProperty |NA |
|nbo.owl |is_about                                   |http://purl.obolibrary.org/obo/nbo#is_about        |        21|ObjectProperty |NA |
|nbo.owl |in_response_to                             |http://purl.obolibrary.org/obo/nbo#in_response_to  |        20|ObjectProperty |NA |
|nbo.owl |regulates                                  |http://purl.obolibrary.org/obo/RO_0002211          |        19|ObjectProperty |NA |
|nbo.owl |liquid consumption                         |http://purl.obolibrary.org/obo/NBO_0000130         |        14|Class          |NA |
|nbo.owl |towards                                    |http://purl.obolibrary.org/obo/pato#towards        |        13|ObjectProperty |NA |
|nbo.owl |has_participant                            |http://purl.obolibrary.org/obo/nbo#has_participant |        12|ObjectProperty |NA |
|nbo.owl |regulation of drinking behavior            |http://purl.obolibrary.org/obo/NBO_0000064         |        10|Class          |NA |
|nbo.owl |by_means                                   |http://purl.obolibrary.org/obo/nbo#by_means        |         8|ObjectProperty |NA |
|nbo.owl |sensation behavior                         |http://purl.obolibrary.org/obo/NBO_0000308         |         6|Class          |NA |
|nbo.owl |food consumption                           |http://purl.obolibrary.org/obo/NBO_0000134         |         5|Class          |NA |
|nbo.owl |nociceptive behavior                       |http://purl.obolibrary.org/obo/NBO_0000331         |         5|Class          |NA |
|nbo.owl |increased rate                             |http://purl.obolibrary.org/obo/PATO_0000912        |         5|Class          |NA |
|nbo.owl |behavioral response to addictive substance |http://purl.obolibrary.org/obo/NBO_0001728         |         5|Class          |NA |
