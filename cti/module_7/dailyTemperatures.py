
'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Input
The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Sample
Input#1

T = [73, 74, 75, 71, 69, 72, 76, 73]

Output#1

[1, 1, 4, 2, 1, 1, 0, 0]


** pseudocode **
wait_list = []
length = len(dailyTemps)
for t in range(length):
    days_remaining = length - (t + 1)
    wait_period = 1
    while dailyTemps[t + wait_period] <= dailyTemps[t] and wait_period < days_remaining:
        wait_period += 1
    if dailyTemps[t + wait_period] > dailyTemps[t]:
        wait_list.append(wait_period)
    else:
        wait_list.append(0)
return wait_list


'''



def dailyTemperatures(dailyTemps):
    wait_list = []
    length = len(dailyTemps)
    for t in range(length - 1):
        days_remaining = length - (t + 1)
        wait_period = 1
        while dailyTemps[t + wait_period] <= dailyTemps[t] and wait_period < days_remaining:
            wait_period += 1
        if dailyTemps[t + wait_period] > dailyTemps[t]:
            wait_list.append(wait_period)
        else:
            wait_list.append(0)
    wait_list.append(0)
    return wait_list


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))
