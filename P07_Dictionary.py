# Aufgabe 0: List vs tuple
"""Gegeben ist eine Liste mit dem Name "list1" und ein Tuple mit dem Namen
 "tup1". Ersetzen Sie den zweiten Namen in der Liste und im Tupel mit dem
 Namen "Stefan"

"""
list1=["Andi","Michi","Anna"]
tup1=("Andi","Michi","Anna")

# Aufgabe 0.1: Verschachtelte listen
"""
Gegeben ist eine Verschachtelte Liste "list_nest". Speichern sie das erste 
Element aus dem zweiten Elemtn der Liste "list_nest" in eine neue Variable ab
"""
list_nest=["Andi", [1,2,3], "Anna"]


# Aufgabe 1: Erstellen eines Dictionaries
""" 
Erstellen sie ein Dictionary mit dem Namen "noten", das die Noten von 3 
Studenten abspeichert. Die Namen der Studenten sind hierbei die "keys" und die 
Noten sind die "values". Folgende Notenverteilung ist gegeben: 
    Andi:1, Michi:3, Anna:2 """

# Aufgabe 2: Abrufen der Values in einem Dictionary mit einem Key
""" 
Benutzen Sie das erstellte Dictionary aus Aufgabe 1. Legen Sie nun die Note vom 
Studenten "Michi" in eine seperate Variable mit dem Namen "note_michi"
"""

#Aufgabe 3:
""" 
Erstellen sie ein Dictionary das die Notensammlung von 3 Studenten abspeichert. 
Die Namen der Studenten sind hierbei die "keys" und die Noten-Liste sind die
 "values". Folgende Notenverteilung ist gegeben: 
     Andi:[1,1,2], Michi:[3,2,1], Anna:[2,2] """

#Aufgabe 4: 
""" 
Benutzen Sie das erstellte Dictionary aus Aufgabe 3. Legen Sie nun die zweite 
Note vom Studenten "Michi" in eine seperate Variable mit dem Namen "note_michi". 
Bonus Aufgabe: Speichern Sie die Durchschnittsnote von dem Studenten Michi in 
der variable durchschnitt_michi ab. Benutzen Sie evtl google um die Loesung zu 
finden. Tipp Durchschnitt heist im englischen mean oder average
"""

#Aufgabe 5: 
""" 
Benutzen Sie das erstellte Dictionary aus Aufgabe 1 und fuegen Sie einen neuen 
Studenten hinzu. Der neue Student hat den Namen "Stefan" und die Note 2
"""

#Aufgabe 6: 
""" 
Benutzen Sie das erstellte Dictionary aus Aufgabe 1 und entfernen Sie den 
Studenten mit dem Namen Andi aus dem Dictionary
"""

#Aufgabe 7: Vereinen von Dictionaries
""" Erweitern sie das Dictionary "dict_1" mit dem Inhalt von "dict_2". 
Tipp: Googlen Sie das Problem (z.b.: python append dictionary)
"""
dict_1={"Tino":2, "Andreas":3, "Christian":1}
dict_2={"Maria":1, "Julia":4, "Kathrin":1}


#Aufgabe 8: Verschachteln von Dictionaries
""" Man kann als value ein beliebiegen Datentyp nehmen. Das heisst man koennte 
ein Dictionary verwenden fuer einen value Wert. Aendern sie die untenstehende 
Zeile so, dass das Dictonary "dict_nest" bei dem key "dict_1" den value von dem 
Dictionary dict_1 hat.
"""
dict_1={"Tino":2, "Andreas":3, "Christian":1}
dict_nest={"dict_1":"bitte hier dict_1 einfuegen"}

#Aufgabe 8.1:
""" Verwenden Sie das Dictionary "dict_nest" aus Aufgabe 8. Legen Sie nun den 
value vom Studenten "Andreas" in eine seperate Variable mit dem Namen 
"note_andreas"
"""

#Aufgabe 9: Dictionary mit for-Schleife
""" Verwenden sie das dictionary "noten" aus Aufgabe 1, erstellen Sie ein for-Schleife die jede Note ausdruckt. Hier ist ein Beispiel wie man nur die Namen ausdruckt
""" 
for ii in noten:
    print(ii)
    
    
#Aufgabe 10:
""" Erweitern Sie die for-Schleife von Aufgabe 8 in dem der Name und die Note zusammen in einer Zeile ausgedruckt wird. Z.B. Andi 1. Denken Sie daran wie man strings vereint (Achten Sie darauf das die Noten keine Strings sind)
Bonus: Trennen Sie Name und Note mit einem Doppelpunkt
"""

#Aufgabe 11: Ausgabe von Keys und Values in einer Liste
""" Verwenden sie das dictionary "noten" aus Aufgabe 1, und erstellen Sie zwei Listen eine Liste die nur die Namen der Studenten enthaelt und eine die nur die Noten entaehlt. Wie sie die 2 neuen Listen benennen ist Ihnen ueberlassen
""" 

