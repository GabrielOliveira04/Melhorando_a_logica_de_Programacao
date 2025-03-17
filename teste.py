n1 = input("n: ")
n2 = input("n: ")

sign = input("sinal : ")

if sign == "+":
    result = float(n1) + float(n2)
    print(result)

elif sign == "-":
    result = float(n1) - float(n2)
    print(result)


elif sign == "/":
    result = float(n1) / float(n2) or int(n1) / int(n2)
    if result % 2 == 0:
        print(f" Esse número é par {result}")
        print(result)
        
    else:
        print("numero impar")
