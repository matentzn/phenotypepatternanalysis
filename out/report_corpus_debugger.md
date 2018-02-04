[[Compatibility analysis of corpus /data/corpus]]

# Analysing individual ontologies for 
## Ontology: http://purl.obolibrary.org/obo/upheno/imports/pr_import.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/upheno.owl
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


## Ontology: http://purl.obolibrary.org/obo/MF/external/GO_import.owl
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


## Ontology: http://purl.obolibrary.org/obo/mp.owl
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


## Ontology: http://purl.obolibrary.org/obo/hp.owl
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


## Ontology: http://purl.obolibrary.org/obo/MF/external/ontology-metadata-slim.owl
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


## Ontology: http://purl.obolibrary.org/obo/MF/external/behavior-slim.owl
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


## Ontology: http://purl.obolibrary.org/obo/MF.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/MF/internal/MF-core.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/MFOEM.owl
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


## Ontology: http://purl.obolibrary.org/obo/upheno/imports/nbo_import.owl
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


## Ontology: http://purl.obolibrary.org/obo/abo_in_nbo.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/bfo.owl
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


## Ontology: http://purl.obolibrary.org/obo/MF/external/bfo-properties-slim.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


## Ontology: http://purl.obolibrary.org/obo/iao/ontology-metadata.owl
### Profile Conformance

### Consistency analysis
Consistent:true
#### Unsatisfiable Classes
Nothing


# Analyse Incompatibilites of Union

## Explanations

UNSAT:UBERON_2002101|http://purl.obolibrary.org/obo/UBERON_2002101
### Individual explanations: 

Axioms that impose constraints that might affect satisfiability
continuant ⊑ ¬ occurrent
RO_0002092 ⊑ RO_0002091
∃ RO_0002091.⊤ ⊑ occurrent
part_of ⊑ RO_0002092

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] occurrent
[-, -] X1 (∃ part_of.UBERON_0003113)
[-, -, -] {UBERON_2002101}
[-, -, -] Nothing
[-] UBERON_0003113
[-, -] {UBERON_2002101}
[-, -] Nothing
[-] X0 (¬occurrent)
[-, -] continuant
[-, -, -] independent continuant
[-, -, -, -] UBERON_0001062
[-, -, -, -, -] UBERON_0000477
[-, -, -, -, -, -] {UBERON_2002101}
[-, -, -, -, -, -] Nothing

Other unsatisfiable classes in explanation: 
{UBERON_2002101}


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


UNSAT:hydrometrocolpos|http://purl.obolibrary.org/obo/MP_0003537
### Individual explanations: 

Axioms that impose constraints that might affect satisfiability
∃ RO_0002258.⊤ ⊑ continuant
continuant ⊑ ¬ occurrent
RO_0002092 ⊑ RO_0002091
∃ RO_0002091.⊤ ⊑ occurrent
RO_0002202 ⊑ RO_0002258
part_of ⊑ RO_0002092

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] UBERON_0000164
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-] occurrent
[-, -] X4 (∃ part_of.UBERON_0003975)
[-, -, -] {hydrometrocolpos}
[-, -, -] Nothing
[-, -, -] abnormal vagina morphology
[-, -, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -, -] UBERON_0000996
[-] X5 (¬occurrent)
[-, -] continuant
[-, -, -] X2 (∃ RO_0002202.UBERON_0000164)
[-, -, -, -] {hydrometrocolpos}
[-, -, -, -] Nothing
[-, -, -, -] abnormal vagina morphology
[-, -, -, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -, -, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -, -, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -, -, -] UBERON_0000996
[-] X6 (∃ has modifier.abnormal)
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-] abnormal
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-] morphology
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-] UBERON_0003975
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -] X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] X1 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996

Other unsatisfiable classes in explanation: 
{hydrometrocolpos}
abnormal vagina morphology
X0 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
X3 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
X1 (∃ inheres_in.UBERON_0000996)
UBERON_0000996


Axioms that impose constraints that might affect satisfiability
∃ RO_0002091.⊤ ⊑ occurrent
RO_0002202 ⊑ RO_0002258
part_of ⊑ RO_0002092
∃ RO_0002258.⊤ ⊑ continuant
RO_0002092 ⊑ RO_0002091
continuant ⊑ ¬ ∃ part_of.occurrent

