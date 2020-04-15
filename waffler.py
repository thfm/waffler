import click
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
    synonyms = list(set(synonyms))  # Removes duplicate synonyms
    return synonyms


# Replaces each 'significant' word of an essay with
# a more complicated counterpart
@click.command()
@click.argument("source")
@click.option("-f", "--file", "is_file", is_flag=True,
              help="Source the essay content from a file.")
def waffle(source: str, is_file: bool):
    essay = open(source).read() if is_file else source
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
    click.echo(waffled)


if __name__ == "__main__":
    waffle()
