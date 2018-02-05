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



|entity                                             | mentioned|oid     |entity_label                               |entity_class   |X  |
|:--------------------------------------------------|---------:|:-------|:------------------------------------------|:--------------|:--|
|http://purl.obolibrary.org/obo/uberon#has_quality  |        77|nbo.owl |has_quality                                |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/BFO_0000056         |        73|nbo.owl |BFO_0000056                                |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/PATO_0000001        |        47|nbo.owl |quality                                    |Class          |NA |
|http://purl.obolibrary.org/obo/RO_0000052          |        22|dpo.owl |inheres_in                                 |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/PATO_0000001        |        21|dpo.owl |quality                                    |Class          |NA |
|http://purl.obolibrary.org/obo/PATO_0000460        |        21|dpo.owl |abnormal                                   |Class          |NA |
|http://purl.obolibrary.org/obo/fbcv#qualifier      |        21|dpo.owl |qualifier                                  |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/nbo#is_about        |        21|nbo.owl |is_about                                   |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/nbo#in_response_to  |        20|nbo.owl |in_response_to                             |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/RO_0002211          |        19|nbo.owl |regulates                                  |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/NBO_0000130         |        14|nbo.owl |liquid consumption                         |Class          |NA |
|http://purl.obolibrary.org/obo/pato#towards        |        13|nbo.owl |towards                                    |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/nbo#has_participant |        12|nbo.owl |has_participant                            |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/NBO_0000064         |        10|nbo.owl |regulation of drinking behavior            |Class          |NA |
|http://purl.obolibrary.org/obo/nbo#by_means        |         8|nbo.owl |by_means                                   |ObjectProperty |NA |
|http://purl.obolibrary.org/obo/NBO_0000308         |         6|nbo.owl |sensation behavior                         |Class          |NA |
|http://purl.obolibrary.org/obo/NBO_0000134         |         5|nbo.owl |food consumption                           |Class          |NA |
|http://purl.obolibrary.org/obo/NBO_0000331         |         5|nbo.owl |nociceptive behavior                       |Class          |NA |
|http://purl.obolibrary.org/obo/PATO_0000912        |         5|nbo.owl |increased rate                             |Class          |NA |
|http://purl.obolibrary.org/obo/NBO_0001728         |         5|nbo.owl |behavioral response to addictive substance |Class          |NA |
