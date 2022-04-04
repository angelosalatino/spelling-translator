# Spelling Translator


This simple python scripts parses input text and makes spelling conversion between British and American English and viceversa.

**Problem**: *Convert to a single spelling (normalise) 28 million sentences as quick as possible*.

When looking for solutions to such conversion problem, I found some, including [https://stackoverflow.com/a/42373173](https://stackoverflow.com/a/42373173), which I felt being computationally expensive for my problem. These solutions cross check the mappings to the input sentence. Specifically, they scroll over the various words in the mapping, check if that word is in the input text and convert their instance. The current mapping consists of 1,737 mappings (words in british english to american english), hence for each sentence, the algorithm would perform a 1,737 checks to find terms in one spelling and convert them into the other. Working out the math, it would perform 48,636,000,000 checks. A mere waste of time.

This solution is much quicker because:
* uses regex to identify the words in the sentence
* check if the words in the sentence are available in the mapping

# Table of Content
- [Spelling Translator](#spelling-translator)
- [Table of Content](#table-of-content)
- [Set up](#set-up)
- [Run](#run)
  - [Test](#test)
  - [Run on your sentence (British to American)](#run-on-your-sentence-british-to-american)
  - [Run on your sentence (America to British)](#run-on-your-sentence-america-to-british)
- [Updating mapping of spelling](#updating-mapping-of-spelling)
- [Coming soon](#coming-soon)



# Set up

Either download this repo or from your terminal run:
```bash
git clone https://github.com/angelosalatino/spelling-translator.git
```

# Run

## Test
```python
from spelling_translator import Spelling_Translator as ST

st = ST()

st.test()
```

## Run on your sentence (British to American)
```python
from spelling_translator import Spelling_Translator as ST

st = ST()

my_sentence = "I realise I can see the world in colour but I can't vocalise its splendour"
out_sentence = st.translate_to_american(my_sentence)
print(out_sentence)
```

## Run on your sentence (America to British)
```python
from spelling_translator import Spelling_Translator as ST

st = ST()

my_sentence = "I realize I can see the world in color but I can't vocalize its splendor"
out_sentence = st.translate_to_british(my_sentence)
print(out_sentence)
```



# Updating mapping of spelling

The mapping file in the repository (```uk2us.json```) is a simple dictionary with british-spelled words as keys and the corresponding american-spelled equivalent as values.

Here is an exerpt of the dictionary:

```json
{
    "accessorise": "accessorize",
    "accessorised": "accessorized",
    "accessorises": "accessorizes",
    "accessorising": "accessorizing",
    "acclimatisation": "acclimatization",
    "acclimatise": "acclimatize",
    "acclimatised": "acclimatized",
    "acclimatises": "acclimatizes",
    "...": "..."
}
```

This mapping has been parsed from [http://www.tysto.com/uk-us-spelling-list.html](http://www.tysto.com/uk-us-spelling-list.html). Ideally, it is possible to extend/reduce this mapping as you please.


# Coming soon

Here are some features that would be cool to have and if I have time I will probably implement:
* retain the capital letters