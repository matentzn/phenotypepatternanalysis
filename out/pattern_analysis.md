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
## Warning in file(file, "rt"): cannot open file 'entitycounts.csv': No such
## file or directory
```

```
## Error in file(file, "rt"): cannot open the connection
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
