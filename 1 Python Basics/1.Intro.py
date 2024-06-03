import math
import numpy as np
#star pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" ")


#function to check prime number
def isPrime(n):
    if n <= 1:
        return 0
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return 0
        return 1
    
for i in range(2, 101):
    if isPrime(i):
        print(i,end=" ")

print('\n')
list=[1,2,3,4,5,6]
tple =(1,2,3)
array = np.array(list)

print(tple)
print(list)

print(array)

'''
my_dict ={
  "name":"Anurag",
  "id":123,
  "country":"India",
  1:"dfds"
}

print(my_dict["name"])
print(my_dict[1])

def frequency_array(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

# Example usage:
my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
frequency = frequency_array(my_list)
print(frequency)
'''
