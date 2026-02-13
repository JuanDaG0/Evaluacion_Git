def analizar (lista):
    suma = sum(lista)
    mayor = max(lista)
    return(
        "suma": suma,
        "mayor": mayor 
    )

if __main__=="__main__":

numeros = [4, 8, 2, 10]
    resultado = analizar (numeros)
        print (resultado)