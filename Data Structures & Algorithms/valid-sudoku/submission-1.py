class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        cannot think of anything other than brute force so checking 
        solution. should try brute force on my own, and bitmask once
        I get the hang of bits again.
        '''
        # use hash sets for finding duplicate easily
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) # key = row/3 , col/3

        # go through whole grid
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue    # ignore empty
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]):  # is the value found already in the row or col or box?
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True
