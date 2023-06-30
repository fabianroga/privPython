
import string
import random


# opening the file in read mode
my_file = open("names.txt", "r")
# reading the file
data = my_file.read()
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
my_file.close()



def id_generator():
    car = ""
    for n in range(3):
        num = random.randint(0, 800)
        char = random.choice(string.ascii_uppercase)
        car = car + char
        car = car + str(num)
    return car

def asignar_valor():
    for n in data_into_list:
        print(n + "  "+id_generator())



asignar_valor()
print(id_generator())


    




