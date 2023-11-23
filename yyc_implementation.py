from typing import List
import time

# Reciber dos argumentos: el primero es el set de testores típicos obtenidos 
# hasta una determinada fila, el segundo argumento recibe una nueva columna en
# donde existe un valor de 1. Devuelve true si el nuevo set forma un testor típico
# y false si no.
#
# Para determinar si es un set compatible, debe formar una matriz identidad y
# que todas las filas al menos contengan un valor de 1.
def isCompatibleSet(originalBM, typicalTestorSubset, newColumn, actualRowIndex):
    
    subMatrix = []

    columnsIndex = list(typicalTestorSubset)
    columnsIndex.append(newColumn)

    # for para generar la submatriz
    for rowIndex in range(len(originalBM)):
        if (rowIndex > actualRowIndex) : break

        row = originalBM[rowIndex]

        subRow = []

        for column in columnsIndex:
            subRow.append(row[column])
        
        subMatrix.append(subRow)

    numColumns = len(subMatrix[0])
    counter = 0
    
    positions: List[int] = []

    for row in subMatrix:
        positionDetectedTemp = -1

        tempSum = 0
        for index in range(len(row)):
            element:int = row[index]
            
            if (element == 1):
                positionDetectedTemp = index

            tempSum += element

        if (tempSum == 1): 

            if not positionDetectedTemp in positions and positionDetectedTemp != -1:
                positions.append(positionDetectedTemp)
                counter += 1 
        
        elif (tempSum == 0): 
            # si la fila solo tiene ceros, entonces no es un testor tipico.
            return False

        if (counter == numColumns): return True

    return False

def yycAlgorithm(bm) -> List[List[int]]:
    begin = time.time()

    # Es una lista de listas. Cada sub-lista representa el set de testores tipicos
    typicalTestorsSet = []
    firstRow = bm[0]

    for index in range(len(firstRow)):
        if firstRow[index] == 1:
            typicalTestorsSet.append([index])

    for rowIndex in range(1, len(bm)):
        typicalTestorsSetAux = []
        actualRow = bm[rowIndex]

        for testor in typicalTestorsSet:
            isTestorTheSame = False

            for positions in testor:
                if (actualRow[positions] == 1) :
                    typicalTestorsSetAux.append(testor)
                    isTestorTheSame = True
                    break

            if (not isTestorTheSame):
                for columnIndex in range(len(actualRow)):
                    element = actualRow[columnIndex]

                    if (element == 1):
                        if (isCompatibleSet(bm, testor, columnIndex, rowIndex)):
                            newTestor = list(testor)
                            newTestor.append(columnIndex)

                            typicalTestorsSetAux.append(newTestor)

        typicalTestorsSet = typicalTestorsSetAux

    for testor in typicalTestorsSet:
        for elementIndex in range(len(testor)):
            testor[elementIndex] += 1

    end = time.time()
    print(f"Tiempo de ejecucuión: {end-begin} segundos")
    
    return typicalTestorsSet

basicMatrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1],
]

# yycAlgorithm(basicMatrix)
