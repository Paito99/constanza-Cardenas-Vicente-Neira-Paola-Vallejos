#Definir Variables 
import random 
numero=random.randint(2,15);


#jugar
print("Bienvenido a Me quiere mucho, poquito o nada.");
print("introducciones:\n-En este juego debes escribir con minusculas mucho, poquito o nada");
print("¡Ahora a Jugar!")

while(numero>0):
    #mucho
    variable=input("me quiere");
    numero=(numero - 1);

    #Poquito 
    variable=input("me quiere");
    numero=(numero - 1);

    #Nada
    variable=input("me quiere");
    numero=(numero - 1);

#Decir cuanto quieren al usuario
if (variable=="mucho"): 
    print("TE QUIEREN MUCHO!!");
elif (variable=="poquito"):
    print("Te QUIEREN POQUITO :((");
elif (variable=="nada"):
    print("NO TE QUIEREN NADITA.");
else:
    print("En las instrucciones dice minusculas, vuelve a intentarlo. ");