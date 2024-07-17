from autocorrect import Speller
import language_tool_python

# Initialize the spell checker
spell = Speller(lang='en')

def getParaphraser(paragraph):
    # Tokenize the paragraph into words
    words = paragraph.split()

    # Correct misspelled words
    corrected_words = [spell(word) for word in words]

    # Join the corrected words back into a paragraph
    corrected_paragraph = ' '.join(corrected_words)

    # Creating a LanguageTool object
    tool = language_tool_python.LanguageTool('en-US')

    # Checking the text for errors
    matches = tool.check(corrected_paragraph)

    # Correcting the text
    corrected_text = language_tool_python.utils.correct(corrected_paragraph, matches)

    return corrected_text

