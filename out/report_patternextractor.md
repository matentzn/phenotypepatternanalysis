
# Definitions Impact
Report only considers patterns with at least 100 indirect instances.
See generated dataset for complete view of the data.
http://ebi.ac.uk#Pattern824
BFO_0000056 some . 
    (NBO_0000313 . 
     and (has_quality some PATO_0000001)) . 
Direct SubClasses overall: 5
Indirect SubClasses overall: 166
Direct SubClasses nbo.owl: 5
Indirect SubClasses nbo.owl: 165

http://ebi.ac.uk#Pattern246
BFO_0000056 some 
    (GO_0008150
     and (has_quality some PATO_0000001))
Direct SubClasses overall: 0
Indirect SubClasses overall: 115
Indirect SubClasses nbo.owl: 114

http://ebi.ac.uk#Pattern485
BFO_0000056 some 
    (Thing
     and (has_quality some PATO_0000001))
Direct SubClasses overall: 0
Indirect SubClasses overall: 177
Indirect SubClasses nbo.owl: 176


# Prominent relations used across definitions

* qualifier|onts:[dpo.owl, nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#qualifier>, <http://purl.obolibrary.org/obo/fbcv#qualifier>]
## http://purl.obolibrary.org/obo/nbo#qualifier
* hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
* adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
## http://purl.obolibrary.org/obo/fbcv#qualifier
* chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
* locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* feeding behavior defective ≡ quality ⊓ (∃ inheres_in.feeding behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* hatching behavior defective ≡ quality ⊓ (∃ inheres_in.hatching behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* memory defective ≡ quality ⊓ (∃ inheres_in.memory) ⊓ (∃ qualifier.abnormal) | dpo.owl
* behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* mating rhythm defective ≡ quality ⊓ (∃ inheres_in.circadian mating behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* learning defective ≡ quality ⊓ (∃ inheres_in.learning) ⊓ (∃ qualifier.abnormal) | dpo.owl
* courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
* eclosion rhythm defective ≡ quality ⊓ (∃ inheres_in.eclosion rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
* locomotor rhythm defective ≡ quality ⊓ (∃ inheres_in.locomotor rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
* jump response defective ≡ quality ⊓ (∃ inheres_in.jump response) ⊓ (∃ qualifier.abnormal) | dpo.owl
* song defective ≡ quality ⊓ (∃ inheres_in.male courtship behavior, veined wing generated song production) ⊓ (∃ qualifier.abnormal) | dpo.owl
* visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* proboscis extension reflex defective ≡ quality ⊓ (∃ inheres_in.proboscis extension reflex) ⊓ (∃ qualifier.abnormal) | dpo.owl
* circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* grooming behavior defective ≡ quality ⊓ (∃ inheres_in.grooming behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* optomotor response defective ≡ quality ⊓ (∃ inheres_in.optokinetic behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* oviposition defective ≡ quality ⊓ (∃ inheres_in.oviposition) ⊓ (∃ qualifier.abnormal) | dpo.owl
* photoperiod response variant ≡ quality ⊓ (∃ inheres_in.entrainment of circadian clock by photoperiod) ⊓ (∃ qualifier.abnormal) | dpo.owl

* has_role|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/chebi#has_role>]
## http://purl.obolibrary.org/obo/chebi#has_role
* behavioral response to xenobiotics ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.(∃ has_role.CHEBI_35703)) | nbo.owl

* part_of|onts:[dpo.owl]|rels:[<http://purl.obolibrary.org/obo/BFO_0000050>]
## http://purl.obolibrary.org/obo/BFO_0000050
* courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
* mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl

* has_participant|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#has_participant>]
## http://purl.obolibrary.org/obo/nbo#has_participant
* feeding behavior ≡ consumption behavior ⊓ ((∃ has_participant.CHEBI_33290) ⊔ (∃ has_participant.PATO_0000145)) | nbo.owl
* regulation of alcohol preference behavior ≡ regulation of drinking preference behavior ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
* alcohol consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
* saccharin consumption ≡ food consumption ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
* cocaine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_27958) | nbo.owl
* limb posture ≡ posture ⊓ (∃ has_participant.UBERON_0002101) | nbo.owl
* nicotine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_18723) | nbo.owl
* food consumption ≡ feeding behavior ⊓ (∃ has_participant.CHEBI_33290) | nbo.owl
* morphine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_17303) | nbo.owl
* water consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_15377) | nbo.owl
* regulation of saccharin preference behavior ≡ regulation of eating preference behavior ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
* body posture ≡ posture ⊓ (∃ has_participant.UBERON_0000309) | nbo.owl

* BFO_0000056|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/BFO_0000056>]
## http://purl.obolibrary.org/obo/BFO_0000056
* mating preference ≡ ∃ BFO_0000056.(regulation of mating preference ⊓ (∃ has_quality.rate)) | nbo.owl
* behavioral control of lacrimation phenotype ≡ ∃ BFO_0000056.(behavioral control of lacrimation ⊓ (∃ has_quality.quality)) | nbo.owl
* voluntary movement behavior phenotype ≡ ∃ BFO_0000056.(voluntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
* NREM frequency ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
* circadian behavior phenotype ≡ ∃ BFO_0000056.(circadian behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* emotional behavior phenotype ≡ ∃ BFO_0000056.(emotional behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* mating behavior phenotype ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* emission behavior phenotype ≡ ∃ BFO_0000056.(emission behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* behavioral control of excretion phenotype ≡ ∃ BFO_0000056.(behavioral control of excretion ⊓ (∃ has_quality.quality)) | nbo.owl
* social behavior phenotype ≡ ∃ BFO_0000056.(GO_0035176 ⊓ (∃ has_quality.quality)) | nbo.owl
* rhythmic behavior phenotype ≡ ∃ BFO_0000056.(rhythmic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* memory behavior behavior ≡ ∃ BFO_0000056.(memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* food aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.decreased rate)) | nbo.owl
* sensation behavior phenotype ≡ ∃ BFO_0000056.(sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* alcohol aversion ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.decreased rate)) | nbo.owl
* sleeping behavior phenotype ≡ ∃ BFO_0000056.(sleeping behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* reproductive behavior phenotype ≡ ∃ BFO_0000056.(reproductive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* post-mating behavior phenotype ≡ ∃ BFO_0000056.(GO_0045297 ⊓ (∃ has_quality.quality)) | nbo.owl
* copulation phenotype ≡ ∃ BFO_0000056.(copulation ⊓ (∃ has_quality.quality)) | nbo.owl
* male courtship behavior phenotype ≡ ∃ BFO_0000056.(male courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* behavioral control of production of sound phenotype ≡ ∃ BFO_0000056.(behavioral control of production of sound ⊓ (∃ has_quality.quality)) | nbo.owl
* increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
* crying behavior phenotype ≡ ∃ BFO_0000056.(GO_0060273 ⊓ (∃ has_quality.quality)) | nbo.owl
* dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* chemosensory behavior phenotype ≡ ∃ BFO_0000056.(chemosensory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* vocalization behavior phenotype ≡ ∃ BFO_0000056.(vocalization behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* mating frequency ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
* rapid eye movement sleep phenotype ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.quality)) | nbo.owl
* liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* food preference ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.increased rate)) | nbo.owl
* locomotory behavior phenotype ≡ ∃ BFO_0000056.(locomotory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* behavioral control of urination phenotype ≡ ∃ BFO_0000056.(behavioral control of urination ⊓ (∃ has_quality.quality)) | nbo.owl
* involuntary movement behavior phenotype ≡ ∃ BFO_0000056.(involuntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* auditory behavior phenotype ≡ ∃ BFO_0000056.(GO_0031223 ⊓ (∃ has_quality.quality)) | nbo.owl
* cutaneous sensation behavior phenotype ≡ ∃ BFO_0000056.(cutaneous sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* drinking behavior phenotype ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has_quality.quality)) | nbo.owl
* polyphagia ≡ ∃ BFO_0000056.(food consumption ⊓ (∃ has_quality.increased rate)) | nbo.owl
* REM frequency ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.frequency)) | nbo.owl
* female courtship behavior phenotype ≡ ∃ BFO_0000056.(GO_0008050 ⊓ (∃ has_quality.quality)) | nbo.owl
* courtship behavior phenotype ≡ ∃ BFO_0000056.(courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* somatic sensation related behavior phenotype ≡ ∃ BFO_0000056.(somatic sensation related behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* visual behavior phenotype ≡ ∃ BFO_0000056.(visual behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* sleep duration ≡ ∃ BFO_0000056.(sleep ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
* alcohol preference ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
* kinesthetic behavior phenotype ≡ ∃ BFO_0000056.(kinesthetic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* cognitive behavior phenotype ≡ ∃ BFO_0000056.(cognitive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* NREM duration ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
* male sexual activity phenotype ≡ ∃ BFO_0000056.(male sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
* female sexual activity phenotype ≡ ∃ BFO_0000056.(female sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
* REM duration ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
* learning behavior phenotype ≡ ∃ BFO_0000056.(learning behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* food preference/aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.rate)) | nbo.owl
* behavioral control of defecation phenotype ≡ ∃ BFO_0000056.(behavioral control of defecation ⊓ (∃ has_quality.quality)) | nbo.owl
* feeding behavior phenotype ≡ ∃ BFO_0000056.(feeding behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* sexual activity phenotype ≡ ∃ BFO_0000056.(sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
* eating behavior phenotype ≡ ∃ BFO_0000056.(GO_0042755 ⊓ (∃ has_quality.quality)) | nbo.owl
* learning and/or memory behavior phenotype ≡ ∃ BFO_0000056.(learning and/or memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* non-rapid eye movement sleep behavior phenotype ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* vestibular behavior phenotype ≡ ∃ BFO_0000056.(vestibular behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* motor coordination phenotype ≡ ∃ BFO_0000056.(motor coordination ⊓ (∃ has_quality.quality)) | nbo.owl
* saccharin preference ≡ ∃ BFO_0000056.(regulation of saccharin preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
* polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
* behavioral control of external secretion phenotype ≡ ∃ BFO_0000056.(behavioral control of external secretion ⊓ (∃ has_quality.quality)) | nbo.owl
* olfactory behavior phenotype ≡ ∃ BFO_0000056.(olfactory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* mobbing calling phenotype ≡ ∃ BFO_0000056.(mobbing calling ⊓ (∃ has_quality.quality)) | nbo.owl

* by_means|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#by_means>]
## http://purl.obolibrary.org/obo/nbo#by_means
* behavioral control of urination ≡ behavioral control of excretion ⊓ (∃ by_means.UBERON_0001256) ⊓ (∃ is_about.GO_0060073) | nbo.owl
* visual hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0002104) | nbo.owl
* behavioral control of lacrimation ≡ behavioral control of external secretion ⊓ (∃ by_means.UBERON_0001817) ⊓ (∃ is_about.GO_0070075) | nbo.owl
* vocal aggression behavior ≡ aggressive behavior ⊓ (∃ by_means.vocalization behavior) | nbo.owl
* reflexive behavior ≡ involuntary movement behavior ⊓ (∃ by_means.reflex) | nbo.owl
* irritable aggressive behavior ≡ GO_0002118 ⊓ (∃ by_means.irritability behavior) | nbo.owl
* auditory hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0002105) | nbo.owl
* olfactory hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0005725) | nbo.owl

* regulates|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/RO_0002211>]
## http://purl.obolibrary.org/obo/RO_0002211
* regulation of addiction response ≡ ∃ regulates.addiction response | nbo.owl
* regulation of water consumption ≡ ∃ regulates.water consumption | nbo.owl
* increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
* regulation of nicotine consumption ≡ ∃ regulates.nicotine consumption | nbo.owl
* regulation of alcohol consumption ≡ ∃ regulates.alcohol consumption | nbo.owl
* regulation of drinking behavior ≡ ∃ regulates.liquid consumption | nbo.owl
* regulation of feeding behavior ≡ ∃ regulates.(liquid consumption ⊔ food consumption) | nbo.owl
* regulation of withdrawal response ≡ ∃ regulates.withdrawal response | nbo.owl
* regulation of morphine consumption ≡ ∃ regulates.morphine consumption | nbo.owl
* regulation of sexual activity ≡ ∃ regulates.sexual activity | nbo.owl
* regulation of behavioral response to chemical stimulus ≡ ∃ regulates.behavioral response to chemical stimulus | nbo.owl
* regulation of consumption behavior ≡ ∃ regulates.consumption behavior | nbo.owl
* regulation of eating behavior ≡ ∃ regulates.food consumption | nbo.owl
* regulation of cocaine consumption ≡ ∃ regulates.cocaine consumption | nbo.owl
* regulation of consumption of an addictive substance ≡ ∃ regulates.consumption of an addictive substance | nbo.owl
* regulation of saccharin consumption ≡ ∃ regulates.saccharin consumption | nbo.owl
* polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
* regulation of behavioral response to addictive substance ≡ ∃ regulates.behavioral response to addictive substance | nbo.owl
* regulation of behavior ≡ ∃ regulates.behavior | nbo.owl

* is_about|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#is_about>]
## http://purl.obolibrary.org/obo/nbo#is_about
* behavioral control of urination ≡ behavioral control of excretion ⊓ (∃ by_means.UBERON_0001256) ⊓ (∃ is_about.GO_0060073) | nbo.owl
* behavioral control of lacrimation ≡ behavioral control of external secretion ⊓ (∃ by_means.UBERON_0001817) ⊓ (∃ is_about.GO_0070075) | nbo.owl
* vocal learning ≡ associative learning behavior ⊓ (∃ is_about.vocalization behavior) | nbo.owl
* behavioral control of external secretion ≡ emission behavior ⊓ (∃ is_about.GO_0007589) | nbo.owl
* colour constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.color) | nbo.owl
* rapid eye movement sleep ≡ sleeping behavior ⊓ (∃ is_about.GO_0042747) | nbo.owl
* size constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.size) | nbo.owl
* form perception behavior ≡ sensation behavior ⊓ (∃ is_about.shape) | nbo.owl
* shape constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.shape) | nbo.owl
* emotional conditioning ≡ classical conditioning ⊓ (∃ is_about.emotional behavior) | nbo.owl
* motor learning ≡ associative learning behavior ⊓ (∃ is_about.motor coordination) | nbo.owl
* behavioral control of defecation ≡ behavioral control of excretion ⊓ (∃ is_about.GO_0030421) | nbo.owl
* spatial perception ≡ sensation behavior ⊓ (∃ is_about.size) | nbo.owl
* circadian behavior ≡ rhythmic behavior ⊓ (∃ is_about.circadian rhythm) | nbo.owl
* depth perception behavior ≡ sensation behavior ⊓ (∃ is_about.PATO_0001595) | nbo.owl
* eye blink conditioning behavior ≡ classical conditioning ⊓ (∃ is_about.blinking) | nbo.owl
* jaw movement conditioning behavior ≡ classical conditioning ⊓ (∃ is_about.jaw movement) | nbo.owl
* fear conditioning ≡ classical conditioning ⊓ (∃ is_about.fear-related behavior) | nbo.owl
* language learning behavior ≡ learning behavior ⊓ (∃ is_about.language communication behavior) | nbo.owl
* distance perception behavior ≡ spatial perception ⊓ (∃ is_about.PATO_0000040) | nbo.owl
* behavioral control of excretion ≡ emission behavior ⊓ (∃ is_about.GO_0007588) | nbo.owl

* in_response_to|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#in_response_to>]
## http://purl.obolibrary.org/obo/nbo#in_response_to
* visual behavior ≡ sensation behavior ⊓ (∃ in_response_to.GO_0007601) | nbo.owl
* thermosensory behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0050955) | nbo.owl
* cold sensation behavior ≡ thermosensory behavior ⊓ (∃ in_response_to.PATO_0001306) | nbo.owl
* hot sensation behavior ≡ thermosensory behavior ⊓ (∃ in_response_to.PATO_0001305) | nbo.owl
* thermal nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050965) | nbo.owl
* behavioral response to morphine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.morphine consumption) | nbo.owl
* nociceptive behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0019233) | nbo.owl
* behavioral response to xenobiotics ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.(∃ has_role.CHEBI_35703)) | nbo.owl
* electrical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050967) | nbo.owl
* taste behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of taste) | nbo.owl
* chemical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050968) | nbo.owl
* mechanical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050966) | nbo.owl
* olfactory behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of smell) | nbo.owl
* behavioral response to alcohol ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.alcohol consumption) | nbo.owl
* touch related behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.sensory perception of touch) | nbo.owl
* chemosensory behavior ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.sensory perception of chemical stimulus) | nbo.owl
* conditioned emotional response ≡ associative learning behavior ⊓ (∃ in_response_to.emotional conditioning) | nbo.owl
* behavioral response to cocaine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.cocaine consumption) | nbo.owl
* behavioral response to nicotine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.nicotine consumption) | nbo.owl
* auditory behavior ≡ sensation behavior ⊓ (∃ in_response_to.sensory perception of sound) | nbo.owl

