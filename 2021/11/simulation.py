import numpy as np

class Simulation:

    FLASH_LEVEL = 9
    
    def __init__(self, initial_state, display_steps=False):
        self.m_state = np.matrix(initial_state)
        self.m_flashed = np.zeros_like(self.m_state)
        self.m_step = 0
        self.m_flash_count = 0
        self.m_display_steps = display_steps
        

    def nextStep(self):
        self.m_state += 1
        self.m_step += 1

        if self.m_display_steps:
            print('Step {:3d} '.format(self.m_step) + '#'*20)

        while True:
            idx_to_flash = np.where(self.m_state > Simulation.FLASH_LEVEL)

            for idx in zip(idx_to_flash[0], idx_to_flash[1]):
                self.__update_neighbours(idx)

            self.m_flashed[idx_to_flash] = 1
            
            prev = (np.copy(idx_to_flash[0]), np.copy(idx_to_flash[1]))
            idx_to_flash = np.where(self.m_state > Simulation.FLASH_LEVEL)

            if len(prev[0]) == len(idx_to_flash[0]):
                break
            

        idx = np.where(self.m_state >= Simulation.FLASH_LEVEL + 1)
        self.m_flashed[idx] = 0
        self.m_state[idx] = 0

        self.m_flash_count += len(idx_to_flash[0])

        if self.m_display_steps:
            print(self.m_state)


    def __update_neighbours(self, idx):
        i = idx[0]
        j = idx[1]

        if self.m_flashed[(i, j)] == 1:
            return

        rows = self.m_state.shape[0]
        cols = self.m_state.shape[1]

        for k in range(i - 1,i + 2):
            for l in range(j - 1, j + 2):
                if k < 0 or l < 0 or k >= rows or l >= cols or (k == i and l == j):
                    continue

                self.m_state[(k, l)] += 1


