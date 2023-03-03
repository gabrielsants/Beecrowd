data = input().split()
pi = 3.14159
a = float(data[0])
b = float(data[1])
c = float(data[2])


triangulo = (a * c)/2
circulo = (c * c) * pi
trapezio =((a + b) / 2) * c
quadrado = b * b
retangulo = a * b

print("TRIANGULO: %0.3f" %triangulo)
print("CIRCULO: %0.3f" %circulo)
print("TRAPEZIO: %0.3f" %trapezio)
print("QUADRADO: %0.3f" %quadrado)
print("RETANGULO: %0.3f" %retangulo)