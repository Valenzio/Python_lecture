
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
"""Fuehren Sie folgende Zeilen Code, nicht wie bisher Zeile fuer Zeile aus. 
Sobald Sie das Schluessel Wort 'if' eingeben, erwartet python eine Eingabe in
dem Einzug unter dem 'if'.
Deshalb muessen Zeilen in Python die einen Einzug haben, IMMER 
zusammen/gleichzeitig ausgefuehrt werden."""

x = 20
if x>10:
    print("x ist groesser")#diese Zeile wird nur ausgefuehrt wenn x>10 ist
    
print("Ende") # diese Zeile wird immer ausgefuert


#
## Indentation (Einzug) Zeilen sprung in Python editor

# geht nicht
a = 10 + 
    15 

#Trennung mit Backslash funktioniert
a = 10 +\
    15

# Trennung mit Klammern funktioniert
b= 1 + 2 +(  
    3+4)
    
## = vs ==

x= 10
y = 10

if x==y:
    print("x und y sind gleich")
    
if x!=y:
    print("x und y sind nicht gleich")

    
#Aufgabe 4
"""Bauen Sie die If-Abfrage wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""


#If Verschachtelungen
"""Spielen Sie mit der Variablen x, indem Sie sie veraendern und dann die 
IF-Schleife durchlaufen
"""
x=50
if x>1:
    print("Mehr als Eins")
    if x<100:
        print("Weniger als 100")
print("Alles fertig")


#Aufgabe 5
"""Bauen Sie die If-Abfrage wie sie im Flussdiagramm abgebildet ist"""


#IF-ELSE
x=50
if x>20:
    print("groesser")
else:
    print("kleiner")
print("Alles fertig")


#Aufgabe 6
"""Bauen Sie die If-Abfrage wie sie im Flussdiagramm abgebildet ist"""



#Aufgabe 7
"""Loesen Sie die Aufgabe"""

