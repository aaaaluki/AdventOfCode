import numpy as np

class Line:
    max_x = 0
    max_y = 0

    def __init__(self, s:str):
        # Calculate points
        s = s.split('->')
        p1 = s[0].strip()
        p2 = s[1].strip()

        self.m_p1 = [int(p) for p in p1.split(',')]
        self.m_p2 = [int(p) for p in p2.split(',')]

        # Check if the line is diagonal
        if self.m_p1[0] != self.m_p2[0] and self.m_p1[1] != self.m_p2[1]:
            self.m_diagonal = True
        else:
            self.m_diagonal = False

        Line.max_x = max(Line.max_x, self.m_p1[0], self.m_p2[0])
        Line.max_y = max(Line.max_y, self.m_p1[1], self.m_p2[1])


    def draw(self, canvas, diagonals=False):
        # If diagonals are not drawn return
        if not diagonals and self.m_diagonal:
            return

        line = np.zeros_like(canvas)

        # Distance: p2 - p1
        distx = self.m_p2[0] - self.m_p1[0]
        disty = self.m_p2[1] - self.m_p1[1]
        steps = max(abs(distx), abs(disty))
        
        dx = int(distx/steps)
        dy = int(disty/steps)

        for i in range(steps + 1):
            line[self.m_p1[1] + dy*i][self.m_p1[0] + dx*i] = 1

        # Add line to the canvas
        canvas += line
