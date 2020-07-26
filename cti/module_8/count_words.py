
'''
Given a long text string, count the number of occurrences of each word. Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old" are one word, and three different words, respectively. 

Return the word counts as a string formatted with line breaks, in alphanumeric order.

Example:

"I do not like green eggs and ham,
I do not like them, Sam-I-Am"


Output:

i 2
do 2
not 2
like 2
green 1
eggs 1
and 1
ham 1
them 1
sam-i-am 1


Also Valid:
and 1
do 2
eggs 1
green 1
ham 1
i 2
like 2
not 2
sam-i-am 1
them 1



** pseudocode **

break into list
sort alphabetically
count each word once
store counts in a dict



'''

import re
from collections import Counter


def count_words(text):
    text_list = []
    text_to_list(text, text_list)
    text_list.sort()
    counts = Counter()
    for word in text_list:
        if word not in counts:
            counts[word] = sum(1 for z in re.finditer(word, text, re.IGNORECASE))
    output = ""
    for key in counts:
        output = output + key + " " + str(counts[key]) + "\n"
    return output

        
def text_to_list(text, text_list):
    # break up text into a list of words, dashes included
    for each in re.findall(r'[-\w]+', text):
    # for each in re.split(r'\s+|\W+\s+', text):
        text_list.append(each.lower())
    # substitutes /n with a space
    for n in range(len(text_list)):
        text_list[n] = re.sub('\n', ' ', text_list[n])
    return text_list


SamIAm = '''I do not like green eggs and ham,
I do not like them, Sam-I-Am'''
print(count_words(SamIAm))


