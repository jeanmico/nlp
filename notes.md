#2018-07-19 CL221 (Parnassus)

python perspective of getting started in NLP
longitudinal learning project

Robert Thombley (IHPS)

#Project: Clinical Trials
[project](clinicaltrials.ucsf.edu)

develop a method for classifying a clinical trial, using its text description into one of a set of categories

where do the trials in the *Other* category belong?
can we build a classifier to categorize them?

*test case*: schizoaffective disorder should be in Mental Health

2 approaches:
 - heuristic (works for basic projects)
 - statistical/machine learning

problem: medical/clinical data breaks lots of implied rules
 - specific terminology, grammatical constructs
*shorthand*, *abbreviations* that are specific to the field

NLP == creating a pipeline
extracting txt > formatting & txt cleaning > tokenizing & vocab building > embedding & modelling
>80% of work is in the first two steps

# NLP tools
- many existing clinical tools use Java

# Step 1: extraction
where is your text source?
how can you put it in a consistent format?
where can you store it?

# Step 2: formatting & cleaning
get in utf-8, deal with abbreviations, shorthand, etc.
how? *regex* 
remove special characters, find expressions of interest
existing tool: metamap

sentence segmentation
(often both heuristic and statistical)
most packages include a tokenization: 
spacy
nltk

complexity reduction - many tokens are redundant
ex: patient == pt.
unpack acronyms/abbr.
convert words to root forms: lemmatization/stemming
*tokenization*

POS tagging: part of speech
(often, all you care about is noun phrases)
can be tough with clinical data
see NER: extracts concepts from text

how to convert words to numbers?
bag of words
TF-IDF bag of words
neural net approaches

# final step: modelling
the cool part
