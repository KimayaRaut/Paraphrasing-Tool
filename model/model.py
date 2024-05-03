from autocorrect import Speller

# Initialize the spell checker
spell = Speller(lang='en')

def getParaphraser(paragraph):
    # Tokenize the paragraph into words
    words = paragraph.split()

    # Correct misspelled words
    corrected_words = [spell(word) for word in words]

    # Join the corrected words back into a paragraph
    corrected_paragraph = ' '.join(corrected_words)

    return corrected_paragraph

# Example usage:
# paragraph = "i like to eat mangoo but it smeels kinda wirde"
# corrected = correct_paragraph(paragraph)
# print(corrected)
