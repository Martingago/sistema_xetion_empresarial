class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo =  self.saldo + cantidad
        else:
            print("Error, no puedes ingresar cantidades negativas")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
        else:
            print ("No tienes sufiente saldo a retirar")
    
    def mostrar_saldo(self):
        print(self.nombre, " tu saldo es de", self.saldo)


cuenta = CuentaBancaria("Martin", 1000)
cuenta.depositar(20)
cuenta.mostrar_saldo()
cuenta.retirar(80)
cuenta.mostrar_saldo()
cuenta.retirar(2000)
        