* towards|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/pato#towards>]
## http://purl.obolibrary.org/obo/pato#towards
* increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* anhedonia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.pleasure behavior)) | nbo.owl
* dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* depressive disorder ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.depression behavior)) | nbo.owl
* aphagia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.GO_0042755)) | nbo.owl
* liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* forgetfulness ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.memory loss behavior)) | nbo.owl
* frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* has-input|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#has-input>]
## http://purl.obolibrary.org/obo/nbo#has-input
* increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
* increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
* polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl

* inheres_in|onts:[dpo.owl]|rels:[<http://purl.obolibrary.org/obo/RO_0000052>]
## http://purl.obolibrary.org/obo/RO_0000052
* chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
* locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* feeding behavior defective ≡ quality ⊓ (∃ inheres_in.feeding behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* hatching behavior defective ≡ quality ⊓ (∃ inheres_in.hatching behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* memory defective ≡ quality ⊓ (∃ inheres_in.memory) ⊓ (∃ qualifier.abnormal) | dpo.owl
* behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* mating rhythm defective ≡ quality ⊓ (∃ inheres_in.circadian mating behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* learning defective ≡ quality ⊓ (∃ inheres_in.learning) ⊓ (∃ qualifier.abnormal) | dpo.owl
* courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
* eclosion rhythm defective ≡ quality ⊓ (∃ inheres_in.eclosion rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
* locomotor rhythm defective ≡ quality ⊓ (∃ inheres_in.locomotor rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
* jump response defective ≡ quality ⊓ (∃ inheres_in.jump response) ⊓ (∃ qualifier.abnormal) | dpo.owl
* song defective ≡ quality ⊓ (∃ inheres_in.male courtship behavior, veined wing generated song production) ⊓ (∃ qualifier.abnormal) | dpo.owl
* visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* proboscis extension reflex defective ≡ quality ⊓ (∃ inheres_in.proboscis extension reflex) ⊓ (∃ qualifier.abnormal) | dpo.owl
* circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* grooming behavior defective ≡ quality ⊓ (∃ inheres_in.grooming behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* optomotor response defective ≡ quality ⊓ (∃ inheres_in.optokinetic behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
* uncoordinated ≡ uncoordinated ⊓ (∃ inheres_in.organism) | dpo.owl
* oviposition defective ≡ quality ⊓ (∃ inheres_in.oviposition) ⊓ (∃ qualifier.abnormal) | dpo.owl
* photoperiod response variant ≡ quality ⊓ (∃ inheres_in.entrainment of circadian clock by photoperiod) ⊓ (∃ qualifier.abnormal) | dpo.owl

* has_quality|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/uberon#has_quality>]
## http://purl.obolibrary.org/obo/uberon#has_quality
* mating preference ≡ ∃ BFO_0000056.(regulation of mating preference ⊓ (∃ has_quality.rate)) | nbo.owl
* behavioral control of lacrimation phenotype ≡ ∃ BFO_0000056.(behavioral control of lacrimation ⊓ (∃ has_quality.quality)) | nbo.owl
* voluntary movement behavior phenotype ≡ ∃ BFO_0000056.(voluntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
* NREM frequency ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
* circadian behavior phenotype ≡ ∃ BFO_0000056.(circadian behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* emotional behavior phenotype ≡ ∃ BFO_0000056.(emotional behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* aphagia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.GO_0042755)) | nbo.owl
* liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* mating behavior phenotype ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* emission behavior phenotype ≡ ∃ BFO_0000056.(emission behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* behavioral control of excretion phenotype ≡ ∃ BFO_0000056.(behavioral control of excretion ⊓ (∃ has_quality.quality)) | nbo.owl
* social behavior phenotype ≡ ∃ BFO_0000056.(GO_0035176 ⊓ (∃ has_quality.quality)) | nbo.owl
* rhythmic behavior phenotype ≡ ∃ BFO_0000056.(rhythmic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* memory behavior behavior ≡ ∃ BFO_0000056.(memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* food aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.decreased rate)) | nbo.owl
* sensation behavior phenotype ≡ ∃ BFO_0000056.(sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* alcohol aversion ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.decreased rate)) | nbo.owl
* sleeping behavior phenotype ≡ ∃ BFO_0000056.(sleeping behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* reproductive behavior phenotype ≡ ∃ BFO_0000056.(reproductive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* post-mating behavior phenotype ≡ ∃ BFO_0000056.(GO_0045297 ⊓ (∃ has_quality.quality)) | nbo.owl
* copulation phenotype ≡ ∃ BFO_0000056.(copulation ⊓ (∃ has_quality.quality)) | nbo.owl
* male courtship behavior phenotype ≡ ∃ BFO_0000056.(male courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* behavioral control of production of sound phenotype ≡ ∃ BFO_0000056.(behavioral control of production of sound ⊓ (∃ has_quality.quality)) | nbo.owl
* increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
* crying behavior phenotype ≡ ∃ BFO_0000056.(GO_0060273 ⊓ (∃ has_quality.quality)) | nbo.owl
* dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* depressive disorder ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.depression behavior)) | nbo.owl
* chemosensory behavior phenotype ≡ ∃ BFO_0000056.(chemosensory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* vocalization behavior phenotype ≡ ∃ BFO_0000056.(vocalization behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* mating frequency ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
* rapid eye movement sleep phenotype ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.quality)) | nbo.owl
* liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* food preference ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.increased rate)) | nbo.owl
* locomotory behavior phenotype ≡ ∃ BFO_0000056.(locomotory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* behavioral control of urination phenotype ≡ ∃ BFO_0000056.(behavioral control of urination ⊓ (∃ has_quality.quality)) | nbo.owl
* involuntary movement behavior phenotype ≡ ∃ BFO_0000056.(involuntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* auditory behavior phenotype ≡ ∃ BFO_0000056.(GO_0031223 ⊓ (∃ has_quality.quality)) | nbo.owl
* cutaneous sensation behavior phenotype ≡ ∃ BFO_0000056.(cutaneous sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* forgetfulness ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.memory loss behavior)) | nbo.owl
* increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
* drinking behavior phenotype ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has_quality.quality)) | nbo.owl
* anhedonia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.pleasure behavior)) | nbo.owl
* polyphagia ≡ ∃ BFO_0000056.(food consumption ⊓ (∃ has_quality.increased rate)) | nbo.owl
* REM frequency ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.frequency)) | nbo.owl
* female courtship behavior phenotype ≡ ∃ BFO_0000056.(GO_0008050 ⊓ (∃ has_quality.quality)) | nbo.owl
* courtship behavior phenotype ≡ ∃ BFO_0000056.(courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* somatic sensation related behavior phenotype ≡ ∃ BFO_0000056.(somatic sensation related behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* visual behavior phenotype ≡ ∃ BFO_0000056.(visual behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* sleep duration ≡ ∃ BFO_0000056.(sleep ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
* alcohol preference ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
* kinesthetic behavior phenotype ≡ ∃ BFO_0000056.(kinesthetic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* cognitive behavior phenotype ≡ ∃ BFO_0000056.(cognitive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* NREM duration ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
* male sexual activity phenotype ≡ ∃ BFO_0000056.(male sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
* female sexual activity phenotype ≡ ∃ BFO_0000056.(female sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
* REM duration ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
* learning behavior phenotype ≡ ∃ BFO_0000056.(learning behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* food preference/aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.rate)) | nbo.owl
* behavioral control of defecation phenotype ≡ ∃ BFO_0000056.(behavioral control of defecation ⊓ (∃ has_quality.quality)) | nbo.owl
* feeding behavior phenotype ≡ ∃ BFO_0000056.(feeding behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* sexual activity phenotype ≡ ∃ BFO_0000056.(sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
* eating behavior phenotype ≡ ∃ BFO_0000056.(GO_0042755 ⊓ (∃ has_quality.quality)) | nbo.owl
* learning and/or memory behavior phenotype ≡ ∃ BFO_0000056.(learning and/or memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* non-rapid eye movement sleep behavior phenotype ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* vestibular behavior phenotype ≡ ∃ BFO_0000056.(vestibular behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* motor coordination phenotype ≡ ∃ BFO_0000056.(motor coordination ⊓ (∃ has_quality.quality)) | nbo.owl
* saccharin preference ≡ ∃ BFO_0000056.(regulation of saccharin preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
* polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
* behavioral control of external secretion phenotype ≡ ∃ BFO_0000056.(behavioral control of external secretion ⊓ (∃ has_quality.quality)) | nbo.owl
* olfactory behavior phenotype ≡ ∃ BFO_0000056.(olfactory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
* mobbing calling phenotype ≡ ∃ BFO_0000056.(mobbing calling ⊓ (∃ has_quality.quality)) | nbo.owl

# Prominent classes used across definitions
Omitting classes that only occur in one definition

## regulation of drinking preference behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_16236>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000138> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000911> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000137> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000912> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0002702 EquivalentTo NBO_0002660 and (has_participant some CHEBI_16236)
  * nbo.owl
* NBO_0000138 EquivalentTo BFO_0000056 some 
(NBO_0002660 and (has_quality some 
(PATO_0000911 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000137 EquivalentTo BFO_0000056 some 
(NBO_0002660 and (has_quality some 
(PATO_0000912 and (towards some NBO_0000130))))
  * nbo.owl

## regulation of saccharin preference behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000143> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002794> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002794> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002743> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_32111>)) )]
* NBO_0000143 EquivalentTo BFO_0000056 some 
(NBO_0002794 and (has_quality some PATO_0000912))
  * nbo.owl
* NBO_0002794 EquivalentTo NBO_0002743 and (has_participant some CHEBI_32111)
  * nbo.owl

## behavioral response to addictive substance|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001987> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0001915>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002021> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0001952>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002065> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0002086>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001763> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0000131>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0003104> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0001728>) )]
* NBO_0001987 EquivalentTo NBO_0001728 and (in_response_to some NBO_0001915)
  * nbo.owl
* NBO_0002021 EquivalentTo NBO_0001728 and (in_response_to some NBO_0001952)
  * nbo.owl
* NBO_0002065 EquivalentTo NBO_0001728 and (in_response_to some NBO_0002086)
  * nbo.owl
* NBO_0001763 EquivalentTo NBO_0001728 and (in_response_to some NBO_0000131)
  * nbo.owl
* NBO_0003104 EquivalentTo RO_0002211 some NBO_0001728
  * nbo.owl

## consumption behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001845> ObjectUnionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/PATO_0000145>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002169> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0001845>) )]
* NBO_0000079 EquivalentTo NBO_0001845 and ((has_participant some CHEBI_33290) or (has_participant some PATO_0000145))
  * nbo.owl
* NBO_0002169 EquivalentTo RO_0002211 some NBO_0001845
  * nbo.owl

## PATO_0000145|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001845> ObjectUnionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/PATO_0000145>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000851> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000886> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000542> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>))) )]
* NBO_0000079 EquivalentTo NBO_0001845 and ((has_participant some CHEBI_33290) or (has_participant some PATO_0000145))
  * nbo.owl
* NBO_0000851 EquivalentTo BFO_0000056 some 
(GO_0042756 and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563))))
  * nbo.owl
* NBO_0000886 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (RO_0002211 some (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))))
  * nbo.owl
* NBO_0000542 EquivalentTo BFO_0000056 some 
((NBO_0000064 and (RO_0002211 some NBO_0000130) and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))) and (qualifier some PATO_0001333))
  * nbo.owl

## feeding behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001845> ObjectUnionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/PATO_0000145>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000270> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>)) )]
* NBO_0000079 EquivalentTo NBO_0001845 and ((has_participant some CHEBI_33290) or (has_participant some PATO_0000145))
  * nbo.owl
* NBO_0000270 EquivalentTo BFO_0000056 some 
(NBO_0000079 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000134 EquivalentTo NBO_0000079 and (has_participant some CHEBI_33290)
  * nbo.owl

## CHEBI_32111|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000136> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_32111>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002794> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002743> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_32111>)) )]
* NBO_0000136 EquivalentTo NBO_0000134 and (has_participant some CHEBI_32111)
  * nbo.owl
* NBO_0002794 EquivalentTo NBO_0002743 and (has_participant some CHEBI_32111)
  * nbo.owl

## decreased frequency|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000993> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002519> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000993 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0002519 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl

## increased frequency|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000961> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000543> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000541> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000961 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000543 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001333) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000541 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl

## sensation behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000466> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0001595>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000314> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0007601>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000655> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000465> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000052>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000746> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000117>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000316> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0007605>)) )]
* NBO_0000466 EquivalentTo NBO_0000308 and (is_about some PATO_0001595)
  * nbo.owl
* NBO_0000314 EquivalentTo NBO_0000308 and (in_response_to some GO_0007601)
  * nbo.owl
* NBO_0000655 EquivalentTo BFO_0000056 some 
(NBO_0000308 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000465 EquivalentTo NBO_0000308 and (is_about some PATO_0000052)
  * nbo.owl
* NBO_0000746 EquivalentTo NBO_0000308 and (is_about some PATO_0000117)
  * nbo.owl
* NBO_0000316 EquivalentTo NBO_0000308 and (in_response_to some GO_0007605)
  * nbo.owl

## size|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000461> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000225> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000117>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000746> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000117>)) )]
* NBO_0000461 EquivalentTo NBO_0000225 and (is_about some PATO_0000117)
  * nbo.owl
* NBO_0000746 EquivalentTo NBO_0000308 and (is_about some PATO_0000117)
  * nbo.owl

## behavioral response to chemical stimulus|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000322> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001632> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0007606>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0003047> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0001632>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001679> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001632> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/chebi#has_role> <http://purl.obolibrary.org/obo/CHEBI_35703>))) )]
* NBO_0000322 EquivalentTo NBO_0001632 and (in_response_to some GO_0007606)
  * nbo.owl
* NBO_0003047 EquivalentTo RO_0002211 some NBO_0001632
  * nbo.owl
* NBO_0001679 EquivalentTo NBO_0001632 and (in_response_to some (has_role some CHEBI_35703))
  * nbo.owl

## PATO_0001563|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000851> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000886> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000542> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>))) )]
* NBO_0000851 EquivalentTo BFO_0000056 some 
(GO_0042756 and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563))))
  * nbo.owl
* NBO_0000886 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (RO_0002211 some (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))))
  * nbo.owl
* NBO_0000542 EquivalentTo BFO_0000056 some 
((NBO_0000064 and (RO_0002211 some NBO_0000130) and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))) and (qualifier some PATO_0001333))
  * nbo.owl

## increased rate|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000141> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060259> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000546> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000137> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000912> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000143> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002794> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000140> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) )]
* NBO_0000141 EquivalentTo BFO_0000056 some 
(GO_0060259 and (has_quality some PATO_0000912))
  * nbo.owl
* NBO_0000546 EquivalentTo BFO_0000056 some 
(NBO_0000134 and (has_quality some PATO_0000912))
  * nbo.owl
* NBO_0000137 EquivalentTo BFO_0000056 some 
(NBO_0002660 and (has_quality some 
(PATO_0000912 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000143 EquivalentTo BFO_0000056 some 
(NBO_0002794 and (has_quality some PATO_0000912))
  * nbo.owl
* NBO_0000140 EquivalentTo BFO_0000056 some 
(NBO_0002702 and (has_quality some PATO_0000912))
  * nbo.owl

## decreased rate|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000142> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060259> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000911>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000139> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000911>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000138> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000911> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000142 EquivalentTo BFO_0000056 some 
(GO_0060259 and (has_quality some PATO_0000911))
  * nbo.owl
* NBO_0000139 EquivalentTo BFO_0000056 some 
(NBO_0002702 and (has_quality some PATO_0000911))
  * nbo.owl
* NBO_0000138 EquivalentTo BFO_0000056 some 
(NBO_0002660 and (has_quality some 
(PATO_0000911 and (towards some NBO_0000130))))
  * nbo.owl

## emotional conditioning|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000221> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000171> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0000778>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000778> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000208> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000003>)) )]
* NBO_0000221 EquivalentTo NBO_0000171 and (in_response_to some NBO_0000778)
  * nbo.owl
* NBO_0000778 EquivalentTo NBO_0000208 and (is_about some NBO_0000003)
  * nbo.owl

## PATO_0001333|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000543> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000542> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>))) )]
* NBO_0000543 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001333) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000542 EquivalentTo BFO_0000056 some 
((NBO_0000064 and (RO_0002211 some NBO_0000130) and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))) and (qualifier some PATO_0001333))
  * nbo.owl

## quality|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000403> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007635>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000774> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000042> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000644> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000403> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000414> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007626>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000669> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0035187>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000474> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0048512> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000601> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000003> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000768> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000035> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000387> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007610>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000769> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000564> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0035176> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000473> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000008> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000767> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000170> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000655> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000419> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000024> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000755> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0019098> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000757> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0045297> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000762> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007620> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000761> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0008049> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000772> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000036> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000419> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007631>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000775> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060273> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000398> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007613>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007635> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000777> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000037> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000401> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0035648>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000397> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007612>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000754> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042747> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000399> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007619> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007619>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000396> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0008062>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000720> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007630>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000009> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007626> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000771> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000040> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000643> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000388> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000658> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0031223> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000657> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000680> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007637>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000412> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007634>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0006004> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0018991>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000721> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007617>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000540> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000760> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0008050> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000759> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007619> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000656> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000327> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000659> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007632> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000568> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000338> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000422> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0043153>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000266> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000607> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000764> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000548> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000763> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000549> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000766> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000022> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000770> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000039> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000270> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000758> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000034> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000539> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042755> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000765> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000006> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000753> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000229> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000317> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000591> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000339> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000395> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0045475>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000402> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0045433>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000411> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007632>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000679> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0048512>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000420> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007625>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000773> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000041> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000661> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000323> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000776> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000632> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* FBcv_0000403 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007635) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000774 EquivalentTo BFO_0000056 some 
(NBO_0000042 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000644 EquivalentTo BFO_0000056 some 
(NBO_0000403 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000414 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007626) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000669 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0035187) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000474 EquivalentTo BFO_0000056 some 
(GO_0048512 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000601 EquivalentTo BFO_0000056 some 
(NBO_0000003 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000756 EquivalentTo BFO_0000056 some 
(GO_0007617 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000768 EquivalentTo BFO_0000056 some 
(NBO_0000035 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000387 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007610) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000769 EquivalentTo BFO_0000056 some 
(NBO_0000038 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000564 EquivalentTo BFO_0000056 some 
(GO_0035176 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000473 EquivalentTo BFO_0000056 some 
(NBO_0000008 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000767 EquivalentTo BFO_0000056 some 
(NBO_0000170 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000655 EquivalentTo BFO_0000056 some 
(NBO_0000308 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000419 EquivalentTo BFO_0000056 some 
(NBO_0000024 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000755 EquivalentTo BFO_0000056 some 
(GO_0019098 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000757 EquivalentTo BFO_0000056 some 
(GO_0045297 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000762 EquivalentTo BFO_0000056 some 
(GO_0007620 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000761 EquivalentTo BFO_0000056 some 
(GO_0008049 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000772 EquivalentTo BFO_0000056 some 
(NBO_0000036 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000419 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007631) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000775 EquivalentTo BFO_0000056 some 
(GO_0060273 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000398 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007613) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000660 EquivalentTo BFO_0000056 some 
(GO_0007635 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000777 EquivalentTo BFO_0000056 some 
(NBO_0000037 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000401 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0035648) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000397 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007612) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000754 EquivalentTo BFO_0000056 some 
(GO_0042747 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000399 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007619 or (GO_0007610 and (BFO_0000050 some GO_0007619)))) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000396 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0008062) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000720 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007630) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000009 EquivalentTo BFO_0000056 some 
(GO_0007626 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000771 EquivalentTo BFO_0000056 some 
(NBO_0000040 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000643 EquivalentTo BFO_0000056 some 
(NBO_0000388 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000658 EquivalentTo BFO_0000056 some 
(GO_0031223 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000657 EquivalentTo BFO_0000056 some 
(NBO_0000330 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000680 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007637) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000412 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007634) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0006004 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0018991) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000721 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007617 or (GO_0007610 and (BFO_0000050 some GO_0007617)))) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000540 EquivalentTo BFO_0000056 some 
(GO_0042756 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000760 EquivalentTo BFO_0000056 some 
(GO_0008050 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000759 EquivalentTo BFO_0000056 some 
(GO_0007619 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000656 EquivalentTo BFO_0000056 some 
(NBO_0000327 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000659 EquivalentTo BFO_0000056 some 
(GO_0007632 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000568 EquivalentTo BFO_0000056 some 
(NBO_0000338 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000422 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0043153) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000266 EquivalentTo BFO_0000056 some 
(NBO_0000607 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000764 EquivalentTo BFO_0000056 some 
(NBO_0000548 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000763 EquivalentTo BFO_0000056 some 
(NBO_0000549 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000766 EquivalentTo BFO_0000056 some 
(NBO_0000022 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000770 EquivalentTo BFO_0000056 some 
(NBO_0000039 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000270 EquivalentTo BFO_0000056 some 
(NBO_0000079 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000758 EquivalentTo BFO_0000056 some 
(NBO_0000034 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000539 EquivalentTo BFO_0000056 some 
(GO_0042755 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000765 EquivalentTo BFO_0000056 some 
(NBO_0000006 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000753 EquivalentTo BFO_0000056 some 
(NBO_0000161 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000229 EquivalentTo BFO_0000056 some 
(NBO_0000317 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000591 EquivalentTo BFO_0000056 some 
(NBO_0000339 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000395 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0045475) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000402 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0045433) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000411 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007632) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000679 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0048512) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000420 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007625) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000773 EquivalentTo BFO_0000056 some 
(NBO_0000041 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000661 EquivalentTo BFO_0000056 some 
(NBO_0000323 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000776 EquivalentTo BFO_0000056 some 
(NBO_0000632 and (has_quality some PATO_0000001))
  * nbo.owl

## classical conditioning|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000227> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000208> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000749>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000228> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000208> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000747>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000209> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000208> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000091>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000778> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000208> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000003>)) )]
* NBO_0000227 EquivalentTo NBO_0000208 and (is_about some NBO_0000749)
  * nbo.owl
* NBO_0000228 EquivalentTo NBO_0000208 and (is_about some NBO_0000747)
  * nbo.owl
* NBO_0000209 EquivalentTo NBO_0000208 and (is_about some NBO_0000091)
  * nbo.owl
* NBO_0000778 EquivalentTo NBO_0000208 and (is_about some NBO_0000003)
  * nbo.owl

## thermosensory behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000326> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050955>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000329> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000326> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/PATO_0001306>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000328> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000326> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/PATO_0001305>)) )]
* NBO_0000326 EquivalentTo NBO_0000330 and (in_response_to some GO_0050955)
  * nbo.owl
* NBO_0000329 EquivalentTo NBO_0000326 and (in_response_to some PATO_0001306)
  * nbo.owl
* NBO_0000328 EquivalentTo NBO_0000326 and (in_response_to some PATO_0001305)
  * nbo.owl

## chemosensory behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000322> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001632> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0007606>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000324> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000322> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050909>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000323> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000322> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0007608>)) )]
* NBO_0000322 EquivalentTo NBO_0001632 and (in_response_to some GO_0007606)
  * nbo.owl
* NBO_0000324 EquivalentTo NBO_0000322 and (in_response_to some GO_0050909)
  * nbo.owl
* NBO_0000323 EquivalentTo NBO_0000322 and (in_response_to some GO_0007608)
  * nbo.owl

## olfactory behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000323> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000322> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0007608>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000661> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000323> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000323 EquivalentTo NBO_0000322 and (in_response_to some GO_0007608)
  * nbo.owl
* NBO_0000661 EquivalentTo BFO_0000056 some 
(NBO_0000323 and (has_quality some PATO_0000001))
  * nbo.owl

## shape|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000465> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000052>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000463> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000225> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000052>)) )]
* NBO_0000465 EquivalentTo NBO_0000308 and (is_about some PATO_0000052)
  * nbo.owl
* NBO_0000463 EquivalentTo NBO_0000225 and (is_about some PATO_0000052)
  * nbo.owl

## PATO_0002361|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000515> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0002361> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000085>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000606> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0002361> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000304>))) )]
* NBO_0000515 EquivalentTo has_quality some 
(PATO_0002361 and (towards some NBO_0000085))
  * nbo.owl
* NBO_0000606 EquivalentTo has_quality some 
(PATO_0002361 and (towards some NBO_0000304))
  * nbo.owl

## consumption of an addictive substance|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001915> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001884> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_27958>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002086> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001884> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_18723>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001952> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001884> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_17303>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002234> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0001884>) )]
* NBO_0001915 EquivalentTo NBO_0001884 and (has_participant some CHEBI_27958)
  * nbo.owl
* NBO_0002086 EquivalentTo NBO_0001884 and (has_participant some CHEBI_18723)
  * nbo.owl
* NBO_0001952 EquivalentTo NBO_0001884 and (has_participant some CHEBI_17303)
  * nbo.owl
* NBO_0002234 EquivalentTo RO_0002211 some NBO_0001884
  * nbo.owl

## perceptual constancy behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000462> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000225> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000014>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000461> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000225> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000117>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000463> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000225> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000052>)) )]
* NBO_0000462 EquivalentTo NBO_0000225 and (is_about some PATO_0000014)
  * nbo.owl
* NBO_0000461 EquivalentTo NBO_0000225 and (is_about some PATO_0000117)
  * nbo.owl
* NBO_0000463 EquivalentTo NBO_0000225 and (is_about some PATO_0000052)
  * nbo.owl

## CHEBI_33290|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001845> ObjectUnionOf(ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/PATO_0000145>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>)) )]
* NBO_0000079 EquivalentTo NBO_0001845 and ((has_participant some CHEBI_33290) or (has_participant some PATO_0000145))
  * nbo.owl
* NBO_0000134 EquivalentTo NBO_0000079 and (has_participant some CHEBI_33290)
  * nbo.owl

## nicotine consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002273> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0002086>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002086> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001884> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_18723>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002065> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0002086>)) )]
* NBO_0002273 EquivalentTo RO_0002211 some NBO_0002086
  * nbo.owl
* NBO_0002086 EquivalentTo NBO_0001884 and (has_participant some CHEBI_18723)
  * nbo.owl
* NBO_0002065 EquivalentTo NBO_0001728 and (in_response_to some NBO_0002086)
  * nbo.owl

## motor coordination|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000591> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000339> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000174> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000171> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000339>)) )]
* NBO_0000591 EquivalentTo BFO_0000056 some 
(NBO_0000339 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000174 EquivalentTo NBO_0000171 and (is_about some NBO_0000339)
  * nbo.owl

## nociceptive behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000335> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000331> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050965>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000331> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0019233>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000752> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000331> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050967>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000333> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000331> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050968>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000334> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000331> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050966>)) )]
* NBO_0000335 EquivalentTo NBO_0000331 and (in_response_to some GO_0050965)
  * nbo.owl
* NBO_0000331 EquivalentTo NBO_0000330 and (in_response_to some GO_0019233)
  * nbo.owl
* NBO_0000752 EquivalentTo NBO_0000331 and (in_response_to some GO_0050967)
  * nbo.owl
* NBO_0000333 EquivalentTo NBO_0000331 and (in_response_to some GO_0050968)
  * nbo.owl
* NBO_0000334 EquivalentTo NBO_0000331 and (in_response_to some GO_0050966)
  * nbo.owl

## frequency|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000165> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000044>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000163> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042747> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000044>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000144> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000044>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000929> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000044> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000165 EquivalentTo BFO_0000056 some 
(NBO_0000161 and (has_quality some PATO_0000044))
  * nbo.owl
* NBO_0000163 EquivalentTo BFO_0000056 some 
(GO_0042747 and (has_quality some PATO_0000044))
  * nbo.owl
* NBO_0000144 EquivalentTo BFO_0000056 some 
(GO_0007617 and (has_quality some PATO_0000044))
  * nbo.owl
* NBO_0000929 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000044 and (towards some NBO_0000130))))
  * nbo.owl

## cutaneous sensation behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000326> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050955>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000331> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0019233>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000657> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000332> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000330> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/GO_0050975>)) )]
* NBO_0000326 EquivalentTo NBO_0000330 and (in_response_to some GO_0050955)
  * nbo.owl
* NBO_0000331 EquivalentTo NBO_0000330 and (in_response_to some GO_0019233)
  * nbo.owl
* NBO_0000657 EquivalentTo BFO_0000056 some 
(NBO_0000330 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000332 EquivalentTo NBO_0000330 and (in_response_to some GO_0050975)
  * nbo.owl

## rate|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002948> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000161>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000133> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000135> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060259> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000161>))) )]
* NBO_0000145 EquivalentTo BFO_0000056 some 
(NBO_0002948 and (has_quality some PATO_0000161))
  * nbo.owl
* NBO_0000133 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000161 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000135 EquivalentTo BFO_0000056 some 
(GO_0060259 and (has_quality some PATO_0000161))
  * nbo.owl

## PATO_0001863|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000541> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002519> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000541 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0002519 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl

## emotional behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000601> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000003> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000778> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000208> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000003>)) )]
* NBO_0000601 EquivalentTo BFO_0000056 some 
(NBO_0000003 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000778 EquivalentTo NBO_0000208 and (is_about some NBO_0000003)
  * nbo.owl

## regulation of alcohol preference behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_16236>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000139> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000911>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000140> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) )]
* NBO_0002702 EquivalentTo NBO_0002660 and (has_participant some CHEBI_16236)
  * nbo.owl
* NBO_0000139 EquivalentTo BFO_0000056 some 
(NBO_0002702 and (has_quality some PATO_0000911))
  * nbo.owl
* NBO_0000140 EquivalentTo BFO_0000056 some 
(NBO_0002702 and (has_quality some PATO_0000912))
  * nbo.owl

## behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000399> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007619> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007619>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000721> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007617>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000387> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007610>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) )]
* FBcv_0000399 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007619 or (GO_0007610 and (BFO_0000050 some GO_0007619)))) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000721 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007617 or (GO_0007610 and (BFO_0000050 some GO_0007617)))) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000387 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007610) and (qualifier some PATO_0000460)
  * dpo.owl

## posture|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000357> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000355> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/UBERON_0002101>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000356> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000355> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/UBERON_0000309>)) )]
* NBO_0000357 EquivalentTo NBO_0000355 and (has_participant some UBERON_0002101)
  * nbo.owl
* NBO_0000356 EquivalentTo NBO_0000355 and (has_participant some UBERON_0000309)
  * nbo.owl

## courtship behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000399> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007619> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007619>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000759> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007619> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* FBcv_0000399 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007619 or (GO_0007610 and (BFO_0000050 some GO_0007619)))) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000759 EquivalentTo BFO_0000056 some 
(GO_0007619 and (has_quality some PATO_0000001))
  * nbo.owl

## mating behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000721> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007617>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000144> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000044>))) )]
* FBcv_0000721 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007617 or (GO_0007610 and (BFO_0000050 some GO_0007617)))) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000756 EquivalentTo BFO_0000056 some 
(GO_0007617 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000144 EquivalentTo BFO_0000056 some 
(GO_0007617 and (has_quality some PATO_0000044))
  * nbo.owl

## cocaine consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001987> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0001915>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001915> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001884> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_27958>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002132> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0001915>) )]
* NBO_0001987 EquivalentTo NBO_0001728 and (in_response_to some NBO_0001915)
  * nbo.owl
* NBO_0001915 EquivalentTo NBO_0001884 and (has_participant some CHEBI_27958)
  * nbo.owl
* NBO_0002132 EquivalentTo RO_0002211 some NBO_0001915
  * nbo.owl

## involuntary movement behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000389> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000388> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/GO_0060004>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000643> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000388> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000389 EquivalentTo NBO_0000388 and (by_means some GO_0060004)
  * nbo.owl
* NBO_0000643 EquivalentTo BFO_0000056 some 
(NBO_0000388 and (has_quality some PATO_0000001))
  * nbo.owl

## locomotory behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000414> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007626>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000009> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007626> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* FBcv_0000414 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007626) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000009 EquivalentTo BFO_0000056 some 
(GO_0007626 and (has_quality some PATO_0000001))
  * nbo.owl

## sleeping behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000159> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000024> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0042747>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000419> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000024> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000159 EquivalentTo NBO_0000024 and (is_about some GO_0042747)
  * nbo.owl
* NBO_0000419 EquivalentTo BFO_0000056 some 
(NBO_0000024 and (has_quality some PATO_0000001))
  * nbo.owl

## learning behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000766> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000022> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000216> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000022> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000745>)) )]
* NBO_0000766 EquivalentTo BFO_0000056 some 
(NBO_0000022 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000216 EquivalentTo NBO_0000022 and (is_about some NBO_0000745)
  * nbo.owl

## visual behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000659> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007632> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000411> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007632>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) )]
* NBO_0000659 EquivalentTo BFO_0000056 some 
(GO_0007632 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000411 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007632) and (qualifier some PATO_0000460)
  * dpo.owl

## GO_0060259|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000142> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060259> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000911>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000141> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060259> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000135> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0060259> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000161>))) )]
* NBO_0000142 EquivalentTo BFO_0000056 some 
(GO_0060259 and (has_quality some PATO_0000911))
  * nbo.owl
* NBO_0000141 EquivalentTo BFO_0000056 some 
(GO_0060259 and (has_quality some PATO_0000912))
  * nbo.owl
* NBO_0000135 EquivalentTo BFO_0000056 some 
(GO_0060259 and (has_quality some PATO_0000161))
  * nbo.owl

## saccharin consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000136> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_32111>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002511> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000136>) )]
* NBO_0000136 EquivalentTo NBO_0000134 and (has_participant some CHEBI_32111)
  * nbo.owl
* NBO_0002511 EquivalentTo RO_0002211 some NBO_0000136
  * nbo.owl

## food consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000136> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_32111>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002436> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> ObjectUnionOf(<http://purl.obolibrary.org/obo/NBO_0000130> <http://purl.obolibrary.org/obo/NBO_0000134>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000063> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000134>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000546> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000912>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000134> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000079> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_33290>)) )]
* NBO_0000136 EquivalentTo NBO_0000134 and (has_participant some CHEBI_32111)
  * nbo.owl
* NBO_0002436 EquivalentTo RO_0002211 some 
(NBO_0000130 or NBO_0000134)
  * nbo.owl
* NBO_0000063 EquivalentTo RO_0002211 some NBO_0000134
  * nbo.owl
* NBO_0000546 EquivalentTo BFO_0000056 some 
(NBO_0000134 and (has_quality some PATO_0000912))
  * nbo.owl
* NBO_0000134 EquivalentTo NBO_0000079 and (has_participant some CHEBI_33290)
  * nbo.owl

## chemosensory behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000403> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007635>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007635> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* FBcv_0000403 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007635) and (qualifier some PATO_0000460)
  * dpo.owl
* NBO_0000660 EquivalentTo BFO_0000056 some 
(GO_0007635 and (has_quality some PATO_0000001))
  * nbo.owl

## alcohol consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000131> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000130> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_16236>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001824> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000131>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001763> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0000131>)) )]
* NBO_0000131 EquivalentTo NBO_0000130 and (has_participant some CHEBI_16236)
  * nbo.owl
* NBO_0001824 EquivalentTo RO_0002211 some NBO_0000131
  * nbo.owl
* NBO_0001763 EquivalentTo NBO_0001728 and (in_response_to some NBO_0000131)
  * nbo.owl

## water consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002468> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000132>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000132> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000130> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_15377>)) )]
* NBO_0002468 EquivalentTo RO_0002211 some NBO_0000132
  * nbo.owl
* NBO_0000132 EquivalentTo NBO_0000130 and (has_participant some CHEBI_15377)
  * nbo.owl

## liquid consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000961> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000543> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000993> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000131> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000130> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_16236>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000541> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002436> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> ObjectUnionOf(<http://purl.obolibrary.org/obo/NBO_0000130> <http://purl.obolibrary.org/obo/NBO_0000134>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000138> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000911> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000137> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000912> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000132> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000130> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_15377>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002519> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000133> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000542> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000929> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000044> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000961 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000543 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001333) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000993 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000131 EquivalentTo NBO_0000130 and (has_participant some CHEBI_16236)
  * nbo.owl
* NBO_0000541 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000064 EquivalentTo RO_0002211 some NBO_0000130
  * nbo.owl
* NBO_0002436 EquivalentTo RO_0002211 some 
(NBO_0000130 or NBO_0000134)
  * nbo.owl
* NBO_0000138 EquivalentTo BFO_0000056 some 
(NBO_0002660 and (has_quality some 
(PATO_0000911 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000137 EquivalentTo BFO_0000056 some 
(NBO_0002660 and (has_quality some 
(PATO_0000912 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000132 EquivalentTo NBO_0000130 and (has_participant some CHEBI_15377)
  * nbo.owl
* NBO_0002519 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000133 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000161 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000542 EquivalentTo BFO_0000056 some 
((NBO_0000064 and (RO_0002211 some NBO_0000130) and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))) and (qualifier some PATO_0001333))
  * nbo.owl
* NBO_0000929 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000044 and (towards some NBO_0000130))))
  * nbo.owl

## hallucination|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000609> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000608> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0002104>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000610> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000608> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0002105>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000611> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000608> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0005725>)) )]
* NBO_0000609 EquivalentTo NBO_0000608 and (by_means some UBERON_0002104)
  * nbo.owl
* NBO_0000610 EquivalentTo NBO_0000608 and (by_means some UBERON_0002105)
  * nbo.owl
* NBO_0000611 EquivalentTo NBO_0000608 and (by_means some UBERON_0005725)
  * nbo.owl

## behavioral control of external secretion|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000042> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000041> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0001817>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0070075>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000041> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000035> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0007589>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000773> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000041> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000042 EquivalentTo NBO_0000041 and (by_means some UBERON_0001817) and (is_about some GO_0070075)
  * nbo.owl
* NBO_0000041 EquivalentTo NBO_0000035 and (is_about some GO_0007589)
  * nbo.owl
* NBO_0000773 EquivalentTo BFO_0000056 some 
(NBO_0000041 and (has_quality some PATO_0000001))
  * nbo.owl

## behavioral control of lacrimation|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000042> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000041> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0001817>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0070075>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000774> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000042> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000042 EquivalentTo NBO_0000041 and (by_means some UBERON_0001817) and (is_about some GO_0070075)
  * nbo.owl
* NBO_0000774 EquivalentTo BFO_0000056 some 
(NBO_0000042 and (has_quality some PATO_0000001))
  * nbo.owl

## non-rapid eye movement sleep behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000164> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001309>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000165> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000044>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000753> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000164 EquivalentTo BFO_0000056 some 
(NBO_0000161 and (has_quality some PATO_0001309))
  * nbo.owl
* NBO_0000165 EquivalentTo BFO_0000056 some 
(NBO_0000161 and (has_quality some PATO_0000044))
  * nbo.owl
* NBO_0000753 EquivalentTo BFO_0000056 some 
(NBO_0000161 and (has_quality some PATO_0000001))
  * nbo.owl

## behavioral control of urination|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000040> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0001256>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0060073>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000771> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000040> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000040 EquivalentTo NBO_0000038 and (by_means some UBERON_0001256) and (is_about some GO_0060073)
  * nbo.owl
* NBO_0000771 EquivalentTo BFO_0000056 some 
(NBO_0000040 and (has_quality some PATO_0000001))
  * nbo.owl

## GO_0042755|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000544> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0001558> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/GO_0042755>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000539> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042755> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000544 EquivalentTo has_quality some 
(PATO_0001558 and (towards some GO_0042755))
  * nbo.owl
* NBO_0000539 EquivalentTo BFO_0000056 some 
(GO_0042755 and (has_quality some PATO_0000001))
  * nbo.owl

## GO_0042756|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000851> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000540> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042756> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000851 EquivalentTo BFO_0000056 some 
(GO_0042756 and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563))))
  * nbo.owl
* NBO_0000540 EquivalentTo BFO_0000056 some 
(GO_0042756 and (has_quality some PATO_0000001))
  * nbo.owl

## PATO_0001309|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000164> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001309>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000162> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042747> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001309>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000160> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0030431> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001309>))) )]
* NBO_0000164 EquivalentTo BFO_0000056 some 
(NBO_0000161 and (has_quality some PATO_0001309))
  * nbo.owl
* NBO_0000162 EquivalentTo BFO_0000056 some 
(GO_0042747 and (has_quality some PATO_0001309))
  * nbo.owl
* NBO_0000160 EquivalentTo BFO_0000056 some 
(GO_0030431 and (has_quality some PATO_0001309))
  * nbo.owl

## lacking processual parts|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000547> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0001558> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000230>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000544> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0001558> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/GO_0042755>))) )]
* NBO_0000547 EquivalentTo has_quality some 
(PATO_0001558 and (towards some NBO_0000230))
  * nbo.owl
* NBO_0000544 EquivalentTo has_quality some 
(PATO_0001558 and (towards some GO_0042755))
  * nbo.owl

## behavioral control of excretion|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000040> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/UBERON_0001256>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0060073>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000039> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0030421>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000035> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0007588>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000769> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000040 EquivalentTo NBO_0000038 and (by_means some UBERON_0001256) and (is_about some GO_0060073)
  * nbo.owl
* NBO_0000039 EquivalentTo NBO_0000038 and (is_about some GO_0030421)
  * nbo.owl
* NBO_0000038 EquivalentTo NBO_0000035 and (is_about some GO_0007588)
  * nbo.owl
* NBO_0000769 EquivalentTo BFO_0000056 some 
(NBO_0000038 and (has_quality some PATO_0000001))
  * nbo.owl

## behavioral control of defecation|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000770> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000039> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000039> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0030421>)) )]
* NBO_0000770 EquivalentTo BFO_0000056 some 
(NBO_0000039 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000039 EquivalentTo NBO_0000038 and (is_about some GO_0030421)
  * nbo.owl

## vocalization behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000276> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000015> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#by_means> <http://purl.obolibrary.org/obo/NBO_0000037>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000176> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000171> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000037>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000777> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000037> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000276 EquivalentTo NBO_0000015 and (by_means some NBO_0000037)
  * nbo.owl
* NBO_0000176 EquivalentTo NBO_0000171 and (is_about some NBO_0000037)
  * nbo.owl
* NBO_0000777 EquivalentTo BFO_0000056 some 
(NBO_0000037 and (has_quality some PATO_0000001))
  * nbo.owl

## sexual activity|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000758> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000034> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002603> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000034>) )]
* NBO_0000758 EquivalentTo BFO_0000056 some 
(NBO_0000034 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0002603 EquivalentTo RO_0002211 some NBO_0000034
  * nbo.owl

## emission behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000041> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000035> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0007589>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000768> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000035> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000038> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000035> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0007588>)) )]
* NBO_0000041 EquivalentTo NBO_0000035 and (is_about some GO_0007589)
  * nbo.owl
* NBO_0000768 EquivalentTo BFO_0000056 some 
(NBO_0000035 and (has_quality some PATO_0000001))
  * nbo.owl
* NBO_0000038 EquivalentTo NBO_0000035 and (is_about some GO_0007588)
  * nbo.owl

## GO_0042747|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000162> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042747> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001309>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000159> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000024> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/GO_0042747>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000163> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042747> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000044>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000754> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0042747> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) )]
* NBO_0000162 EquivalentTo BFO_0000056 some 
(GO_0042747 and (has_quality some PATO_0001309))
  * nbo.owl
* NBO_0000159 EquivalentTo NBO_0000024 and (is_about some GO_0042747)
  * nbo.owl
* NBO_0000163 EquivalentTo BFO_0000056 some 
(GO_0042747 and (has_quality some PATO_0000044))
  * nbo.owl
* NBO_0000754 EquivalentTo BFO_0000056 some 
(GO_0042747 and (has_quality some PATO_0000001))
  * nbo.owl

## abnormal|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000403> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007635>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000721> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007617> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007617>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000414> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007626>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000419> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007631>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000669> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0035187>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000398> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007613>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000387> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007610>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000401> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0035648>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000397> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007612>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000399> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> ObjectUnionOf(<http://purl.obolibrary.org/obo/GO_0007619> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0007610> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000050> <http://purl.obolibrary.org/obo/GO_0007619>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000396> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0008062>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000395> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0045475>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000720> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007630>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000402> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0045433>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000411> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007632>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000680> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007637>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000679> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0048512>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000420> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007625>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000412> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0007634>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0006004> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0018991>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000422> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0043153>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) )]
* FBcv_0000403 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007635) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000721 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007617 or (GO_0007610 and (BFO_0000050 some GO_0007617)))) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000414 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007626) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000419 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007631) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000669 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0035187) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000398 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007613) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000387 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007610) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000401 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0035648) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000397 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007612) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000399 EquivalentTo PATO_0000001 and (RO_0000052 some 
(GO_0007619 or (GO_0007610 and (BFO_0000050 some GO_0007619)))) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000396 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0008062) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000395 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0045475) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000720 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007630) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000402 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0045433) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000411 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007632) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000680 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007637) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000679 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0048512) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000420 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007625) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000412 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0007634) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0006004 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0018991) and (qualifier some PATO_0000460)
  * dpo.owl
* FBcv_0000422 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0043153) and (qualifier some PATO_0000460)
  * dpo.owl

## CHEBI_16236|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_16236>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000131> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000130> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_16236>)) )]
* NBO_0002702 EquivalentTo NBO_0002660 and (has_participant some CHEBI_16236)
  * nbo.owl
* NBO_0000131 EquivalentTo NBO_0000130 and (has_participant some CHEBI_16236)
  * nbo.owl

## spatial perception|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000467> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000746> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000040>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000746> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/PATO_0000117>)) )]
* NBO_0000467 EquivalentTo NBO_0000746 and (is_about some PATO_0000040)
  * nbo.owl
* NBO_0000746 EquivalentTo NBO_0000308 and (is_about some PATO_0000117)
  * nbo.owl

## morphine consumption|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002021> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001728> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0001952>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0001952> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0001884> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has_participant> <http://purl.obolibrary.org/obo/CHEBI_17303>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0002308> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0001952>) )]
* NBO_0002021 EquivalentTo NBO_0001728 and (in_response_to some NBO_0001952)
  * nbo.owl
* NBO_0001952 EquivalentTo NBO_0001884 and (has_participant some CHEBI_17303)
  * nbo.owl
* NBO_0002308 EquivalentTo RO_0002211 some NBO_0001952
  * nbo.owl

## regulation of drinking behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000961> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000543> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000993> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000133> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000161> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000886> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000541> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000380> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000542> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0002211> <http://purl.obolibrary.org/obo/NBO_0000130>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#has-input> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000145> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0001563>)))) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001333>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/behavior.owl/NBO_0002519> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000381> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#qualifier> <http://purl.obolibrary.org/obo/PATO_0001863>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000929> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000064> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000044> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/pato#towards> <http://purl.obolibrary.org/obo/NBO_0000130>))))) )]
* NBO_0000961 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000543 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001333) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000993 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000133 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000161 and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000886 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (RO_0002211 some (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))))
  * nbo.owl
* NBO_0000541 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000380 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000064 EquivalentTo RO_0002211 some NBO_0000130
  * nbo.owl
* NBO_0000542 EquivalentTo BFO_0000056 some 
((NBO_0000064 and (RO_0002211 some NBO_0000130) and (has-input some 
(PATO_0000145 and (has_quality some PATO_0001563)))) and (qualifier some PATO_0001333))
  * nbo.owl
* NBO_0002519 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000381 and (qualifier some PATO_0001863) and (towards some NBO_0000130))))
  * nbo.owl
