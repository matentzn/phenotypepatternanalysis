# Pattern analysis
This repository contains the ongoing work of extracting and documenting phenotype related patterns across relevant phenotype ontologies

Our toolkit aims at supporting the following tasks:
* We call
  * CORPUS a set of ontologies
  * O an ontology
  * AX an axiom
  * B a branch of an ontology, i.e. the set of indirect subclasses of a particular class
  * MAPPING a mapping between sets of terms
* Harmonising ontology patterns
  * within ontologies <O>
  * across ontologies <C>
  * by branch (default: owl:Thing)
  * by
      * Identifying patterns
          1. DEFINITIONS = CORPUS.O.AX.filter(AX of the form A = C, where C is a complex class expression ): identifying all equivalent class axioms across all O in CORPUS.
          2. GENERATED = For each definition D in DEFINITIONS, instantiate a set of more general patterns by gradually replacing all class names in D with a more general one (superclass in O)
      * Quantifying their impact
          1. IMPACT1: For each pattern P in GENERATED, count the number of classes in B (branch) that are
            * direct subclasses of P
            * indirect subclasses of P
      * Presenting the patterns and impact in an easy to navigate way
        * By exporting the patterns as an OWL ontology
          * For convenience, we also export the inferred class hierarchy
        * Given a fast enough reasoner, such as Fact++ the patterns can be queried using the DL query tab by
            * Asking for all patterns with a particular impact, i.e. hasImpact some integer[>100].
            * For convenience, we add a few defined classes with some default values for these.
      * Suggesting patterns to be replaced:
        * Based on MAPPING,
