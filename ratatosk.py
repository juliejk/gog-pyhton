from sys import stdin

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    stakk = [rot]
    while stakk:
        denne = stakk[len(stakk) - 1]
        if denne.ratatosk:
            return len(stakk) - 1
        if denne.nesteBarn == len(denne.barn):
            stakk.pop()
        else:
            stakk.append(denne.barn[denne.nesteBarn])
            denne.nesteBarn += 1

def bfs(rot):
    ko = [ (rot, 0) ] 
    while len(ko) > 0:
        denne, dybde = ko.pop(0)
        if denne.ratatosk:
            return dybde
        for b in denne.barn:
            ko.append( (b, dybde + 1) )

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print dfs(start_node)

