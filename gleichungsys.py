import numpy as np

def getData():
    return "1.49,1.98;-0.48,-1.49;0.98,0.66;2.73,0.19"#input("Punkte angeben mit format: zahl.dezimal,zahl.dezimal;...")

def splitDataIntoPoints(data):
    return data.split(";")

#not optimal
def createGleichungssystem(points):
    exponent = int(input("exponent: "))
    bigger_arr = []
    arr =  []
    for p in points:
        x,y = p.split(",")
        for i in range(exponent, -2, -1):
            if(i > 1):
                arr.append(pow(float(x),i))
            elif(i == 1):
                arr.append(float(x))
            elif(i == 0):
                arr.append(1.0)
            elif(i == -1):
                arr.append(float(y))
        bigger_arr.append(arr.copy())
        arr.clear()
    return np.array(bigger_arr)
    
data = getData()  
points = splitDataIntoPoints(data)
gleichungssystem = createGleichungssystem(points)
#first step, first row
for i in range(1,4):
    multiplier = gleichungssystem[0]/gleichungssystem[i]
    res = gleichungssystem[i]*multiplier[0] - gleichungssystem[0]
    gleichungssystem[i] = res

print(gleichungssystem)