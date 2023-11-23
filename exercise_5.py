import matrix_operators as operators
from yyc_implementation import yycAlgorithm as yyc
from reorder_matrix import reorderMatrixInAscOrder

def exercise5() :
    matrixA = [
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
    ]

    matrixB = [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
    ]

    thetaOperator = operators.thetaOperator(matrixA, matrixB)
    reorderedThetaOperator = reorderMatrixInAscOrder(thetaOperator)

    table5withPhi(thetaOperator, reorderedThetaOperator)
    print("\n=============================================\n")
    table6withGamma(thetaOperator, reorderedThetaOperator)


def table5withPhi(thetaMatrix, reorderedThetaMatrix):
    for i in range(1, 6):
        print(f"Phi Operador (N = {i}):")

        resultMatrix = operators.phiOperator(thetaMatrix, nTimes=i)
        typicalTestorsSet = yyc(resultMatrix)

        print(f"\tNúmero de Filas: {len(resultMatrix)}")
        print(f"\tNúmero de Columnas: {len(resultMatrix[0])}")
        print(f"\tNúmero de Testores: {len(typicalTestorsSet)}")

    print("\n---------------------------------------------\n")

    for i in range(1, 6):
        print(f"Phi Operador (reordenado) (N = {i}):")

        resultMatrix = operators.phiOperator(reorderedThetaMatrix, nTimes=i)
        typicalTestorsSet = yyc(resultMatrix)

        print(f"\tNúmero de Filas: {len(resultMatrix)}")
        print(f"\tNúmero de Columnas: {len(resultMatrix[0])}")
        print(f"\tNúmero de Testores: {len(typicalTestorsSet)}")

    print(" ")

def table6withGamma(thetaMatrix, reorderedThetaMatrix):
    for i in range(1, 6):
        print(f"Gamma Operador (N = {i}):")

        resultMatrix = operators.gammaOperator(thetaMatrix, nTimes=i)
        typicalTestorsSet = yyc(resultMatrix)

        print(f"\tNúmero de Filas: {len(resultMatrix)}")
        print(f"\tNúmero de Columnas: {len(resultMatrix[0])}")
        print(f"\tNúmero de Testores: {len(typicalTestorsSet)}")

    print("\n---------------------------------------------\n")

    for i in range(1, 6):
        print(f"Gamma Operador (reordenado) (N = {i}):")

        resultMatrix = operators.gammaOperator(reorderedThetaMatrix, nTimes=i)
        typicalTestorsSet = yyc(resultMatrix)

        print(f"\tNúmero de Filas: {len(resultMatrix)}")
        print(f"\tNúmero de Columnas: {len(resultMatrix[0])}")
        print(f"\tNúmero de Testores: {len(typicalTestorsSet)}")

    print(" ")
    

# exercise5() 