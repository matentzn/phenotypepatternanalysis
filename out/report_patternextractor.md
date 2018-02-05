
# Definitions Impact
Report only considers patterns with at least 100 indirect instances.
See generated dataset for complete view of the data.
http://ebi.ac.uk#Pattern824
BFO_0000056 some 
    (NBO_0000313
     and (has_quality some PATO_0000001))
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
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
## http://purl.obolibrary.org/obo/fbcv#qualifier
chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
feeding behavior defective ≡ quality ⊓ (∃ inheres_in.feeding behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
hatching behavior defective ≡ quality ⊓ (∃ inheres_in.hatching behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
memory defective ≡ quality ⊓ (∃ inheres_in.memory) ⊓ (∃ qualifier.abnormal) | dpo.owl
behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating rhythm defective ≡ quality ⊓ (∃ inheres_in.circadian mating behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
learning defective ≡ quality ⊓ (∃ inheres_in.learning) ⊓ (∃ qualifier.abnormal) | dpo.owl
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
eclosion rhythm defective ≡ quality ⊓ (∃ inheres_in.eclosion rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor rhythm defective ≡ quality ⊓ (∃ inheres_in.locomotor rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
jump response defective ≡ quality ⊓ (∃ inheres_in.jump response) ⊓ (∃ qualifier.abnormal) | dpo.owl
song defective ≡ quality ⊓ (∃ inheres_in.male courtship behavior, veined wing generated song production) ⊓ (∃ qualifier.abnormal) | dpo.owl
visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
proboscis extension reflex defective ≡ quality ⊓ (∃ inheres_in.proboscis extension reflex) ⊓ (∃ qualifier.abnormal) | dpo.owl
circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
grooming behavior defective ≡ quality ⊓ (∃ inheres_in.grooming behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
optomotor response defective ≡ quality ⊓ (∃ inheres_in.optokinetic behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
oviposition defective ≡ quality ⊓ (∃ inheres_in.oviposition) ⊓ (∃ qualifier.abnormal) | dpo.owl
photoperiod response variant ≡ quality ⊓ (∃ inheres_in.entrainment of circadian clock by photoperiod) ⊓ (∃ qualifier.abnormal) | dpo.owl

* has_role|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/chebi#has_role>]
## http://purl.obolibrary.org/obo/chebi#has_role
behavioral response to xenobiotics ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.(∃ has_role.CHEBI_35703)) | nbo.owl

* part_of|onts:[dpo.owl]|rels:[<http://purl.obolibrary.org/obo/BFO_0000050>]
## http://purl.obolibrary.org/obo/BFO_0000050
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl

* has_participant|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#has_participant>]
## http://purl.obolibrary.org/obo/nbo#has_participant
feeding behavior ≡ consumption behavior ⊓ ((∃ has_participant.CHEBI_33290) ⊔ (∃ has_participant.PATO_0000145)) | nbo.owl
regulation of alcohol preference behavior ≡ regulation of drinking preference behavior ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
alcohol consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
saccharin consumption ≡ food consumption ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
cocaine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_27958) | nbo.owl
limb posture ≡ posture ⊓ (∃ has_participant.UBERON_0002101) | nbo.owl
nicotine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_18723) | nbo.owl
food consumption ≡ feeding behavior ⊓ (∃ has_participant.CHEBI_33290) | nbo.owl
morphine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_17303) | nbo.owl
water consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_15377) | nbo.owl
regulation of saccharin preference behavior ≡ regulation of eating preference behavior ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
body posture ≡ posture ⊓ (∃ has_participant.UBERON_0000309) | nbo.owl

* BFO_0000056|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/BFO_0000056>]
## http://purl.obolibrary.org/obo/BFO_0000056
mating preference ≡ ∃ BFO_0000056.(regulation of mating preference ⊓ (∃ has_quality.rate)) | nbo.owl
behavioral control of lacrimation phenotype ≡ ∃ BFO_0000056.(behavioral control of lacrimation ⊓ (∃ has_quality.quality)) | nbo.owl
voluntary movement behavior phenotype ≡ ∃ BFO_0000056.(voluntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
NREM frequency ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
circadian behavior phenotype ≡ ∃ BFO_0000056.(circadian behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emotional behavior phenotype ≡ ∃ BFO_0000056.(emotional behavior ⊓ (∃ has_quality.quality)) | nbo.owl
liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
mating behavior phenotype ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emission behavior phenotype ≡ ∃ BFO_0000056.(emission behavior ⊓ (∃ has_quality.quality)) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
behavioral control of excretion phenotype ≡ ∃ BFO_0000056.(behavioral control of excretion ⊓ (∃ has_quality.quality)) | nbo.owl
social behavior phenotype ≡ ∃ BFO_0000056.(GO_0035176 ⊓ (∃ has_quality.quality)) | nbo.owl
rhythmic behavior phenotype ≡ ∃ BFO_0000056.(rhythmic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
memory behavior behavior ≡ ∃ BFO_0000056.(memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
food aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.decreased rate)) | nbo.owl
sensation behavior phenotype ≡ ∃ BFO_0000056.(sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
alcohol aversion ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.decreased rate)) | nbo.owl
sleeping behavior phenotype ≡ ∃ BFO_0000056.(sleeping behavior ⊓ (∃ has_quality.quality)) | nbo.owl
reproductive behavior phenotype ≡ ∃ BFO_0000056.(reproductive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
post-mating behavior phenotype ≡ ∃ BFO_0000056.(GO_0045297 ⊓ (∃ has_quality.quality)) | nbo.owl
copulation phenotype ≡ ∃ BFO_0000056.(copulation ⊓ (∃ has_quality.quality)) | nbo.owl
male courtship behavior phenotype ≡ ∃ BFO_0000056.(male courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
behavioral control of production of sound phenotype ≡ ∃ BFO_0000056.(behavioral control of production of sound ⊓ (∃ has_quality.quality)) | nbo.owl
increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
crying behavior phenotype ≡ ∃ BFO_0000056.(GO_0060273 ⊓ (∃ has_quality.quality)) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
chemosensory behavior phenotype ≡ ∃ BFO_0000056.(chemosensory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
vocalization behavior phenotype ≡ ∃ BFO_0000056.(vocalization behavior ⊓ (∃ has_quality.quality)) | nbo.owl
mating frequency ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
rapid eye movement sleep phenotype ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.quality)) | nbo.owl
liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
food preference ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.increased rate)) | nbo.owl
locomotory behavior phenotype ≡ ∃ BFO_0000056.(locomotory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of urination phenotype ≡ ∃ BFO_0000056.(behavioral control of urination ⊓ (∃ has_quality.quality)) | nbo.owl
involuntary movement behavior phenotype ≡ ∃ BFO_0000056.(involuntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
auditory behavior phenotype ≡ ∃ BFO_0000056.(GO_0031223 ⊓ (∃ has_quality.quality)) | nbo.owl
cutaneous sensation behavior phenotype ≡ ∃ BFO_0000056.(cutaneous sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
drinking behavior phenotype ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has_quality.quality)) | nbo.owl
polyphagia ≡ ∃ BFO_0000056.(food consumption ⊓ (∃ has_quality.increased rate)) | nbo.owl
REM frequency ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.frequency)) | nbo.owl
female courtship behavior phenotype ≡ ∃ BFO_0000056.(GO_0008050 ⊓ (∃ has_quality.quality)) | nbo.owl
courtship behavior phenotype ≡ ∃ BFO_0000056.(courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
somatic sensation related behavior phenotype ≡ ∃ BFO_0000056.(somatic sensation related behavior ⊓ (∃ has_quality.quality)) | nbo.owl
visual behavior phenotype ≡ ∃ BFO_0000056.(visual behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sleep duration ≡ ∃ BFO_0000056.(sleep ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
alcohol preference ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
kinesthetic behavior phenotype ≡ ∃ BFO_0000056.(kinesthetic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
cognitive behavior phenotype ≡ ∃ BFO_0000056.(cognitive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
NREM duration ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
male sexual activity phenotype ≡ ∃ BFO_0000056.(male sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
female sexual activity phenotype ≡ ∃ BFO_0000056.(female sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
REM duration ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
learning behavior phenotype ≡ ∃ BFO_0000056.(learning behavior ⊓ (∃ has_quality.quality)) | nbo.owl
food preference/aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.rate)) | nbo.owl
behavioral control of defecation phenotype ≡ ∃ BFO_0000056.(behavioral control of defecation ⊓ (∃ has_quality.quality)) | nbo.owl
feeding behavior phenotype ≡ ∃ BFO_0000056.(feeding behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sexual activity phenotype ≡ ∃ BFO_0000056.(sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
eating behavior phenotype ≡ ∃ BFO_0000056.(GO_0042755 ⊓ (∃ has_quality.quality)) | nbo.owl
learning and/or memory behavior phenotype ≡ ∃ BFO_0000056.(learning and/or memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
non-rapid eye movement sleep behavior phenotype ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.quality)) | nbo.owl
vestibular behavior phenotype ≡ ∃ BFO_0000056.(vestibular behavior ⊓ (∃ has_quality.quality)) | nbo.owl
motor coordination phenotype ≡ ∃ BFO_0000056.(motor coordination ⊓ (∃ has_quality.quality)) | nbo.owl
saccharin preference ≡ ∃ BFO_0000056.(regulation of saccharin preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
behavioral control of external secretion phenotype ≡ ∃ BFO_0000056.(behavioral control of external secretion ⊓ (∃ has_quality.quality)) | nbo.owl
olfactory behavior phenotype ≡ ∃ BFO_0000056.(olfactory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
mobbing calling phenotype ≡ ∃ BFO_0000056.(mobbing calling ⊓ (∃ has_quality.quality)) | nbo.owl

* by_means|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#by_means>]
## http://purl.obolibrary.org/obo/nbo#by_means
behavioral control of urination ≡ behavioral control of excretion ⊓ (∃ by_means.UBERON_0001256) ⊓ (∃ is_about.GO_0060073) | nbo.owl
visual hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0002104) | nbo.owl
behavioral control of lacrimation ≡ behavioral control of external secretion ⊓ (∃ by_means.UBERON_0001817) ⊓ (∃ is_about.GO_0070075) | nbo.owl
vocal aggression behavior ≡ aggressive behavior ⊓ (∃ by_means.vocalization behavior) | nbo.owl
reflexive behavior ≡ involuntary movement behavior ⊓ (∃ by_means.reflex) | nbo.owl
irritable aggressive behavior ≡ GO_0002118 ⊓ (∃ by_means.irritability behavior) | nbo.owl
auditory hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0002105) | nbo.owl
olfactory hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0005725) | nbo.owl

* regulates|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/RO_0002211>]
## http://purl.obolibrary.org/obo/RO_0002211
regulation of addiction response ≡ ∃ regulates.addiction response | nbo.owl
regulation of water consumption ≡ ∃ regulates.water consumption | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
regulation of nicotine consumption ≡ ∃ regulates.nicotine consumption | nbo.owl
regulation of alcohol consumption ≡ ∃ regulates.alcohol consumption | nbo.owl
regulation of drinking behavior ≡ ∃ regulates.liquid consumption | nbo.owl
regulation of feeding behavior ≡ ∃ regulates.(liquid consumption ⊔ food consumption) | nbo.owl
regulation of withdrawal response ≡ ∃ regulates.withdrawal response | nbo.owl
regulation of morphine consumption ≡ ∃ regulates.morphine consumption | nbo.owl
regulation of sexual activity ≡ ∃ regulates.sexual activity | nbo.owl
regulation of behavioral response to chemical stimulus ≡ ∃ regulates.behavioral response to chemical stimulus | nbo.owl
regulation of consumption behavior ≡ ∃ regulates.consumption behavior | nbo.owl
regulation of eating behavior ≡ ∃ regulates.food consumption | nbo.owl
regulation of cocaine consumption ≡ ∃ regulates.cocaine consumption | nbo.owl
regulation of consumption of an addictive substance ≡ ∃ regulates.consumption of an addictive substance | nbo.owl
regulation of saccharin consumption ≡ ∃ regulates.saccharin consumption | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
regulation of behavioral response to addictive substance ≡ ∃ regulates.behavioral response to addictive substance | nbo.owl
regulation of behavior ≡ ∃ regulates.behavior | nbo.owl

* is_about|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#is_about>]
## http://purl.obolibrary.org/obo/nbo#is_about
behavioral control of urination ≡ behavioral control of excretion ⊓ (∃ by_means.UBERON_0001256) ⊓ (∃ is_about.GO_0060073) | nbo.owl
behavioral control of lacrimation ≡ behavioral control of external secretion ⊓ (∃ by_means.UBERON_0001817) ⊓ (∃ is_about.GO_0070075) | nbo.owl
vocal learning ≡ associative learning behavior ⊓ (∃ is_about.vocalization behavior) | nbo.owl
behavioral control of external secretion ≡ emission behavior ⊓ (∃ is_about.GO_0007589) | nbo.owl
colour constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.color) | nbo.owl
rapid eye movement sleep ≡ sleeping behavior ⊓ (∃ is_about.GO_0042747) | nbo.owl
size constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.size) | nbo.owl
form perception behavior ≡ sensation behavior ⊓ (∃ is_about.shape) | nbo.owl
shape constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.shape) | nbo.owl
emotional conditioning ≡ classical conditioning ⊓ (∃ is_about.emotional behavior) | nbo.owl
motor learning ≡ associative learning behavior ⊓ (∃ is_about.motor coordination) | nbo.owl
behavioral control of defecation ≡ behavioral control of excretion ⊓ (∃ is_about.GO_0030421) | nbo.owl
spatial perception ≡ sensation behavior ⊓ (∃ is_about.size) | nbo.owl
circadian behavior ≡ rhythmic behavior ⊓ (∃ is_about.circadian rhythm) | nbo.owl
depth perception behavior ≡ sensation behavior ⊓ (∃ is_about.PATO_0001595) | nbo.owl
eye blink conditioning behavior ≡ classical conditioning ⊓ (∃ is_about.blinking) | nbo.owl
jaw movement conditioning behavior ≡ classical conditioning ⊓ (∃ is_about.jaw movement) | nbo.owl
fear conditioning ≡ classical conditioning ⊓ (∃ is_about.fear-related behavior) | nbo.owl
language learning behavior ≡ learning behavior ⊓ (∃ is_about.language communication behavior) | nbo.owl
distance perception behavior ≡ spatial perception ⊓ (∃ is_about.PATO_0000040) | nbo.owl
behavioral control of excretion ≡ emission behavior ⊓ (∃ is_about.GO_0007588) | nbo.owl

* in_response_to|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#in_response_to>]
## http://purl.obolibrary.org/obo/nbo#in_response_to
visual behavior ≡ sensation behavior ⊓ (∃ in_response_to.GO_0007601) | nbo.owl
thermosensory behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0050955) | nbo.owl
cold sensation behavior ≡ thermosensory behavior ⊓ (∃ in_response_to.PATO_0001306) | nbo.owl
hot sensation behavior ≡ thermosensory behavior ⊓ (∃ in_response_to.PATO_0001305) | nbo.owl
thermal nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050965) | nbo.owl
behavioral response to morphine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.morphine consumption) | nbo.owl
nociceptive behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0019233) | nbo.owl
behavioral response to xenobiotics ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.(∃ has_role.CHEBI_35703)) | nbo.owl
electrical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050967) | nbo.owl
taste behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of taste) | nbo.owl
chemical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050968) | nbo.owl
mechanical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050966) | nbo.owl
olfactory behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of smell) | nbo.owl
behavioral response to alcohol ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.alcohol consumption) | nbo.owl
touch related behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.sensory perception of touch) | nbo.owl
chemosensory behavior ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.sensory perception of chemical stimulus) | nbo.owl
conditioned emotional response ≡ associative learning behavior ⊓ (∃ in_response_to.emotional conditioning) | nbo.owl
behavioral response to cocaine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.cocaine consumption) | nbo.owl
behavioral response to nicotine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.nicotine consumption) | nbo.owl
auditory behavior ≡ sensation behavior ⊓ (∃ in_response_to.sensory perception of sound) | nbo.owl

