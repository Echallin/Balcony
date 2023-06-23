a = 245
h = 200
b = 585
pole_balkonu=(a+b)*h/2


a = int(input("Podaj długość krawędzi a: "))
b = int(input("Podaj długość krawędzi b: "))
p_meb1 = a*b


a = int(input("Podaj długość krawędzi a: "))
b = int(input("Podaj długość krawędzi b: "))
p_meb2 = a*b


a = int(input("Podaj długość krawędzi a: "))
b = int(input("Podaj długość krawędzi b: "))
p_meb3= a*b


a = int(input("Podaj długość krawędzi a: "))
b = int(input("Podaj długość krawędzi b: "))
p_meb4 = a*b

a = int(input("Podaj długość krawędzi a: "))
b = int(input("Podaj długość krawędzi b: "))
p_meb5 = a*b

a = int(input("Podaj długość krawędzi a: "))
b = int(input("Podaj długość krawędzi b: "))
p_meb6 = a*b

a_1 = 60
b_1 = 40

pole_skrzyni=5*(a_1*b_1)

sum_mebl = p_meb1+p_meb2+p_meb3+p_meb4+p_meb5+p_meb6+pole_skrzyni

pozostala_powierzchnia = pole_balkonu-sum_mebl

if sum_mebl<=pole_balkonu:
    print("meble się zmieszczą")
else:
    print("meble się nie zmieszczą")

print("Pozostała powierzcnia to:" ,pozostala_powierzchnia)
