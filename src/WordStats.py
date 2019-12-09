import pymsgbox as pmb
import matplotlib.pyplot as plt
import numpy as np

"""
Get word statistics. Written in Python so you know it goes EXTRA slow.
- Sean Xie
"""

PROGRAM_NAME = 'WordStats'

# User input -----
text = ''


def user_input():
    global text
    file_path = pmb.prompt('Enter complete file path below.', PROGRAM_NAME)

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
    """A class that does it all."""

    def __init__(self, string=''):
        self.str = string
        plt.rcParams['figure.figsize'] = [10, 6]  # Set figure size.

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

    @staticmethod
    def get_alphabet_dict():
        alphabet = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
                    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                    'Y': 0, 'Z': 0}

        for word in words.keys():
            if word[0].upper() in alphabet.keys():
                alphabet[word[0].upper()] += 1

        return alphabet

    # Graph. ---
    @staticmethod
    def plot_word_quantity():
        word_label = words.keys()
        y_max = np.arange(len(word_label))
        quantity = list(words.values())

        plt.barh(y_max, quantity, align='center')
        plt.yticks(y_max, word_label)
        plt.xlabel('# of appearances')
        plt.title('Word Quantity Statistics')

        plt.ylim(-1, 30)
        plt.show()

    @staticmethod
    def plot_alphabet_quantity():
        alphabet_label = ab_dict.keys()
        y_max = np.arange(len(alphabet_label))
        quantity = list(ab_dict.values())

        plt.barh(y_max, quantity, align='center')
        plt.yticks(y_max, alphabet_label)
        plt.xlabel('# of appearances')
        plt.title('First Letter Statistics')

        plt.show()

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
analyzed_text = StringAnalyzer(string=text)

words = analyzed_text.get_word_dict()
ab_dict = analyzed_text.get_alphabet_dict()
unique_words = len(words.keys())
total_words = sum(words.values())

# I know this is a lousy way to display text. But, who doesn't like docstrings?
response = pmb.alert(
    f"""
Some facts about your text:
———————————————————————————
Total Words: {total_words}
Unique Words: {unique_words}
""", PROGRAM_NAME, 'Take me to the graphs (may take some time)')

if response == 'Take me to the graphs (may take some time)':
    response = pmb.confirm(
        """
Here are a few functions that come with the graph:
———————————————————————————
The button at the bottom left corner with 4 arrows pointing in different directions is for easy navigation.
———————————————————————————
To move around, click on the button mentioned and drag your mouse around while holding left-click.
———————————————————————————
Additionally, you can resize and adjust the scale by right-clicking and dragging your mouse around.
———————————————————————————
To save a graph, press the "floppy disk" icon also located at the bottom left corner of the graph.
———————————————————————————
        """, PROGRAM_NAME, ['Take me to the word count graph', 'Take me to the alphabet graph'])

    if response == 'Take me to the word count graph':
        analyzed_text.plot_word_quantity()

    elif response == 'Take me to the alphabet graph':
        analyzed_text.plot_alphabet_quantity()
