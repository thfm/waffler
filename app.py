from nltk.corpus import wordnet


# Gets the unique synonyms of a word
def __get_synonyms(word: str):
    synonyms = []
    for synset in wordnet.synsets(word):
        name = synset.lemmas()[0].name()
        # Checks that the synonym is not the original word
        if name != word:
            synonyms.append(name)

    # Removes underscores from those synonyms with multiple words
    synonyms = [s.replace("_", " ") for s in synonyms]
    synonyms = list(set(synonyms)) # Removes duplicate synonyms
    return synonyms


# Replaces each 'significant' word of an essay with
# a more complicated counterpart
def waffle(essay: str):
    waffled = ""
    for word in essay.split(" "):
        synonyms = __get_synonyms(word)
        # If the word is not 'significant'
        # i.e. it is either short or has no synonyms...
        if len(word) <= 3 or len(synonyms) == 0:
            # ... then the original word is used
            waffled += word + " "
        else:
            waffled += synonyms[0] + " "
    return waffled


print(waffle("I have a lot of time on my hands"))
