import pymsgbox as pmb
import matplotlib.pyplot as plt
import numpy as np

"""
Get word statistics. Written in Python so you know it goes EXTRA slow.
- Sean Xie
"""

# User input -----
text = ''


def user_input():
    global text
    file_path = pmb.prompt('Enter complete file path below.', 'WordStats')

    try:
        try:
            with open(file_path, 'r') as file:
                text = file.read().replace('\n', '')  # Turn text into string with newlines stripped.

        except TypeError:
            pass  # In this case, the user has exited and the input is NoneType. We exit the program.

    except FileNotFoundError:
        pmb.alert(f'"{file_path}" cannot be found on your computer.', 'WordStats | Error: File not found', 'Retry')
        user_input()


user_input()  # Get input.


# Defining the tools for data analysis. -----
class StringAnalyzer:
    def __init__(self, string=''):
        self.str = string

    def get_word_dict(self):
        # Words are kept as keys to their respective number of appearances in a dictionary(hash map).
        word_dict = {}

        while 1:  # We'll keep iterating until there are no more spaces left (last word).
            whitespace_idx = self.str.find(' ')

            word = self.str[0:whitespace_idx]
            self.str = self.str[whitespace_idx + 1:]

            if word not in word_dict.keys():  # An unrecorded word is encountered.
                word_dict.update({self.strip_punctuation(word).lower(): 1})  # Add it to the dict with count = 1.

            else:
                word_dict[word] += 1  # Word has been encountered before. Count += 1.

            if whitespace_idx == -1:  # Cannot find space. We have reached the last word. Break.
                break

        return word_dict

    def get_alphabet_dict(self):
        pass

    # A static method that removes punctuation "attached" to a word (ex. "word.!.?,!" is considered a word).
    @staticmethod
    def strip_punctuation(word):
        punctuation = ['.', ',', '?', '!']
        res = ''
        for char in word:
            if char not in punctuation:
                res += char

        return res


# Analyse and display data. -----
words = StringAnalyzer(string=text).get_word_dict()
unique_words = len(words.keys())


# Graph. ---
def plot_word_quantity():
    plt.rcParams['figure.figsize'] = [len(words.keys()) // 4, len(words.keys()) // 4]

    plt.figure().gca()

    word_label = words.keys()
    y_max = np.arange(len(word_label))
    quantity = list(words.values())

    plt.barh(y_max, quantity, align='center')
    plt.yticks(y_max, word_label)
    plt.xlabel('# of appearances')
    plt.title('Word Quantity Statistics')

    plt.show()