* NBO_0000929 EquivalentTo BFO_0000056 some 
(NBO_0000064 and (has_quality some 
(PATO_0000044 and (towards some NBO_0000130))))
  * nbo.owl

## circadian behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000474> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/BFO_0000056> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/GO_0048512> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/uberon#has_quality> <http://purl.obolibrary.org/obo/PATO_0000001>))) ), EquivalentClasses(<http://purl.obolibrary.org/obo/FBcv_0000679> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/PATO_0000001> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/RO_0000052> <http://purl.obolibrary.org/obo/GO_0048512>) ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/fbcv#qualifier> <http://purl.obolibrary.org/obo/PATO_0000460>)) )]
* NBO_0000474 EquivalentTo BFO_0000056 some 
(GO_0048512 and (has_quality some PATO_0000001))
  * nbo.owl
* FBcv_0000679 EquivalentTo PATO_0000001 and (RO_0000052 some GO_0048512) and (qualifier some PATO_0000460)
  * dpo.owl

## associative learning behavior|onts:[EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000221> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000171> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#in_response_to> <http://purl.obolibrary.org/obo/NBO_0000778>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000176> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000171> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000037>)) ), EquivalentClasses(<http://purl.obolibrary.org/obo/NBO_0000174> ObjectIntersectionOf(<http://purl.obolibrary.org/obo/NBO_0000171> ObjectSomeValuesFrom(<http://purl.obolibrary.org/obo/nbo#is_about> <http://purl.obolibrary.org/obo/NBO_0000339>)) )]
* NBO_0000221 EquivalentTo NBO_0000171 and (in_response_to some NBO_0000778)
  * nbo.owl
