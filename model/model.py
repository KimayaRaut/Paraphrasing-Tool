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

# import nltk
# from nltk.corpus import wordnet
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

# def correct_spelling(paragraph):
#     corrected_paragraph = []
#     stop_words = set(stopwords.words('english'))
    
#     for word in word_tokenize(paragraph):
#         # Check if the word is not a stop word and not a punctuation mark
#         if word.isalpha() and word.lower() not in stop_words:
#             # Check if the word is misspelled
#             if not wordnet.synsets(word):
#                 # Get similar words using WordNet
#                 candidates = set()
#                 for syn in wordnet.synsets(word):
#                     for lemma in syn.lemmas():
#                         candidates.add(lemma.name())
                
#                 if candidates:
#                     # Choose the candidate with the maximum similarity
#                     corrected_word = max(candidates, key=lambda x: nltk.edit_distance(word, x))
#                     corrected_paragraph.append(corrected_word)
#                 else:
#                     corrected_paragraph.append(word)
#             else:
#                 corrected_paragraph.append(word)
#         else:
#             corrected_paragraph.append(word)
    
#     return ' '.join(corrected_paragraph)

# Example usage:
# paragraph = "applee"
# corrected = correct_paragraph(paragraph)
# print(corrected)