* towards|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/pato#towards>]
## http://purl.obolibrary.org/obo/pato#towards
increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
anhedonia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.pleasure behavior)) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
depressive disorder ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.depression behavior)) | nbo.owl
aphagia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.GO_0042755)) | nbo.owl
liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
forgetfulness ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.memory loss behavior)) | nbo.owl
frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* has-input|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/nbo#has-input>]
## http://purl.obolibrary.org/obo/nbo#has-input
increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl

* inheres_in|onts:[dpo.owl]|rels:[<http://purl.obolibrary.org/obo/RO_0000052>]
## http://purl.obolibrary.org/obo/RO_0000052
chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
feeding behavior defective ≡ quality ⊓ (∃ inheres_in.feeding behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
hatching behavior defective ≡ quality ⊓ (∃ inheres_in.hatching behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
memory defective ≡ quality ⊓ (∃ inheres_in.memory) ⊓ (∃ qualifier.abnormal) | dpo.owl
behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating rhythm defective ≡ quality ⊓ (∃ inheres_in.circadian mating behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
learning defective ≡ quality ⊓ (∃ inheres_in.learning) ⊓ (∃ qualifier.abnormal) | dpo.owl
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
eclosion rhythm defective ≡ quality ⊓ (∃ inheres_in.eclosion rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor rhythm defective ≡ quality ⊓ (∃ inheres_in.locomotor rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
jump response defective ≡ quality ⊓ (∃ inheres_in.jump response) ⊓ (∃ qualifier.abnormal) | dpo.owl
song defective ≡ quality ⊓ (∃ inheres_in.male courtship behavior, veined wing generated song production) ⊓ (∃ qualifier.abnormal) | dpo.owl
visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
proboscis extension reflex defective ≡ quality ⊓ (∃ inheres_in.proboscis extension reflex) ⊓ (∃ qualifier.abnormal) | dpo.owl
circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
grooming behavior defective ≡ quality ⊓ (∃ inheres_in.grooming behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
optomotor response defective ≡ quality ⊓ (∃ inheres_in.optokinetic behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
uncoordinated ≡ uncoordinated ⊓ (∃ inheres_in.organism) | dpo.owl
oviposition defective ≡ quality ⊓ (∃ inheres_in.oviposition) ⊓ (∃ qualifier.abnormal) | dpo.owl
photoperiod response variant ≡ quality ⊓ (∃ inheres_in.entrainment of circadian clock by photoperiod) ⊓ (∃ qualifier.abnormal) | dpo.owl

* has_quality|onts:[nbo.owl]|rels:[<http://purl.obolibrary.org/obo/uberon#has_quality>]
## http://purl.obolibrary.org/obo/uberon#has_quality
mating preference ≡ ∃ BFO_0000056.(regulation of mating preference ⊓ (∃ has_quality.rate)) | nbo.owl
behavioral control of lacrimation phenotype ≡ ∃ BFO_0000056.(behavioral control of lacrimation ⊓ (∃ has_quality.quality)) | nbo.owl
voluntary movement behavior phenotype ≡ ∃ BFO_0000056.(voluntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
NREM frequency ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
circadian behavior phenotype ≡ ∃ BFO_0000056.(circadian behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emotional behavior phenotype ≡ ∃ BFO_0000056.(emotional behavior ⊓ (∃ has_quality.quality)) | nbo.owl
aphagia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.GO_0042755)) | nbo.owl
liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
mating behavior phenotype ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emission behavior phenotype ≡ ∃ BFO_0000056.(emission behavior ⊓ (∃ has_quality.quality)) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
behavioral control of excretion phenotype ≡ ∃ BFO_0000056.(behavioral control of excretion ⊓ (∃ has_quality.quality)) | nbo.owl
social behavior phenotype ≡ ∃ BFO_0000056.(GO_0035176 ⊓ (∃ has_quality.quality)) | nbo.owl
rhythmic behavior phenotype ≡ ∃ BFO_0000056.(rhythmic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
memory behavior behavior ≡ ∃ BFO_0000056.(memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
food aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.decreased rate)) | nbo.owl
sensation behavior phenotype ≡ ∃ BFO_0000056.(sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
alcohol aversion ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.decreased rate)) | nbo.owl
sleeping behavior phenotype ≡ ∃ BFO_0000056.(sleeping behavior ⊓ (∃ has_quality.quality)) | nbo.owl
reproductive behavior phenotype ≡ ∃ BFO_0000056.(reproductive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
post-mating behavior phenotype ≡ ∃ BFO_0000056.(GO_0045297 ⊓ (∃ has_quality.quality)) | nbo.owl
copulation phenotype ≡ ∃ BFO_0000056.(copulation ⊓ (∃ has_quality.quality)) | nbo.owl
male courtship behavior phenotype ≡ ∃ BFO_0000056.(male courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
behavioral control of production of sound phenotype ≡ ∃ BFO_0000056.(behavioral control of production of sound ⊓ (∃ has_quality.quality)) | nbo.owl
increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
crying behavior phenotype ≡ ∃ BFO_0000056.(GO_0060273 ⊓ (∃ has_quality.quality)) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
depressive disorder ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.depression behavior)) | nbo.owl
chemosensory behavior phenotype ≡ ∃ BFO_0000056.(chemosensory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
vocalization behavior phenotype ≡ ∃ BFO_0000056.(vocalization behavior ⊓ (∃ has_quality.quality)) | nbo.owl
mating frequency ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
rapid eye movement sleep phenotype ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.quality)) | nbo.owl
liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
food preference ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.increased rate)) | nbo.owl
locomotory behavior phenotype ≡ ∃ BFO_0000056.(locomotory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of urination phenotype ≡ ∃ BFO_0000056.(behavioral control of urination ⊓ (∃ has_quality.quality)) | nbo.owl
involuntary movement behavior phenotype ≡ ∃ BFO_0000056.(involuntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
auditory behavior phenotype ≡ ∃ BFO_0000056.(GO_0031223 ⊓ (∃ has_quality.quality)) | nbo.owl
cutaneous sensation behavior phenotype ≡ ∃ BFO_0000056.(cutaneous sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
forgetfulness ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.memory loss behavior)) | nbo.owl
increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
drinking behavior phenotype ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has_quality.quality)) | nbo.owl
anhedonia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.pleasure behavior)) | nbo.owl
polyphagia ≡ ∃ BFO_0000056.(food consumption ⊓ (∃ has_quality.increased rate)) | nbo.owl
REM frequency ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.frequency)) | nbo.owl
female courtship behavior phenotype ≡ ∃ BFO_0000056.(GO_0008050 ⊓ (∃ has_quality.quality)) | nbo.owl
courtship behavior phenotype ≡ ∃ BFO_0000056.(courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
somatic sensation related behavior phenotype ≡ ∃ BFO_0000056.(somatic sensation related behavior ⊓ (∃ has_quality.quality)) | nbo.owl
visual behavior phenotype ≡ ∃ BFO_0000056.(visual behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sleep duration ≡ ∃ BFO_0000056.(sleep ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
alcohol preference ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
kinesthetic behavior phenotype ≡ ∃ BFO_0000056.(kinesthetic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
cognitive behavior phenotype ≡ ∃ BFO_0000056.(cognitive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
NREM duration ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
male sexual activity phenotype ≡ ∃ BFO_0000056.(male sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
female sexual activity phenotype ≡ ∃ BFO_0000056.(female sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
REM duration ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
learning behavior phenotype ≡ ∃ BFO_0000056.(learning behavior ⊓ (∃ has_quality.quality)) | nbo.owl
food preference/aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.rate)) | nbo.owl
behavioral control of defecation phenotype ≡ ∃ BFO_0000056.(behavioral control of defecation ⊓ (∃ has_quality.quality)) | nbo.owl
feeding behavior phenotype ≡ ∃ BFO_0000056.(feeding behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sexual activity phenotype ≡ ∃ BFO_0000056.(sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
eating behavior phenotype ≡ ∃ BFO_0000056.(GO_0042755 ⊓ (∃ has_quality.quality)) | nbo.owl
learning and/or memory behavior phenotype ≡ ∃ BFO_0000056.(learning and/or memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
non-rapid eye movement sleep behavior phenotype ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.quality)) | nbo.owl
vestibular behavior phenotype ≡ ∃ BFO_0000056.(vestibular behavior ⊓ (∃ has_quality.quality)) | nbo.owl
motor coordination phenotype ≡ ∃ BFO_0000056.(motor coordination ⊓ (∃ has_quality.quality)) | nbo.owl
saccharin preference ≡ ∃ BFO_0000056.(regulation of saccharin preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
behavioral control of external secretion phenotype ≡ ∃ BFO_0000056.(behavioral control of external secretion ⊓ (∃ has_quality.quality)) | nbo.owl
olfactory behavior phenotype ≡ ∃ BFO_0000056.(olfactory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
mobbing calling phenotype ≡ ∃ BFO_0000056.(mobbing calling ⊓ (∃ has_quality.quality)) | nbo.owl

# Prominent classes used across definitions
Omitting classes that only occur in one definition

* regulation of drinking preference behavior|onts:[nbo.owl]
regulation of alcohol preference behavior ≡ regulation of drinking preference behavior ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* regulation of saccharin preference behavior|onts:[nbo.owl]
saccharin preference ≡ ∃ BFO_0000056.(regulation of saccharin preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
regulation of saccharin preference behavior ≡ regulation of eating preference behavior ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl

* behavioral response to addictive substance|onts:[nbo.owl]
behavioral response to cocaine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.cocaine consumption) | nbo.owl
behavioral response to morphine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.morphine consumption) | nbo.owl
behavioral response to nicotine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.nicotine consumption) | nbo.owl
behavioral response to alcohol ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.alcohol consumption) | nbo.owl
regulation of behavioral response to addictive substance ≡ ∃ regulates.behavioral response to addictive substance | nbo.owl

* consumption behavior|onts:[nbo.owl]
feeding behavior ≡ consumption behavior ⊓ ((∃ has_participant.CHEBI_33290) ⊔ (∃ has_participant.PATO_0000145)) | nbo.owl
regulation of consumption behavior ≡ ∃ regulates.consumption behavior | nbo.owl

* PATO_0000145|onts:[nbo.owl]
feeding behavior ≡ consumption behavior ⊓ ((∃ has_participant.CHEBI_33290) ⊔ (∃ has_participant.PATO_0000145)) | nbo.owl
increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl

* feeding behavior|onts:[nbo.owl]
feeding behavior ≡ consumption behavior ⊓ ((∃ has_participant.CHEBI_33290) ⊔ (∃ has_participant.PATO_0000145)) | nbo.owl
feeding behavior phenotype ≡ ∃ BFO_0000056.(feeding behavior ⊓ (∃ has_quality.quality)) | nbo.owl
food consumption ≡ feeding behavior ⊓ (∃ has_participant.CHEBI_33290) | nbo.owl

* CHEBI_32111|onts:[nbo.owl]
saccharin consumption ≡ food consumption ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
regulation of saccharin preference behavior ≡ regulation of eating preference behavior ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl

* decreased frequency|onts:[nbo.owl]
decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* increased frequency|onts:[nbo.owl]
increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* sensation behavior|onts:[nbo.owl]
depth perception behavior ≡ sensation behavior ⊓ (∃ is_about.PATO_0001595) | nbo.owl
visual behavior ≡ sensation behavior ⊓ (∃ in_response_to.GO_0007601) | nbo.owl
sensation behavior phenotype ≡ ∃ BFO_0000056.(sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
form perception behavior ≡ sensation behavior ⊓ (∃ is_about.shape) | nbo.owl
spatial perception ≡ sensation behavior ⊓ (∃ is_about.size) | nbo.owl
auditory behavior ≡ sensation behavior ⊓ (∃ in_response_to.sensory perception of sound) | nbo.owl

* size|onts:[nbo.owl]
size constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.size) | nbo.owl
spatial perception ≡ sensation behavior ⊓ (∃ is_about.size) | nbo.owl

* behavioral response to chemical stimulus|onts:[nbo.owl]
chemosensory behavior ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.sensory perception of chemical stimulus) | nbo.owl
regulation of behavioral response to chemical stimulus ≡ ∃ regulates.behavioral response to chemical stimulus | nbo.owl
behavioral response to xenobiotics ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.(∃ has_role.CHEBI_35703)) | nbo.owl

* PATO_0001563|onts:[nbo.owl]
increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl

* increased rate|onts:[nbo.owl]
food preference ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.increased rate)) | nbo.owl
polyphagia ≡ ∃ BFO_0000056.(food consumption ⊓ (∃ has_quality.increased rate)) | nbo.owl
liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
saccharin preference ≡ ∃ BFO_0000056.(regulation of saccharin preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl
alcohol preference ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl

* decreased rate|onts:[nbo.owl]
food aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.decreased rate)) | nbo.owl
alcohol aversion ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.decreased rate)) | nbo.owl
liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* emotional conditioning|onts:[nbo.owl]
conditioned emotional response ≡ associative learning behavior ⊓ (∃ in_response_to.emotional conditioning) | nbo.owl
emotional conditioning ≡ classical conditioning ⊓ (∃ is_about.emotional behavior) | nbo.owl

