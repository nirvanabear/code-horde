'''
mylist = ["a", "b", "a", "c", "c"]

output = ["a", "b", "c"]
'''

# what kind of data types?
# how long?
# is order important?

def remove_dupes(array):
    '''Remove duplicates from a list.'''
    convert_to_set = set(array)
    return list(convert_to_set)


if __name__ == "__main__":
    mylist = ["a", "b", "a", "c", "c"]
    print(remove_dupes(mylist))


