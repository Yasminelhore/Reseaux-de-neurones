import math
import numpy as np
import matplotlib.pyplot as plt


def function_y(w,x,b):
    sum = 0
    for i in range(x.size):
        sum=sum+x[i]*w[i]
    y = sum+b
    if y >= 0 : return 1
    else : return 0    



def W_Hroff(x,d,w,b,y):
    for i in range(y.size):
        y[i]=function_y(x[i],w,b)
        for j in range(w.size):
            w[j]=w[j]+0.7*(d[i]-y[i])*x[i][j]    
        b=b+0.7*(d[i]-y[i])
    return y,w,b        

def Err_Quadratique(y,d):
    E = 0
    for i in range(d.size):
        E =E+((d[i]-y[i])**2)
    E = (1/2)*E    
    return E

def test(x1,x2,x,y):
    for i in range(y.size):
        if x[i][0] == x1 and x[i][1] == x2 :
            return y[i] 
    return -1    



X = np.array([])
X = np.append(X,[(0,0)])
X = np.append(X,[(0,1)])
X = np.append(X,[(1,0)])
X = np.append(X,[(1,1)])
X = np.reshape(X,(4,2))

D = np.array([])
D = np.append(D,[(0,0,0,1)])
D = np.append(D,[(0,1,1,1)])
D = np.append(D,[(0,1,1,0)])
D = np.reshape(D,(3,4))

W = np.zeros(2)
Y = np.zeros(4)
b = 0

while (1):
    print("---------------------------------FONCTION LOGIQUE A APPRENDRE par la perception monocouche--------------------------------")
    print("ET \t \t 1")
    print("OU \t \t 2")
    print("XOR \t \t 3")
    print("sortir \t \t 0")
    print("-----------------------------------------------------------------")
    fl = int(input("choisir la fonction logique : "))
    if fl == 1 : fl_word = "ET"
    elif fl == 2 : fl_word = "OU"
    elif fl == 3 : fl_word = "XOR"
    elif fl == 0 : break
    else : 
        print("ERROR")
        break
    print("Apprentissage de la fonction logique ** ",fl_word," **")
    print("Entrainement termine")
    E = np.zeros(20)
    for i in range(20):
        Y,W,b = W_Hroff(X,D[fl-1],W,b,Y)
        E[i] = Err_Quadratique(Y,D[fl-1])
    for i in range(W.size): print("** w",i+1," = ",W[i])
    print("** b = ",b)
    for i in range(1,20):
        if(E[i]==0 and E[i-1]==0): 
            a = i
            break
    print("** la fonction a appris dans la ",a," -eme iteration")
    print("E =",E)
    print("D =",D)
    print("Y =",Y)
    plt.plot(E)
    plt.ylabel("Erreur Quadratique moyenne")
    plt.xlabel("nombre d iterations")
    plt.title("La courbe EQM en fonction du NI")
    plt.show()
    print("---------------------------------LE TEST--------------------------------")
    while (1):
        t1 = int(input("entrer le x1 : ")) 
        t2 = int(input("entrer le x2 : "))
        v_test = test(t1,t2,X,Y)
        if v_test != -1 :
            print("Le resultat est : ====>",v_test)
            o_n = input("tester la fonction o/n :")
            if o_n == "o":
                print("---------------------------------LE TEST--------------------------------")
                continue
            elif o_n == "n":
                break
        else: 
            print("---------------------------------ERROR : REPETER LE TEST--------------------------------")
            continue   
print("---------------------------------MERCI, au revoir--------------------------------")           



