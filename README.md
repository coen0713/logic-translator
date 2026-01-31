Overview:
This project implements a rule-based system that translates a restricted subset of English sentences into propositional logic. The goal is to produce clean, interpretable logical forms suitable for learning, teaching, and experimentation–not to handle unrestricted natural language.

This system is not intended to handle unrestricted English, resolve ambiguity using world knowledge or statistical inference, or replace large language models or full NLP pipelines.
The system assumes that inputs are grammatically well-formed with explicit logical structure, following the controlled English guidelines.

Features:
The system supports propositional logic with the following operators:
Atomic propositions


Negation (¬)


Conjunction (∧)


Disjunction (∨)


Implication (→)
The system accepts simple declarative English sentences conforming to the following constraints:
No questions or commands


No tense or modality reasoning


No relative clauses


No pronouns requiring reference resolution


Vocabulary is unrestricted, but syntax is limited
Supported constructions include:
Simple statements (“It is raining”)


Negation (“It is not raining”)


Conjunction (“It is raining and it is cold”)


Disjunction (“It is raining or it is snowing”)


Conditionals (“If it is raining, then the ground is wet”)

Atomic Propositions-
Atomic propositions correspond to simple clauses describing a single fact or state of affairs.
Examples:
“It is raining” → raining


“The light is on” → light_on
Atoms are normalized by lowercasing, removing determiners, and lemmatizing verbs where appropriate

Usage-
Input:
If it is raining and it is cold, then the ground is wet
Output:
(raining ∧ cold) → wet

Input:
Not A or B
Output:
(¬A) ∨ B
If the sentence is ambiguous, the system will reject the input or produce an error explaining the unsupported construction.

