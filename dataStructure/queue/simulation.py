from random import *

class Simulation:

    def __init__(self, process_rate, min_req_rate, max_req_rate):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate

    def run(self, iteration):
        count = 0
        for i in range(iteration):
            random_num = randint(self.min_req_rate, self.max_req_rate)
            if self.process_rate < random_num:
                count += random_num - self.process_rate
            
        return count / iteration

sim = Simulation(5, 4, 7)
assert(hasattr(sim, "process_rate"))
assert(hasattr(sim, "min_req_rate"))
assert(hasattr(sim, "max_req_rate"))
assert(hasattr(sim, "run"))

lost_requests_rate = sim.run(100000)
print(lost_requests_rate)
assert(lost_requests_rate > 0.74)
assert(lost_requests_rate < 0.76)