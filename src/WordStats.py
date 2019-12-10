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
file_path = ''


def user_input():
    global text, file_path
    file_path = pmb.prompt('Enter complete file path below.', PROGRAM_NAME)

    try:
        try:
            with open(file_path, 'r') as file:
                text = file.read().replace('\n', '')  # Turn text into string with newlines stripped.

        except TypeError:
            return 0

    except FileNotFoundError:
        pmb.alert(f'"{file_path}" cannot be found on your computer.', 'WordStats | Error: File not found', 'Retry')
        user_input()


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
            target_idx = self.str.find(' ')  # Default target index is ' '.

            word = self.str[0:target_idx]
            self.str = self.str[target_idx + 1:]

            if word != '':  # TODO: Don't know what causing this bug. Temporary fix.
                if word not in word_dict.keys():  # An unrecorded word is encountered.
                    word_dict.update({self.strip_punctuation(word).lower(): 1})  # Add it to the dict with count = 1.

                else:
                    word_dict[word] += 1  # Word has been encountered before. Count += 1.

            if target_idx == -1:  # Cannot find space. We have reached the last word. Break.
                break

        return word_dict

    def get_num_sentences(self):
        # Brute force.
        sentance_count = 0
        sentance_ends = ('.', '?', '!')
        for char in self.str:
            if char in sentance_ends:
                sentance_count += 1

        return sentance_count

    @staticmethod
    def get_approx_reading_time():
        # Based off of the 200 words per minute average.
        value = round(sum(words.values()) / 200, 2)
        decimal = int(str(value)[2:]) / 100

        minutes = int(str(value)[0])
        seconds = int(round(decimal * 0.6, 0))

        return minutes, seconds

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
        plt.title(f'Word Quantity Statistics for "{file_path}"')

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
        plt.title(f'First Letter Statistics for "{file_path}"')

        plt.show()

    # A static method that removes punctuation "attached" to a word (ex. "word.!.?,!" is considered a word).
    @staticmethod
    def strip_punctuation(word):
        punctuation = ['.', ',', '?', '!', '"']
        res = ''
        for char in word:
            if char not in punctuation:
                res += char

        return res


# Analyse and display data. -----
words = dict()
ab_dict = dict()


def start():
    global words, ab_dict

    if user_input() == 0:  # Get input.
        return None

    analyzed_text = StringAnalyzer(string=text)

    words = analyzed_text.get_word_dict()
    ab_dict = analyzed_text.get_alphabet_dict()

    unique_words = len(words.keys())
    total_words = sum(words.values())
    num_sentences = analyzed_text.get_num_sentences()
    approx_time = analyzed_text.get_approx_reading_time()

    # I know this is a lousy way to display text. But, who doesn't like docstrings?
    response = pmb.alert(
        f"""
    Some facts about your text:
    ———————————————————————————
    Total Words: {total_words}
    Unique Words: {unique_words}
    Total Sentences: {num_sentences}
    Approximate Reading Time: {approx_time[0]} minute(s), {approx_time[1]} second(s)
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


if __name__ == '__main__':
    start()
