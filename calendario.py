

from this import d


class Calendario:
    def __init__(self,dia, mes, ano):
       self.dia = dia
       self.mes = mes
       self.ano = ano
       
    def data(self):
        return print ("A data de hoje é {}/{}/{}". format(self.dia,self.mes,self.ano))