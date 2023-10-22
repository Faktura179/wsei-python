abcString = input("Podaj trzy liczby (oddzielone przecinkami): ")

abc = []

for number in abcString.split(','):
    abc.append(float(number))

def TriangleArea(a, b, c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

def QuadraticEquation(a, b, c):
    if a == 0:
        raise ValueError("a jest równe 0")
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("Delta jest mniejsza niż 0 - nie ma rozwiązań w liczbach rzeczywistych") 
    elif delta == 0:
        return -b/(2*a)
    else:
        return ((-b-delta**0.5)/(2*a), (-b+delta**0.5)/(2*a))
    
task = int(input("Podaj zadanie ktore chcesz wykonac (1 - równanie kwadratowe, 2 - pole trójkata): "))

if(task == 1):
    print(f"Rozwiązania równania kwadratowego o współczynnikach {abc[0]}, {abc[1]}, {abc[2]} to {QuadraticEquation(abc[0], abc[1], abc[2])}")
else:
    print(f"Pole trójkąta o bokach {abc[0]}, {abc[1]}, {abc[2]} wynosi {TriangleArea(abc[0], abc[1], abc[2])}")