* PATO_0001333|onts:[nbo.owl]
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl

* quality|onts:[dpo.owl, nbo.owl]
chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
feeding behavior defective ≡ quality ⊓ (∃ inheres_in.feeding behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
hatching behavior defective ≡ quality ⊓ (∃ inheres_in.hatching behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
memory defective ≡ quality ⊓ (∃ inheres_in.memory) ⊓ (∃ qualifier.abnormal) | dpo.owl
behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating rhythm defective ≡ quality ⊓ (∃ inheres_in.circadian mating behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
learning defective ≡ quality ⊓ (∃ inheres_in.learning) ⊓ (∃ qualifier.abnormal) | dpo.owl
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
eclosion rhythm defective ≡ quality ⊓ (∃ inheres_in.eclosion rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor rhythm defective ≡ quality ⊓ (∃ inheres_in.locomotor rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
jump response defective ≡ quality ⊓ (∃ inheres_in.jump response) ⊓ (∃ qualifier.abnormal) | dpo.owl
song defective ≡ quality ⊓ (∃ inheres_in.male courtship behavior, veined wing generated song production) ⊓ (∃ qualifier.abnormal) | dpo.owl
visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
proboscis extension reflex defective ≡ quality ⊓ (∃ inheres_in.proboscis extension reflex) ⊓ (∃ qualifier.abnormal) | dpo.owl
circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
grooming behavior defective ≡ quality ⊓ (∃ inheres_in.grooming behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
optomotor response defective ≡ quality ⊓ (∃ inheres_in.optokinetic behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
oviposition defective ≡ quality ⊓ (∃ inheres_in.oviposition) ⊓ (∃ qualifier.abnormal) | dpo.owl
photoperiod response variant ≡ quality ⊓ (∃ inheres_in.entrainment of circadian clock by photoperiod) ⊓ (∃ qualifier.abnormal) | dpo.owl
drinking behavior phenotype ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of lacrimation phenotype ≡ ∃ BFO_0000056.(behavioral control of lacrimation ⊓ (∃ has_quality.quality)) | nbo.owl
voluntary movement behavior phenotype ≡ ∃ BFO_0000056.(voluntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
circadian behavior phenotype ≡ ∃ BFO_0000056.(circadian behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emotional behavior phenotype ≡ ∃ BFO_0000056.(emotional behavior ⊓ (∃ has_quality.quality)) | nbo.owl
female courtship behavior phenotype ≡ ∃ BFO_0000056.(GO_0008050 ⊓ (∃ has_quality.quality)) | nbo.owl
mating behavior phenotype ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emission behavior phenotype ≡ ∃ BFO_0000056.(emission behavior ⊓ (∃ has_quality.quality)) | nbo.owl
courtship behavior phenotype ≡ ∃ BFO_0000056.(courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of excretion phenotype ≡ ∃ BFO_0000056.(behavioral control of excretion ⊓ (∃ has_quality.quality)) | nbo.owl
social behavior phenotype ≡ ∃ BFO_0000056.(GO_0035176 ⊓ (∃ has_quality.quality)) | nbo.owl
somatic sensation related behavior phenotype ≡ ∃ BFO_0000056.(somatic sensation related behavior ⊓ (∃ has_quality.quality)) | nbo.owl
rhythmic behavior phenotype ≡ ∃ BFO_0000056.(rhythmic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
memory behavior behavior ≡ ∃ BFO_0000056.(memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sensation behavior phenotype ≡ ∃ BFO_0000056.(sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
visual behavior phenotype ≡ ∃ BFO_0000056.(visual behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sleeping behavior phenotype ≡ ∃ BFO_0000056.(sleeping behavior ⊓ (∃ has_quality.quality)) | nbo.owl
reproductive behavior phenotype ≡ ∃ BFO_0000056.(reproductive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
kinesthetic behavior phenotype ≡ ∃ BFO_0000056.(kinesthetic behavior ⊓ (∃ has_quality.quality)) | nbo.owl
post-mating behavior phenotype ≡ ∃ BFO_0000056.(GO_0045297 ⊓ (∃ has_quality.quality)) | nbo.owl
copulation phenotype ≡ ∃ BFO_0000056.(copulation ⊓ (∃ has_quality.quality)) | nbo.owl
male courtship behavior phenotype ≡ ∃ BFO_0000056.(male courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of production of sound phenotype ≡ ∃ BFO_0000056.(behavioral control of production of sound ⊓ (∃ has_quality.quality)) | nbo.owl
cognitive behavior phenotype ≡ ∃ BFO_0000056.(cognitive behavior ⊓ (∃ has_quality.quality)) | nbo.owl
male sexual activity phenotype ≡ ∃ BFO_0000056.(male sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
female sexual activity phenotype ≡ ∃ BFO_0000056.(female sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
learning behavior phenotype ≡ ∃ BFO_0000056.(learning behavior ⊓ (∃ has_quality.quality)) | nbo.owl
crying behavior phenotype ≡ ∃ BFO_0000056.(GO_0060273 ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of defecation phenotype ≡ ∃ BFO_0000056.(behavioral control of defecation ⊓ (∃ has_quality.quality)) | nbo.owl
feeding behavior phenotype ≡ ∃ BFO_0000056.(feeding behavior ⊓ (∃ has_quality.quality)) | nbo.owl
sexual activity phenotype ≡ ∃ BFO_0000056.(sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
eating behavior phenotype ≡ ∃ BFO_0000056.(GO_0042755 ⊓ (∃ has_quality.quality)) | nbo.owl
learning and/or memory behavior phenotype ≡ ∃ BFO_0000056.(learning and/or memory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
chemosensory behavior phenotype ≡ ∃ BFO_0000056.(chemosensory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
vocalization behavior phenotype ≡ ∃ BFO_0000056.(vocalization behavior ⊓ (∃ has_quality.quality)) | nbo.owl
rapid eye movement sleep phenotype ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.quality)) | nbo.owl
non-rapid eye movement sleep behavior phenotype ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.quality)) | nbo.owl
vestibular behavior phenotype ≡ ∃ BFO_0000056.(vestibular behavior ⊓ (∃ has_quality.quality)) | nbo.owl
motor coordination phenotype ≡ ∃ BFO_0000056.(motor coordination ⊓ (∃ has_quality.quality)) | nbo.owl
locomotory behavior phenotype ≡ ∃ BFO_0000056.(locomotory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of urination phenotype ≡ ∃ BFO_0000056.(behavioral control of urination ⊓ (∃ has_quality.quality)) | nbo.owl
involuntary movement behavior phenotype ≡ ∃ BFO_0000056.(involuntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl
auditory behavior phenotype ≡ ∃ BFO_0000056.(GO_0031223 ⊓ (∃ has_quality.quality)) | nbo.owl
cutaneous sensation behavior phenotype ≡ ∃ BFO_0000056.(cutaneous sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of external secretion phenotype ≡ ∃ BFO_0000056.(behavioral control of external secretion ⊓ (∃ has_quality.quality)) | nbo.owl
olfactory behavior phenotype ≡ ∃ BFO_0000056.(olfactory behavior ⊓ (∃ has_quality.quality)) | nbo.owl
mobbing calling phenotype ≡ ∃ BFO_0000056.(mobbing calling ⊓ (∃ has_quality.quality)) | nbo.owl

* classical conditioning|onts:[nbo.owl]
eye blink conditioning behavior ≡ classical conditioning ⊓ (∃ is_about.blinking) | nbo.owl
jaw movement conditioning behavior ≡ classical conditioning ⊓ (∃ is_about.jaw movement) | nbo.owl
fear conditioning ≡ classical conditioning ⊓ (∃ is_about.fear-related behavior) | nbo.owl
emotional conditioning ≡ classical conditioning ⊓ (∃ is_about.emotional behavior) | nbo.owl

* thermosensory behavior|onts:[nbo.owl]
thermosensory behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0050955) | nbo.owl
cold sensation behavior ≡ thermosensory behavior ⊓ (∃ in_response_to.PATO_0001306) | nbo.owl
hot sensation behavior ≡ thermosensory behavior ⊓ (∃ in_response_to.PATO_0001305) | nbo.owl

* chemosensory behavior|onts:[nbo.owl]
chemosensory behavior ≡ behavioral response to chemical stimulus ⊓ (∃ in_response_to.sensory perception of chemical stimulus) | nbo.owl
taste behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of taste) | nbo.owl
olfactory behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of smell) | nbo.owl

* olfactory behavior|onts:[nbo.owl]
olfactory behavior ≡ chemosensory behavior ⊓ (∃ in_response_to.sensory perception of smell) | nbo.owl
olfactory behavior phenotype ≡ ∃ BFO_0000056.(olfactory behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* shape|onts:[nbo.owl]
form perception behavior ≡ sensation behavior ⊓ (∃ is_about.shape) | nbo.owl
shape constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.shape) | nbo.owl

* PATO_0002361|onts:[nbo.owl]
depressive disorder ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.depression behavior)) | nbo.owl
forgetfulness ≡ ∃ has_quality.(PATO_0002361 ⊓ (∃ towards.memory loss behavior)) | nbo.owl

* consumption of an addictive substance|onts:[nbo.owl]
cocaine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_27958) | nbo.owl
nicotine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_18723) | nbo.owl
morphine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_17303) | nbo.owl
regulation of consumption of an addictive substance ≡ ∃ regulates.consumption of an addictive substance | nbo.owl

* perceptual constancy behavior|onts:[nbo.owl]
colour constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.color) | nbo.owl
size constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.size) | nbo.owl
shape constancy behavior ≡ perceptual constancy behavior ⊓ (∃ is_about.shape) | nbo.owl

* CHEBI_33290|onts:[nbo.owl]
feeding behavior ≡ consumption behavior ⊓ ((∃ has_participant.CHEBI_33290) ⊔ (∃ has_participant.PATO_0000145)) | nbo.owl
food consumption ≡ feeding behavior ⊓ (∃ has_participant.CHEBI_33290) | nbo.owl

* nicotine consumption|onts:[nbo.owl]
regulation of nicotine consumption ≡ ∃ regulates.nicotine consumption | nbo.owl
nicotine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_18723) | nbo.owl
behavioral response to nicotine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.nicotine consumption) | nbo.owl

* motor coordination|onts:[nbo.owl]
motor coordination phenotype ≡ ∃ BFO_0000056.(motor coordination ⊓ (∃ has_quality.quality)) | nbo.owl
motor learning ≡ associative learning behavior ⊓ (∃ is_about.motor coordination) | nbo.owl

* nociceptive behavior|onts:[nbo.owl]
thermal nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050965) | nbo.owl
nociceptive behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0019233) | nbo.owl
electrical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050967) | nbo.owl
chemical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050968) | nbo.owl
mechanical nociceptive behavior ≡ nociceptive behavior ⊓ (∃ in_response_to.GO_0050966) | nbo.owl

* frequency|onts:[nbo.owl]
NREM frequency ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
REM frequency ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.frequency)) | nbo.owl
mating frequency ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* cutaneous sensation behavior|onts:[nbo.owl]
thermosensory behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0050955) | nbo.owl
nociceptive behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.GO_0019233) | nbo.owl
cutaneous sensation behavior phenotype ≡ ∃ BFO_0000056.(cutaneous sensation behavior ⊓ (∃ has_quality.quality)) | nbo.owl
touch related behavior ≡ cutaneous sensation behavior ⊓ (∃ in_response_to.sensory perception of touch) | nbo.owl

* rate|onts:[nbo.owl]
mating preference ≡ ∃ BFO_0000056.(regulation of mating preference ⊓ (∃ has_quality.rate)) | nbo.owl
liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
food preference/aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.rate)) | nbo.owl

