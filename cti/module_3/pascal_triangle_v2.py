def pascal_triangle(n):
    if n > 1:
        list_of_lists = pascal_triangle(n-1)
    if n == 1:
        return [[1]]
    if n == 2:
        list_of_lists = [[1],[1,1]]
        return list_of_lists
    if n > 2:
        next_list = [1]
        for i in range(len(list_of_lists[-1])-1):
            coeff = list_of_lists[-1][i] + list_of_lists[-1][i+1]
            next_list.append(coeff)
        next_list.append(1)
        list_of_lists.append(next_list)
        return list_of_lists 

if __name__ == "__main__":
    print(pascal_triangle(1))
    print(pascal_triangle(2))
    print(pascal_triangle(3))