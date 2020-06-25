def fizzbuzz(n):
    for i in range(1, n + 1):
        # check if divisible by 3 and 5, just 3, just 5, or neither.
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)

# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears

test_case = 15
#= int(input("Please enter an input number:"))
fizzbuzz(test_case)
