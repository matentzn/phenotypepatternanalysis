[[Compatibility analysis of corpus /data/corpus]]

# Analysing individual ontologies for 
## Ontology: http://purl.obolibrary.org/obo/upheno/imports/pr_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/extra.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/ro_extra.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/chebi_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/dpo.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/pato_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/hsapdv.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/nbo_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/hp.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/cl_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/doid_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/mpath_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/abo_in_nbo.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/wbphenotype.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/pato.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/behavior.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


# Analyse Incompatibilites of Union

## Explanations

UNSAT:UBERON_0013173|http://purl.obolibrary.org/obo/UBERON_0013173
### Individual explanations: 

Axioms that impose constraints that might affect satisfiability
∃ RO_0002091.⊤ ⊑ occurrent
RO_0002202 ⊑ RO_0002258
part_of ⊑ RO_0002092
∃ RO_0002258.⊤ ⊑ continuant
RO_0002092 ⊑ RO_0002091
continuant ⊑ ¬ ∃ part_of.occurrent

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] UBERON_0003104
[-, -] X5 (∃ part_of.UBERON_0010066)
[-, -] X6 (∃ RO_0002202.UBERON_0002218)
[-, -] UBERON_0010066
[-, -] {UBERON_0013173}
[-, -] Nothing
[-, -] UBERON_0002218
[-] occurrent
[-, -] X3 (∃ part_of.UBERON_0001690)
[-, -, -] UBERON_0001756
[-, -, -, -] X5 (∃ part_of.UBERON_0010066)
[-, -, -, -] X6 (∃ RO_0002202.UBERON_0002218)
[-, -, -, -] UBERON_0010066
[-, -, -, -] {UBERON_0013173}
[-, -, -, -] Nothing
[-, -, -, -] UBERON_0002218
[-, -] X2 (∃ part_of.occurrent)
[-, -, -] X4 (∃ part_of.UBERON_0001756)
[-, -, -, -] X5 (∃ part_of.UBERON_0010066)
[-, -, -, -] X6 (∃ RO_0002202.UBERON_0002218)
[-, -, -, -] UBERON_0010066
[-, -, -, -] {UBERON_0013173}
[-, -, -, -] Nothing
[-, -, -, -] UBERON_0002218
[-] UBERON_0001690
[-, -] X5 (∃ part_of.UBERON_0010066)
[-, -] X6 (∃ RO_0002202.UBERON_0002218)
[-, -] UBERON_0010066
[-, -] {UBERON_0013173}
[-, -] Nothing
[-, -] UBERON_0002218
[-] X0 (¬(∃ part_of.occurrent))
[-, -] continuant
[-, -, -] X1 (∃ RO_0002202.UBERON_0003104)
[-, -, -, -] UBERON_0002514
[-, -, -, -, -] X5 (∃ part_of.UBERON_0010066)
[-, -, -, -, -] X6 (∃ RO_0002202.UBERON_0002218)
[-, -, -, -, -] UBERON_0010066
[-, -, -, -, -] {UBERON_0013173}
[-, -, -, -, -] Nothing
[-, -, -, -, -] UBERON_0002218

Other unsatisfiable classes in explanation: 
X5 (∃ part_of.UBERON_0010066)
X6 (∃ RO_0002202.UBERON_0002218)
UBERON_0010066
{UBERON_0013173}
UBERON_0002218


Axioms that impose constraints that might affect satisfiability
continuant ⊑ ¬ occurrent
RO_0002092 ⊑ RO_0002091
∃ RO_0002091.⊤ ⊑ occurrent
∃ RO_0002202.⊤ ⊑ independent continuant
part_of ⊑ RO_0002092

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] occurrent
[-, -] X2 (∃ part_of.UBERON_0010066)
[-, -, -] {UBERON_0013173}
[-, -, -] Nothing
[-] UBERON_0002342
[-, -] {UBERON_0013173}
[-, -] Nothing
[-] UBERON_0010066
[-, -] {UBERON_0013173}
[-, -] Nothing
[-] X0 (¬occurrent)
[-, -] continuant
[-, -, -] independent continuant
[-, -, -, -] X1 (∃ RO_0002202.UBERON_0002342)
[-, -, -, -, -] UBERON_0010313
[-, -, -, -, -, -] {UBERON_0013173}
[-, -, -, -, -, -] Nothing

