
class Simulation:

    def __init__(self, initial_state, cycle, new_cycle):
        self.m_cycle = cycle
        self.m_new_cycle = new_cycle
        self.m_state = Simulation.histogram(initial_state, new_cycle)


    def nextDay(self):
        # See how many fishes are going to create new ones
        new_fishes = self.m_state[0]

        # Shift array left, same as subtracting 1 to all fishes cycles
        # And add new fishes with cycle = new_cycle
        self.m_state = self.m_state[1::] + [new_fishes]

        # The fishes with cycle=0 now go to cycle
        self.m_state[self.m_cycle] += new_fishes

    # Calculate the histogram, some supositions are made:
    #   - The smalles number is zero or bigger
    #   - The bigest number is max_val
    #   - There are only integer values
    def histogram(arr, max_val):
        result = [0]*(max_val + 1)
        for n in arr:
            result[n] += 1
        
        return result
