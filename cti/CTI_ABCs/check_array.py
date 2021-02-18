'''
#Problem:
#Check if arr can be reconstructed by the values in array pieces. 

#Return true if it is possible to form the array arr from pieces. otherwise, return false. 

#Examples: 
#arr = [1,2,3,4], pieces = [1,2,3] --> False
#arr = [1,2,3], pieces = [3,2,1] --> True
#arr = [9,8,7], pieces = [9,8,8] --> False


** pseudocode **
create match equal to true
create a counter
while match is still equal to true and counter is less than array length:
	if array[counter] is not in pieces:
		set match equal to false
	else:
		increment counter
return match


'''



def arrayFormationI(arr, pieces):
        """
        :type arr: List[int]
        :type arr: List[int]
        :rtype: bool
        """
	match = True
	counter = 0
	while match and counter < len(arr):
		if arr[counter] not in pieces:
			match = False
		else:
			counter += 1
	return match


'''
#Problem:
# Check if the values in array pieces can be found in array arr (in the same order). 


#Return true if the values in pieces can be found in arr (in the same order). otherwise, return false. 

#Examples: 
#arr = [91,4,64,78], pieces = [4,64] --> True
#arr = [91,4,64,78], pieces = [64,4] --> False


** psedocode **

set match to true
create counter
while match is true and counter is less than length of pieces:
        if pieces[counter] is in arr:

                but do we need an index into arr
                what about repeated initial matches


** psedocode 2 **

set match equal to true
for i in range(len(pieces)):
        for j in range(len(arr)):
                if number from pieces equals number from arr:
                        create counter1 equals i + 1
                        create counter2 equals j + 1
                        while match equals true and counter1 < len of pieces and counter2 < len of arr:
                                if list[counters] don't match:
                                        match equals false
return match

'''

def arrayFormationII(arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[int]
        :rtype: bool
        """
        match = True
        for i in range(len(pieces)):
                for j in range(len(arr)):
                        if pieces[i] == arr[j]:
                                m = i + 1
                                n = j + 1
                                while match and m < len(pieces):
                                        if n >= len(arr) or pieces[m] != arr[n]:
                                                match = False
                                        else:
                                                m += 1
                                                n += 1
        return match



'''
#Problem:
#You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array of pieces[i].

#Return true if it is possible to form the array arr from pieces. otherwise, return false. 

#Examples: 
#arr = [85], pieces = [[85]] --> True
#arr = [15,88], pieces = [[88],[15]] --> True
#arr = [49,18,16], pieces = [[16,18,49]] --> False
#arr = [91,4,64,78], pieces = [[78],[4,64],[91]] --> True
#arr = [1,3,5,7], pieces = [[2,4,6,8]] --> false


** pseudocode **

for i in range(len(pieces)):
        # match routine jumps back here
        create sub-pieces index counter
        create match equals true
        while sub-pieces_index < length of sub-pieces and
              match = True and
              
                for item in arr:
                        if every == item:
                                # start match check routine


** pseudocode 2 **


match = True
# at all loops: while match remains true
go through pieces
        go through each sub-piece
                go through arr:
                        if sub-piece matches arr item:
                                # check if all other elements match
                                sub-piece index = spi + 1
                                arr index = index + 1
                                while sub-piece index < len(arr) and arr index < len(arr):
                                        if sub-piece does not equal arr item:
                                                match = False
                                                exit all loops and end program
                        if match still true:
                                remove sub-pieces from arr





'''


def arrayFormation(arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        match = True
        i = 0
        while match and i < len(pieces):
                j = 0
                while match and j < len(pieces[i]):
                        k = 0
                        while match and k < len(arr) and j < len(pieces[i]):
                                # runs match routine
                                if pieces[i][j] == arr[k]:
                                        start = k
                                        j += 1
                                        k += 1
                                        while match and k < len(arr) and j < len(pieces[i]):
                                                if pieces[i][j] != arr[k]:
                                                        match = False
                                                else:
                                                        j += 1
                                                        k += 1
                                        # prevents out-of-order True
                                        if k >= len(arr) and j < len(pieces[i]):
                                                match = False
                                        # removes matched items
                                        if match == True:
                                                arr = arr[:start] + arr[k:]
                                # prevents no-match True
                                elif k == len(arr) - 1 and j < len(pieces[i]):
                                        match = False
                                else:
                                        k += 1
                        j += 1
                i += 1
        return match
                            #arr = [91,4,64,78], pieces = [[78],[4,64],[91]] --> True            
                        


