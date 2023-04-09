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

# sort list

# list of stump lists
# for num in coinlist:
    # create blank stump_list
    # while sum of list <= total_amt
        # append 


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



# create list of lists accumulator
# for i in range(len(coinlist[i])):
    # create a combolist
    # while sum of combolist < total amount

        # append coinlist[i]
        # 


        #     append another coinlist[i]
        #     sum the list
        #     if equal


        # for j in coinlist:
        #     create a jlist
        #     append j -> i,j
        

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

# c = [1, 2, 5]

# coinlist = reversed(coins)
# listoflists = []
# checklist = []
# start = 0
# target = 7
def coin_recurse(coinlist, checklist, listoflists, target, start):
    for i in range(start, len(coinlist)):
        print("***********************")
        print(f"for: {coinlist[i]}")  
        print(f"starting checklist: {checklist}") 
        print(f"start index: {start}")         
        checklist.append(coinlist[i])            
        total = sum(checklist)
        print(f"checklist sum: {total}")
        if total == target:
            print(f"target checklist: {checklist}")
            print(f"target total: {total}")
            addlist = checklist
            listoflists.append(checklist[:])
            print(f"popped listoflists: {listoflists}")
            checklist.pop()
        elif total > target:
            checklist.pop()
            print(f"checklist popped: {checklist}")
        elif total < target:
            start = i
            print(f"call fn")
            coin_recurse(coinlist, checklist, listoflists, target, start)
            print("function return")
            checklist.pop()
    # print(f"list of lists: {listoflists}")
    print("End loop")
    # return listoflists


if __name__ == "__main__":
    coinlist = [1, 2, 5]
    coinlist.reverse()
    print(f"coinlist: {coinlist}")
    listoflists = []
    checklist = []
    start = 0
    target = 7
    print(coin_recurse(coinlist, checklist, listoflists,target, start))
    print(f"final list of lists: {listoflists}")


        # print(f"total: {total}")  
        # print(f"checklist: {checklist}")  