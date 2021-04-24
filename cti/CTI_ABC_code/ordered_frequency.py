'''
Problem
Given a string, str_a, return each word and that word's frequency in descending order by frequency.

 

Constraints

    Not case sensitive.
    A word does not contain any spaces
    The order doesn't matter for words with the same frequency.


"Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la" -> [('la', 20), ('fa', 2)]
"lala"-> [('lala', 1)] 


#Problem:
#Given two strings,str_a and str_b, find the number of times 
#str_b occurs in string a. 
#Constraints
#Not case sensitive.
#A word does not contain any spaces
#If a word ends with a punctuation mark, ignore it. 


** pseudocode **
create counter
split string into list with space as delineator
for each in list:
    if each is equal to str_b, increment counter
return counter

'''

import timeit

# Faster version
def strFrequencyA(str_a, str_b):
    counter = 0
    word_list = str_a.split(' ')
    for each in word_list:
        if ''.join(filter(str.isalnum, each.lower())) == str_b.lower():
            counter += 1
    return counter

def strFrequencyB(str_a, str_b):
    counter = 0
    word_list = str_a.split(' ')
    for each in word_list:
        match = True
        for m in range(len(str_b)):
            if str_b[m].lower() != each[m].lower():
                match = False
        if match == True:
            counter += 1
    return counter



sample = "Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la"
query = "la"


print("A :",timeit.Timer('f(sample, query)', 'from __main__ import sample,query,strFrequencyA as f').timeit(50000))
print("B :",timeit.Timer('f(sample, query)', 'from __main__ import sample,query,strFrequencyB as f').timeit(50000))

## Speed Test ##
# Verson B is slightly faster at 1000 repetitions
# A : 0.021235230000456795
# B : 0.019970036002632696

# but Version A is faster at 50000
# A : 0.8384799749983358
# B : 0.8633899909982574


'''
#Problem:
#Given a string, str_a, output all unique words.
#Constraints
#Not case sensitive.
#A word does not contain any spaces
#If a word ends with a punctuation mark, ignore it. 

#Examples
# "Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la" -> {fa, la}
# "lala"-> {lala}
# "Fa la la la la, la la la la Fa la la la la, la la la la Oh no no Deck the halls with boughs of holly Fa la la la la, la la la la (fa la la la la, la la la la) 'Tis the season to be jolly Fa la la la la, la la la la (fa la la la la, la la la la) Don we now our gay apparel Fa la la la la, la la la la (fa la la la la, la la la la) Troll the ancient Yuletide carol Fa la la la la, la la la la Fa la la la la, la la la la la la Fa la la la la, fa la la la Fa la la la la, la la la la la la Fa la la la la, fa la la la See the blazing yule before us Fa la la la la, la la la la (fa la la la la, la la la la) Strike the harp and join the chorus (Fa la la la la, la la la, fa la la la la, la la la) Follow me in merry measure Fa la la la la, la la la la, fa la la la la, la la la la While I tell of Yuletide treasure (Fa la la la la, la la la la) Fa la la la la, la la la la la la Fa la la la la, fa la la la Fa la la la la, la la la la la la Fa la la la la, fa la la la Fast away, the old year passes Fa la la la la, la la la la (fa la la la la, la la la la) Hail the new, ye lads and lasses (Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la) Sing we joyous all together, oh Heedless of the wind and weather Fa la la la la, la la la la (hey) Fa la la la la, la la la la la la (oh) Fa la la la la, fa la la la (oh) Oh oh fa la la la la, la la la la la la Fa la la la la, fa la la la Deck the halls with boughs of holly Fa la la la la, la la la la 'Tis the season to be jolly Fa la la la la, la la la la Don we now our gay apparel Fa la la la la, la la la la Troll the ancient Yuletide carol Fa la la la la, la la la la Fa la la la la, la la la la Fa la la la la, la la la la La la la la, la la la la" -> {'carol', 'ancient', 'the', 'while', 'new', 'away', 'halls', 'gay', 'follow', 'our', 'yuletide', 'strike', 'harp', 'fast', 'join', 'i', 'hail', 'joyous', 'holly', 'be', 'and', 'weather', 'hey', 'la', 'to', 'troll', 'we', 'in', 'sing', 'together', 'wind', 'with', 'deck', 'measure', 'oh', 'before', 'us', 'year', 'apparel', 'heedless', 'now', 'boughs', 'merry', 'passes', 'ye', 'yule', 'lasses', 'blazing', 'don', 'no', 'me', 'fa', 'tis', 'see', 'lads', 'season', 'chorus', 'tell', 'of', 'treasure', 'all', 'jolly', 'old'}


** pseudocode **
create empty set
separate the string into a list
for each word in the list:
    if word is not in the set, add it
return dict


'''

