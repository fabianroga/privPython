
import string
import random


# opening the file in read mode
#my_file = open("names.txt", "r")
# reading the file
#data = my_file.read()
# replacing end splitting the text 
# when newline ('\n') is seen.
#data_into_list = data.split("\n")
#my_file.close()

data2= ["fabian","andres","rojas","garcia"]

data3 = {
    "fabian" : "perro",
    "rojas" :"",
    "garcia" : ""
} 

def id_generator():
    car = ""
    for n in range(3):
        num = random.randint(0, 800)
        char = random.choice(string.ascii_uppercase)
        car = car + char
        car = car + str(num)
    return car

def asignar_valor():
    for n in data2:
        print(n + "  "+id_generator())

def asignar_valor_dic():
    for n in data3:
        data3[n]= str(id_generator())
        print(n + "  " +data3[n])


#data3["fabian"] = "loca"
#print(data3["fabian"])
asignar_valor_dic()
