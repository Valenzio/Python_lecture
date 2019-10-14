
#Aufgabe 1 (Vergleichsoperator ==)
"""1. Leeren Sie Ihren Variable explorer, indem Sie auf das Radiergummi Zeichen 
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

#Loesung
print(r>s)

#Aufgabe 3 (Zeilenumbruch im Editor)
"""Es kommt in Python vor das man eine Lange Zeile Code schreiben muss. Um die 
Uebersicht zu behalten kann man einen Zeilenumbruch einfuegen. Hier einige 
Beispiele wie ein Zeilenumbruch in Python funktioniert.
Natuerlich muss man beide (bzw. mehrere) Zeilen gleichzeitig ausfuehren"""
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

#Aufgabe 4 (If Else Abfrage)
"""Fuehren Sie folgende Zeilen Code aus, aber nicht wie bisher, Zeile fuer 
Zeile, sondern alle Zeilen auf einmal.  
Dies kommt daher, das sobald das Schluessel Wort 'if' eingeben wird, wartet
python auf eine Eingabe in dem Einzug unter dem 'if'.
Deshalb muessen Zeilen in Python die einen Einzug haben, IMMER 
zusammen/gleichzeitig ausgefuehrt werden."""
x = 5
if x>10:
    print("x ist groesser")#diese Zeile wird nur ausgefuehrt wenn x>10 ist
    
print("Ende") # diese Zeile wird immer ausgefuert

#Aufgabe 5 (= vs ==)
x= 10
y = 10

if x==y:
    print("x und y sind gleich")
    
if x!=y:
    print("x und y sind nicht gleich")
    
#Aufgabe 6
"""Bauen Sie die If-Abfrage, wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""
#Loesung
x=5
if x<10:
    print("kleiner")
print("ende")

#Aufgabe 7
"""Bauen Sie die If-Abfrage, wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""
#Loesung
x=10
if x<10:
    print("kleiner")
if x>10:
    print("groesser")
print("ende")

#Aufgabe 8
"""Fuehren Sie folgende Zeilen Code auf einmal aus. Veraendern Sie den Wert x,
so dass die Ausgabe "Weniger als 1" in der Konsole angezeigt wird."""
#Loesung
x=-1
if x<1:
    print("Weniger als Eins")
    if x>0:
        print("Mehr als 0")
print("Alles fertig")

#Aufgabe 9
"""Bauen Sie die If-Abfrage, wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""
#Loesung
x=50
if x>1:
    print("Mehr als Eins")
    if x<100:
        print("Weniger als 100")
print("Alles fertig")

#Aufgabe 10 (Einfache If Else Abfrage)
"""Fuehren Sie folgende Zeilen Code auf einmal aus. Veraendern Sie den Wert x,
so dass die Ausgabe "kleiner gleich" in der Konsole angezeigt wird."""
#Loesung
x=19
if x>20:
    print("groesser")
else:
    print("kleiner gleich")
print("Alles fertig")

#Aufgabe 11
"""Bauen Sie die If Else-Abfrage, wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""
#Loesung
x=50
y=20
if x>20:
    print("Groesser")
    if y>20:
        print("GrossGross")
    else:
        print("GrossKlein")
else:
    print("Kleiner")
print("ende")
    
#Aufgabe 12 (Einfache If-Elif-Else Abfrage)
"""Fuehren Sie folgende Zeilen Code auf einmal aus. Fuegen Sie dem Code eine 
elif Abfrage ein, so dass die Ausgabe "groesser als 5" in der Konsole 
angezeigt wird."""
#Loesung
x=7
if x>20:
    print("groesser als 20")
elif x>10:
    print("groesser als 10")
elif x>5:
    print("groesser als 5")
else: 
    print("kleiner gleich 20")
    
print("Alles fertig")

#Aufgabe 13
"""Bauen Sie die If-Elif-Else-Abfrage, wie sie im Flussdiagramm auf der Folie 
abgebildet ist"""
#Loesung
x=50
if x<40:
    print("L")
elif x<100:
    print("XL")
else: 
    print("XXL")
    
print("Alles fertig")


#Aufgabe 14 (Aufgabe 1.2 aus der VBA Aufgabensammlung 3.7)
"""Aufgabe: Erstellen Sie eine VBA-Prozedur, in der bestimmt werden soll, ob 
sich der Wert für x in einem Bereich von [a, b], mit a<b befindet. Für die 
Eingabe aller Variablen soll jeweils die input-Funktion verwendet werden, die 
fuer die 2 Variablen a und b gegeben ist. 
Die Variablen sollen vom Typ float sein. Es soll geprüft werden, ob die 
eingegebenen Bereichsgrenzen gültig sind (a>b)! Der Wert von x soll erst dann 
eingeben werden, wenn ein gültiger Bereich vorliegt."""

a= float(input("Geben Sie eine Zahl fuer a ein\n"))
b= float(input("Geben Sie eine Zahl fuer b ein\n"))

#Aufgabe 14.1 (Aufgabe 1.2A aus der VBA Aufgabensammlung 3.7)
"""Der Wert soll innerhalb des Bereichs ]a, b[ liegen. """
#Aufgabe 14.2 (Aufgabe 1.2B aus der VBA Aufgabensammlung 3.7)
"""Der Wert von x soll außerhalb des Bereichs [a, b] liegen."""
#Aufgabe 14.3 (Aufgabe 1.2C aus der VBA Aufgabensammlung 3.7)
"""Der Wert von x soll größer als 0 sein und innerhalb des Bereichs [a, b] 
liegen."""
#Aufgabe 14.4 (Aufgabe 1.2D aus der VBA Aufgabensammlung 3.7)
"""Der Wert von x soll innerhalb des Bereichs [a, b] oder [-b, -a] liegen. 
Option: An Stelle der Bereichsprüfung soll für a der kleinere der beiden 
eingegebenen Werte verwendet werden."""