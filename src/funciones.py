import math
    

def es_cadena(valor):
    return isinstance(valor,str)

def es_nulo(valor):
    return math.isnan(valor)

def encontrar_numero_entero_simple(cadena):
    if isinstance(cadena, str):
        numero = ""
        encontrado = False
        for caracter in cadena:
            if caracter.isdigit():
                numero += caracter
                encontrado = True
            elif encontrado:
                encontrado = False
                break
        return int(numero)
    return None  

def modificar_rango_etario(valor):
    
        if valor == '1 - 4 ANIOS' or valor == '< 1 ANIO':
            return 'Infante'
        elif valor == '15 - 19 ANIOS':
            return 'Adolescente'
        elif valor == '40-69 ANIOS':
            return 'Adulto'
        elif valor == '>=70 AÑOS':
            return 'Anciano'
        else:
            return 'No declarado'