* PATO_0001863|onts:[nbo.owl]
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* emotional behavior|onts:[nbo.owl]
emotional behavior phenotype ≡ ∃ BFO_0000056.(emotional behavior ⊓ (∃ has_quality.quality)) | nbo.owl
emotional conditioning ≡ classical conditioning ⊓ (∃ is_about.emotional behavior) | nbo.owl

* regulation of alcohol preference behavior|onts:[nbo.owl]
regulation of alcohol preference behavior ≡ regulation of drinking preference behavior ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
alcohol aversion ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.decreased rate)) | nbo.owl
alcohol preference ≡ ∃ BFO_0000056.(regulation of alcohol preference behavior ⊓ (∃ has_quality.increased rate)) | nbo.owl

* behavior|onts:[dpo.owl]
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl

* posture|onts:[nbo.owl]
limb posture ≡ posture ⊓ (∃ has_participant.UBERON_0002101) | nbo.owl
body posture ≡ posture ⊓ (∃ has_participant.UBERON_0000309) | nbo.owl

* courtship behavior|onts:[dpo.owl, nbo.owl]
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
courtship behavior phenotype ≡ ∃ BFO_0000056.(courtship behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* mating behavior|onts:[dpo.owl, nbo.owl]
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior phenotype ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.quality)) | nbo.owl
mating frequency ≡ ∃ BFO_0000056.(mating behavior ⊓ (∃ has_quality.frequency)) | nbo.owl

