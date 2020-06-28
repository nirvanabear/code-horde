#%%
def excel_column_to_number(column):
    sum = 0
    counter = 0
    for i in range(len(column)):
        rank = ord(column[-(i + 1)].upper()) - 64
        # if counter > 0:
        rank = rank * (pow(26, counter))
        counter += 1
        sum += rank
    return sum

excel_column_to_number('AAA')

# Third time changing this file



# %%
def Number(C):
    return ord(C) - ord('A') + 1

Column = 'AD'

x = Number(Column[0]) * 26
y = Number(Column[1])
n = x + y
print(n)
# %%
print("Hi!")

# %%
