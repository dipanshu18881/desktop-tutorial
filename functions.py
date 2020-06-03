#parameters also introduced
def greet_user(first_name, last_name): #arguments
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "Snow")   #remember always use keyword arguments before positional arguments
greet_user(last_name="Smith", first_name="John") #keyword arguments firstname, lastname
#greet_user("Mary", "Weather")
print("Finish")