Other unsatisfiable classes in explanation: 
{UBERON_0013173}


UNSAT:UBERON_2002101|http://purl.obolibrary.org/obo/UBERON_2002101
### Individual explanations: 

Axioms that impose constraints that might affect satisfiability
∃ RO_0002091.⊤ ⊑ occurrent
RO_0002202 ⊑ RO_0002258
part_of ⊑ RO_0002092
∃ RO_0002258.⊤ ⊑ continuant
RO_0002092 ⊑ RO_0002091
continuant ⊑ ¬ ∃ part_of.occurrent

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] occurrent
[-, -] X5 (∃ part_of.UBERON_0000467)
[-, -, -] UBERON_0011216
[-, -, -, -] UBERON_0000075
[-, -, -, -, -] X7 (∃ part_of.UBERON_0010323)
[-, -, -, -, -] UBERON_0003113
[-, -, -, -, -] X6 (∃ part_of.UBERON_0011137)
[-, -, -, -, -] {UBERON_2002101}
[-, -, -, -, -] UBERON_0010323
[-, -, -, -, -] Nothing
[-, -, -, -, -] UBERON_0011137
[-, -, -, -, -] X0 (∃ has part.UBERON_0005944)
[-, -, -, -, -] UBERON_0005944
[-, -, -, -, -] X2 (∃ part_of.UBERON_0003113)
[-, -] X3 (∃ part_of.occurrent)
[-, -, -] X7 (∃ part_of.UBERON_0010323)
[-, -, -] UBERON_0003113
[-, -, -] X6 (∃ part_of.UBERON_0011137)
[-, -, -] {UBERON_2002101}
[-, -, -] UBERON_0010323
[-, -, -] Nothing
[-, -, -] UBERON_0011137
[-, -, -] X0 (∃ has part.UBERON_0005944)
[-, -, -] UBERON_0005944
[-, -, -] X2 (∃ part_of.UBERON_0003113)
[-] UBERON_0003089
[-, -] X7 (∃ part_of.UBERON_0010323)
[-, -] UBERON_0003113
[-, -] X6 (∃ part_of.UBERON_0011137)
[-, -] {UBERON_2002101}
[-, -] UBERON_0010323
[-, -] Nothing
[-, -] UBERON_0011137
[-, -] X0 (∃ has part.UBERON_0005944)
[-, -] UBERON_0005944
[-, -] X2 (∃ part_of.UBERON_0003113)
[-] UBERON_0000467
[-, -] X7 (∃ part_of.UBERON_0010323)
[-, -] UBERON_0003113
[-, -] X6 (∃ part_of.UBERON_0011137)
[-, -] {UBERON_2002101}
[-, -] UBERON_0010323
[-, -] Nothing
[-, -] UBERON_0011137
[-, -] X0 (∃ has part.UBERON_0005944)
[-, -] UBERON_0005944
[-, -] X2 (∃ part_of.UBERON_0003113)
[-] X1 (¬(∃ part_of.occurrent))
[-, -] continuant
[-, -, -] X4 (∃ RO_0002202.UBERON_0003089)
[-, -, -, -] X7 (∃ part_of.UBERON_0010323)
[-, -, -, -] UBERON_0003113
[-, -, -, -] X6 (∃ part_of.UBERON_0011137)
[-, -, -, -] {UBERON_2002101}
[-, -, -, -] UBERON_0010323
[-, -, -, -] Nothing
[-, -, -, -] UBERON_0011137
[-, -, -, -] X0 (∃ has part.UBERON_0005944)
[-, -, -, -] UBERON_0005944
[-, -, -, -] X2 (∃ part_of.UBERON_0003113)

Other unsatisfiable classes in explanation: 
X7 (∃ part_of.UBERON_0010323)
UBERON_0003113
X6 (∃ part_of.UBERON_0011137)
{UBERON_2002101}
UBERON_0010323
UBERON_0011137
X0 (∃ has part.UBERON_0005944)
UBERON_0005944
X2 (∃ part_of.UBERON_0003113)


