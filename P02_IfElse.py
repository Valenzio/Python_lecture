
#Aufgabe 1
"""
1. Leeren Sie Ihren Variable explorer, indem Sie auf das Radiergummi Zeichen 
Klicken
2. Fuehren Sie folgende Zeilen Code nacheinander aus, indem Sie die jeweilige 
Zeile kopieren und F9 druecken (Alternativ: Zeile markieren, rechte Maustaste, 
run selection of current line)"""

s= 20
r= 10
p= 10

s==r #was wird in der Konsole ausgegeben?
r==p #was wird in der Konsole ausgegeben?

print(s==r)
print(True)


#Aufgabe 2
"""Ueberpruefen Sie ob r groesser ist als s. Verwenden Sie die print Funktion 
um das Ergebniss in der Konsole anzuzeigen"""

s= 20
r= 10


#Aufgabe 3
"""Es kommt in Python vor das man eine Lange Zeile Code schreiben muss. Um die 
Uebersicht zu behalten kann einen Zeilenumbruch einfuegen. Hier einige 
Beispiele wie ein Zeilenumbruch in Python funktioniert"""
## Indentation (Einzug) Zeilen sprung in Python editor

# geht nicht
a = 10 + 
15 

#Trennung mit Backslash funktioniert
a = 10 +\
    15
    
#So funktioniert ist auch, ist aber nicht so schoen
a = 10 +\
15

# Trennung mit Klammern funktioniert
b= 1 + 2 +(  
   3+4)


#Aufgabe 5
"""Fuehren Sie folgende Zeilen Code aus, aber nicht wie bisher Zeile fuer Zeile
sondern alle Zeilen auf einmal.  
Dies kommt daher, das sobald das Schluessel Wort 'if' eingeben wird, wartet
python auf eine Eingabe in dem Einzug unter dem 'if'.
Deshalb muessen Zeilen in Python die einen Einzug haben, IMMER 
zusammen/gleichzeitig ausgefuehrt werden."""

x = 20
if x>10:
    print("x ist groesser")#diese Zeile wird nur ausgefuehrt wenn x>10 ist
    
print("Ende") # diese Zeile wird immer ausgefuert


#Aufgabe 6
## = vs ==

x= 10
y = 10

if x==y:
    print("x und y sind gleich")
    
if x!=y:
    print("x und y sind nicht gleich")
    

#Aufgabe 7
"""Bauen Sie die If-Abfrage, wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""


#Aufgabe 8
"""Fuehren Sie folgende Zeilen Code auf einmal aus. Veraendern Sie den Wert x,
so dass die Ausgabe "Weniger als 100" in der Konsole angezeigt wird.
"""
x=50
if x>1:
    print("Mehr als Eins")
    if x<100:
        print("Weniger als 100")
print("Alles fertig")


