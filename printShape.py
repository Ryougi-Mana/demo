# coding:utf-8

rows = int(input('输入列数： '))
# 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
i = j = k = 1

# 等腰直角三角形1
def printIsosRightTri():
	"等腰直角三角形---isosceles right triangle"
	for i in range(0, rows):
		for k in range(0, rows - i):
			print("  *  ",end = "")
			# 注意这里的","，一定不能省略，可以起到不换行的作用
			k += 1
		i += 1
		print("\n")

# 打印等边三角形
def printEquLatTri():
	"打印空心?等边三角形，这里去掉if-else条件判断就是实心的:Equi lateral triangle"
	for i in range(0, rows + 1):  # 变量i控制行数
		for j in range(0, rows - i):  # (1,rows-i)
			print(" ",end = "")
			j += 1
		for k in range(0, 2 * i - 1):  # (1,2*i)
			if k == 0 or k == 2 * i - 2 or i == rows:
				if i == rows:
					if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
						print("*",end = "")

					else:
						print(" ",end = "")
						# 注意这里的","，一定不能省略，可以起到不换行的作用
				else:
					print("*",end = "")
			else:
				print(" ",end = "")
			k += 1
		print("")
		i += 1

# 打印菱形
def printDiamond():
	"打印空心菱形，这里去掉if-else条件判断就是实心的"
	for i in range(rows):  # 变量i控制行数
		for j in range(rows - i):  # (1,rows-i)
			print(" ",end = "")
			j += 1
		for k in range(2 * i - 1):  # (1,2*i)
			if k == 0 or k == 2 * i - 2:
				print("*", end="")
			else:
				print(" ", end="")
			k += 1
		print("")
		i += 1
	# 菱形的下半部分
	for i in range(rows):
		for j in range(i):  # (1,rows-i)
			print(" ",end = "")
			j += 1
		for k in range(2 * (rows - i) - 1):  # (1,2*i)
			if k == 0 or k == 2 * (rows - i) - 2:
				print("*",end = "")
			else:
				print(" ",end = "")

			k += 1
		print("")
		i += 1


# 实心正方形
print("实心正方形")
def printSolidSquare():
	"打印实心正方形"
	for i in range(0, rows):
		for k in range(0, rows):
			print(" * ",end = "")
			# 注意这里的","，一定不能省略，可以起到不换行的作用
			k += 1
		i += 1
		print("")


# 空心正方形
def printHollowSquare():
	"打印空心正方形"
	for i in range(0, rows):
		for k in range(0, rows):
			if i != 0 and i != rows - 1:
				if k == 0 or k == rows - 1:
					# 由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
					print(" * ",end = "")
					# 注意这里的","，一定不能省略，可以起到不换行的作用
				else:
					print("   ",end = "")
					# 该处有三个空格
			else:
				print(" * ",end = "")
				# 这里*两侧加了空格
			k += 1
		i += 1
		print("")
def inputHere():
	"asd"
	print("")
	return ;

printEquLatTri()
printIsosRightTri()
printDiamond()
printSolidSquare()
printHollowSquare()

