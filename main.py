#****************************************************************************************#
#							comprobaciones del mapa										 #
#****************************************************************************************#
def check_map(row1, row2, col1, col2): #comprueba que es un mapa valido
	cnt_one = map_nums(1, row1) + map_nums(1, row2) + map_nums(1, col1) + map_nums(1, col2)
	cnt_two = map_nums(2, row1) + map_nums(2, row2) + map_nums(2, col1) + map_nums(2, col2)
	cnt_three = map_nums(3, row1) + map_nums(3, row2) + map_nums(3, col1) + map_nums(3, col2)
	cnt_four = map_nums(4, row1) + map_nums(4, row2) + map_nums(4, col1) + map_nums(4, col2)
	if cnt_one == 4:
		if cnt_four == 0:
			if cnt_two + cnt_three == 12:
				return 1
		if cnt_four == 1:
			if cnt_two + cnt_three == 11:
				return 1
		if cnt_four == 2:
			if cnt_two + cnt_three == 10:
				return 1
		for i in range (len(row1)):
			if row1[i] == 4 and row2 == 4:
				return 0
			if row1[i] == 1 and row2 == 1:
				return 0
			if col1[i] == 4 and col2 == 4:
				return 0
			if col1[i] == 1 and col2 == 1:
				return 0
	return 0

def check_error(row1, row2, col1, col2):
	if (num_not_repeated(4, row1) == 0) or (num_not_repeated(4, row2) == 0):
		return 0
	if (num_not_repeated(4, col1) == 0) or (num_not_repeated(4, col2) == 0):
		return 0
	if check_map(row1, row2, col1, col2) == 0:
		return 0
	return 1

#****************************************************************************************#
#								creacion del mapa										 #
#****************************************************************************************#

def create_row():  #crear las dos filas del mapa
	row=[]
	for i in range(4):
		row1=int(input("Introduce un numero la fila de derecha a izquierda, deben ser del 1 al 4: "))
		row.append(row1)
	return row

def create_col():  #crear las dos columnas del mapa
	col=[]
	for i in range(4):
		col1=int(input("Introduce la columna  de arriba a bajo, deben ser del 1 al 4: "))
		col.append(col1)
	return col

#En esta funcion creamos la matriz con tres contadores,
#para la misma linea se puede usar el mismo, pero para la colina no.
def create_matrix(row1, col1, row2, col2):
	matrix=[]
	n2 = 0
	n3 = 0
	for i in range (6):
		n1 = 0
		row=[]
		for j in range (6):
			if i == 0 and (j >= 1 and j <= 4):
				row.append(row1[n1])
				n1 = n1 + 1
			elif i == 5 and (j >= 1 and j <= 4):
				row.append(row2[n1])
				n1 = n1 + 1
			elif j == 0 and (i >= 1 and i <= 4):
				row.append(col1[n2])
				n2 = n2 + 1
			elif j == 5 and (i >= 1 and i <= 4):
				row.append(col2[n3])
				n3 = n3 + 1
			else:
				row.append(0)
		matrix.append(row)
	return matrix

#****************************************************************************************#
#											utils										 #
#****************************************************************************************#
def is_not_repeated(line): #comprueba si un array no está repetido
	for i in range(1,5):
		j = i + 1
		while j <= len(line) - 1:
			if line[j] == line[i]:
				return 0
			j = j + 1
	return 1

def num_not_repeated(num, array): #comprueba que no se repita mas de una vez un caracter en un array
	count = 1
	for i in range (len(array)):
		if array[i] == num:
			count = count + 1
	if count > 1:
		return 0
	return 1

def map_nums(num, array): #retorna el numero de repeticiones de un int en un array
	count = 0
	for i in range (len(array)):
		if array[i] == num:
			count = count + 1
	return count

def find_left_one(line): #busca el numero que falta en un array, es decir el numero que no se repita
	pos = 0
	for i in range(len(line)):
		if line[i] == 0:
			pos = i
	line[pos] = 1
	line[1:5]
	while 1:
		if num_not_repeated(line[pos], line) == 0:
			break
		line[pos] = line[pos] + 1
	return line[pos], pos

def return_left_one(line): #devuelve el numero que no sea repetido en un array
	num = [1, 2, 3, 4]
	j = 0
	for i in range(len(line)):
		if line[i] == num[j]:
			num.pop(j)
		else:
			j = j + 1
	return num[0]

def coordenates(matrix, num): #devuelve las coordenadas donde aparezca el numero del argumento
	crds=[]
	for i in range(1,5):
		for j in range(1,5):
			if matrix[i][j] == num:
				crds.append([i,j])
	return crds

def count_num(matrix): #retorna el numero de repeticiones de 1 2 3 y 4 en la matriz
	count_four = 0
	count_three = 0
	count_two = 0
	count_one = 0

	for i in range (1,5):
		for j in range (1,5):
			if matrix[i][j] == 4:
				count_four = count_four + 1
			elif matrix[i][j] == 3:
				count_three = count_three + 1
			elif matrix[i][j] == 2:
				count_two = count_two + 1
			elif matrix[i][j] == 1:
				count_one = count_one + 1
	return count_one, count_two, count_three, count_four

