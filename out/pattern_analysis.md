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



| mentioned|oid     |entity                                             |entity_label                               |entity_class   |X  |
|---------:|:-------|:--------------------------------------------------|:------------------------------------------|:--------------|:--|
|        77|nbo.owl |http://purl.obolibrary.org/obo/uberon#has_quality  |has_quality                                |ObjectProperty |NA |
|        73|nbo.owl |http://purl.obolibrary.org/obo/BFO_0000056         |BFO_0000056                                |ObjectProperty |NA |
|        47|nbo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |quality                                    |Class          |NA |
|        22|dpo.owl |http://purl.obolibrary.org/obo/RO_0000052          |inheres_in                                 |ObjectProperty |NA |
|        21|dpo.owl |http://purl.obolibrary.org/obo/PATO_0000001        |quality                                    |Class          |NA |
|        21|dpo.owl |http://purl.obolibrary.org/obo/PATO_0000460        |abnormal                                   |Class          |NA |
|        21|dpo.owl |http://purl.obolibrary.org/obo/fbcv#qualifier      |qualifier                                  |ObjectProperty |NA |
|        21|nbo.owl |http://purl.obolibrary.org/obo/nbo#is_about        |is_about                                   |ObjectProperty |NA |
|        20|nbo.owl |http://purl.obolibrary.org/obo/nbo#in_response_to  |in_response_to                             |ObjectProperty |NA |
|        19|nbo.owl |http://purl.obolibrary.org/obo/RO_0002211          |regulates                                  |ObjectProperty |NA |
|        14|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000130         |liquid consumption                         |Class          |NA |
|        13|nbo.owl |http://purl.obolibrary.org/obo/pato#towards        |towards                                    |ObjectProperty |NA |
|        12|nbo.owl |http://purl.obolibrary.org/obo/nbo#has_participant |has_participant                            |ObjectProperty |NA |
|        10|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000064         |regulation of drinking behavior            |Class          |NA |
|         8|nbo.owl |http://purl.obolibrary.org/obo/nbo#by_means        |by_means                                   |ObjectProperty |NA |
|         6|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000308         |sensation behavior                         |Class          |NA |
|         5|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000134         |food consumption                           |Class          |NA |
|         5|nbo.owl |http://purl.obolibrary.org/obo/NBO_0000331         |nociceptive behavior                       |Class          |NA |
|         5|nbo.owl |http://purl.obolibrary.org/obo/PATO_0000912        |increased rate                             |Class          |NA |
|         5|nbo.owl |http://purl.obolibrary.org/obo/NBO_0001728         |behavioral response to addictive substance |Class          |NA |
