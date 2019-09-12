# Aufgabe 1 (for - Schleife durch eine Liste)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Beobachten Sie die 
Ausgabe in der Konsole. Welche Zahlen werden ausgegeben."""
for i in [1,2,3,4,5]:
    print (i)
print("alles fertig")


# Aufgabe 2 (for - Scheife durch einen String)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Beobachten Sie die 
Ausgabe in der Konsole. Welche Ausgabe sehen Sie?"""
for i in "hello World":
    print (i)
print ("alles fertig")


# Aufgabe 3 (for - Schleife mit der range Funktion)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Beobachten Sie die 
Ausgabe in der Konsole. Welche Ausgabe sehen Sie?"""
for i in range(5):
    print (i)    
print ("alles fertig")


# Aufgabe 4 (Schleife mit if-Abfrage)
"""Erstellen Sie eine for-Schleife, die Zahlen von 0 bis 5 ausgibt. Bei der 
Zahl 3 wird folgender Text ausgegeben: "Alle guten Dinge sind drei"
Verwenden Sie eine if-Abfrage und die range Funktion, um die Aufgabe
umzusetzten. """


# Aufgabe 5 (Schleife die aufsummiert)
"""Erstellen Sie eine for-Schleife, die Zahlen von 0 bis 10 aufsummiert. """


# Aufgabe 6 (Modifikation der range-Funktion)
"""Erstellen Sie eine for-Schleife, die Zahlen von 5 bis 10 ausgibt. Verwenden 
Sie die range Funktion, aehnlich wie in Aufgabe 3.
Suchen Sie im Internet wie man die range-Funktion so aendert das die 
gewuenschten Zahlen ausgegeben werden. """


# Aufgabe 7
"""Erstellen Sie eine for-Schleife, die Zahlen von 5 bis 20 ausgibt, aber nur 
ungerade Zahlen. 
Verwenden Sie die range Funktion, aehnlich wie in Aufgabe 3.
Suchen Sie im Internet wie man die range-Funktion so aendert das die 
gewuenschten Zahlen ausgegeben werden. 
Bonus Aufgabe fuer die Pros: Verwenden Sie range(20) fuer die Definition der
Schleife und loesen Sie trotzdem die Aufgabe."""


# Aufgabe 8
"""Erstellen Sie eine for-Schleife, die Zahlen von 10 bis 0 (10, 9, 8, 7, 6...) 
ausgibt. Also im vergleich zu Aufgabe 3, rueckwaerts. Verwenden Sie die range 
Funktion. Suchen Sie im Internet wie man die range-Funktion so aendert das die 
Zahlen in umgekehrter Reihenfolge ausgegeben werden.
Bonus Aufgabe fuer die Pros: Verwenden Sie range(11) fuer die Definition der
Schleife und loesen Sie trotzdem die Aufgabe.
"""

# Aufgabe 9 (While-Schleife Einfuehrung)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Es handelt sich hierbei 
um eine einfache while-Schleife. Vergleichen Sie die while-Schleife mit der 
for-Schleife. Welche Unterschiede erkennen Sie?"""
x=4

while x<10:
    x= x+1  
    print(x)
print("Jetzt ist x nicht mehr kleiner als 10")


