def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio de la temperatura semanal es: {promedio:.2f}")

if __name__ == "__main__":
    main()
