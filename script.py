def imprimir_tablero(tablero):
    """Imprime el tablero en formato legible."""
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else "." for num in fila))


def es_valido(tablero, fila, col, num):
    """
    Verifica si un número puede colocarse en la posición dada
    sin violar las reglas del Sudoku.
    """
    # Verificar fila
    if num in tablero[fila]:
        return False

    # Verificar columna
    if num in [tablero[i][col] for i in range(9)]:
        return False

    # Verificar subcuadrícula 3x3
    inicio_fila, inicio_col = 3 * (fila // 3), 3 * (col // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False

    return True


def resolver_sudoku(tablero):
    """
    Intenta resolver el tablero de Sudoku usando el algoritmo de backtracking.
    Devuelve True si el tablero se resuelve; de lo contrario, False.
    """
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:  # Si la celda está vacía
                for num in range(1, 10):  # Probar números del 1 al 9
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num  # Colocar número
                        if resolver_sudoku(tablero):  # Intentar resolver el resto del tablero
                            return True
                        tablero[fila][col] = 0  # Retroceder
                return False  # No se pudo resolver en esta rama
    return True  # Tablero completamente resuelto


# Ejemplo de un tablero de Sudoku incompleto
tablero_inicial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Tablero inicial:")
imprimir_tablero(tablero_inicial)

if resolver_sudoku(tablero_inicial):
    print("\nSudoku resuelto:")
    imprimir_tablero(tablero_inicial)
else:
    print("\nNo se pudo resolver el Sudoku.")
