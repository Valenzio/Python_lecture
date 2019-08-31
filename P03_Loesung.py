
# Aufgabe 1
"""Erstellen Sie folgende Variablen in Python mit den Entsprechenden Werten
x=1
y=2
z=3
"""

#Loesung
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
"""
x=1
y=2
z=3
f=(x**2)+ y**3 + z**4

# Aufgabe 3
"""
Loeschen Sie alle Variablen im Workspace.
Definieren Sie eine Funktion in Python mit dem Funktionsnamen 'func1', 
Eingangsparamter sind x, y und z
Im Funktionskörper wird folgendes berechnet
f=(x**2)+ y**3 + z**4
Ausgabewert ist f
Hier nochmal das Beispiel von der Powerpoint Folie
"""
def myfunc(a,b):
    c=a+b
    return(c)

#Loesung
def func(x,y,z):
    f=(x**2)+ y**3 + z**4
    return(f)

# Aufgabe 4
"""
Nehmen Sie sich die Funktion von Aufgabe 3 zur Hilfe und Berechnen Sie folgenden
Wert: f=(1**2)+ 2**3 + 3**4
"""    

#Loesung
f=func(1,2,3)
f=func(1,2,5)

# Aufgabe 5
"""Definieren Sie eine Funktion in Python mit dem Funktionsnamen func2, 
Eingangsparamter sind x, y und z
Im Funktionskörper wird folgendes berechnet
 für x>0
und
f= y**3 + z**4 für x<=0
Ausgabewert ist f
"""

#Loesung
def func2(x,y,z):
    if x>0:
       f=(x**2)+ y**3 + z**4
    else:
       f= y**3 + z**4
    return(f)
       


#Aufgabe 6:
"""
Nehmen Sie sich die Funktion von Aufgabe 5 zur Hilfe und Berechnen Sie folgenden
Werte:
g1=func2(3,4,5)
g2=func2(-3,4,5)

g1 und g2 sind dabei neue Variablen, denen Sie die Funktionswerte zuweisen.
"""   
#Loesung
g1=func2(3,4,5)
g2=func2(-3,4,5)
 

#Aufgabe 7
"""
Definieren Sie eine Funktion in Python mit dem Funktionsnamen func, Eingangsparamter 
sind x, y und z
Im Funktionskörper wird folgendes berechnet
f=(x**2)+ y**3 + z**4 
und
g= y**3 + z**4 
Ausgabewerte sind f und g

"""
#Loesung
def func(x,y,z):
    f=(x**2)+ y**3 + z**4 
    g= y**3 + z**4 
    return(f,g)

#Aufgabe 8
"""
Verwenden Sie die Funktion aus Aufgabe 7, mit x=1,y=2 und z=3
1. Speichern Sie sich f und g gleichzeitig in die Variablen a11 und a12 ab
2. Speichern Sie sich nur f in die Variable a2


"""
#Loesung
a11,a12 = func(1,2,3)

# Aufgabe 9
"""
Definieren Sie eine Funktion in Python mit dem Funktionsnamen func, Eingangsparamter 
sind x, y und z
Im Funktionskörper wird folgendes berechnet
f=(x**2)+ y**3 + z**4 für x>0
und
f= y**3 + z**4 für x<=0
Sie brauchen keinen Ausgabewert, aber lassen Sie das Ergebnis mit der print 
Funktion anzeigen
"""

#Loesung
def func(x,y,z):
    if x>0:
        f=(x**2)+ y**3 + z**4
    else:
        f= y**3 + z**4 
    print(f)

func(1,2)


# Aufgabe 10
"""
Definieren Sie eine Funktion in Python mit dem Funktionsnamen func, Eingangsparamter 
sind x, y und z
Im Funktionskörper wird folgendes berechnet
f=(x**2)+ y**3 + z**4 
Ausgabewerte ist f.
Erstellen Sie die Funktion so, dass der User 
nur den Parameter fuer x Angeben muss. Falls 
dies der Fall ist nehmen die restlichen Eingangsparameter folgende Werte an
y=0
z=0
"""

def func (x,y=0,z=0):
    f=(x**2)+ y**3 + z**4 
    return(f)
    
a = func(1)
print(a)
    
#Beispiel 
round(5.234)
round(5.234,2)
round(5.234,0)

#Aufgabe 11
"""
Verwenden Sie die Funktion aus Aufgabe 10, um den Funktionswert f zu
berechnen. Verwenden Sie folgende Eingangsparameter mit x=1,y=2
"""
#Loesung
f= func(1,2)

#Aufgabe 12
"""
Loeschen Sie alle Variablen im Workspace.
Gegeben ist die Funktion mit dem Namen "myfunc". Fuehren Sie den unten stehenden 
Code aus. Beobachten Sie welche Variablen in Ihrem Workspace angelegt werden.
Aendern Sie die Funktion "myfunc" so, dass nach dem Durchlaufen des codes, die 
Variable "c" im Workspace erscheint. 
"""

#Loesung
def myfunc(a,b):
    global c
    c=a+b
    return(c) 

result=myfunc(5,10)

#Aufgabe 13
"""
Loeschen Sie alle Variablen im Workspace.
Gegeben ist die Funktion mit dem Namen "myfunc2". Fuehren Sie den unten stehenden 
Code aus. Beobachten Sie welche Variablen in Ihrem Workspace angelegt werden.
Welchen Wert haben die Variablen "a", "b" und "c" am Ende, warum?
Aendern Sie die Funktion "myfunc2" so, dass nach dem Durchlaufen des codes, die 
Variable "c" den Wert aus der Funktion hat. 
"""
a=1
b=2
c=3

def myfunc2(a,b):
    c=a+b
    return(c) 

result=myfunc2(5,10)

#Loesung
def myfunc2(a,b):
    global c
    c=a+b
    return(c) 

result=myfunc2(5,10)

#Aufgabe 14
"""
Weisen Sie der Varibale x einen beliebigen Satz zu, indem Sie eine Eingabe 
von dem User in der Konsole aufnehmen. Verwenden Sie die "input()" Funktion 
Geben Sie die Eingabe in der Konsole aus.
"""
x = "Hello World" #Falsch
#Loesung
print ("geben sie ihren Satz ein")
x=input()
print(x)
#alternative
x = input("Geben Sie ihren Satz hier ein\n")
print(x)

#Loesung