* cocaine consumption|onts:[nbo.owl]
behavioral response to cocaine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.cocaine consumption) | nbo.owl
cocaine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_27958) | nbo.owl
regulation of cocaine consumption ≡ ∃ regulates.cocaine consumption | nbo.owl

* involuntary movement behavior|onts:[nbo.owl]
reflexive behavior ≡ involuntary movement behavior ⊓ (∃ by_means.reflex) | nbo.owl
involuntary movement behavior phenotype ≡ ∃ BFO_0000056.(involuntary movement behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* locomotory behavior|onts:[dpo.owl, nbo.owl]
locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotory behavior phenotype ≡ ∃ BFO_0000056.(locomotory behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* sleeping behavior|onts:[nbo.owl]
rapid eye movement sleep ≡ sleeping behavior ⊓ (∃ is_about.GO_0042747) | nbo.owl
sleeping behavior phenotype ≡ ∃ BFO_0000056.(sleeping behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* learning behavior|onts:[nbo.owl]
learning behavior phenotype ≡ ∃ BFO_0000056.(learning behavior ⊓ (∃ has_quality.quality)) | nbo.owl
language learning behavior ≡ learning behavior ⊓ (∃ is_about.language communication behavior) | nbo.owl

* visual behavior|onts:[dpo.owl, nbo.owl]
visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
visual behavior phenotype ≡ ∃ BFO_0000056.(visual behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* GO_0060259|onts:[nbo.owl]
food aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.decreased rate)) | nbo.owl
food preference ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.increased rate)) | nbo.owl
food preference/aversion ≡ ∃ BFO_0000056.(GO_0060259 ⊓ (∃ has_quality.rate)) | nbo.owl

