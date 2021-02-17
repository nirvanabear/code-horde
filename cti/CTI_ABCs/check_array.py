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
