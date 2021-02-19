import numpy as np

def getData():
    return "1,10;2,9.4;3,9;4,8.4"#input("Punkte angeben mit format: zahl.dezimal,zahl.dezimal;...")

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
multiplier = gleichungssystem[0]/gleichungssystem[1]
res = gleichungssystem[1]*multiplier[0] -gleichungssystem[0]
print(multiplier)
print(res)
gleichungssystem[1] = res
print(gleichungssystem)