def create_options():


#****************************************************************************************#
#								solucion del sudoku										 #
#****************************************************************************************#
def one_logic(matrix): #cambia los valores de la matriz que seran siempre 4
	for i in range(6):
		for j in range(6):
			if i == 0 and  matrix[i][j] == 1:
				matrix[i + 1][j]= 4
			if i == 5 and matrix[i][j] == 1:
				matrix[i - 1][j] = 4
			if j == 0 and matrix[i][j] == 1:
				matrix[i][j + 1] = 4
			if j == 5 and matrix[i][j] == 1:
				matrix[i][j - 1] = 4

def four_logic(matrix): #pone 1 2 3 4 reppectivamente donde haya un 4
	for i in range(6):
		for j in range(6):
			if i == 0 and matrix[i][j] == 4:
				for x in range(1, 5):
					matrix[x][j] = x
			if i == 5 and matrix[i][j] == 4:
				count = 4
				for x in range(1, 5):
					matrix[x][j] = count
					count = count - 1
			if j == 0 and matrix[i][j] == 4:
				for x in range(1, 5):
					matrix[i][x] = x
			if j == 5 and matrix[i][j] == 4:
				count = 4
				for x in range(1, 5):
					matrix[i][x] = count
					count = count - 1


def line_logic(matrix): #me comprueba que si en una fila o linea falta un numero, pondra el que no se repita
	for i in range (1,5):
		cnt_row = 0
		for j in range(1,5):
			if matrix[i][j] != 0:
				cnt_row = cnt_row + 1
			if cnt_row == 3:
				val, pos = find_left_one(matrix[i])
				matrix[i][pos] = val
				return 1
	i = 1
	while i < 5: #aqui se comprueban las columnas
		temp=[]
		j = 1
		cnt_col = 0
		for x in range(1,5): #guardo la columna por separado proque se recorre diferente
			temp.append(matrix[x][i])
		while j < 5:
			if matrix[j][i] != 0:
				cnt_col = cnt_col + 1
				if cnt_col == 3:
					val, pos = find_left_one(temp[:])
					matrix[pos+1][i] = val
					return 1
			j = j + 1
		i = i + 1
	return 0

def fill_num(matrix): #si hay 3 numeros iguales en la matriz, busca donde colocar el que falta
	cnt_one , cnt_two, cnt_three, cnt_four = count_num(matrix)

	if cnt_one == 3:
		cords=coordenates(matrix, 1)
		axe_i=[]
		axe_j=[]
		for x in range(len(cords)):
			axe_i.append(cords[x][0])
			axe_j.append(cords[x][1])
		i = return_left_one(axe_i)
		j = return_left_one(axe_j)
		matrix[i][j + 1] = 1
		return 1

	if cnt_two == 3:
		cords=coordenates(matrix, 2)
		axe_i=[]
		axe_j=[]
		for x in range(len(cords)):
			axe_i.append(cords[x][0])
			axe_j.append(cords[x][1])
		i = return_left_one(axe_i)
		j = return_left_one(axe_j)
		matrix[i][j + 1] = 2
		return 1

	if cnt_three == 3:
		cords=coordenates(matrix, 3)
		axe_i=[]
		axe_j=[]
		for x in range(len(cords)):
			axe_i.append(cords[x][0])
			axe_j.append(cords[x][1])
		i = return_left_one(axe_i)
		j = return_left_one(axe_j)
		matrix[i][j + 1] = 3
		return 1

	if cnt_four == 3:
		cords=coordenates(matrix, 4)
		axe_i=[]
		axe_j=[]
		for x in range(len(cords)):
			axe_i.append(cords[x][0])
			axe_j.append(cords[x][1])
		i = return_left_one(axe_i)
		j = return_left_one(axe_j)
		print(i, j)
		matrix[i][j + 1] = 4
		return 1

	return 0

def solve_sudoku(matrix):
	cnt_line = 0
	cnt_row = 0
	while cnt_row < 5:
		while 1:
			if fill_num(matrix) == 0 and line_logic(matrix) == 0:
				break


def check_sudoku(matrix):
	for i in range(1,5):
		if is_not_repeated(matrix[i]) == 0:
			return 0

#Bloque proncipal

row1= create_row()
col1= create_col()
row2= create_row()
col2= create_col()
#if check_error(row1, row2, col1, col2) == 0:
#	print("El mapa no es valido")
#	exit()
#else:
matrix = create_matrix(row1, col2, row2, col1)
one_logic(matrix)
four_logic(matrix)
line_logic(matrix)
fill_num(matrix)
for i in range (len(matrix)):
		print(matrix[i], sep=" ")

