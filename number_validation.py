

def validar_numero(numero_cliente):
    try:
        int(numero_cliente)
        return False
    except:
        return True
  