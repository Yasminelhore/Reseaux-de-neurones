import math
import numpy as np
import matplotlib.pyplot as plt
import sklearn.neural_network as nrl_net 


# les vecteurs d'entrées
X = np.array([])
X = np.append(X,[(0,0)])
X = np.append(X,[(0,1)])
X = np.append(X,[(1,0)])
X = np.append(X,[(1,1)])
X = np.reshape(X,(4,2))
# les sorties d'entrées
D = np.array([])
D = np.append(D,[(0,0,0,1)])
D = np.append(D,[(0,1,1,1)])
D = np.append(D,[(0,1,1,0)])
D = np.reshape(D,(3,4))

while (1):
    print("---------------------------------FONCTION LOGIQUE A APPRENDRE par la perception multicouche--------------------------------")
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
    cl = nrl_net.MLPClassifier(activation='relu',max_iter=1000)
    cl.fit(X,D[fl-1])

    E = cl.loss_curve_  
    plt.plot(E)
    plt.ylabel("Erreur Quadratique moyenne")
    plt.xlabel("nombre d iterations")
    plt.title("La courbe EQM en fonction du NI")
    plt.show()
    print("---------------------------------LE TEST--------------------------------")
    while (1):
        tmp = np.zeros(2)
        tmp[0] = int(input("entrer le x1 : ")) 
        tmp[1] = int(input("entrer le x2 : "))
        v_test = cl.predict(tmp.reshape(1,-1))
        #X[2].reshape(1,-1)
        if tmp[0] != 0 and tmp[0]  != 1 or tmp[1] != 0 and tmp[1] != 1: 
            print("---------------------------------ERROR : REPETER LE TEST--------------------------------")
        else :
            print("Le resultat est : ====>",v_test)
            o_n = input("tester la fonction o/n :")
            if o_n == "o":
                print("---------------------------------LE TEST--------------------------------")
                continue
            elif o_n == "n":
                break
            else :
                break
            continue   
print("---------------------------------MERCI, au revoir--------------------------------")

