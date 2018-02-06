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



|entity_label                               |oid     |entity                                             | mentioned|entity_class   |X  |
|:------------------------------------------|:-------|:--------------------------------------------------|---------:|:--------------|:--|
|has_quality                                |nbo.owl |http://purl.obolibrary.org/obo/uberon#has_quality  |        77|ObjectProperty |NA |
|BFO_0000056                                |nbo.owl |http://purl.obolibrary.org/obo/BFO_0000056         |        73|ObjectProperty |NA |
|quality                                    |nbo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |        47|Class          |NA |
|inheres_in                                 |dpo.owl |http://purl.obolibrary.org/obo/RO_0000052          |        22|ObjectProperty |NA |
|quality                                    |dpo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |        21|Class          |NA |
|abnormal                                   |dpo.owl |http://purl.obolibrary.org/obo/PATO_0000460        |        21|Class          |NA |
|qualifier                                  |dpo.owl |http://purl.obolibrary.org/obo/fbcv#qualifier      |        21|ObjectProperty |NA |
|is_about                                   |nbo.owl |http://purl.obolibrary.org/obo/nbo#is_about        |        21|ObjectProperty |NA |
|in_response_to                             |nbo.owl |http://purl.obolibrary.org/obo/nbo#in_response_to  |        20|ObjectProperty |NA |
|regulates                                  |nbo.owl |http://purl.obolibrary.org/obo/RO_0002211          |        19|ObjectProperty |NA |
|liquid consumption                         |nbo.owl |http://purl.obolibrary.org/obo/NBO_0000130         |        14|Class          |NA |
|towards                                    |nbo.owl |http://purl.obolibrary.org/obo/pato#towards        |        13|ObjectProperty |NA |
|has_participant                            |nbo.owl |http://purl.obolibrary.org/obo/nbo#has_participant |        12|ObjectProperty |NA |
|regulation of drinking behavior            |nbo.owl |http://purl.obolibrary.org/obo/NBO_0000064         |        10|Class          |NA |
|by_means                                   |nbo.owl |http://purl.obolibrary.org/obo/nbo#by_means        |         8|ObjectProperty |NA |
|sensation behavior                         |nbo.owl |http://purl.obolibrary.org/obo/NBO_0000308         |         6|Class          |NA |
|food consumption                           |nbo.owl |http://purl.obolibrary.org/obo/NBO_0000134         |         5|Class          |NA |
|nociceptive behavior                       |nbo.owl |http://purl.obolibrary.org/obo/NBO_0000331         |         5|Class          |NA |
|increased rate                             |nbo.owl |http://purl.obolibrary.org/obo/PATO_0000912        |         5|Class          |NA |
|behavioral response to addictive substance |nbo.owl |http://purl.obolibrary.org/obo/NBO_0001728         |         5|Class          |NA |
