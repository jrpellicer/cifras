operaciones=["+", "-", "*", "/", "$", "~"] # La operación A$B equivale a B/A y la operación A~B equivale a B-A
aprox_inicial=9999

objetivo = 433
numeros = [2,8,3,1,25,9]


def calcula(operando1, operando2, operacion):
    # Calcula la operación indicada y devuelve error en caso de cero, negativo o con decimales
    resultado=0
    error=0

    if operacion=="+": resultado = operando1 + operando2
    if operacion=="-": resultado = operando1 - operando2
    if operacion=="*": resultado = operando1 * operando2
    if operacion=="~": resultado = operando2 - operando1
    if operacion=="/": 
        resultado = operando1 / operando2
        if operando1 % operando2 != 0:
            error=1
    if operacion=="$": 
        resultado = operando2 / operando1
        if operando2 % operando1 != 0:
            error=1
    
    if resultado <=0:
        error=2
    
    return resultado, error

def combina(numeros,objetivo,serie,mejor_aprox, mejor_serie):
    # Recorremos cada elemento de la lista de números
    for i in range(len(numeros)):
        # Para cada elemento recorrido i, recorremos sólo las posiciones posteriores (i+1 …)
        for j in range(i + 1, len(numeros)):
            # Para cada par de números i,j, recorre todas las operaciones posibles
            for k in range(len(operaciones)):
                resultado ,error = calcula(numeros[i], numeros[j], operaciones[k])

                # Si no ha habido error en la operación, continuamos iterando con el resultado
                if error==0:
                    operacion = (numeros[i], operaciones[k], numeros[j])
                    serie.append(operacion)

                    nueva_aprox = abs(resultado - objetivo)
                    # Comprobamos si mejora la aproximación al resultado
                    if nueva_aprox < mejor_aprox:
                        mejor_aprox  = nueva_aprox
                        mejor_serie  = serie.copy()
                        #print(mejor_serie, mejor_aprox)
                        
                    nuevos_numeros = [num for l, num in enumerate(numeros) if l not in (i, j)]
                    nuevos_numeros.append(resultado)
                    # Llamamos de nuevo a la función si aún quedan pares por calcular
                    if len(nuevos_numeros)>1:
                        mejor_aprox, mejor_serie = combina(nuevos_numeros,objetivo,serie,mejor_aprox,mejor_serie)
                    
                    serie.remove(operacion)
    
    return mejor_aprox, mejor_serie


aproximacion, serie_ganadora = combina(numeros,objetivo,[], aprox_inicial, [])
print(serie_ganadora,aproximacion)
