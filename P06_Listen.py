# Aufgabe 1 (Erstellen einer Liste)
""" Aehnlich wie bei strings koennen wir Listen erstellen, bloss anstatt 
Buchstaben/Zeichen koennen wir in die Liste verschiedene Elemente abspeichern, 
diese Elemente koennen beliebige Datentypen sein.
Erstellen sie eine Liste mit dem Namen "friends" die 3 strings enthaelt. 
Die drei strings sind Namen: Andi, Michi, Anna
Hier ist ein Beispiel wie man eine Liste erstellt mit  3 Zahlen"""
num_list= [1,2,3]
#Loesung
friends = ["Andi", "Michi", "Anna"]

#Aufgabe 2 (Ausgabe von Listen)
""" Erstellen sie eine Liste mit dem Namen "friends" die 3 strings enthaelt. 
Die drei strings sind Namen: Andi, Michi, Anna
Benutzten sie die print() Funktion um den kompletten Inhalt der Liste an zu 
zeigen"""
#Loesung
friends = ["Andi", "Michi", "Anna"]
print(friends)

#Aufgabe 3 (Ausgabe von einzelnen Listen-Elementen)
"""Erstellen sie eine Liste mit dem Namen "friends" die 3 strings enthaelt. 
Die drei strings sind Namen: Andi, Michi, Anna. 
Erstellen sie nun eine neue Variable: name_1. Weisen Sie dieser Variable das 
zweite Element aus der Liste "friends" zu. 
Hier ist ein Beispiel, wo das erste Element zu einer Variablen zugewiesen wird 
"""
num_list=[1,2,3]
num_1=num_list[0]
print(num_1)
#Loesung
friends = ["Andi", "Michi", "Anna"]
name_1 = friends[1]


#Aufgabe 4 (List-Slicing)
""" Verwenden sie die Liste "friends" aus Aufgabe 1, erstellen Sie eine Neue 
Liste "friends_reduced" die nur die ersten 2 Namen von der "friends" Liste 
enthaelt. Achten Sie darauf das sie die neue Liste nur in Abhaengikeit von der 
alten Liste erstellen. Tip benutzen Sie das gleiche verfahren, so wie wir es 
bei den strings gelernt haben, unten ist ein Beispiel abgebildet.
Bonus fuer die Pros: Die Liste "friends_reduced" hat den ersten und letzten 
Namen aus der Liste "friends""""
sen="Hello World"
sen_reduced=sen[0:3]
print(sen_reduced)
#Loesung
friends = ["Andi", "Michi", "Anna"]
friends_reduced = friends[0:2]
#alternativ
friends_reduced = friends[:2]

#Aufgabe 5 (List manipulation)
""" Verwenden sie die liste "friends" aus Aufgabe 1. 
Aendern Sie nun den 2ten Namen in der Liste zu "Stefan, ohne dabei die
komplette Liste neu zu definieren"""
friends=["Andi", "Michi", "Anna"]
#Loesung
friends[1] = "Stefan"


#Aufgabe 6 (Laenge von Listen
"""Gegeben sind die zwei Listen "friends_m" und "friends_f". Lassen Sie sich 
die Laenge von beiden Listen mit print ausgeben. Verwenden sie die len() 
Funktion"""
friends_m= ["Andi", "Michi", "Tom"]
friends_f= ["Anna", "Julia"]
#Loesung
print("Laenge der ersten Liste: " + str(len(friends_m)))
print("Laenge der zweiten Liste: " + str(len(friends_f)))


#Aufgabe 7 (Vereinen von Listen)
""" Verwenden Sie die beiden Listen aus Aufgabe 6, und vereinen Sie die beiden 
Listen zur einer Liste, mit dem Namen "all_friends". Hier ist ein Beispiel wie 
man 2 strings zusammen fuerht:
Bonus fuer die Pros: Fuegen Sie die 2te Liste nach dem 2ten Namen aus der 
ersten Liste ein."""
str_1="Hello "
str_2="World"
all_str=str_1 + str_2
print(all_str)
#Loesung
all_friends = friends_m + friends_f

#Aufgabe 7.1:
"""Gegeben ist eine while-Schleife die Eingaben vom User einliest bis er den 
String "fertig" eingibt. Ihre Aufgabe ist nun jede dieser Eingaben in eine 
Liste zu Speichern. Die Eingabe "fertig" wird nicht in die Liste geschrieben.
Zur Hilfe steht der folgende Code der angepasst werden kann
"""
#Loesung
list_input=[] #erstellt eine leere Liste die befuellt wird
while True:
    zeile= input("Neue Eingabe:\n")
    if zeile == "fertig":
        break
    list_input.append(zeile)
    print("Ihre Eingabe:"+zeile)
