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
```

```
## Error in read.table(file = file, header = header, sep = sep, quote = quote, : no lines available in input
```

```r
#df_p<-read.csv(pattern_file)

df_ec<-df_ec[order(-df_ec$mentioned),]
```

```
## Error in eval(expr, envir, enclos): object 'df_ec' not found
```

```r
kable(head(df_ec,20),row.names = FALSE)
```

```
## Error in head(df_ec, 20): object 'df_ec' not found
```
