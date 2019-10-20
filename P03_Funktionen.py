# Aufgabe 1
"""Erstellen Sie folgende Variablen in Python mit den Entsprechenden Werten
x=1
y=2
z=3"""
# Loesung
x=1
y=2
z=3

# Aufgabe 2
"""Berechnen Sie folgendes in Python
f=(x**2)+ y**3 + z**4
mit:
x=1
y=2
z=3
Ueberlegen Sie sich, was passiert wenn Sie die Funktion f immer wieder 
verwenden muessen, aber mit wechselnden Eingangsparameter x,y,z"""
#Loesung
f=(x**2)+ y**3 + z**4


# Aufgabe 3 (Definieren einer Funktion)
"""Loeschen Sie alle Variablen im Workspace.
Definieren Sie eine Funktion in Python mit dem Funktionsnamen 'func1', 
Eingangsparamter sind x, y und z
Im Funktionskörper wird folgendes berechnet
f=(x**2)+ y**3 + z**4
Ausgabewert ist f
Hier nochmal das Beispiel von der Powerpoint Folie"""
def myfunc(a,b):
    c=a+b
    return(c)
#Loesung
def func1(x,y,z):
    f=(x**2)+ y**3 + z**4
    return(f)


# Aufgabe 4 (Ausfuehren einer Funktion)
"""Nehmen Sie sich die Funktion von Aufgabe 3 zur Hilfe und Berechnen Sie f, 
wenn f folgendermassen definiert ist: f=(1**2)+ 2**3 + 3**4"""    
#Beispiel Runden
gerundete_nummer = round(10.001)
#Loesung
f = func1(1,2,3)
#alternativ
x=1
y=2
z=3
f= func1(x,y,z)
print(func1(x,y,z))

a=10
b=11
c=13

wert= func1(a,b,c)
print(wert)


# Aufgabe 5 (If-Else in einer Funktion)
"""Definieren Sie sich eine Funktion in Python mit dem Funktionsnamen func2, 
Eingangsparamter sind x, y und z. Im Funktionskörper wird folgendes berechnet:
f=x**2+ y**3 + z**4 für x>0
und
f= y**3 + z**4 für x<=0
Ausgabewert ist f. Verwenden Sie eine if-else Abfrage im Funktionskoerper"""
#Loesung
def func2(x,y,z):
    if x>0:
        f=x**2+ y**3 + z**4
    else:
        f= y**3 + z**4
    return(f)


#Aufgabe 6:
"""Nehmen Sie sich die Funktion von Aufgabe 5 zur Hilfe und Berechnen Sie  
folgenden Werte:
g1=func2(3,4,5)
g2=func2(-3,4,5)
g1 und g2 sind dabei neue Variablen, denen Sie die Funktionswerte zuweisen."""    
#Loesung
g1=func2(3,4,5)
g2=func2(-3,4,5)


#Aufgabe 7 (Funktion mit mehreren Ausgabewerten)
"""Definieren Sie eine Funktion in Python mit dem Funktionsnamen func, 
Eingangsparamter sind x, y und z. Im Funktionskörper wird folgendes berechnet:
f=(x**2)+ y**3 + z**4 
und
g= y**3 + z**4 
Ausgabewerte sind f und g"""
#Loesung
def func(x,y,z):
    f=x**2+ y**3 + z**4
    g= y**3 + z**4 
    
    return(f,g)

#Aufgabe 8 
"""Verwenden Sie die Funktion aus Aufgabe 7, mit x=1,y=2 und z=3
1. Speichern Sie sich f und g gleichzeitig in die Variablen a11 und a12 ab
2. Speichern Sie sich nur f in die Variable a2"""
#Loesung
a11,a12 = func(1,2,3)
a2=func(1,2,3)


# Aufgabe 9 (Funktionen ohne Ausgabe)
"""Definieren Sie eine Funktion in Python mit dem Funktionsnamen func, 
Eingangsparamter sind x, y und z. Im Funktionskörper wird folgendes berechnet:
f=(x**2)+ y**3 + z**4 für x>0
und
f= y**3 + z**4 für x<=0
Sie brauchen keinen Ausgabewert, aber lassen Sie das Ergebnis mit der print 
Funktion anzeigen"""
#Loesung
def func2(x,y,z):
    if x>0:
        f=x**2+ y**3 + z**4
    else:
        f= y**3 + z**4
    print(f)
    
func2(1,2,3)


