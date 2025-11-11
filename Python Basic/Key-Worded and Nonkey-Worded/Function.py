#Variable numbers of argument
#Non-keyworded Arguments (*args)
def total(*number):
    return sum(number)

print(total(2,3,4,5)) 

# Keyworded Argument(**args)
def print_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")
print_details(name = "Payel", Age = 24, City = "Bangalore")


# Key argument
def details(name,age):
    print(f"Name : {name} Age : {age}")
details(name="Shaswata",age=26)


# Normal function Passing Multiple Arguments
def cal(a,b):
    return a+b, a*b
print(cal(20,10))

# Passing list in a function
def maxima(lst):
    return max(lst)
print(maxima([2,1,4,6,5]))