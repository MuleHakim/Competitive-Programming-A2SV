class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.timeToLead = {}
        count = Counter()
        lead = -1
        for person, time in zip(persons, times):
            count[person] += 1
            if count[person] >= count[lead]:
                lead = person
            self.timeToLead[time] = lead        

    def q(self, t: int) -> int:
        i = bisect_right(self.times, t)
        return self.timeToLead[self.times[i - 1]]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
