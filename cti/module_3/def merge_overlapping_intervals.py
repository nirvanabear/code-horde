'''
Given [1,3],[2,6],[8,10],[5,7],[15,18],

return [1,7],[8,10],[15,18].

take 1,3 in list
take 1,3 in list
ignore since same
take 2,6 in list
compare first and second items
overlapping
combine elements to 1,6
take 1,6
compare to 8,10
not overlapping
compare to 15,18
not overlapping

take 8,10


take each element of list
    take each element in list
        compare two elements
            if overlapping
                append new element to a new list
                delete two elements
                begin from beginning of list again
            else



'''




#%%

intervals1 = [[1,3],[2,6],[8,12],[5,7],[15,18]]


def merge_overlapping_intervals(intervals):
    # empty collector for building new list of merged intervals
    new_intervals = []
    # counter for tracking if an interval has been merged
    switch_count = 0
    
    for i in range(len(intervals)):
        check_count = 0
        for j in range(len(intervals)):
            # checks the address to make sure it's not the same element
            if intervals[i] is not intervals[j]:

                # if the two intervals are equal
                # or if the i interval contains the j interval
                if intervals[i] == intervals[j] or (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]):
                    new_intervals.append(intervals[i])
                    switch_count += 1

                # if the j interval contains the i interval
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    new_intervals.append(intervals[j])
                    switch_count += 1

                # if i loop element overlaps from below
                elif intervals[i][1] >= intervals[j][0] and intervals[i][0] <= intervals[j][0]:
                    new_intervals.append([intervals[i][0], intervals[j][1]])
                    switch_count += 1

                # if the i loop element overlaps from above
                elif intervals[i][0] <= intervals[j][1] and intervals[i][1] >= intervals[j][1]:
                    new_intervals.append([intervals[j][0], intervals[i][1]])
                    switch_count += 1

                # if no comparisons occurred
                else:
                    check_count += 1

            # if an element has no overlaps anywhere, add to list
            if check_count == len(intervals) - 1:
                new_intervals.append(intervals[i])

    # removes duplicate items
    no_duplicates = []
    for k in new_intervals:
        if k not in no_duplicates:
            no_duplicates.append(k)

    # if not all overlapping intervals have merged, call the function again
    if switch_count != 0:
        no_duplicates = merge_overlapping_intervals(no_duplicates)

    return no_duplicates




merged_intervals = merge_overlapping_intervals(intervals1)

print(merged_intervals)



#%%

                    # intervals[i] = [intervals[i][0], intervals[j][1]]
                    # intervals[j] = [intervals[i][0], intervals[j][1]]

                    # intervals[i] = [intervals[i][0], intervals[j][1]]
                    # intervals[j] = [intervals[i][0], intervals[j][1]] 


# intervals2 = [[1,3],[4,6],[8,10],[12,14],[15,18]]

# intervals3 = []

# def test_fn(intervals):
#     intervals.remove([1,3])
#     intervals.remove([8,10])
#     return intervals

# answer = test_fn(intervals1)

# print(answer)
# print(intervals1)



    # new_intervals = []
    # remove_list = []
    # # i = 0
    # # while i < len(intervals):
    # for i in range(len(intervals)):
    #     check_count = 0
    #     j = 0
    #     while j < len(intervals):
    #     # for j in range(len(intervals)):
    #         # checks the address to make sure it's not the same element
    #         if intervals[i] is not intervals[j]:

    #             # if the two intervals are equal
    #             # or if the i interval contains the j interval
    #             if intervals[i] == intervals[j] or (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]):
    #                 new_intervals.append(intervals[i])

    #             # if the j interval contains the i interval
    #             elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
    #                 new_intervals.append(intervals[j])

    #             # if i loop element overlaps from below
    #             elif intervals[i][1] >= intervals[j][0] and intervals[i][0] <= intervals[j][0]:
    #                 # intervals[i] = [intervals[i][0], intervals[j][1]]
    #                 # intervals[j] = [intervals[i][0], intervals[j][1]]
    #                 # new_intervals.append([intervals[i][0], intervals[j][1]])
    #                 intervals.append([intervals[i][0], intervals[j][1]])
    #                 intervals.remove(intervals[i])
    #                 intervals.remove(intervals[j])
    #                 i = 0
                    

    #             # if the i loop element overlaps from above
    #             elif intervals[i][0] <= intervals[j][1] and intervals[i][1] >= intervals[j][1]:
    #                 # intervals[i] = [intervals[i][0], intervals[j][1]]
    #                 # intervals[j] = [intervals[i][0], intervals[j][1]] 
    #                 new_intervals.append([intervals[i][0], intervals[j][1]])








    #             # if no comparisons occurred
    #             else:
    #                 check_count += 1

    #         # if an element has no overlaps anywhere
    #         if check_count == len(intervals) - 1:
    #             new_intervals.append(intervals[i])

    # # removes duplicate items
    # no_duplicates = []
    # for k in new_intervals:
    #     if k not in no_duplicates:
    #         no_duplicates.append(k)

    # return no_duplicates



# [[1,3],[2,6],[8,12],[5,7],[15,18]]


                # else:
                #     new_intervals.append(intervals[j])
            # else:
            #     new_intervals.append(intervals[i])

    # new_intervals = []
    # addNew = False
    # for i in range(len(intervals)):
    #     while not addNew:
    #         for j in range(len(intervals)):
    #             if intervals[i] != intervals[j]:
    #                 if intervals[i][1] >= intervals[j][0]:
    #                     new_intervals.append([intervals[i][0], intervals[j][1]])
                        
    #                 elif intervals[i][0] <= intervals[j][1]:
    #                     new_intervals.append([intervals[j][0], intervals[i][1]])
    #                 else:
    #                     new_intervals
    # .append(intervals[i])





    # # first_item = intervals[0]
    # new_intervals = compare_element(intervals)
    # print(new_intervals)

# def compare_element(listing):
#     # new_listing = []
#     for element in listing:
#         for each in listing:
#             # compare element to each in listing if not identical
#             if element != each:
#                 # if overlapping
#                 if element[1] >= each[0] and element[0] <= each[0]:
#                     # write new element
#                     new_element = [element[0], each[1]]
#                     # remove element and each from list
#                     listing.remove(element)
#                     listing.remove(each)
#                     # write new list
#                     listing.append(new_element)
#                     # for every in listing:
#                     #     new_listing.append(every)
#                     # call recursive function
#                     compare_element(listing)
#                 elif element[0] <= each[1] and element[1] >= each[1]:
#                     # write new element
#                     new_element = [each[0], element[1]]
#                     # remove element and each from list
#                     listing.remove(element)
#                     listing.remove(each)
#                     # write new list
#                     listing.append(new_element)
#                     # for every in listing:
#                     #     new_listing.append(every)
#                     compare_element(listing)

                  
    # return listing

            # begin again
    # return modified intervals






#%%
# intervals1 = [[1,3],[2,6],[8,10],[15,18]]
# # print(intervals1[2][1])
# # 1 != 2
# for interval in range(len(intervals1)):
#     print(interval)