* saccharin consumption|onts:[nbo.owl]
saccharin consumption ≡ food consumption ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
regulation of saccharin consumption ≡ ∃ regulates.saccharin consumption | nbo.owl

* food consumption|onts:[nbo.owl]
saccharin consumption ≡ food consumption ⊓ (∃ has_participant.CHEBI_32111) | nbo.owl
regulation of feeding behavior ≡ ∃ regulates.(liquid consumption ⊔ food consumption) | nbo.owl
regulation of eating behavior ≡ ∃ regulates.food consumption | nbo.owl
polyphagia ≡ ∃ BFO_0000056.(food consumption ⊓ (∃ has_quality.increased rate)) | nbo.owl
food consumption ≡ feeding behavior ⊓ (∃ has_participant.CHEBI_33290) | nbo.owl

* chemosensory behavior|onts:[dpo.owl, nbo.owl]
chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
chemosensory behavior phenotype ≡ ∃ BFO_0000056.(chemosensory behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* alcohol consumption|onts:[nbo.owl]
alcohol consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
regulation of alcohol consumption ≡ ∃ regulates.alcohol consumption | nbo.owl
behavioral response to alcohol ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.alcohol consumption) | nbo.owl

* water consumption|onts:[nbo.owl]
regulation of water consumption ≡ ∃ regulates.water consumption | nbo.owl
water consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_15377) | nbo.owl

* liquid consumption|onts:[nbo.owl]
increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
alcohol consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
regulation of drinking behavior ≡ ∃ regulates.liquid consumption | nbo.owl
regulation of feeding behavior ≡ ∃ regulates.(liquid consumption ⊔ food consumption) | nbo.owl
liquid aversion ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(decreased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference ≡ ∃ BFO_0000056.(regulation of drinking preference behavior ⊓ (∃ has_quality.(increased rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
water consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_15377) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* hallucination|onts:[nbo.owl]
visual hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0002104) | nbo.owl
auditory hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0002105) | nbo.owl
olfactory hallucination ≡ hallucination ⊓ (∃ by_means.UBERON_0005725) | nbo.owl

* behavioral control of external secretion|onts:[nbo.owl]
behavioral control of lacrimation ≡ behavioral control of external secretion ⊓ (∃ by_means.UBERON_0001817) ⊓ (∃ is_about.GO_0070075) | nbo.owl
behavioral control of external secretion ≡ emission behavior ⊓ (∃ is_about.GO_0007589) | nbo.owl
behavioral control of external secretion phenotype ≡ ∃ BFO_0000056.(behavioral control of external secretion ⊓ (∃ has_quality.quality)) | nbo.owl

* behavioral control of lacrimation|onts:[nbo.owl]
behavioral control of lacrimation ≡ behavioral control of external secretion ⊓ (∃ by_means.UBERON_0001817) ⊓ (∃ is_about.GO_0070075) | nbo.owl
behavioral control of lacrimation phenotype ≡ ∃ BFO_0000056.(behavioral control of lacrimation ⊓ (∃ has_quality.quality)) | nbo.owl

* non-rapid eye movement sleep behavior|onts:[nbo.owl]
NREM duration ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
NREM frequency ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.frequency)) | nbo.owl
non-rapid eye movement sleep behavior phenotype ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* behavioral control of urination|onts:[nbo.owl]
behavioral control of urination ≡ behavioral control of excretion ⊓ (∃ by_means.UBERON_0001256) ⊓ (∃ is_about.GO_0060073) | nbo.owl
behavioral control of urination phenotype ≡ ∃ BFO_0000056.(behavioral control of urination ⊓ (∃ has_quality.quality)) | nbo.owl

* GO_0042755|onts:[nbo.owl]
aphagia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.GO_0042755)) | nbo.owl
eating behavior phenotype ≡ ∃ BFO_0000056.(GO_0042755 ⊓ (∃ has_quality.quality)) | nbo.owl

