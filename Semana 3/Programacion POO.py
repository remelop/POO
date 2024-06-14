class RegistroClima:
  """
  Clase que representa la información diaria del clima.

  Atributos:
    dia: El día de la semana (por ejemplo, "Lunes", "Martes").
    temperatura: La temperatura del día.
  """

  def __init__(self, dia):
    self.dia = dia
    self.temperatura = None

  def ingresar_temperatura(self):
    """
    Método para ingresar la temperatura del día.
    """
    self.temperatura = float(input(f"Ingrese la temperatura para {self.dia}: "))

  def calcular_promedio_semanal(self, registros_clima):
    """
    Método para calcular el promedio semanal de temperaturas.

    Args:
      registros_clima: Una lista de objetos RegistroClima.

    Returns:
      El promedio semanal de temperaturas como un valor flotante.
    """
    suma_temperaturas = 0
    for registro in registros_clima:
      suma_temperaturas += registro.temperatura
    promedio = suma_temperaturas / len(registros_clima)
    return promedio

# Programa principal
registros_semanales = []
for _ in range(7):
  dia = input("Ingrese el día de la semana: ")
  registro_dia = RegistroClima(dia)
  registro_dia.ingresar_temperatura()
  registros_semanales.append(registro_dia)

promedio_semanal = registros_semanales[0].calcular_promedio_semanal(registros_semanales)
print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")
