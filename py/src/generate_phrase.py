import markovify
from utils import print_colored

text = open('sherlock.txt').read()
text_model = markovify.Text(text)
sentence = text_model.make_sentence()

print("Sentence: ", print_colored(sentence, "92"))

with open('output.txt', 'w') as out:
    out.write(sentence if sentence else "No sentence generated")