* NBO_0000176 EquivalentTo NBO_0000171 and (is_about some NBO_0000037)
  * nbo.owl
* NBO_0000174 EquivalentTo NBO_0000171 and (is_about some NBO_0000339)
  * nbo.owl

# Entity counts
Omitting entities that occur only once.

* http://purl.obolibrary.org/obo/uberon#has_quality (has_quality)
   nbo.owl|77

* http://purl.obolibrary.org/obo/BFO_0000056 (BFO_0000056)
   nbo.owl|73

* http://purl.obolibrary.org/obo/PATO_0000001 (quality)
   dpo.owl|21
   nbo.owl|47

* http://purl.obolibrary.org/obo/RO_0000052 (inheres_in)
   dpo.owl|22

* http://purl.obolibrary.org/obo/PATO_0000460 (abnormal)
   dpo.owl|21

* http://purl.obolibrary.org/obo/fbcv#qualifier (qualifier)
   dpo.owl|21

* http://purl.obolibrary.org/obo/nbo#is_about (is_about)
   nbo.owl|21

* http://purl.obolibrary.org/obo/nbo#in_response_to (in_response_to)
   nbo.owl|20

* http://purl.obolibrary.org/obo/RO_0002211 (regulates)
   nbo.owl|19

* http://purl.obolibrary.org/obo/NBO_0000130 (liquid consumption)
   nbo.owl|14

