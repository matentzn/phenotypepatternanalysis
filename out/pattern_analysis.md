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



|entity_class   |entity_label                               |oid     | mentioned|entity                                             |X  |
|:--------------|:------------------------------------------|:-------|---------:|:--------------------------------------------------|:--|
|ObjectProperty |has_quality                                |nbo.owl |        77|http://purl.obolibrary.org/obo/uberon#has_quality  |NA |
|ObjectProperty |BFO_0000056                                |nbo.owl |        73|http://purl.obolibrary.org/obo/BFO_0000056         |NA |
|Class          |quality                                    |nbo.owl |        47|http://purl.obolibrary.org/obo/PATO_0000001        |NA |
|ObjectProperty |inheres_in                                 |dpo.owl |        22|http://purl.obolibrary.org/obo/RO_0000052          |NA |
|Class          |quality                                    |dpo.owl |        21|http://purl.obolibrary.org/obo/PATO_0000001        |NA |
|Class          |abnormal                                   |dpo.owl |        21|http://purl.obolibrary.org/obo/PATO_0000460        |NA |
|ObjectProperty |qualifier                                  |dpo.owl |        21|http://purl.obolibrary.org/obo/fbcv#qualifier      |NA |
|ObjectProperty |is_about                                   |nbo.owl |        21|http://purl.obolibrary.org/obo/nbo#is_about        |NA |
|ObjectProperty |in_response_to                             |nbo.owl |        20|http://purl.obolibrary.org/obo/nbo#in_response_to  |NA |
|ObjectProperty |regulates                                  |nbo.owl |        19|http://purl.obolibrary.org/obo/RO_0002211          |NA |
|Class          |liquid consumption                         |nbo.owl |        14|http://purl.obolibrary.org/obo/NBO_0000130         |NA |
|ObjectProperty |towards                                    |nbo.owl |        13|http://purl.obolibrary.org/obo/pato#towards        |NA |
|ObjectProperty |has_participant                            |nbo.owl |        12|http://purl.obolibrary.org/obo/nbo#has_participant |NA |
|Class          |regulation of drinking behavior            |nbo.owl |        10|http://purl.obolibrary.org/obo/NBO_0000064         |NA |
|ObjectProperty |by_means                                   |nbo.owl |         8|http://purl.obolibrary.org/obo/nbo#by_means        |NA |
|Class          |sensation behavior                         |nbo.owl |         6|http://purl.obolibrary.org/obo/NBO_0000308         |NA |
|Class          |food consumption                           |nbo.owl |         5|http://purl.obolibrary.org/obo/NBO_0000134         |NA |
|Class          |nociceptive behavior                       |nbo.owl |         5|http://purl.obolibrary.org/obo/NBO_0000331         |NA |
|Class          |increased rate                             |nbo.owl |         5|http://purl.obolibrary.org/obo/PATO_0000912        |NA |
|Class          |behavioral response to addictive substance |nbo.owl |         5|http://purl.obolibrary.org/obo/NBO_0001728         |NA |