# Aufgabe 10 (Funktionen mit standart (default) Eingabewerten)
"""Definieren Sie eine Funktion in Python mit dem Funktionsnamen func, 
Eingangsparamter sind x, y und z. Im Funktionskörper wird folgendes berechnet
f=(x**2)+ y**3 + z**4 
Ausgabewert ist f.
Erstellen Sie die Funktion so, dass der User nur den Parameter fuer x Angeben
kann. Zum Beispiel: func(10).
Falls dies der Fall ist nehmen die restlichen Eingangsparameter folgende 
Werte an:
y=0
z=0
Unser Beispiel func(10) wuerde folgendes Ergebniss liefern: 100 """
#Loesung
def func(x,y=0,z=0):
    f=(x**2)+ y**3 + z**4 
    return(f)

#Aufgabe 11
"""Verwenden Sie die Funktion aus Aufgabe 10, um den Funktionswert f zu
berechnen. Verwenden Sie folgende Eingangsparameter mit x=1,y=2"""
#Loesung
f = func(1,2)
print(f)

#Aufgabe 12 (global vs local Variablen)
"""Loeschen Sie alle Variablen im Workspace.
Gegeben ist die Funktion mit dem Namen "myfunc". Fuehren Sie den unten stehenden 
Code aus. Beobachten Sie welche Variablen in Ihrem Workspace angelegt werden.
Aendern Sie die Funktion "myfunc" so, dass nach dem Durchlaufen des codes, die 
Variable "c" im Workspace erscheint. """
def myfunc(a,b):
    c=a+b
    return(c) 

result=myfunc(5,10)


#Aufgabe 13
"""Loeschen Sie alle Variablen im Workspace.
Gegeben ist die Funktion mit dem Namen "myfunc2". Fuehren Sie den unten 
stehenden Code aus. Beobachten Sie welche Variablen in Ihrem Workspace angelegt 
werden. Welchen Wert haben die Variablen "a", "b" und "c" am Ende, warum?
Aendern Sie die Funktion "myfunc2" so, dass nach dem Durchlaufen des codes, die 
Variable "c" den Wert aus der Funktion hat (15). """
a=1
b=2
c=3

def myfunc2(a,b):
    c=a+b
    return(c) 

result=myfunc2(5,10)
result = c

#Aufgabe 14 (global vs local Variablen fuer Fortgeschrittene)
"""Fuehren Sie den Code der unten steht aus. """
a = 1

# Verwendet globale Variablen, da es kein lokales 'a' existiert.
def f(): 
	print ('Inside f() : ', a )

# Variable 'a' wird lokal definiert und wird in der Funktion verwendet
def g():	 
	a = 2
	print ('Inside g() : ',a )

# Variable wird in der Funktion als global deklariert und ueberschrieben
def h():	 
	global a 
	a = 3
	print ('Inside h() : ',a) 

"""Ab hier jede Zeile einzeln ausfuehren. Beobachten Sie was mit der Variablen
mit dem Namen 'a' passiert."""
print (a)
f() 
print (a)
g() 
print (a)
h() 
print (a)


#Aufgabe 15 (input Funktion)
"""Weisen Sie der Varibale x den Satz "Hello World" zu, indem Sie eine Eingabe 
von dem User in der Konsole aufnehmen. Verwenden Sie die "input()" Funktion 
Geben Sie die Eingabe in der Konsole aus."""
#Loesung
satz = input()

#Aufgabe 16 ((Aufgabe 1.7A aus der VBA Aufgabensammlung 3.7))
"""Erstellen Sie eine Funktion Quadrat, die den Flächeninhalt eines Quadrats 
berechnet. Ueberlegen Sie sich was die Input und Output Parameter sind"""


#Aufgabe 17 ((Aufgabe 1.7C aus der VBA Aufgabensammlung 3.7))
"""Erstellen Sie eine Funktion Kreis, die den Flächeninhalt eines Kreises
berechnet. Der Standardwert fuer den Radius ist 1, falls kein Radius an die 
Funktion uebergeben wird Ueberlegen Sie sich was die Input und Output Parameter
sind?"""


#Aufgabe 18
"""Schreiben sie eine Funktion die die Steigung von der Funktion f(x)=x**n 
berechnet. Input ist x und n und output ist f'(x)
der Wert x und n soll durch eine Input-Abfrage vollzogen warden,
die Ausgabe der Funktion soll durch einen print Befehl geschehen.
"""


