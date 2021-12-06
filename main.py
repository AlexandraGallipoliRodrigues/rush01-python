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
	for i in range (len(matrix)):
		print(matrix[i])

def is_not_repeated(num, array): #comprueba que no se repita mas de una vez un caracter en un array
	count = 0
	for i in range (len(array)):
		if array[i] == num:
			count = count + 1
	if count == 2:
		return 0
	return 1

def map_nums(num, array): #retorna el numero de repeticiones de un int en un array
	count = 0
	for i in range (len(array)):
		if array[i] == num:
			count = count + 1
	return count

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
	if (is_not_repeated(4, row1) == 0) or (is_not_repeated(4, row2) == 0):
		return 0
	if (is_not_repeated(4, col1) == 0) or (is_not_repeated(4, col2) == 0):
		return 0
	if check_map(row1, row2, col1, col2) == 0:
		return 0
	return 1

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
	print("***")
	for i in range (len(matrix)):
		print(matrix[i])
#Bloque proncipal

row1= create_row()
col1= create_col()
row2= create_row()
col2= create_col()
if check_error(row1, row2, col1, col2) == 0:
	print("El mapa no es valido")
	#exit()
else:
	matrix = create_matrix(row1, col2, row2, col1)
	one_logic(matrix)

