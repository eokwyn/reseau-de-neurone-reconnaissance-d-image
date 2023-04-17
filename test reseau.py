def accuracy (y_t,y_pred):
    valide=0
    for k in range (len(y_t)):
        if y_pred[k]==y_t[k]:
            valide+=1
    return valide/len(y_t)

def test (X_t,y_t,parametres):
    y_pred=predict(X_t,parametres)#prediction des resultats sur donnees test
    accu=accuracy(y_t.flatten(),y_pred.flatten())#check des predictions / resultat vrai
    return accu,y_pred