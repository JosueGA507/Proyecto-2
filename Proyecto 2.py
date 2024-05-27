def crear_matriz(f,c):
    matriz = []
    for i in range(f):  #itera f veces una por cada fila
        fila = []
        for j in range(c): #itera c veces una por cada columna y añade un 0 a la lista fila
            fila.append(0)
        matriz.append(fila) #fila, que tiene una fila de la matriz se añadé a la lista matriz
    return matriz
#i: indice de columna    y  j: indice de fila







def cortarM(M):#cortar lista en sublistas de 4 y almacenarlas en nueva lista L
    L = []
    while M!=[]:
        L.append(M[len(M)-4:]) #añadir a L los últimos 4 elemntos de M
        M=M[0:len(M)-4] #ACTUALIZA A m PARA CONTENER TODOS ELEMNETOS MENOS ULTIMOS 4
    return(L)




def rotar_matriz(Mat):
    rotada=[]
    for i in range(len(Mat[0])): #En rango de colms de MAT añado lista vacía a rotada
        rotada.append([])#lista vacia paar poner figura rotada
        for j in range(len(Mat)): #Para J en filas de Mat
            rotada[i].append(Mat[len(Mat)-1-j][i])#incluimos ya la figura de filas que es len Mat    
            #len(Mat) - 1 es el índice de la última fila de Mat (ya que los índices en Python son 0-basados)
            #- j nos permite iterar hacia atrás a través de las filas de Mat en el bucle interno
            # si j = 0, len(Mat) - 1 - j selecciona la última fila. Si j = 1, selecciona la penúltima fila, y así sucesivamente.
            #[i]: Selecciona la columna i de la fila len(Mat) - 1 - j
            #i: indice de columna    y  j: indice de fila
    return rotada



# Función auxiliar para verificar si una pieza se puede colocar en una posición determinada
def is_valid(Tab, P, row, col):
    for i in range(len(P)):
        for j in range(len(P[0])):
            if (row + i >= len(Tab)) or (col + j >= len(Tab[0])):  # Verifica si los índices están dentro del rango válido
                return False
            if P[i][j] != '.' and Tab[row + i][col + j] != 0:
                return False
    return True

def colocar_pieza(Tab, P, fila, columna):
    for i in range(len(P)):
        for j in range(len(P[0])):
            if P[i][j] != '.':
                Tab[fila + i][columna + j] = P[i][j]

def Colocar(Tab, P):
    for i in range(len(Tab)):
        for j in range(len(Tab[0])):
            if Tab[i][j] == 0:
                for k in range(len(P)):
                    for l in range(len(P[0])):
                        if is_valid(Tab, P, i, j):
                            Tab_temporal = [fila[:] for fila in Tab]
                            colocar_pieza(Tab_temporal, P, i, j)
                            return Tab_temporal
                return Colocar(rotar_matriz(Tab), P)
    return Tab



def imprimir_tablero(tablero):
    for fila in tablero:
        print(''.join(map(str, fila)))


print("Ingrese el largo, ancho y cantidad de piezas separados por espacios:")
largo, ancho, cantidad_piezas = map(int, input().split())
tablero = crear_matriz(largo, ancho)
piezas = []

print("Ingrese las descripciones de las piezas:")
for _ in range(cantidad_piezas):
    pieza = [input() for _ in range(4)]
    piezas.append(pieza)

# Solución
tablero_final = Colocar(tablero, piezas)


imprimir_tablero(tablero_final)