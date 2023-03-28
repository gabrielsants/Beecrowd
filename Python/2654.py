class Candidate():
    def __init__(self, name, power, kill, death):
        self.name = name
        self.power = power
        self.kill = kill
        self.death = death
    def __lt__(self, competitor):
        if(self.power != competitor.power):
            return self.power > competitor.power
        elif(self.kill != competitor.kill):
            return self.kill > competitor.kill
        elif(self.death != competitor.death):
            return self.death < competitor.death
        else:
            return self.name < competitor.name
        

n = int(input())
competitors = []
for i in range(n):
    data = input().split()
    name = data[0]
    power = int(data[1])
    kill = int(data[2])
    death = int(data[3])
    competitors.append(Candidate(name, power, kill, death))
competitors.sort()

print(competitors[0].name)