* GO_0042756|onts:[nbo.owl]
increased amount of liquid in a single drinking act ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) | nbo.owl
drinking behavior phenotype ≡ ∃ BFO_0000056.(GO_0042756 ⊓ (∃ has_quality.quality)) | nbo.owl

* PATO_0001309|onts:[nbo.owl]
NREM duration ≡ ∃ BFO_0000056.(non-rapid eye movement sleep behavior ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
REM duration ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
sleep duration ≡ ∃ BFO_0000056.(sleep ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl

* lacking processual parts|onts:[nbo.owl]
anhedonia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.pleasure behavior)) | nbo.owl
aphagia ≡ ∃ has_quality.(lacking processual parts ⊓ (∃ towards.GO_0042755)) | nbo.owl

* behavioral control of excretion|onts:[nbo.owl]
behavioral control of urination ≡ behavioral control of excretion ⊓ (∃ by_means.UBERON_0001256) ⊓ (∃ is_about.GO_0060073) | nbo.owl
behavioral control of defecation ≡ behavioral control of excretion ⊓ (∃ is_about.GO_0030421) | nbo.owl
behavioral control of excretion ≡ emission behavior ⊓ (∃ is_about.GO_0007588) | nbo.owl
behavioral control of excretion phenotype ≡ ∃ BFO_0000056.(behavioral control of excretion ⊓ (∃ has_quality.quality)) | nbo.owl

* behavioral control of defecation|onts:[nbo.owl]
behavioral control of defecation phenotype ≡ ∃ BFO_0000056.(behavioral control of defecation ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of defecation ≡ behavioral control of excretion ⊓ (∃ is_about.GO_0030421) | nbo.owl

* vocalization behavior|onts:[nbo.owl]
vocal aggression behavior ≡ aggressive behavior ⊓ (∃ by_means.vocalization behavior) | nbo.owl
vocal learning ≡ associative learning behavior ⊓ (∃ is_about.vocalization behavior) | nbo.owl
vocalization behavior phenotype ≡ ∃ BFO_0000056.(vocalization behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* sexual activity|onts:[nbo.owl]
sexual activity phenotype ≡ ∃ BFO_0000056.(sexual activity ⊓ (∃ has_quality.quality)) | nbo.owl
regulation of sexual activity ≡ ∃ regulates.sexual activity | nbo.owl

* emission behavior|onts:[nbo.owl]
behavioral control of external secretion ≡ emission behavior ⊓ (∃ is_about.GO_0007589) | nbo.owl
emission behavior phenotype ≡ ∃ BFO_0000056.(emission behavior ⊓ (∃ has_quality.quality)) | nbo.owl
behavioral control of excretion ≡ emission behavior ⊓ (∃ is_about.GO_0007588) | nbo.owl

* GO_0042747|onts:[nbo.owl]
REM duration ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.PATO_0001309)) | nbo.owl
rapid eye movement sleep ≡ sleeping behavior ⊓ (∃ is_about.GO_0042747) | nbo.owl
REM frequency ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.frequency)) | nbo.owl
rapid eye movement sleep phenotype ≡ ∃ BFO_0000056.(GO_0042747 ⊓ (∃ has_quality.quality)) | nbo.owl

