class Termostato:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, nova_temperatura):
        if 16 <= nova_temperatura <= 30:
            self.__temperatura = nova_temperatura
        else:
            print("Temperatura invalida! A temperatura deve estar entre 16 e 30 graus Celsius.")

    def exibir_status(self):
        print(f"A temperatura atual é: {self.__temperatura} graus celsius")

t1 = Termostato(22)
t1.set_temperatura(15)
t1.exibir_status()

t2 = Termostato(23)
t2.set_temperatura(26)
t2.exibir_status()