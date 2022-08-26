'''


Understand: 	Analyze the problem statement
    if pairs overlap, rewrite them as a single interval with the high and low as endpoints
Match: 		    Recall problems you have seen, determine similarities
    item is in collection
Plan: 			Perform the steps, write them out, describe the process
    Example:
        Given [1,3],[2,6],[8,10],[5,7],[15,18],
        return [1,7],[8,10],[15,18].


    Naive Pseudocode: O(n^2)
        # create target variable, set to first item
        create counter, set to length of list
        while counter is not past end of list of pairs


            # save interval to list location
            compare element to next using indices
                merge if needed (rewrite target to new value)
                or delete next if enpoints are within endpoints
                decrement counter
            change comparison object during loop (copy item)
        return new list

    Sort then use a stack Pseudocode:
        call list sort method to sort in-place
        create a stack
        Nope. The added step of creating a stack and pushing
        to it makes no sense to me.


    Sort then merge in-place Pseudocode
        sort
        create counter
        check if end of a is larger than start of b
            check if end of a is larger than end of b
                if yes, delete b
            or else, change end a to equal end b
            delete b
            increment counter


Implement: 	    Translate your plan to code
Review: 		Make sure your code works, handle corner cases
Evaluate: 		Determine time & space efficiency of solution


Given [1,3],[2,6],[8,10],[5,7],[15,18],

return [1,7],[8,10],[15,18].



'''

def naive_merge_intervals(pairs):
    # print("start")
    i = 0
    while i < len(pairs):
        j = i + 1
        while j < len(pairs):
            # print(str(pairs[i]) + " vs " + str(pairs[j]))
            if pairs[i][1] > pairs[j][0]:
                if pairs[i][0] > pairs[j][0] and pairs[i][1] < pairs[j][1]:
                    pairs[i] = pairs[j]
                    # print("op1")
                    del pairs[j]
                elif pairs[i][0] < pairs[j][0] and pairs[i][1] < pairs[j][1]:
                    pairs[i] = [pairs[i][0], pairs[j][1]]
                    # print("op2")
                    del pairs[j]
            if pairs[i][0] < pairs[j][1]:
                if pairs[i][0] < pairs[j][0] and pairs[i][1] > pairs[j][1]: 
                    del pairs[j]
                    # print("op3")
                elif pairs[i][0] > pairs[j][0] and pairs[i][1] > pairs[j][1]:
                    pairs[i] = [pairs[j][0], pairs[i][1]]
                    del pairs[j]
                    # print("op4")    
            # print(pairs)
            j += 1
        i +=1
    return pairs

def sorted_merge_intervals(pairs):
    pairs.sort()
    i = 0
    while i < len(pairs) - 1:
        j = i + 1
        # print("len: " + str(len(pairs)) + ", i: " + str(i) + ", j: " + str(j))
        if pairs[i][1] > pairs[j][0]:
            if pairs[i][1] > pairs[j][1]:
                del pairs[j]
            else:
                pairs[i][1] = pairs[j][1]
                del pairs[j]
        i += 1
    return pairs

    


if __name__ == "__main__":
    laurene = [[1,3],[2,5],[2,4],[7,9],[6,8]]
    camille = [[1,3],[2,6],[8,10],[5,7],[15,18]]
    # print(naive_merge_pairs(laurene))
    # print(naive_merge_pairs(camille))

    marion = [[1,3],[2,5],[2,4],[7,9],[6,8]]
    # marion.sort()
    # print(marion)

    marion.sort(key=lambda item: item[0])
    print(marion)


    print(sorted_merge_intervals(laurene))