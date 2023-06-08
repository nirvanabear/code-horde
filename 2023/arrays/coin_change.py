'''
Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. We can make changes in the following 6 ways:

1 1 1 1 1 1 1
1 1 1 1 1 2
1 1 1 2 2
1 2 2 2
1 1 5
2 5

Total Methods: 6
'''

# using American coin system, .50? 1.00?, 
# unique arrangements: set?
# iterate the first digit through each option, then append with 1s
    # then iterate the second digit
    # then third
        # until sum is automatically too large


# [1, 2, 5]
# list starter length:
# 1
#
# 2
# 2 2
# 2 2 2
# 
# 5
# 5 2
# 5 2 2
#
# 5 5  
# 5 5 2
# 5 5 2 2 
# ...


# reverse sort list        # [5,2,1]
# create list_of_addlists
# for num in coinlist:
    # create addlist
    # append num to addlist
    # for each in coinlist:
        # while sum of addlist is less than target_sum:
            # append each
        # if sum of addlist is equal to target_sum:
            # append addlist to list_of_addlists
        

'''
create listoflists
create checklist
reverse coinlist
start = 0
def fn(checklist, listoflists, start)                   
    for i in range(len(coinlist)):              
        append coinlist[i] to checklist              
        sum the checklist                                    
        if equal to targetsum:
            append checklist to listoflists
            pop checklist
        elif greater than targetsum:
            pop checklist
        elif less than targetsum:
            start = i
            listoflists = fn(checklist, listoflists, start)
    return listoflists

'''


def coin_recurse(coinlist, checklist, listoflists, target, start):
    '''Recursively explores permutations of coinlist that have sums
    which equal the target, then stores matching permutations'''
    for i in range(start, len(coinlist)):        
        checklist.append(coinlist[i])            
        total = sum(checklist)
        if total == target:
            addlist = checklist
            listoflists.append(checklist[:])
            checklist.pop()
        elif total > target:
            checklist.pop()
        elif total < target:
            start = i
            coin_recurse(coinlist, checklist, listoflists, target, start)
            checklist.pop()

def coin_change(coinlist, total):
    '''Wrapper which formats data, initializes objects to be
    used in permutation recursion, then calls recursive function.'''
    coinlist.reverse()
    listoflists = []
    checklist = []
    start = 0
    coin_recurse(coinlist, checklist, listoflists,total, start)
    return listoflists
    
# O(n) == n^n

if __name__ == "__main__":
    coinlist = [1, 2, 5]
    total = 7
    output = coin_change(coinlist, total)
    print(output)
    print(len(output))

