# Solution

# Sum of First n Natural numbers , Ask user for Number.


def myreduce(num):
    ''' This functionm will return sum of n Natural numbers'''
    num_list = list(range(1, number + 1))
    sum_of_elements = 0

    for i in num_list:
        sum_of_elements += i

    return num_list, sum_of_elements


# Input
print("Input:")
number = int(input("Please insert the number :"))

# Function Execution

output_value = myreduce(number)

# Output
print("Output:")
print("List of First n Natural numbers are:", output_value[0])
print("Sum of List elements are :", output_value[1])

print("Input:")
number=int(input("Please insert the number :"))

num_list= list(range(1,(number+1)))
# Import reduce function
from functools import reduce
sum_of_elements = reduce((lambda x, y: x + y), num_list)

#Output
print("Output:")
print("List of First n Natural numbers are:",num_list)
print("Sum of List elements are :",sum_of_elements)

# Solution

# Filter the even and odd number from list which are multiples  of 5

# Input

print("Input:")
number = int(input("Please insert the number: "))

num_list = list(range(1, number + 1))


def myfilter(num_list):
    '''This function will filter even and odd numbers from list which are multiples of 5 '''
    num_even_list = []
    num_odd_list = []

    for i in num_list:
        if (i % 5 == 0):
            if (i % 2 == 0):
                num_even_list.append(i)
            else:
                num_odd_list.append(i)

    return num_even_list, num_odd_list


# Function Execution
output_value = myfilter(num_list)

# Output

print("Output:")
print("List of numbers:", num_list)
print("List of Even numbers, which are multiples of 5 are:", output_value[0])
print("List of Odd numbers, which are multiples of 5 are:", output_value[1])

print("Input:")
number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))

num_even_list=list(filter(lambda x: x%2==0,list(filter(lambda x: x%5==0 ,num_list))))
num_odd_list= list(filter(lambda x: x%2!=0,list(filter(lambda x: x%5==0 ,num_list))))

print("Output:")

print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",num_even_list)
print("List of Odd numbers, which are multiples of 5 are:",num_odd_list)
