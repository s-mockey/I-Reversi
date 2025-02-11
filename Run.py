# パスすることも必要
# どっちが勝ったか出力しない
# -止めバグあり


import sys
import numpy
import random

class Reversi() :
	# コンストラクタ
	def __init__ (self) :
		self.board = numpy.full((8,8),'-')
		self.board[3,3] = self.board[4,4] = 'O'
		self.board[3,4] = self.board[4,3] = 'X'
		self.direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		self.stone_pat = [('X','O'),('O','X')]


	# 盤面画面表示出力
	def view (self) :
		print (self.board)
		print('\n')

	# 設石入力
	def stone_put(self, player) :
		if player == 1 : pos = list(map(int, input(str(player) + 'さんの番です！').split()))
		else : pos = self.intelligent_put()
		return pos

	# AI_Player入力
	def intelligent_put (self) :
		# 現時点では乱数による　将来は盤面先読みを再帰する
		pos = [random.randint(0, 7), random.randint(0, 7)]
		return pos

	# 設石判定
	def stone_put_chk (self, player, pos) :
		if not self.stone_put_chk1(pos) :
			if player == 1 : print('入力ミス！ もう一度！')
			return False
		elif not self.stone_put_chk2(pos) :
			if player == 1 : print('そこは置けない！ もう一度！')
			return False
		elif (result := self.stone_put_chk3(player, pos)) == []:
			if player == 1 : print('そこは置けないよ！ もう一度！')
			return False
		return result

	# 設石判定1
	def stone_put_chk1 (self, pos) :
		try :
			if 0 <= pos[0] <=7 and 0 <= pos[1] <= 7 : return True
			raise ValueError()
		except :
			return False

	# 設石判定2
	def stone_put_chk2 (self, pos) :
		if self.board[pos[0],pos[1]] == '-' : return True
		else : return False

	# 設石判定3
	def stone_put_chk3 (self,player, pos) :
		result = []

		for px, py in self.direction :
			nx = pos[0] + px
			ny = pos[1] + py

			if 0 <= nx <= 7 and 0 <= ny <= 7 :
				if self.board[nx, ny] == self.stone_pat[player - 1][0] :
					while True :
						nx += px
						ny += py
						if 0 <= nx <= 7 and 0 <= ny <= 7 :
							if self.board[nx, ny] == self.stone_pat[player - 1][1] :
								result.append([px,py])
								break
						else : break
		return result

	# 設石と反転
	def stone_update (self ,player, pos ,dir) :
		for px, py in dir :
			nx = pos[0]
			ny = pos[1]

			while True :
				self.board[nx, ny] = self.stone_pat[player - 1][1]
				nx += px
				ny += py
				if nx < 0 or nx >7 or ny < 0 or ny > 7 or self.board[nx, ny] == self.stone_pat[player - 1][1] : break

	# Player操作
	def play(self,player) :
		pos = self.stone_put(player)
		if not (dir := self.stone_put_chk(player, pos)) : return self.play(player)
		print(pos)
		self.stone_update(player, pos, dir)

	# ゲーム開始
	def start(self) :
		count = 0
		self.view()

		while (numpy.any(self.board == '-')) :
			self.play(count%2+1)
			self.view()
			count += 1

if __name__ == "__main__":

	Reversi().start()
