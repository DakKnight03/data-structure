from random import *

from queue import Queue 

class QueueSimulation:

    def __init__(self, process_rate, min_req_rate, max_req_rate, capacity):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
        self.capacity = capacity
        self.queue = Queue(capacity)

    def step(self, requests):
        result = []
        lost_count = 0
        can_process = self.process_rate
        while not self.queue.is_empty():
            result.append(self.queue.remove())
            if can_process > 0:
                can_process -= 1
        for request in requests:
            if can_process > 0:
                result.append(request)
                can_process -= 1
            else:
                if not self.queue.insert(request):
                    lost_count += 1

        return result, lost_count

    def run(self, iteration):
        lose_count = 0
        for i in range(iteration):
            request_rate = randint(self.min_req_rate, self.max_req_rate)
            request = request_rate*["A"]
            lose = self.step(request)[1]
            lose_count += lose
            
        return lose_count / iteration

sim = QueueSimulation(5, 4, 7, 2)
assert(hasattr(sim, "process_rate"))
assert(hasattr(sim, "min_req_rate"))
assert(hasattr(sim, "max_req_rate"))
assert(hasattr(sim, "step"))
assert(hasattr(sim, "run"))


requests = ["A", "B", "C", "D"]
results, lost_count = sim.step(requests)
assert(results == ["A", "B", "C", "D"])
assert(lost_count == 0)

results, lost_count = sim.step(["E", "F", "G", "H", "I", "K"])
assert(results == ["E", "F", "G", "H", "I"])
assert(lost_count == 0)

results, lost_count = sim.step(["L", "M", "N", "O", "P", "Q"])
assert(results == ["K", "L", "M", "N", "O"])
assert(lost_count == 0)

results, lost_count = sim.step(["R", "S"])
assert(results == ["P", "Q", "R", "S"])
assert(lost_count == 0)

results, lost_count = sim.step(["T", "U", "V", "W", "X", "Y"])
assert(results == ["T", "U", "V", "W", "X"])
assert(lost_count == 0)

results, lost_count = sim.step(["Z", "0", "1", "2", "3", "4", "5"])
assert(results == ["Y", "Z", "0", "1", "2"])
assert(lost_count == 1)

results, lost_count = sim.step(["6", "7", "8", "9", "10", "11", "12", "13"])
assert(results == ["3", "4", "6", "7", "8"])
assert(lost_count == 3)

lost_requests_rate = sim.run(100000)
print(lost_requests_rate)
assert(lost_requests_rate < 0.6)