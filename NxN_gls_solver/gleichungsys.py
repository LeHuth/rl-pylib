import numpy as np

def getData():
    return "-1.49,1.98;-0.48,-1.49;0.98,0.66;2.73,0.19"#input("Punkte angeben mit format: zahl.dezimal,zahl.dezimal;...")

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

def gaussMethod(gls, exponent):
    #rework as such: http://elsenaju.info/Rechner/Gleichungssystem-NxN.html
    for meta in range(1,exponent+1): #1,2,3
        for i in range(meta,exponent+1):
            multiplier = gls[meta-1]/gls[i]
            res = gls[i]*multiplier[meta-1] - gls[meta-1]
            gls[i] = res
    #clean up gls
    for j in range(exponent):  
        for i in range(j+1,exponent+1):
            gls[i][j] = 0

    return gls
def newGaussMethod(gls, exponent):
    for i in range(0,exponent+1):
        gls[i]= gls[i]/gls[i][i]
        if(i < exponent):
            for j in range(i+1,exponent+1):
                gls[j]= gls[j] - gls[i]*gls[j][i]
    #return gls

def jordanMethod(gls, exponent):
    for shift in range(0,exponent):
        for i in range(0,exponent-shift):
            gls [i] = gls[i]-(gls[i+shift+1]*gls[i][i+1+shift])

data = getData()  
points = splitDataIntoPoints(data)
gleichungssystem = createGleichungssystem(points)
print(gleichungssystem)
newGaussMethod(gleichungssystem, 3)

print(gleichungssystem)
jordanMethod(gleichungssystem, 3)
print("--------------------------")
print(gleichungssystem)