import numpy as np

class Board:
    next_idx = 0

    def __init__(self, lines, m_size):
        s = '; '.join(lines)
        self.m_board = np.matrix(s)
        self.m_size = m_size
        self.m_checked = np.ones_like(self.m_board)
        self.m_idx = Board.next_idx
        
        Board.next_idx += 1

    def __str__(self):
        return str(self.m_board)

    def check_number(self, n):
        # Find if the board contains the number
        idx = np.where(self.m_board == n)
        if idx[0].size == 0:
            return False

        # If the board contains the number mark it on the m_checked matrix
        self.m_checked[idx] = 0

        # Find if a row or column is complete, in that case return True
        # First check rows
        tmp = self.m_checked.sum(axis=1)
        idx = np.where(tmp == 0)
        if idx[0].size != 0:
            return True

        # Then check columns
        tmp = self.m_checked.sum(axis=0)
        idx = np.where(tmp == 0)
        if idx[0].size != 0:
            return True

        return False

    def calculate_score(self):
        return np.sum(np.multiply(self.m_board, self.m_checked))
