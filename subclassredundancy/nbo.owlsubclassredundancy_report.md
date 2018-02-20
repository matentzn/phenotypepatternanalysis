# Analysing: http://purl.obolibrary.org/obo/nbo.owl
* Loading ontology..
* done.. (T: 96 sec)
## Imports
http://purl.obolibrary.org/obo/go.owl
http://purl.obolibrary.org/obo/uberon.owl
http://purl.obolibrary.org/obo/chebi.owl
http://purl.obolibrary.org/obo/pato.owl
* Creating analysis ontologies..
* done.. (T: 9 sec)
* Performing reasoning..
* done.. (T: 209 sec)
* Performing analysis..
* done.. (T: 0 sec)
## Bug: Axioms that were implied before removing subclasses, but are not anymore
Restricted to maximum 50 axioms
## Branches of interest: 
## How many subclasses are recapitulated (i.e. redundant) wrt. defined classes?
Restricted to maximum 50 axioms
* food consumption SubClassOf feeding behavior
* water consumption SubClassOf liquid consumption
* alcohol consumption SubClassOf liquid consumption
* saccharin consumption SubClassOf food consumption
* food aversion SubClassOf food preference/aversion
* food preference SubClassOf food preference/aversion
* rapid eye movement sleep SubClassOf sleeping behavior
* motor learning SubClassOf associative learning behavior
* vocal learning SubClassOf associative learning behavior
* mating frequency SubClassOf mating behavior phenotype
* NREM frequency SubClassOf non-rapid eye movement sleep behavior phenotype
* NREM duration SubClassOf non-rapid eye movement sleep behavior phenotype
* REM frequency SubClassOf rapid eye movement sleep phenotype
* REM duration SubClassOf rapid eye movement sleep phenotype
* feeding behavior SubClassOf consumption behavior
* regulation of cocaine consumption SubClassOf regulation of consumption of an addictive substance
* language learning behavior SubClassOf learning behavior
* fear conditioning SubClassOf classical conditioning
* conditioned emotional response SubClassOf associative learning behavior
* behavioral response to xenobiotics SubClassOf behavioral response to chemical stimulus
* jaw movement conditioning behavior SubClassOf classical conditioning
* eye blink conditioning behavior SubClassOf classical conditioning
* vocal aggression behavior SubClassOf aggressive behavior
* regulation of drinking behavior SubClassOf regulation of feeding behavior
* regulation of eating behavior SubClassOf regulation of feeding behavior
* regulation of water consumption SubClassOf regulation of drinking behavior
* regulation of nicotine consumption SubClassOf regulation of consumption of an addictive substance
* regulation of alcohol consumption SubClassOf regulation of drinking behavior
* behavioral response to alcohol SubClassOf behavioral response to addictive substance
* auditory behavior SubClassOf sensation behavior
* visual behavior SubClassOf sensation behavior
* cold sensation behavior SubClassOf thermosensory behavior
* hot sensation behavior SubClassOf thermosensory behavior
* taste behavior SubClassOf chemosensory behavior
* olfactory behavior SubClassOf chemosensory behavior
* thermosensory behavior SubClassOf cutaneous sensation behavior
* touch related behavior SubClassOf cutaneous sensation behavior
* nociceptive behavior SubClassOf cutaneous sensation behavior
* thermal nociceptive behavior SubClassOf nociceptive behavior
* mechanical nociceptive behavior SubClassOf nociceptive behavior
* chemical nociceptive behavior SubClassOf nociceptive behavior
* limb posture SubClassOf posture
* body posture SubClassOf posture
* reflexive behavior SubClassOf involuntary movement behavior
* regulation of saccharin consumption SubClassOf regulation of eating behavior
* regulation of morphine consumption SubClassOf regulation of consumption of an addictive substance
* adipsia SubClassOf decreased frequency of drinking
* chemosensory behavior SubClassOf behavioral response to chemical stimulus
* shape constancy behavior SubClassOf perceptual constancy behavior
* colour constancy behavior SubClassOf perceptual constancy behavior
* size constancy behavior SubClassOf perceptual constancy behavior
## Summary
* All implied Subclass axioms: 12047
* Implied axioms after stripping: 137
* All asserted SubClassOf axioms: 29366
* Union: 12047
* Diff: 11910
* Redundant (implications): 137
* Redundant (assertions): 90
* Only after: 0
* Only before: 11910