* http://purl.obolibrary.org/obo/pato#towards (towards)
   nbo.owl|13

* http://purl.obolibrary.org/obo/nbo#has_participant (has_participant)
   nbo.owl|12

* http://purl.obolibrary.org/obo/NBO_0000064 (regulation of drinking behavior)
   nbo.owl|10

* http://purl.obolibrary.org/obo/nbo#by_means (by_means)
   nbo.owl|8

* http://purl.obolibrary.org/obo/NBO_0000308 (sensation behavior)
   nbo.owl|6

* http://purl.obolibrary.org/obo/NBO_0000134 (food consumption)
   nbo.owl|5

* http://purl.obolibrary.org/obo/NBO_0000331 (nociceptive behavior)
   nbo.owl|5

* http://purl.obolibrary.org/obo/PATO_0000912 (increased rate)
   nbo.owl|5

* http://purl.obolibrary.org/obo/NBO_0001728 (behavioral response to addictive substance)
   nbo.owl|5

* http://purl.obolibrary.org/obo/nbo#qualifier (qualifier)
   nbo.owl|4

* http://purl.obolibrary.org/obo/GO_0042747 (GO_0042747)
   nbo.owl|4

* http://purl.obolibrary.org/obo/NBO_0000038 (behavioral control of excretion)
   nbo.owl|4