Class Hierarchy of Explanation (unsat class marked with {}, Classnames like X1 are named anonymous classes:
[-] UBERON_0000164
[-, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-] occurrent
[-, -] X3 (∃ part_of.occurrent)
[-, -, -] X7 (∃ part_of.UBERON_0003975)
[-, -, -, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -, -, -] {hydrometrocolpos}
[-, -, -, -] Nothing
[-, -, -, -] abnormal vagina morphology
[-, -, -, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -, -, -] UBERON_0000996
[-, -, -, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-, -] X1 (∃ part_of.UBERON_0000990)
[-, -, -] UBERON_0005156
[-, -, -, -] UBERON_0003133
[-, -, -, -, -] UBERON_0004175
[-, -, -, -, -, -] UBERON_0003975
[-, -, -, -, -, -, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -, -, -, -, -, -] {hydrometrocolpos}
[-, -, -, -, -, -, -] Nothing
[-, -, -, -, -, -, -] abnormal vagina morphology
[-, -, -, -, -, -, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -, -, -, -, -, -] UBERON_0000996
[-, -, -, -, -, -, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-] UBERON_0000990
[-, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-] X8 (∃ has modifier.abnormal)
[-, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-] abnormal
[-, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-] X0 (¬(∃ part_of.occurrent))
[-, -] continuant
[-, -, -] X5 (∃ RO_0002202.UBERON_0000164)
[-, -, -, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -, -, -] {hydrometrocolpos}
[-, -, -, -] Nothing
[-, -, -, -] abnormal vagina morphology
[-, -, -, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -, -, -] UBERON_0000996
[-, -, -, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))
[-] morphology
[-, -] X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
[-, -] {hydrometrocolpos}
[-, -] Nothing
[-, -] abnormal vagina morphology
[-, -] X4 (∃ inheres_in.UBERON_0000996)
[-, -] UBERON_0000996
[-, -] X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))

Other unsatisfiable classes in explanation: 
X6 (morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))
{hydrometrocolpos}
abnormal vagina morphology
X4 (∃ inheres_in.UBERON_0000996)
UBERON_0000996
X2 (∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal)))


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
### continuant ⊑ ¬ occurrent|3
Used in: 
http://purl.obolibrary.org/obo/bfo.owl
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
http://purl.obolibrary.org/obo/dpo.owl
### UBERON_0000996 ⊑ ∃ RO_0002202.UBERON_0000164|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_2002101 ⊑ ∃ part_of.UBERON_0003113|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### hydrometrocolpos ⊑ abnormal vagina morphology|2
Used in: 
http://purl.obolibrary.org/obo/upheno.owl
http://purl.obolibrary.org/obo/mp.owl
### UBERON_0000996 ⊑ ∃ part_of.UBERON_0003975|2
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### abnormal vagina morphology ≡ ∃ has part.(morphology ⊓ (∃ inheres_in.UBERON_0000996) ⊓ (∃ has modifier.abnormal))|2
Used in: 
http://purl.obolibrary.org/obo/mp.owl
### UBERON_0005156 ⊑ ∃ part_of.UBERON_0000990|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0000477 ⊑ UBERON_0001062|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0010323 ⊑ ∃ part_of.UBERON_0011137|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0003113 ⊑ ∃ part_of.UBERON_0010323|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0001062 ⊑ independent continuant|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
### UBERON_0005944 ⊑ ∃ RO_0002202.UBERON_0003089|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### independent continuant ⊑ continuant|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/bfo.owl
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
http://purl.obolibrary.org/obo/dpo.owl
### UBERON_0004175 ⊑ UBERON_0003133|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### continuant ⊑ ¬ ∃ part_of.occurrent|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/ro_import.owl
### UBERON_0011137 ⊑ ∃ has part.UBERON_0005944|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0005944 ⊑ ∃ part_of.UBERON_0011137|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_2002101 ⊑ UBERON_0000477|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0003975 ⊑ UBERON_0004175|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl
### UBERON_0003133 ⊑ UBERON_0005156|1
Used in: 
http://purl.obolibrary.org/obo/upheno/imports/go_import.owl
http://purl.obolibrary.org/obo/upheno/imports/uberon_import.owl

