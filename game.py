X = "X"
O = "O"
EMP = " "
NULL = "NULL"
class plane:
	def __init__(self):
		self.homes = []
		for i in range(0,9):
			self.homes.append(EMP)
	def show(self):
			print("--------------------------------------")
			print("   "+self.homes[0]+"    |     "+self.homes[1]+"       |     "+self.homes[2]+"    ")
			print("--------------------------------------")
			print("   "+self.homes[3]+"    |     "+self.homes[4]+"       |     "+self.homes[5]+"    ")
			print("--------------------------------------")
			print("   "+self.homes[6]+"    |     "+self.homes[7]+"       |     "+self.homes[8]+"    ")
			print("--------------------------------------")
	def IsWin(self):
		if(self.homes[0]==self.homes[4]==self.homes[8]==X or self.homes[2]==self.homes[4]==self.homes[6]==X or self.homes[0]==self.homes[1]==self.homes[2]==X or self.homes[3]==self.homes[4]==self.homes[5]==X or self.homes[6]==self.homes[7]==self.homes[8]==X or self.homes[0]==self.homes[3]==self.homes[6]==X or self.homes[1]==self.homes[4]==self.homes[7]==X or self.homes[2]==self.homes[5]==self.homes[8]==X):
			return X
		elif(self.homes[0]==self.homes[4]==self.homes[8]==O or self.homes[2]==self.homes[4]==self.homes[6]==O or self.homes[0]==self.homes[1]==self.homes[2]==O or self.homes[3]==self.homes[4]==self.homes[5]==O or self.homes[6]==self.homes[7]==self.homes[8]==O or self.homes[0]==self.homes[3]==self.homes[6]==O or self.homes[1]==self.homes[4]==self.homes[7]==O or self.homes[2]==self.homes[5]==self.homes[8]==O):
			return O
		else:
			return 0

class branch():
	def __init__(self):
		self.father = NULL
		self.childrens = []
		self.state = NULL

playground = plane()

print(" You Are O and your Oppenent(Computer) Is X")
print("--------------house numbers --------------")
print("     1       |       2      |        3    ")
print("------------------------------------------")
print("     4       |       5      |        6    ")
print("------------------------------------------")
print("     7       |       8      |        9    ")
print("------------------------------------------")
print(" ")
fpstart = int(raw_input("Enter Who First Start 1:Computer 2:you : "))
if(fpstart == 1):
	fpstart = X
if(fpstart == 2):
	fpstart = O
if(fpstart == X):
	playground.homes[4] = X
	playground.show()
while True:
	place = int(raw_input("Is Your Turn Select Place:"))
	place = place-1
	if(place>9):
			print("WTF? Select Smaller ")
	else:
		if(playground.homes[place]!= EMP):
			print("This House Is Full Select Another")
		else:
			playground.homes[place] = O
			playground.show()




	