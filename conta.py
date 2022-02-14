import os


class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto....{}".format(self))
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo de {} do Titular {}.".format(self.__saldo, self.__titular))
    
    def depositar(self, valor):
        self.__saldo -= valor
        
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print ("Saque de {} foi realizado com sucesso".format(valor))
        else:
            print("O valor {} passou do limite".format(valor))
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        return print("Valor {} foi tranferido da conta {} para a conta {}". format(valor,self, destino))
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
     
    @property   
    def codigo_banco(self):
        return self.__codigo_banco
    
    @property
    def codigos_banco():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
        
        
        
        
        


    
        