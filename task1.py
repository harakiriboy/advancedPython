# Task 1
# Write a Python function which receives as an input a list of symbols (e.g. 'a','b','c'), 
# and outputs all possible strings ('abc','acb','bca'). Use the characters exactly once.


mylist = ['a','b','c']
ini_str = ''

for m in range(len(mylist)):
  ini_str += mylist[m]
 
result = []
 
def transform(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):
            # swaping
            data[i], data[j] = data[j], data[i]
            transform(data, i + 1, length)
            data[i], data[j] = data[j], data[i] 


transform(list(ini_str), 0, len(ini_str))
 
# Getting result
print("Resultant permutations", str(result))