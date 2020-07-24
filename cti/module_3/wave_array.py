
'''
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...


Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

    NOTE : If there are multiple answers possible, return the one that is lexicographically smallest.



** pseudocode **

    sort(integers)
    counter = 0
    while counter < len(array):
        swap(integers, counter, counter + 1)
        counter += 2
    return integers

swap(integers, a, b)
    way_station = integers[a]
    integers[a] = integers[b]
    integers[b] = way_station




'''


def wave_array(integers):
    integers.sort()
    counter = 0
    while counter < len(integers) - 1:
        swap(integers, counter, counter + 1)
        counter += 2
    return integers

def swap(integers, a, b):
    way_station = integers[a]
    integers[a] = integers[b]
    integers[b] = way_station




if __name__ == "__main__":
    integers1 = [1, 2, 3, 4]
    print(wave_array(integers1))


