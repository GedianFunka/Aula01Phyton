class Relogio:
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        self.set_hora(horas, minutos, segundos)
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0

    def set_hora(self, h, m ,s):
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            self.__horas = h
            self.__minutos = m
            self.__segundos = s
        else:
            print("Hora inválida! A hora deve estar entre 0 e 23, os minutos entre 0 e 59 e os segundos entre 0 e 59.")

    def get_hora(self):
        return f"{self.__horas:02d}:{self.__minutos:02d}:{self.__segundos:02d}"

    def avancar(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos == 60:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas == 24:
                    self.__horas = 0

    def exibir_horarioatual(self):
        print(self.get_hora())

r1 = Relogio()
r1.set_hora(23, 58, 59)
r1.avancar()
r1.avancar()
r1.exibir_horarioatual()