* http://purl.obolibrary.org/obo/NBO_0000330 (cutaneous sensation behavior)
   nbo.owl|4

* http://purl.obolibrary.org/obo/PATO_0000044 (frequency)
   nbo.owl|4

* http://purl.obolibrary.org/obo/NBO_0001884 (consumption of an addictive substance)
   nbo.owl|4

* http://purl.obolibrary.org/obo/NBO_0000208 (classical conditioning)
   nbo.owl|4

* http://purl.obolibrary.org/obo/PATO_0000145 (PATO_0000145)
   nbo.owl|4

* http://purl.obolibrary.org/obo/NBO_0000171 (associative learning behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0001952 (morphine consumption)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000035 (emission behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000037 (vocalization behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/PATO_0001309 (PATO_0001309)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000161 (non-rapid eye movement sleep behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000041 (behavioral control of external secretion)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000608 (hallucination)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000131 (alcohol consumption)
   nbo.owl|3

* http://purl.obolibrary.org/obo/GO_0060259 (GO_0060259)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0001915 (cocaine consumption)
   nbo.owl|3

* http://purl.obolibrary.org/obo/GO_0007617 (mating behavior)
   dpo.owl|1
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0007610 (behavior)
   dpo.owl|3

* http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702 (regulation of alcohol preference behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/PATO_0000161 (rate)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0002086 (nicotine consumption)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000225 (perceptual constancy behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/nbo#has-input (has-input)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000322 (chemosensory behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000326 (thermosensory behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/PATO_0000911 (decreased rate)
   nbo.owl|3

* http://purl.obolibrary.org/obo/PATO_0001563 (PATO_0001563)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0001632 (behavioral response to chemical stimulus)
   nbo.owl|3

* http://purl.obolibrary.org/obo/PATO_0000380 (increased frequency)
   nbo.owl|3

* http://purl.obolibrary.org/obo/NBO_0000079 (feeding behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660 (regulation of drinking preference behavior)
   nbo.owl|3

* http://purl.obolibrary.org/obo/GO_0048512 (circadian behavior)
   dpo.owl|1
   nbo.owl|1

* http://purl.obolibrary.org/obo/NBO_0000746 (spatial perception)
   nbo.owl|2

* http://purl.obolibrary.org/obo/CHEBI_16236 (CHEBI_16236)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000034 (sexual activity)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000039 (behavioral control of defecation)
   nbo.owl|2

* http://purl.obolibrary.org/obo/PATO_0001558 (lacking processual parts)
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0042756 (GO_0042756)
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0042755 (GO_0042755)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000040 (behavioral control of urination)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000042 (behavioral control of lacrimation)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000132 (water consumption)
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0007635 (chemosensory behavior)
   dpo.owl|1
   nbo.owl|1

* http://purl.obolibrary.org/obo/NBO_0000136 (saccharin consumption)
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0007632 (visual behavior)
   dpo.owl|1
   nbo.owl|1

* http://purl.obolibrary.org/obo/NBO_0000022 (learning behavior)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000024 (sleeping behavior)
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0007626 (locomotory behavior)
   dpo.owl|1
   nbo.owl|1

* http://purl.obolibrary.org/obo/NBO_0000388 (involuntary movement behavior)
   nbo.owl|2

* http://purl.obolibrary.org/obo/GO_0007619 (courtship behavior)
   dpo.owl|1
   nbo.owl|1

* http://purl.obolibrary.org/obo/NBO_0000355 (posture)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000003 (emotional behavior)
   nbo.owl|2

* http://purl.obolibrary.org/obo/PATO_0001863 (PATO_0001863)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000339 (motor coordination)
   nbo.owl|2

* http://purl.obolibrary.org/obo/CHEBI_33290 (CHEBI_33290)
   nbo.owl|2

* http://purl.obolibrary.org/obo/BFO_0000050 (part_of)
   dpo.owl|2

* http://purl.obolibrary.org/obo/PATO_0002361 (PATO_0002361)
   nbo.owl|2

* http://purl.obolibrary.org/obo/PATO_0000052 (shape)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000323 (olfactory behavior)
   nbo.owl|2

* http://purl.obolibrary.org/obo/PATO_0001333 (PATO_0001333)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0000778 (emotional conditioning)
   nbo.owl|2

* http://purl.obolibrary.org/obo/PATO_0000117 (size)
   nbo.owl|2

* http://purl.obolibrary.org/obo/PATO_0000381 (decreased frequency)
   nbo.owl|2

* http://purl.obolibrary.org/obo/CHEBI_32111 (CHEBI_32111)
   nbo.owl|2

* http://purl.obolibrary.org/obo/NBO_0001845 (consumption behavior)
   nbo.owl|2

* http://purl.obolibrary.org/obo/behavior.owl/NBO_0002794 (regulation of saccharin preference behavior)
   nbo.owl|2

# Definition Analysis: Grammar and constructs
ObjectSomeValuesFrom|297
Class|552
ObjectUnionOf|4
ObjectIntersectionOf|173
Number of definitions across all ontologies: 175
