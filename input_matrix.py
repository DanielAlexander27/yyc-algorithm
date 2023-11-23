from typing import List


def separateList(stringRow: str) -> List[int] :

    stringRow = stringRow.strip()

    elements: List[str] = stringRow.split(' ')

    rowNum: List[int] = []

    for element in elements:
        if (element == ''):
            continue
        
        rowNum.append(int(element))

    return rowNum

def checkRowIsCorrect(numColumns: int, row: List[int]):
    assert(len(row) == numColumns), "El número de elementos de la fila excede la cantidad de columnas."

    assert all (element == 0 or element == 1 for element in row), "Es una matriz booleana, por lo tanto, no puedes ingresar valores distintos de 0 y 1."


def requestData() -> List[List[int]]:
    numRows = -1
    numColumns = -1

    while (True):
        numRows = input("Introduce el número de filas para la matriz: ")
        numColumns = input("Introduce el número de columnas para la matriz: ")
        print(" ")

        try: 
            numRows = numRows.strip()
            numColumns = numColumns.strip()

            numRows = int(numRows)
            numColumns = int(numColumns)

            assert(numRows >= 0 and numColumns >= 0)

            break

        except:
            print("Uno de los valores no fue introducido correctamente. Vuelve a introducir.\n")

    matrix:List[List[int]] = []
    currentRow = 0

    while(currentRow < numRows):

        try:
            stringRow = input(f"Fila {currentRow+1:>3}: ")
            numRow = separateList(stringRow)

            checkRowIsCorrect(numColumns, numRow)
            matrix.append(numRow)

            currentRow = currentRow + 1
        except AssertionError as ae:
            print(ae)
        except:
            print("Se ha producido un error. Vuelva a introducir la matriz correctamente.")

    print("") 
    return matrix

