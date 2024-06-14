def ingresar_temperatura_dia(dia):
  """
  Función para ingresar la temperatura de un día específico.

     dia: El día de la semana (por ejemplo, "Lunes", "Martes", "Miercoles" , "Jueves" . "Viernes" , "Sabado" , "Domingo").

  Returns:
    La temperatura ingresada como un valor flotante.
  """
  temperatura = float(input(f"Ingrese la temperatura para {dia}: "))
  return temperatura

def calcular_promedio_semanal(temperaturas):
  """
  Función para calcular el promedio semanal de temperaturas.

  Returns:
    El promedio semanal de temperaturas como un valor flotante.
  """
  suma_temperaturas = 0
  for temperatura in temperaturas.values():
    suma_temperaturas += temperatura
  promedio = suma_temperaturas / len(temperaturas)
  return promedio

# Programa principal
temperaturas_semanales = {}
for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
  temperatura_dia = ingresar_temperatura_dia(dia)
  temperaturas_semanales[dia] = temperatura_dia

promedio_semanal = calcular_promedio_semanal(temperaturas_semanales)
print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")