Axioms that impose constraints that might affect satisfiability
continuant ⊑ ¬ occurrent
∃ RO_0002091.⊤ ⊑ occurrent
RO_0002202 ⊑ RO_0002258
part_of ⊑ RO_0002092
∃ RO_0002258.⊤ ⊑ continuant
RO_0002092 ⊑ RO_0002091

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] occurrent
[-, -] X5 (∃ part_of.UBERON_0010323)
[-, -] UBERON_0003113
[-, -] {UBERON_2002101}
[-, -] UBERON_0010323
[-, -] Nothing
[-, -] UBERON_0011137
[-, -] X0 (∃ has part.UBERON_0005944)
[-, -] X4 (∃ part_of.UBERON_0011137)
[-, -] UBERON_0005944
[-, -] X1 (∃ part_of.UBERON_0003113)
[-] UBERON_0003089
[-, -] X5 (∃ part_of.UBERON_0010323)
[-, -] UBERON_0003113
[-, -] {UBERON_2002101}
[-, -] UBERON_0010323
[-, -] Nothing
[-, -] UBERON_0011137
[-, -] X0 (∃ has part.UBERON_0005944)
[-, -] X4 (∃ part_of.UBERON_0011137)
[-, -] UBERON_0005944
[-, -] X1 (∃ part_of.UBERON_0003113)
[-] X3 (¬occurrent)
[-, -] continuant
[-, -, -] X2 (∃ RO_0002202.UBERON_0003089)
[-, -, -, -] X5 (∃ part_of.UBERON_0010323)
[-, -, -, -] UBERON_0003113
[-, -, -, -] {UBERON_2002101}
[-, -, -, -] UBERON_0010323
[-, -, -, -] Nothing
[-, -, -, -] UBERON_0011137
[-, -, -, -] X0 (∃ has part.UBERON_0005944)
[-, -, -, -] X4 (∃ part_of.UBERON_0011137)
[-, -, -, -] UBERON_0005944
[-, -, -, -] X1 (∃ part_of.UBERON_0003113)

Other unsatisfiable classes in explanation: 
X5 (∃ part_of.UBERON_0010323)
UBERON_0003113
{UBERON_2002101}
UBERON_0010323
UBERON_0011137
X0 (∃ has part.UBERON_0005944)
X4 (∃ part_of.UBERON_0011137)
UBERON_0005944
X1 (∃ part_of.UBERON_0003113)


## Frequently used axioms across unsatisfiability explanations
### RO_0002092 ⊑ RO_0002091|4
Used in: 
http://purl.obolibrary.org/obo/dpo.owl
### part_of ⊑ RO_0002092|4
Used in: 
http://purl.obolibrary.org/obo/dpo.owl
### ∃ RO_0002091.⊤ ⊑ occurrent|4
Used in: 
http://purl.obolibrary.org/obo/dpo.owl
### ∃ RO_0002258.⊤ ⊑ continuant|3
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
### RO_0002202 ⊑ RO_0002258|3
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
### UBERON_0010323 ⊑ ∃ part_of.UBERON_0011137|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0003113 ⊑ ∃ part_of.UBERON_0010323|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_2002101 ⊑ ∃ part_of.UBERON_0003113|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0005944 ⊑ ∃ RO_0002202.UBERON_0003089|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### continuant ⊑ ¬ ∃ part_of.occurrent|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
### UBERON_0011137 ⊑ ∃ has part.UBERON_0005944|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0005944 ⊑ ∃ part_of.UBERON_0011137|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0013173 ⊑ ∃ part_of.UBERON_0010066|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### continuant ⊑ ¬ occurrent|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
http://purl.obolibrary.org/obo/dpo.owl
### UBERON_0001756 ⊑ ∃ part_of.UBERON_0001690|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0002218 ⊑ UBERON_0002514|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0013173 ⊑ UBERON_0010313|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### ∃ RO_0002202.⊤ ⊑ independent continuant|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
### UBERON_0002514 ⊑ ∃ RO_0002202.UBERON_0003104|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0010313 ⊑ ∃ RO_0002202.UBERON_0002342|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### independent continuant ⊑ continuant|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
http://purl.obolibrary.org/obo/dpo.owl
### UBERON_0011216 ⊑ ∃ part_of.UBERON_0000467|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0011137 ⊑ UBERON_0000075|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0002218 ⊑ ∃ part_of.UBERON_0001756|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0000075 ⊑ UBERON_0011216|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0010066 ⊑ ∃ RO_0002202.UBERON_0002218|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl

