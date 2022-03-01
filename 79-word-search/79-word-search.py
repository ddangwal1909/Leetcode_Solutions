class Solution:
    
	# list of transformations that we can
	# apply to check surrounding indicies
    transformations = [(0,-1), (-1,0), (1,0), (0,1)]
    
    def exist(self, board: List[List[str]], word: str) -> bool:
		# iterate over all values in 2d array
        for i in range(len(board)):
            for j in range(len(board[0])):
				# if first letter is found, call recursive 
				# function to check for rest of word
                if board[i][j] == word[0]:
                    if self.checkWordRecurse(i,j,board,word):
                        return True
        return False
    
    def checkWordRecurse(self, i, j, board, word):
		# end of word
        if len(word) < 2: return True
		
		# store first letter for potential reconstruction
        temp = word[0]
		
		# remove current letter from word and null current index on board
        word = word[1:]
        board[i][j] = None
        
		# for each of the above transformations
        for t in self.transformations:
			# check if transformed indicies are out of bounds
			# then check if new indicies contain new first letter of word
            if ((i + t[1] >= 0 and i + t[1] < len(board)) and
                (j + t[0] >= 0 and j + t[0] < len(board[0])) and
                (board[i + t[1]][j + t[0]] == word[0])):
				# if contains, continue
                if self.checkWordRecurse(i + t[1], j + t[0], board, word):
					# once word is found continue to return up the tree
                    return True
					
		# if not found, put letter at i,j back (avoids deepcopy for each iteration)
        board[i][j] = temp
        return False