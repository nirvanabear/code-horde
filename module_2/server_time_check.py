
'''
How many timed tasks in the list can be completed in the time limit?

Input:
6 180
45 30 55 20 80 20

Output:
4
'''

def server_time_check(task_config, task_times):
    task_list = [int(each) for each in task_times.split()]
    config_list = [int(each) for each in task_config.split()]
    runTime = 0
    # taskCounter = 0
    iteration = 0
    while runTime <= config_list[1] and iteration < config_list[0]:
        runTime += task_list[iteration]s
        if runTime <= config_list[1]
            iteration += 1
    
    return iteration
  

## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input("Please input the number of tasks, and the maximum total execution time:")
task_times = input("Please input the execution times of each task, seperated with a space:")

server_time_check(task_config, task_times)


#%%

# numbers = "45 30 55 20 80 20"
# print(numbers.split())

# %%
