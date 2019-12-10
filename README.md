# WordStats
I used ```matplotlib```, ```numpy```, and ```pymsgbox``` to create a convenient (I hope) text analyzing program.
So far the program gives:
- Total words
- Unique Words
- Total sentances
- Approximate reading time
- Bar graph of every unique word and the amount of times it has appeared
- Bar graph of every starting letter of each word and the amount of times the letter has appeared.

# Download
Go to the "release" section of this repository, and download the WordStats.zip file. Extract all and run WordStats.exe.

# Usage
Simply input the entire path of your chosen text(.txt) file and you're good to go.

# Known Issues
The definition of a "word" in the program is anything between 2 spaces. Punctuation such as ".", "!", and "?" are stripped from the words. However, it is difficult to determine when apostrophes or brackets should be removed and we end up with words like "word(anotherword)". Working on it.
