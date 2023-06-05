def transaccion(cantidad, balance, tipo='depósito'):

    def deposito(cantidad, balance):
        return cantidad + balance
    

    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
    
    
    if tipo == 'depósito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)


reuslt = transaccion(10, 30)
print(reuslt)
reuslt = transaccion(10, 30, 'retiro')
print(reuslt)