* abnormal|onts:[dpo.owl]
chemosensitive behavior defective ≡ quality ⊓ (∃ inheres_in.chemosensory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating behavior defective ≡ quality ⊓ (∃ inheres_in.(mating behavior ⊔ (behavior ⊓ (∃ part_of.mating behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor behavior defective ≡ quality ⊓ (∃ inheres_in.locomotory behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
feeding behavior defective ≡ quality ⊓ (∃ inheres_in.feeding behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
hatching behavior defective ≡ quality ⊓ (∃ inheres_in.hatching behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
memory defective ≡ quality ⊓ (∃ inheres_in.memory) ⊓ (∃ qualifier.abnormal) | dpo.owl
behavior defective ≡ quality ⊓ (∃ inheres_in.behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
mating rhythm defective ≡ quality ⊓ (∃ inheres_in.circadian mating behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
learning defective ≡ quality ⊓ (∃ inheres_in.learning) ⊓ (∃ qualifier.abnormal) | dpo.owl
courtship behavior defective ≡ quality ⊓ (∃ inheres_in.(courtship behavior ⊔ (behavior ⊓ (∃ part_of.courtship behavior)))) ⊓ (∃ qualifier.abnormal) | dpo.owl
eclosion rhythm defective ≡ quality ⊓ (∃ inheres_in.eclosion rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
locomotor rhythm defective ≡ quality ⊓ (∃ inheres_in.locomotor rhythm) ⊓ (∃ qualifier.abnormal) | dpo.owl
jump response defective ≡ quality ⊓ (∃ inheres_in.jump response) ⊓ (∃ qualifier.abnormal) | dpo.owl
song defective ≡ quality ⊓ (∃ inheres_in.male courtship behavior, veined wing generated song production) ⊓ (∃ qualifier.abnormal) | dpo.owl
visual behavior defective ≡ quality ⊓ (∃ inheres_in.visual behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
proboscis extension reflex defective ≡ quality ⊓ (∃ inheres_in.proboscis extension reflex) ⊓ (∃ qualifier.abnormal) | dpo.owl
circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
grooming behavior defective ≡ quality ⊓ (∃ inheres_in.grooming behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
optomotor response defective ≡ quality ⊓ (∃ inheres_in.optokinetic behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
oviposition defective ≡ quality ⊓ (∃ inheres_in.oviposition) ⊓ (∃ qualifier.abnormal) | dpo.owl
photoperiod response variant ≡ quality ⊓ (∃ inheres_in.entrainment of circadian clock by photoperiod) ⊓ (∃ qualifier.abnormal) | dpo.owl

* CHEBI_16236|onts:[nbo.owl]
regulation of alcohol preference behavior ≡ regulation of drinking preference behavior ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl
alcohol consumption ≡ liquid consumption ⊓ (∃ has_participant.CHEBI_16236) | nbo.owl

* spatial perception|onts:[nbo.owl]
distance perception behavior ≡ spatial perception ⊓ (∃ is_about.PATO_0000040) | nbo.owl
spatial perception ≡ sensation behavior ⊓ (∃ is_about.size) | nbo.owl

* morphine consumption|onts:[nbo.owl]
behavioral response to morphine ≡ behavioral response to addictive substance ⊓ (∃ in_response_to.morphine consumption) | nbo.owl
morphine consumption ≡ consumption of an addictive substance ⊓ (∃ has_participant.CHEBI_17303) | nbo.owl
regulation of morphine consumption ≡ ∃ regulates.morphine consumption | nbo.owl

* regulation of drinking behavior|onts:[nbo.owl]
increased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
hyperdipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001333) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
decreased frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl
liquid preference/aversion ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(rate ⊓ (∃ towards.liquid consumption)))) | nbo.owl
increased amount of liquid in drinking regulation  ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ regulates.(∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563))))) | nbo.owl
dipsosis ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(increased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
regulation of drinking behavior ≡ ∃ regulates.liquid consumption | nbo.owl
polydipsia ≡ ∃ BFO_0000056.((regulation of drinking behavior ⊓ (∃ regulates.liquid consumption) ⊓ (∃ has-input.(PATO_0000145 ⊓ (∃ has_quality.PATO_0001563)))) ⊓ (∃ qualifier.PATO_0001333)) | nbo.owl
adipsia ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(decreased frequency ⊓ (∃ qualifier.PATO_0001863) ⊓ (∃ towards.liquid consumption)))) | nbo.owl
frequency of drinking ≡ ∃ BFO_0000056.(regulation of drinking behavior ⊓ (∃ has_quality.(frequency ⊓ (∃ towards.liquid consumption)))) | nbo.owl

* circadian behavior|onts:[dpo.owl, nbo.owl]
circadian behavior defective ≡ quality ⊓ (∃ inheres_in.circadian behavior) ⊓ (∃ qualifier.abnormal) | dpo.owl
circadian behavior phenotype ≡ ∃ BFO_0000056.(circadian behavior ⊓ (∃ has_quality.quality)) | nbo.owl

* associative learning behavior|onts:[nbo.owl]
conditioned emotional response ≡ associative learning behavior ⊓ (∃ in_response_to.emotional conditioning) | nbo.owl
vocal learning ≡ associative learning behavior ⊓ (∃ is_about.vocalization behavior) | nbo.owl
motor learning ≡ associative learning behavior ⊓ (∃ is_about.motor coordination) | nbo.owl

# Entity counts
Omitting entities that occur only once.

# http://purl.obolibrary.org/obo/uberon#has_quality (has_quality)
   nbo.owl|77

# http://purl.obolibrary.org/obo/BFO_0000056 (BFO_0000056)
   nbo.owl|73

# http://purl.obolibrary.org/obo/PATO_0000001 (quality)
   dpo.owl|21
   nbo.owl|47

# http://purl.obolibrary.org/obo/RO_0000052 (inheres_in)
   dpo.owl|22

# http://purl.obolibrary.org/obo/PATO_0000460 (abnormal)
   dpo.owl|21

# http://purl.obolibrary.org/obo/fbcv#qualifier (qualifier)
   dpo.owl|21

# http://purl.obolibrary.org/obo/nbo#is_about (is_about)
   nbo.owl|21

# http://purl.obolibrary.org/obo/nbo#in_response_to (in_response_to)
   nbo.owl|20

# http://purl.obolibrary.org/obo/RO_0002211 (regulates)
   nbo.owl|19

# http://purl.obolibrary.org/obo/NBO_0000130 (liquid consumption)
   nbo.owl|14

# http://purl.obolibrary.org/obo/pato#towards (towards)
   nbo.owl|13

# http://purl.obolibrary.org/obo/nbo#has_participant (has_participant)
   nbo.owl|12

# http://purl.obolibrary.org/obo/NBO_0000064 (regulation of drinking behavior)
   nbo.owl|10

# http://purl.obolibrary.org/obo/nbo#by_means (by_means)
   nbo.owl|8

# http://purl.obolibrary.org/obo/NBO_0000308 (sensation behavior)
   nbo.owl|6

# http://purl.obolibrary.org/obo/NBO_0000134 (food consumption)
   nbo.owl|5

# http://purl.obolibrary.org/obo/NBO_0000331 (nociceptive behavior)
   nbo.owl|5

# http://purl.obolibrary.org/obo/PATO_0000912 (increased rate)
   nbo.owl|5

# http://purl.obolibrary.org/obo/NBO_0001728 (behavioral response to addictive substance)
   nbo.owl|5

# http://purl.obolibrary.org/obo/nbo#qualifier (qualifier)
   nbo.owl|4

# http://purl.obolibrary.org/obo/GO_0042747 (GO_0042747)
   nbo.owl|4

# http://purl.obolibrary.org/obo/NBO_0000038 (behavioral control of excretion)
   nbo.owl|4

# http://purl.obolibrary.org/obo/NBO_0000330 (cutaneous sensation behavior)
   nbo.owl|4

# http://purl.obolibrary.org/obo/PATO_0000044 (frequency)
   nbo.owl|4

# http://purl.obolibrary.org/obo/NBO_0001884 (consumption of an addictive substance)
   nbo.owl|4

# http://purl.obolibrary.org/obo/NBO_0000208 (classical conditioning)
   nbo.owl|4

# http://purl.obolibrary.org/obo/PATO_0000145 (PATO_0000145)
   nbo.owl|4

# http://purl.obolibrary.org/obo/NBO_0000171 (associative learning behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0001952 (morphine consumption)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000035 (emission behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000037 (vocalization behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/PATO_0001309 (PATO_0001309)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000161 (non-rapid eye movement sleep behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000041 (behavioral control of external secretion)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000608 (hallucination)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000131 (alcohol consumption)
   nbo.owl|3

# http://purl.obolibrary.org/obo/GO_0060259 (GO_0060259)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0001915 (cocaine consumption)
   nbo.owl|3

# http://purl.obolibrary.org/obo/GO_0007617 (mating behavior)
   dpo.owl|1
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0007610 (behavior)
   dpo.owl|3

# http://purl.obolibrary.org/obo/behavior.owl/NBO_0002702 (regulation of alcohol preference behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/PATO_0000161 (rate)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0002086 (nicotine consumption)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000225 (perceptual constancy behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/nbo#has-input (has-input)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000322 (chemosensory behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000326 (thermosensory behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/PATO_0000911 (decreased rate)
   nbo.owl|3

# http://purl.obolibrary.org/obo/PATO_0001563 (PATO_0001563)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0001632 (behavioral response to chemical stimulus)
   nbo.owl|3

# http://purl.obolibrary.org/obo/PATO_0000380 (increased frequency)
   nbo.owl|3

# http://purl.obolibrary.org/obo/NBO_0000079 (feeding behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/behavior.owl/NBO_0002660 (regulation of drinking preference behavior)
   nbo.owl|3

# http://purl.obolibrary.org/obo/GO_0048512 (circadian behavior)
   dpo.owl|1
   nbo.owl|1

# http://purl.obolibrary.org/obo/NBO_0000746 (spatial perception)
   nbo.owl|2

# http://purl.obolibrary.org/obo/CHEBI_16236 (CHEBI_16236)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000034 (sexual activity)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000039 (behavioral control of defecation)
   nbo.owl|2

# http://purl.obolibrary.org/obo/PATO_0001558 (lacking processual parts)
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0042756 (GO_0042756)
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0042755 (GO_0042755)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000040 (behavioral control of urination)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000042 (behavioral control of lacrimation)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000132 (water consumption)
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0007635 (chemosensory behavior)
   dpo.owl|1
   nbo.owl|1

# http://purl.obolibrary.org/obo/NBO_0000136 (saccharin consumption)
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0007632 (visual behavior)
   dpo.owl|1
   nbo.owl|1

# http://purl.obolibrary.org/obo/NBO_0000022 (learning behavior)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000024 (sleeping behavior)
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0007626 (locomotory behavior)
   dpo.owl|1
   nbo.owl|1

# http://purl.obolibrary.org/obo/NBO_0000388 (involuntary movement behavior)
   nbo.owl|2

# http://purl.obolibrary.org/obo/GO_0007619 (courtship behavior)
   dpo.owl|1
   nbo.owl|1

# http://purl.obolibrary.org/obo/NBO_0000355 (posture)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000003 (emotional behavior)
   nbo.owl|2

# http://purl.obolibrary.org/obo/PATO_0001863 (PATO_0001863)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000339 (motor coordination)
   nbo.owl|2

# http://purl.obolibrary.org/obo/CHEBI_33290 (CHEBI_33290)
   nbo.owl|2

# http://purl.obolibrary.org/obo/BFO_0000050 (part_of)
   dpo.owl|2

# http://purl.obolibrary.org/obo/PATO_0002361 (PATO_0002361)
   nbo.owl|2

# http://purl.obolibrary.org/obo/PATO_0000052 (shape)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000323 (olfactory behavior)
   nbo.owl|2

# http://purl.obolibrary.org/obo/PATO_0001333 (PATO_0001333)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0000778 (emotional conditioning)
   nbo.owl|2

# http://purl.obolibrary.org/obo/PATO_0000117 (size)
   nbo.owl|2

# http://purl.obolibrary.org/obo/PATO_0000381 (decreased frequency)
   nbo.owl|2

# http://purl.obolibrary.org/obo/CHEBI_32111 (CHEBI_32111)
   nbo.owl|2

# http://purl.obolibrary.org/obo/NBO_0001845 (consumption behavior)
   nbo.owl|2

# http://purl.obolibrary.org/obo/behavior.owl/NBO_0002794 (regulation of saccharin preference behavior)
   nbo.owl|2

# Definition Analysis: Grammar and constructs
Class|552
ObjectUnionOf|4
ObjectIntersectionOf|173
ObjectSomeValuesFrom|297
Number of definitions across all ontologies: 175
