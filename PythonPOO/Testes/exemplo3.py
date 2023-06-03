#Treinando métodos estáticos

class ConversorTemperatura:

    @staticmethod
    def celsius_para_fahrenheit(celsius):
        fahrenheit = (celsius * 9) / 5+ 32
        print(f"{celsius}ºC para Fahrenheit é {fahrenheit}ºF")

ConversorTemperatura.celsius_para_fahrenheit(float(input("Digite uma temperatura em Celsius: ")))