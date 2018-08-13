def round():
	#A standard round
	gb = board()
	#gb.reset()
	board.printtestboard(gb)
	choice = int(gb.sanin(input("X, pick a square: ")))
	gb.addValue(choice, "X")
	gb.printboard()
	for i in range(0,8):
		if i%2 == 0:
			choice = int(gb.sanin(input("O, pick a square: ")))
			gb.addValue(choice, "O")
			gb.printboard()
			if gb.chkboard():
				return True
		else:
			choice = int(gb.sanin(input("X, pick a square: ")))
			gb.addValue(choice, "X")
			gb.printboard()
			if gb.chkboard():
				return True
	print("Tie")
	return False
class board:
	'container for game'
	#container list
	#self.cList = [" "," "," "," "," "," "," "," "," "]
	#self.uList = []
	#checkspc = " "
	def __init__(self):
		#Initializes the board
		self.cList = [" "," "," "," "," "," "," "," "," "]
		self.uList = []
		checkspc = " "
		print("")
		#print(self.checkspc)
	def printtestboard(self):
		#prints the current layout of the board
		for i in range(0,9):
			if i%3 == 0:
				print("")
			print("[", (i+1), "]", end="" )
		print("")

	def printboard(self):
		#prints the current layout of the board
		for i in range(0,9):
			if i%3 == 0:
				print("")
			print("[", self.cList[i], "]", end="" )
		print("")

	def addValue(self, v, s):
		#adds a grid value
		self.cList[v-1] = s
		self.uList.append(v)

	def sanin(self, str):
		#checks for valid input
		while 1 == 1:
			#print (self.cList[int(str)-1])
			if (str not in self.uList) and (int(str) in range(1,10)) and (self.cList[int(str)-1] == " "):
				return str
			else:
				print("invalid input")
				str = input("try again: ")

	def chkboard(self):
		#checks for win game
		#check middle
		if self.uList[-1] == 5:
			if (self.cList[1] is self.cList[4] is self.cList[7]) or (self.cList[3] is self.cList[4] is self.cList[5]) or (self.cList[0] is self.cList[4] is self.cList[8]) or (self.cList[2] is self.cList[4] is self.cList[6]):
				print(self.cList[4], " wins!")
				return True
		#check top mid and bottom mid
		if self.uList[-1] == 2 or self.uList[-1] == 8:
			tmp = (self.uList[-1]-1)
			if (self.cList[tmp-1] is self.cList[tmp] is self.cList[tmp+1]) or (self.cList[1] is self.cList[4] is self.cList[7]):
				print(self.cList[tmp], " wins!")
				return True
		#check mid left and mid right
		if self.uList[-1] == 4 or self.uList[-1] == 6:
			tmp = (self.uList[-1]-1)
			if (self.cList[tmp-3] is self.cList[tmp] is self.cList[tmp+3]) or (self.cList[3] is self.cList[4] is self.cList[5]):
				print(self.cList[tmp], " wins!")
				return True
		#check upper left and bottom right
		if self.uList[-1] == 1 or self.uList[-1] == 9:
			tmp = (self.uList[-1]-1)
			if (self.cList[0] is self.cList[4] is self.cList[8]) or (self.cList[(tmp+3)%9] is self.cList[tmp] is self.cList[(tmp+6)%9]) or (self.cList[(tmp*2+1)%11] is self.cList[tmp] is self.cList[(tmp*2+2)%11]):
				print(self.cList[tmp], " wins!")
				return True
		#check upper right and bottom left
		if self.uList[-1] == 3 or self.uList[-1] == 7:
			tmp = (self.uList[-1]-1)
			if (self.cList[2] is self.cList[4] is self.cList[6]) or (self.cList[(tmp+3)%9] is self.cList[tmp] is self.cList[(tmp+6)%9]) or (self.cList[int(1.5*tmp)-2] is self.cList[tmp] is self.cList[(2*tmp)-4]):
				print(self.cList[tmp], " wins!")
				return True
while 1 == 1:
	round()
