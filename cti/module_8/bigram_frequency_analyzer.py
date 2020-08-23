
'''
Given a long string of text, do not ignore punctuation.
Break the text into individual words. Then, for every two words, count the frequency of words that come after those two words by storing them as a list of occurrences. Return a string (with line breaks) that shows the frequency of those words.

For example, given:

I do not like green eggs and ham,
I do not like them, Sam-I-Am!
I do not like them with a fox,
I do not like them in a box.
I do not like them here or there,
I do not like them anywhere!
I do not like them, Sam-I-Am,
I do not like green eggs and ham!


Output:
 

I do : not (8) 
do not : like (8) 
not like : green (2) them, (2) them (4) 
like green : eggs (2) 
green eggs : and (2) 
eggs and : ham, (1) ham! (1) 
and ham, : I (1) 
ham, I : do (1) 
like them, : Sam-I-Am! (1) Sam-I-Am, (1) 
them, Sam-I-Am! : I (1) 
Sam-I-Am! I : do (1) 
like them : with (1) in (1) here (1) anywhere! (1) 
them with : a (1) 
with a : fox, (1) 
a fox, : I (1) 
fox, I : do (1) 
them in : a (1) 
in a : box. (1) 
a box. : I (1) 
box. I : do (1) 
them here : or (1) 
here or : there, (1) 
or there, : I (1) 
there, I : do (1) 
them anywhere! : I (1) 
anywhere! I : do (1) 
them, Sam-I-Am, : I (1) 
Sam-I-Am, I : do (1) 


Important:
Make sure your output string is formatted as shown. Do not trim any whitespace off the end of each line.



** pseudocode **

take text as argument
make a dict for {sequence : [following (count), ...]}
break up text into a list of words, w/ punctuation and spaces attached
for each word in text:
    take the word and next word in sequence
    for each matched instance of that sequence in text:
        store the following word after each match of the sequence
        keep count of following words
        add to dict with the two sequential words as key
display all sequences with following words and counts
    


** scratch paper **

dictionary = {'not like ' : {'green ':4, 'them, ':2, 'them ':4}}


text_list = re.findall(r'\S+\s', SamIAm)
checked_phrases = []
for p in range(len(text_list) - 1):
    phrase = text_list[p] + text_list[p+1]
    text_list.count(text_list[p+2])
    print(text_list[p+2] + str(text_list.count(text_list[p+2])))

    re.sub('\n', ' ', ham) 

    text_list = re.findall(r'\S+\s+', text)
    checked_phrases = []
    for p in range(len(text_list) - 2):  ## EDIT: This MUST be -1 instead
        phrase = text_list[p] + text_list[p+1]
        if phrase not in checked_phrases:
            # text_list.count(text_list[p+2])
            print(re.sub('\n', ' ', text_list[p+2]) + str(text_list.count(text_list[p+2])))
            checked_phrases.append(phrase)



** repl.it error **

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 83, in test_dr_seuss
    self.assertEquals(answer, solution)
AssertionError: 'I do[141 chars] ham!(1) \nand ham, : I (1) \nham, I : do (1) [470 chars]) \n' != 'I do[141 chars] ham! (1) \nand ham, : I (1) \nham, I : do (1)[471 chars]) \n'
Diff is 754 characters long. Set self.maxDiff to None to see it.


** original functional code **

import re

def bigram_frequency_analyzer(text):
    # make a dict for {sequence : [following (count), ...]}
    phrase_dict = {}
    # break up text into a list of words, w/ punctuation and spaces attached
    text_list = re.findall(r'\S+\s+|\S+', text)
    # substitutes /n with a space
    for n in range(len(text_list)):
        text_list[n] = re.sub('\n', ' ', text_list[n])
    # print(text_list)
    # for each word in text, except for the last two
        # since they won't have a following word
    for p in range(len(text_list) - 2):
        # take the word and next word in sequence
        phrase = text_list[p] + text_list[p+1]
        if phrase not in phrase_dict:
            phrase_dict[phrase] = dict()
            # for each matched instance of that sequence in text,
            # store in a sub-dictionary with counts
            for q in range(len(text_list) - 2):
                if phrase == text_list[q] + text_list[q+1]:
                    if text_list[q+2] not in phrase_dict[phrase]:
                        phrase_dict[phrase][text_list[q+2]] = 1
                    else:
                        phrase_dict[phrase][text_list[q+2]] += 1

    frequency = ""
    for each in phrase_dict:
        line = each + ": "
        for every in phrase_dict[each]:
            line = line + every + "(" + str(phrase_dict[each][every]) + ") "
        frequency = frequency + line + "\n"
    return frequency



'''
import re

def bigram_frequency_analyzer(text):

    # make a dict for {two-word-sequence : [following (count), ...]}
    phrase_dict = {}
    text_list = []

    text_to_list(text, text_list)
    third_word_counts(text_list, phrase_dict)
    # print(phrase_dict)
    frequency = ""
    for each in phrase_dict:
        line = each + ": "
        for every in phrase_dict[each]:
            line = line + every + "(" + str(phrase_dict[each][every]) + ") "
        frequency = frequency + line + "\n"

    return frequency


# for each word in text, except for the last two
# since they won't have a following word
def text_to_list(text, text_list):

    # break up text into a list of words, w/ punctuation and spaces attached
    for each in re.findall(r'\S+\s+|\S+', text):
        if each[-1] != ' ':
            each += ' '
        text_list.append(each)
    # substitutes /n with a space
    for n in range(len(text_list)):
        text_list[n] = re.sub('\n', ' ', text_list[n])

    return text_list


def third_word_counts(text_list, phrase_dict):

    for p in range(len(text_list) - 2):
        # take the word and next word in sequence
        phrase = text_list[p] + text_list[p+1]
        if phrase not in phrase_dict:
            phrase_dict[phrase] = dict()
            # for each matched instance of that sequence in text,
            # store in a sub-dictionary, with counts
            for q in range(len(text_list) - 2):
                if phrase == text_list[q] + text_list[q+1]:
                    if text_list[q+2] not in phrase_dict[phrase]:
                        phrase_dict[phrase][text_list[q+2]] = 1
                    else:
                        phrase_dict[phrase][text_list[q+2]] += 1

    return phrase_dict





if __name__ == "__main__":

    SamIAm = '''I do not like green eggs and ham,
I do not like them, Sam-I-Am!
I do not like them with a fox,
I do not like them in a box.
I do not like them here or there,
I do not like them anywhere!
I do not like them, Sam-I-Am,
I do not like green eggs and ham!'''
    print(bigram_frequency_analyzer(SamIAm))
