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

def is_not_repeated(num, array): #comprueba que no se repita mas de una vez un caracter en un array
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

def find_left_one(line):
	print(line)
	pos = 0
	for i in range(len(line)):
		if line[i] == 0:
			pos = i
	line[pos] = 1
	line[1:5]
	while 1:
		if is_not_repeated(line[pos], line) == 0:
			break
		line[pos] = line[pos] + 1
	return line[pos], pos

def line_logic(matrix):
	for i in range (1,4):
		cnt_row = 0
		for j in range(1,4):
			if matrix[i][j] != 0:
				cnt_row = cnt_row + 1
				if cnt_row == 3:
					val, pos = find_left_one(matrix[i])
					matrix[i][pos] = val
	i = 1
	while i < 5:
		temp=[]
		j = 1
		cnt_col = 0
		for x in range(1,5):
			temp.append(matrix[x][i])
		while j < 5:
			if matrix[j][i] != 0:
				cnt_col = cnt_col + 1
				if cnt_col == 3:          #ojo! esto es para que temp contemga el numero 0 restante
					val, pos = find_left_one(temp[:])
					matrix[pos+1][i] = val
			j = j + 1
		i = i + 1

def check_sudoku():
	d
#Bloque proncipal

row1= create_row()
col1= create_col()
row2= create_row()
col2= create_col()
#if check_error(row1, row2, col1, col2) == 0:
#	print("El mapa no es valido")
	#exit()
#else:
matrix = create_matrix(row1, col2, row2, col1)
one_logic(matrix)
matrix[4][4]=2
matrix[4][3]=3
line_logic(matrix)
for i in range (len(matrix)):
		print(matrix[i], sep=" ")
