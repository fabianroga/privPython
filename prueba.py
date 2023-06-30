print("holaaa")

nterms = int(input("cuantos digitos "))

first = 0
second = 1
count = 0

if nterms <= 0:
   print("ingrese numero mayor a 0")
# if there is only one term, return n1
elif nterms == 1:
    print("secuencia fibonnaci de ",nterms," es:")
    print(first)

else:
   print("Secuencia Fibonacci:")
   while count < nterms:
       print(first)  #  0  -  1  - 1 - 2 - 3 
       nth = first + second # 1 - 2 - 3 - 5
        # update values
       first = second  # 1 - 1 - 2 - 3
       second = nth # 1 - 2 - 3 - 5
       count += 1 
    
            