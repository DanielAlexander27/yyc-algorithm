from typing import List
import matrix_operators as operators
from input_matrix import requestData
from yyc_implementation import yycAlgorithm

def printHeader():
    print("\t\tUNIVERSIDAD SAN FRANCISCO DE QUITO")
    print("\t\t\tMATEMÁTICAS DISCRETAS")
    print("\t\t\tTeoría de Testores")


def applyOperator(operatorType: operators.OperatorEnum, matrixA: List[List[int]],  matrixB: List[List[int]] = None, nTimes: int = 1) -> List[List[int]]:
    resultMatrix : List[List[int]] = []

    match operatorType:
        case operators.OperatorEnum.THETHA:
            resultMatrix = operators.thetaOperator(matrixA=matrixA, matrixB=matrixB, nTimes=nTimes)
        case operators.OperatorEnum.GAMMA:
            resultMatrix = operators.gammaOperator(matrixA=matrixA, matrixB=matrixB, nTimes=nTimes)
        case operators.OperatorEnum.PHI:
            resultMatrix = operators.phiOperator(matrixA=matrixA, matrixB=matrixB, nTimes=nTimes)
    
    print(" ")
    operators.calculateRowsAndColumns(resultMatrix)
    print(f"Cantidad de testores típicos: {len(yycAlgorithm(resultMatrix))}\n")


    return resultMatrix

def askToAplyOperator(matrix:List[List[int]]) :
    errorDetected:bool = False

    while (True):

        if not errorDetected:
            print("\n¿Desea aplicar algún operador sobre la matriz resultante?")

            print("\t1. Operador theta")
            print("\t2. Operador gamma")
            print("\t3. Operador phi")
            print("\t4. No deseo aplicar\n")

        try:
            option = input("\t? ")
            option = int(option)

            assert(option >= 1 or option <= 4), "No existe la opción solicitada. Intenta nuevamente"

            if option != 4: 
                nTimes = input("Cantidad de veces a aplicar el operador: ")
                nTimes = int(nTimes)

                assert(nTimes >= 0), "El valor debe ser mayor o igual a cero"
            
            errorDetected: False

            match option:
                case 1:
                    matrixInput = applyOperator(operatorType=operators.OperatorEnum.THETHA, matrixA=matrix, nTimes=nTimes)
                    
                case 2:
                    matrixInput = applyOperator(operatorType=operators.OperatorEnum.GAMMA, matrixA=matrix, nTimes=nTimes)
                    
                case 3:
                    matrixInput = applyOperator(operatorType=operators.OperatorEnum.PHI, matrixA=matrix, nTimes=nTimes)
                    
                case 4:
                    print(" ")
                    break

        except AssertionError as ae:
            errorDetected = True
            print(ae)
        except:
            errorDetected = True
            print("Escoje una opción correcta.\n")


def firstOption():
    matrixInput = requestData()
    typicalTestorsSet = yycAlgorithm(matrixInput)
    print(f"Los testores típicos son: {typicalTestorsSet}")
    print(f"Cantidad de testores típicos encontrados: {len(typicalTestorsSet)}")

    errorDetected:bool = False

    askToAplyOperator()


def secondOption():
    print("Datos para Matriz A")
    matrixA = requestData()

    print("Datos para Matriz B")
    matrixB = requestData()

    matrixResult:List[List[int]] = []
    
    errorDetected:bool = False

    while (True):

        if not errorDetected:
            print("\n¿Qué operador desea aplicar?")

            print("\t1. Operador theta")
            print("\t2. Operador gamma")
            print("\t3. Operador phi\n")

        try:
            option = input("\t? ")
            option = int(option)

            assert(option >= 1 or option <= 3), "No existe la opción solicitada. Intenta nuevamente."
           
            errorDetected: False

            match option:
                case 1:
                    matrixResult = applyOperator(operatorType=operators.OperatorEnum.THETHA, matrixA=matrixA, matrixB=matrixB)
                    
                case 2:
                    matrixResult = applyOperator(operatorType=operators.OperatorEnum.GAMMA, matrixA=matrixA, matrixB=matrixB)
                    
                case 3:
                    matrixResult = applyOperator(operatorType=operators.OperatorEnum.PHI, matrixA=matrixA, matrixB=matrixB)
            
            askToAplyOperator(matrixResult)
            break


        except AssertionError as ae:
            errorDetected = True
            print(ae)
        except:
            errorDetected = True
            print("Escoje una opción correcta.\n")


def printMenu():
 
    while (True):
        print("Escoge una opción:")
        print("\t1. Calcular testores típios de una matriz básica.")
        print("\t2. Aplicar operadores de matriz en dos matrices (A y B)")
        print("\t3. Salir\n")

        try :
            option = input("\t? ")
            option = int(option)
            assert(option == 1 or option == 2 or option == 3), "No existe la opción"

            match option:
                case 1:
                    firstOption()
                case 2:
                    secondOption()
                case 3:
                    print("¡Gracias por usar el programa!")
                    break




        except:
            print("Opción Incorrecta. Intenta nuevamente\n")


def main():
    printHeader()
    printMenu()

main()