# Aufgabe 10 (Endlos Schleife)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Es handelt sich hierbei 
um eine einfache endlos while-Schleife.
Verwenden Sie Strg+c um die endlos Schleife abzubrechen. Aendern Sie den code 
so um, dass die while-Schleife keine endlos Schleife mehr ist. Tipp: Es gibt 
mehrere Moeglichkeiten dies zu tun."""
x=11
while x>10:
    print("Help!!")
    
print("we will never finish")


# Aufgabe 11 (Inkrementieren in einer while-Schleife)
"""Ergaenzen Sie folgenden Code so, dass der Variablen x immer 1 hinzugefuegt 
wird, bis x groesser als 50 ist. Lassen Sie nach jeder Addition das Ergebniss 
mit einer print-Funktion ausgeben.
Gegeben ist ein Beispiel wie man x von 0 auf 1 erhoeht. Sie muessen nun dieses
Beispiel in eine Schleife einfuegen."""
x=0
increment = 1
x=x+increment
print(x)


# Aufgabe 12 
"""Ergaenzen Sie folgenden Code aus Aufgabe 12 so, dass die Variable x immer 
ein beliebiger Wert hinzugefuegt wird, bis x groesser als 50 ist. Der beliebige
Wert wird jedesmal per input-Funktion abgefragt.
Lassen Sie nach jeder Addition das Ergebniss mit einer
print-Funktion ausgeben. Verwenden Sie eine while-Schleife.
Bonus Aufgabe fuer die Pros: Verwenden Sie eine for-Schleife"""
x=0
increment = int(input("Geben Sie eine ganze Zahl zwischen 1 und 10 ein:"))
x=x+increment
print(x)


#Aufgabe 13 (Break-Statement)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Es handelt sich hierbei 
um eine einfache endlos while-Schleife mit eienm break statement. Machen Sie 
mehrere Eingaben. Welche Eingabe muessen Sie taetigen um die endlos 
Schleife zu beenden."""
x=4
while x>3:
    zeile= input("Neue Eingabe:\n")
    if zeile == "fertig":
        break
    print("Ihre Eingabe:"+zeile)
print("Skript ist beendet")


#Aufgabe 14 (continue-Statement)
"""Fuehren Sie den unten stehenden Code auf einmal aus. Es handelt sich hierbei 
um eine einfache endlos while-Schleife mit eienm continue und break statement. 
Machen Sie mehrere Eingaben in der Konsole.
Welche Eingabe muessen Sie taetigen damit Ihre Eingabe nicht in der Konsole
ausgegeben wird, Sie aber trotzdem in der while- Schleife bleiben.
"""
x=4
while x>3:
    zeile= input("Neue Eingabe:\n")
    if zeile == "keine ausgabe": # if you type this than there won't be a print out
        continue
    if zeile == "fertig":
        break
    print("Ihre Eingabe:"+zeile)
print("Skript ist beendet")

   

#Aufgabe 15
""" Gegeben ist eine Ansammlung von Zahlen(Liste):[3, 43,58, 84,30,-2]. 
Ergaenzen Sie den Code so, das die groesste Zahl am Ende ausgegeben wird. Gehen 
Sie davon aus, das Sie keine Einsicht in die Ansammlung von Zahlen haben. Ihr 
Code muss selbstaendig die groesste Zahl finden. (Sie koennen davon ausgehen 
das die kleinste Zahl -10000 ist.)
Bonus Aufgabe fuer die Pros: Loesen Sie die Aufgabe mit einer while-Schleife
"""
for i in [3, 43,58, 84,30,-2]:
    
        
#Aufgabe 16
""" Gegeben ist eine Ansammlung von Zahlen :[3, 43,3,58, 84,3,30,-2,3]. Wie oft
kommt die Zahl 3 in dieser Ansammlung vor?. Ergaenzen Sie den Code so, dass das 
verlangte Ergebnis am Ende in der Konsole ausgegeben wird. Gehen Sie davon aus, 
das Sie keine Einsicht in die Ansammlung von Zahlen haben. Ihr Code muss selbst-
aendig die groesste Zahl finden. 
Bonus Aufgabe fuer die Pros: Loesen Sie die Aufgabe mit einer while-Schleife
"""
lookout=3 # look out for that number in the list
count=0 # set a counter to 0
for i in [3, 43,3,58, 84,3,30,-2,3]:

        
print("Number of times, 3 appeared:" + str(count))


#Aufgabe 17
""" Ergaenzen Sie den Code so, dass jeder Buchstabe einzeln in der Konsole 
ausgegeben wird, aehnlich wie in Aufgabe 2. Ersetzten Sie dabei den Buchstaben 
'l' durch ein 'r'.
Bonus Aufgabe fuer die Pros: Geben Sie am Ende den kompletten Satz in der 
Konsole wieder, mit den geaenderten Buchstaben."""
x=input("Geben Sie einen Satz ein:\n")




