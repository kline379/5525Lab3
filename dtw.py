import numpy as np

def absdiff(num1, num2):
    if num1 > num2:
        return num1-num2
    return num2-num1

def squarediff(num1, num2):
    return absdiff(num1, num2)**2

def sumdist(x1,x2,distfunc):
    s=0
    for i in np.arange(0,x1.shape[-1]):
        s=s+distfunc(x1[i],x2[i])
    return s

def dtw(X,Y, distfunc):
    D = [[0 for x in range(len(Y))] for y in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y)):
            if i == 0:
               if j ==0:
                   D[i][j]=distfunc(X[i],Y[j])
               else:
                   D[i][j]=D[i][j-1]+distfunc(X[i],Y[j])
            elif j==0:
                D[i][j]=D[i-1][j]+distfunc(X[i],Y[j])
            else:
                D[i][j]=min(D[i-1][j],D[i-1][j-1],D[i][j-1])+distfunc(X[i],Y[j])
    return (D[len(X)-1][len(Y)-1], D)

X = [1,2,4,2,3]
Y = [1,1,2,2,3]
(s, D) = dtw(X,Y, absdiff)
print s
print D