print("Skript ist beendet")


#Aufgabe 8 (Lists mit for-Schleife)
""" Verwenden Sie die liste "friends" aus Aufgabe 1, erstellen Sie eine 
for-Schleife die jeden Namen in der Konsole anzeigt. Hier ist ein Beispiel""" 
num_list=[1,"a",3]
for ii in num_list:
    print(ii)
    
#Loesung
friends = ["Andi", "Michi", "Anna"]
for ii in friends:
    print(ii)
   
    
#Aufgabe 9 (List summation)
"""Erstellen Sie eine Liste mit ganzen Zahlen, die von 0 bis 999 geht.
Tip: range, Aufgabe 7.1, for-Schleife
Bonus fuer die Pros: Loesen Sie die Aufgabe ohne eine Schleife zu verwenden"""    
ganze_zahlen=[]
for ii in range(1000):
    ganze_zahlen.append(ii)
 
#Aufgabe 10 
""" Erstellen Sie eine Funktion mit dem Namen sum_even, die "n" als input 
parameter hat. Die Funktion gibt die Summe zurueck von den geraden Zahlen 
zwischen 0 bis n. Wenn die Funktion steht, verwenden sie n=1000 und lassen Sie
sich das Ergebniss ausgeben mit print().
Bonus fuer die Pros: Loesen Sie die Aufgabe, ohne eine Schleife zu verwenden"""   
#Loesung
def sum_even(n):
    sum=0
    for ii in range(0,n+1,2):
        sum = sum + ii
    return(sum)
summe = sum_even(10)

#Aufgabe 11 (Elementwise addition)
""" Gegeben sind die zwei listen "list1" und "list2". Addieren Sie die beiden 
Listen Elementweise, so dass das erste Element aus der ersten Liste mit dem 
ersten Element der zweiten Liste addiert wird, das zweite Element aus der 
ersten Liste mit dem zweiten Element der zweiten Liste, usw.
Bonus fuer die Pros: Loesen Sie die Aufgabe ohne eine Schleife zu verwenden""" 
list1=[1,2,3]
list2=[3,4,5]
#Loesung
list_summe=[]
for ii in range(len(list1)):
    list_summe.append(list1[ii] + list2[ii])


#Aufgabe 12 (Elemente in einer Liste finden)
"""Gegeben ist die Liste mit dem Namen "list_find". Ueberpruefen Sie ob die 
Liste den String "ab" beinhaltet. 
Bonus fuer die Pros: Suchen Sie die Liste "list_con" (Aufgabe 13) durch, ob der
Wert 8 vorkommt. Falls ja lassen Sie sich ein True ausgeben, falls nicht dann
ein False
"""
list_find=["a","c", 1,3,4,"ab","abc"]
#Loesung
"ab" in list_find


#Aufgabe 13 (Verschachtelte Listen)
"""Gegeben ist die Liste mit dem Namen "list_con". Greifen Sie auf das
Listenelement mit dem Wert 8 zu und speichern Sie sich dieses in einer 
neuen Variable mit dem namen "element" ab. Unten ist ein Beispiel abgebildet, 
wie man den Wert 8 aus einer einfachen Liste abruft und den Wert einer anderen
Variablen zuweisst. 
Bonus fuer die Pros: Suchen Sie nach dem Element in der Liste, mit dem Wert 8.
Lassen Sie sich die Position dieses Wert ausgeben.
"""
#Dies ist nur ein Beispiel
list_bsp=[1,2,3,4,5,6,7,8]
element=list_bsp[7]
print(element)

list_con=[1,2,3,[4,5,6,[7,8]],9]
#Loesung
wert = list_con[3][3][1]

#Aufgabe 14 (Aufgabe 1.5A-C aus der VBA Aufgabensammlung 3.7)
"""Erstellen Sie einen Code der Ihnen die vorgegebenen Ergebnisse erzeugt. 
Sehen Sie die Vorlage in Excel als Textausgabe in der Konsole, trennen Sie jede
Zelle mit einem Leerzeichen von einander. Behandeln Sie leere Excel-Zellen als
Leerzeichen. Unten sehen Sie die Python-Loesung fuer das 
"Einfuehrende Beispiel"
"""
count=0
liste=[6,2,7,3,4]
for ii in range(6): 
    text = " "
    if ii==1: #erste Zeile
        for kk in liste:
            text = text + str(kk) + " "
    elif ii>1:
        text = liste[ii-2]

    print(text)
