# # # function call
def message_show(): #defining a function
    print("hello I am function body.")
    print("how can I help you.")
message_show() #function calling or calling a function
a=message_show()
print(a)

# # # message pass 
def message_pass(): #defining a function
    pass    #function body
message_pass
b=message_pass()
print(b)

# # # void function
# # # while defining a function we declare some variables to receive data in function here "session name" is called parameter
def welcome_info(session_name,day):
    print(f"this is {session_name} session.",day)
    print("let's start learning python programming language.")
welcome_info("python",1)#arguments
print("###########################")
print(welcome_info("java",2))

# # # return value
def sum(num1,num2):
    print("sum")
    result=num1+num2
    return (f"the return value is {result}")
print(sum(4,5))
answer=sum(3,4)
print(answer)

# # return two or more than two
def add_subtract_multiply(num1,num2,num3):
    add_result=num1+num2+num3
    subtract_result=num1-num2-num3
    multiply_result=num1*num2*num3

    return add_result,subtract_result,multiply_result

print(add_subtract_multiply(33,44,55))
result1,result2,result3=add_subtract_multiply(22,33,100)
print(result1,result2,result3)
# a,b,c=33,44,55

def api_call():
    # pass
    return 10

if api_call()==None:
    print("error:api did't return anything.")
else:
    print("Api call successfully.")


# *args with pass
def example_fun(*args):
    pass

example_fun(1,2,3,4,5,6,7)

# # *args without pass
def example_func(*args):
    print(*args)
    print(args)
    print(args[0])
example_func(1,2,3,4,5,6,7)

# *args with for loop
def example_function(*args):
    sum=0
    for number in args:
        sum=sum+number

    return sum
print(example_function(1,1,1,4,4,5,8,71))

# keyword arguments
def kwargs1(**kwargs):
    print(kwargs)
    print(kwargs['num'])
    print(kwargs.get('num2'))
    for item in kwargs:
        print(item)

    for item1 in kwargs.items():
            print(item1)

    for keys,values in kwargs.items():
            print(keys,values)
# kwargs1(1,2,3,4,5,6,7) # this is wrong approach
kwargs1(num=1,num2=33,abc="string")

def all_mix(num1,num2,*args,**kwargs):
      print(num1)
      print(num2)
      print(args)
      print(kwargs)
all_mix(22,11,11,441,44,a=33,b=44,c=44)

# default arguments
def greet(name="Binod"):
    print("Hello", name)

greet()
greet(45)