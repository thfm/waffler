from nltk.corpus import wordnet


def get_synonyms(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        name = synset.lemmas()[0].name()
        if name != word:
            synonyms.append(name)
    # Remove duplicate synonyms
    synonyms = list(set(synonyms))
    return synonyms


def waffle(essay):
    rewritten = ""
    for word in essay.split(" "):
        if len(word) <= 2:
            rewritten += word + " "
            continue
        synonyms = get_synonyms(word)
        rewritten += synonyms[0] if len(synonyms) > 0 else word
        rewritten += " "
    return rewritten
