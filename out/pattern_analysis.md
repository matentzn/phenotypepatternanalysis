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



|entity_label                               |entity_class   | mentioned|entity                                             |oid     |X  |
|:------------------------------------------|:--------------|---------:|:--------------------------------------------------|:-------|:--|
|has_quality                                |ObjectProperty |        77|http://purl.obolibrary.org/obo/uberon#has_quality  |nbo.owl |NA |
|BFO_0000056                                |ObjectProperty |        73|http://purl.obolibrary.org/obo/BFO_0000056         |nbo.owl |NA |
|quality                                    |Class          |        47|http://purl.obolibrary.org/obo/PATO_0000001        |nbo.owl |NA |
|inheres_in                                 |ObjectProperty |        22|http://purl.obolibrary.org/obo/RO_0000052          |dpo.owl |NA |
|quality                                    |Class          |        21|http://purl.obolibrary.org/obo/PATO_0000001        |dpo.owl |NA |
|abnormal                                   |Class          |        21|http://purl.obolibrary.org/obo/PATO_0000460        |dpo.owl |NA |
|qualifier                                  |ObjectProperty |        21|http://purl.obolibrary.org/obo/fbcv#qualifier      |dpo.owl |NA |
|is_about                                   |ObjectProperty |        21|http://purl.obolibrary.org/obo/nbo#is_about        |nbo.owl |NA |
|in_response_to                             |ObjectProperty |        20|http://purl.obolibrary.org/obo/nbo#in_response_to  |nbo.owl |NA |
|regulates                                  |ObjectProperty |        19|http://purl.obolibrary.org/obo/RO_0002211          |nbo.owl |NA |
|liquid consumption                         |Class          |        14|http://purl.obolibrary.org/obo/NBO_0000130         |nbo.owl |NA |
|towards                                    |ObjectProperty |        13|http://purl.obolibrary.org/obo/pato#towards        |nbo.owl |NA |
|has_participant                            |ObjectProperty |        12|http://purl.obolibrary.org/obo/nbo#has_participant |nbo.owl |NA |
|regulation of drinking behavior            |Class          |        10|http://purl.obolibrary.org/obo/NBO_0000064         |nbo.owl |NA |
|by_means                                   |ObjectProperty |         8|http://purl.obolibrary.org/obo/nbo#by_means        |nbo.owl |NA |
|sensation behavior                         |Class          |         6|http://purl.obolibrary.org/obo/NBO_0000308         |nbo.owl |NA |
|food consumption                           |Class          |         5|http://purl.obolibrary.org/obo/NBO_0000134         |nbo.owl |NA |
|nociceptive behavior                       |Class          |         5|http://purl.obolibrary.org/obo/NBO_0000331         |nbo.owl |NA |
|increased rate                             |Class          |         5|http://purl.obolibrary.org/obo/PATO_0000912        |nbo.owl |NA |
|behavioral response to addictive substance |Class          |         5|http://purl.obolibrary.org/obo/NBO_0001728         |nbo.owl |NA |
