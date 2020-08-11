
'''
You have a new job at the Center for Disease Control as a Data Analyst. Your job is going well, when your boss comes in and says "we have a problem.". All of the other CDC centers are shut down due to some kind of disaster, no one can communicate with anyone else from the CDC. You're not sure what's going on, but your boss says "We've got some kind of outbreak. We need to figure out where the epicenters are."

Write a function that accepts a 2D plane as a dictionary. The dictionary represents a segment of a map, and it contains map coordinates as keys, and a count of outbreaks in the area as values. The map may be huge, which is why we're using a dictionary (because most of the map will be 0s otherwise.)

Find the center of the outbreak. The center is defined as the average of all points, but treat each case as one data point (eg, if there are 10 reports in one location, add that location to the average 10 times). Round to the nearest integer values, but return as a string: "x,y".


** examples **
straight_line = {
  "0,0": 1,
  "2,0": 2
}

square = {
  "0,0": 1,
  "2,0": 1,
  "2,2": 1,
  "0,2": 1
}


** pseudocode **
x_counter = 0
y_counter = 0
for each key:
    extract x value from key
    multiply the x value by the value
    add value to counter
    extract y
    multiply y * value
    y_counter += value
x = sum x values / count of x values
y = sum y values / count of y values
round x to integer
round y
return "x,y" string format



Example Data:

reported_outbreak = {

  "5,5": 10,

  "5,6": 8,

  "5,4": 8,

  "4,5": 8,

  "4,5": 8,

  "4,6": 8,

  "6,6": 7,

  "6,5": 8,

  "4,4": 8,

  "3,4": 4,

  "3,3": 2,

  "6,7": 2

}



The center is: "5,5" 🧟‍♀️🧟‍♂️






'''


def find_center(matrix):

    counter = 0
    x_total = 0
    y_total = 0
    # for each key:
    for key in matrix:
    #     extract x value from key
        coords = list(map(int, key.split(',')))
    #     multiply the x value by the value
        x_total += coords[0] * matrix[key]
    #     add value to counter
    #     extract y
    #     multiply y * value
        y_total += coords[1] * matrix[key]
    #     y_counter += value
        counter += matrix[key]
    # x = sum x values / count of x values
    x = round(x_total / counter)
    # y = sum y values / count of y values
    y = round(y_total / counter)
    # round x to integer
    # round y
    # return "x,y" string format
    # print(str(x) + "," + str(y))
    return str(x) + "," + str(y)
    


if __name__ == "__main__":

    reported_outbreak = {
    "5,5": 10,
    "5,6": 8,
    "5,4": 8,
    "4,5": 8,
    "4,5": 8,
    "4,6": 8,
    "6,6": 7,
    "6,5": 8,
    "4,4": 8,
    "3,4": 4,
    "3,3": 2,
    "6,7": 2
    }

    print(find_center(reported_outbreak))

