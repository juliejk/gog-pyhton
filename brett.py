brett = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
for i in range(antb):
    for j in range(antk):
        brett[0][0] = 0
        brett[0][i+1] = letters[i]
        brett[j+1][0] = categories[j]
        brett[j+1][i+1] = 0
        
for i in range(antk+1):
    print brett[i]
 
    