def strFrequencyC(str_a):
    unique_words = set()
    word_list = str_a.split(" ")
    for each in word_list:
        no_punct = "".join(filter(str.isalnum, each.lower()))
        if no_punct not in unique_words:
            unique_words.add(no_punct)
    return unique_words




'''
** pseudocode **
create dict for storage
split string into list with space as delineator 
for each in list:
    if no entry in dict, add with value 1
    else, increment
convert dict to list of tuples



'''

def strFrequencyD(str_a):
    unique_words = {}
    word_list = str_a.split(" ")
    for each in word_list:
        no_punct = "".join(filter(str.isalnum, each.lower()))
        if no_punct not in unique_words:
            unique_words[no_punct] = 1
        else:
            unique_words[no_punct] += 1
    return unique_words



'''
#Problem:
#Given a string, str_a, return each word and the word frequency in descending #order by frequency.
#Constraints
#Not case sensitive.
#A word does not contain any spaces
#If a word ends with a punctuation mark, ignore it. 
#Order doesn't matter for words with the same frequency. 
#Examples
# "Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la" -> [('la', 20), ('fa', 2)]
# "lala"-> 	
[('lala', 1)]
# "Fa la la la la, la la la la Fa la la la la, la la la la Oh no no Deck the halls with boughs of holly Fa la la la la, la la la la (fa la la la la, la la la la) 'Tis the season to be jolly Fa la la la la, la la la la (fa la la la la, la la la la) Don we now our gay apparel Fa la la la la, la la la la (fa la la la la, la la la la) Troll the ancient Yuletide carol Fa la la la la, la la la la Fa la la la la, la la la la la la Fa la la la la, fa la la la Fa la la la la, la la la la la la Fa la la la la, fa la la la See the blazing yule before us Fa la la la la, la la la la (fa la la la la, la la la la) Strike the harp and join the chorus (Fa la la la la, la la la, fa la la la la, la la la) Follow me in merry measure Fa la la la la, la la la la, fa la la la la, la la la la While I tell of Yuletide treasure (Fa la la la la, la la la la) Fa la la la la, la la la la la la Fa la la la la, fa la la la Fa la la la la, la la la la la la Fa la la la la, fa la la la Fast away, the old year passes Fa la la la la, la la la la (fa la la la la, la la la la) Hail the new, ye lads and lasses (Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la) Sing we joyous all together, oh Heedless of the wind and weather Fa la la la la, la la la la (hey) Fa la la la la, la la la la la la (oh) Fa la la la la, fa la la la (oh) Oh oh fa la la la la, la la la la la la Fa la la la la, fa la la la Deck the halls with boughs of holly Fa la la la la, la la la la 'Tis the season to be jolly Fa la la la la, la la la la Don we now our gay apparel Fa la la la la, la la la la Troll the ancient Yuletide carol Fa la la la la, la la la la Fa la la la la, la la la la Fa la la la la, la la la la La la la la, la la la la" -> [('la', 328), ('fa', 45), ('the', 12), ('oh', 6), ('of', 4), ('yuletide', 3), ('and', 3), ('we', 3), ('troll', 2), ('carol', 2), ('now', 2), ('holly', 2), ('jolly', 2), ('tis', 2), ('halls', 2), ('season', 2), ('boughs', 2), ('no', 2), ('apparel', 2), ('be', 2), ('our', 2), ('to', 2), ('deck', 2), ('with', 2), ('gay', 2), ('don', 2), ('ancient', 2), ('old', 1), ('follow', 1), ('joyous', 1), ('blazing', 1), ('in', 1), ('measure', 1), ('away', 1), ('chorus', 1), ('harp', 1), ('join', 1), ('weather', 1), ('new', 1), ('merry', 1), ('lasses', 1), ('while', 1), ('wind', 1), ('passes', 1), ('lads', 1), ('i', 1), ('together', 1), ('yule', 1), ('tell', 1), ('treasure', 1), ('year', 1), ('hey', 1), ('fast', 1), ('strike', 1), ('us', 1), ('hail', 1), ('me', 1), ('all', 1), ('heedless', 1), ('before', 1), ('see', 1), ('ye', 1), ('sing', 1)]


** pseudocode **
call previous function to produce a dict
create an iterable of tuples
create a sorted list from iterable




** timing via command line **
$ python -m timeit -s "l = range(10);" "len(l)"
10000000 loops, best of 3: 0.0677 usec per loop


'''


def strFrequencyE(str_a):
    unique_words = {}
    word_list = str_a.split(" ")
    for each in word_list:
        no_punct = "".join(filter(str.isalnum, each.lower()))
        if no_punct not in unique_words:
            unique_words[no_punct] = 1
        else:
            unique_words[no_punct] += 1
    sorted_data = sorted(unique_words.items(), key=lambda entry: entry[1], reverse=True)
    return sorted_data
    