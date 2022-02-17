

from typing import Tuple

DEBUG = False

class Probe:

    def __init__(self, velocity:Tuple[int, int], target:Tuple[Tuple[int, int], Tuple[int, int]]) -> None:
        self.m_position = (0, 0)
        self.m_velocity = list(velocity)
        self.m_max_y = self.m_position[1]
        self.m_target = target


    def step(self) -> Tuple[bool, bool]:
        
        self.m_position = tuple(x + vx for x, vx in zip(self.m_position, self.m_velocity))

        if self.m_velocity[0] > 0:
            self.m_velocity[0] -= 1
        elif self.m_velocity[0] < 0:
            self.m_velocity[0] += 1

        self.m_velocity[1] -= 1

        if self.m_position[1] > self.m_max_y:
            self.m_max_y = self.m_position[1]

        dist = self.__from_target()

        if DEBUG:
            print('Position: {};\tTarget dist: {}'.format(self.m_position, dist), end='')
            if dist[0] == 0 and dist[1] == 0:
                print('\t[INSIDE]')
            else:
                print()

        reached = (dist[0] == 0 and dist[1] == 0)
        below = dist[1] < 0
        return  (below or reached, reached)


    def __from_target(self) -> Tuple[int, int]:
        # Find x diff
        if self.m_position[0] < self.m_target[0][0]:
            # Left from the target
            dx = self.m_position[0] - self.m_target[0][0]
        elif self.m_position[0] > self.m_target[1][0]:
            # Rigth
            dx = self.m_position[0] - self.m_target[1][0]
        else:
            # Inside the target
            dx = 0

        # Find y diff
        if self.m_position[1] > self.m_target[1][1]:
            # Over the target
            dy = self.m_position[1] - self.m_target[1][1]
        elif self.m_position[1] < self.m_target[0][1]:
            # Below the target
            dy = self.m_position[1] - self.m_target[0][1]
        else:
            dy = 0

        return (dx, dy)