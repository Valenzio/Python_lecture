# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:59:47 2018

@author: The machine
"""



# Aufgabe 1:
"""Finden Sie den Fehler im folgenden Code Abschnitt und bessern Sie Ihn aus
"""
def bsp(a,b):
    a=a+b
    retrun(a)
    
f=bsp(19,10)

#Loesung
def bsp(a,b):
    a=a+b
    return(a)
    
f=bsp(19,10)

#Aufgabe 2
"""
Finden Sie den/die Fehler im folgenden Code Abschnitt
"""

counter=0
While counter < 5:
    print "hello"
    counter = counter + 1

#Loesung
counter=0
while counter < 5:
    print ("hello")
    counter = counter + 1
    
#Aufgabe 3
"""
Finden Sie den/die Fehler im folgenden Code Abschnitt und bessern Sie ihn/sie aus
"""
list1=[1,2,3,4]
last_list=list1[4]

#Loesung
last_list=list1[3]

#Aufgabe 4
"""
Finden Sie den/die Fehler im folgenden Code Abschnitt und bessern Sie ihn/sie aus
"""

import pandas as pd

df=pd.DataFrame([[3,4,5],[4,5,3],[3,1,3]], index=[1,2,3],columns=["a","b","c"])

last_column=df.iloc[:,2]
#Loesung
first_column = df["a"]

#Aufgabe 5
"""
Finden Sie den/die Fehler im folgenden Code Abschnitt und bessern Sie ihn/sie aus
"""
zahl1= "10"
zahl2= "01"
zahl3= "1o"

summe=int("zahl1")+int(zahl2) +int(zahl3)

#Loesung
zahl1= "10"
zahl2= "01"
zahl3= "10"

summe=int(zahl1)+int(zahl2) +int(zahl3)

#Aufgabe 6
"""
Führen Sie den untenstehenden Code aus. 
1) Geben Sie für a und b einfache Zahlen ein,
    Sie werden sehen der Code läuft ohne Probleme
2) Geben Sie für a eine Zahl und b einen Buchstaben ein
    Sie werden sehen, dass ein ValueError auftritt
3) Packen Sie die 3 Zeilen Code in eine try-expect Struktur
    Wenn ein Fehler auftritt können sie folgenden Befehl auführen:
        print("User Input Fehler")
"""

#Loesung
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except:
    print("user input Fehler")
        
    
#Aufgabe 7
"""
Erweitern Sie den Loesungscode aus Aufgabe 6 folgendermassen
1) Wenn ein Buchstabe anstatt einer Zahl eingegeben wird (ValueError), kommt das
    print Statement: print("konnte es nicht in eine Zahl umwandeln")
2) Wenn b = 0 ist (ZeroDivisionError), kommt das print Statement:
    print("Kann nicht durch null teilen")
3) Falls irgend ein anderer Fehler auftritt, kommt das Statement:
    print("Irgendwas ist gewaltig schief gelaufen")
"""
#Loesung
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except ValueError:
    print("konnte es nicht in eine Zahl umwandeln")
except ZeroDivisionError:
    print("Kann nicht durch null teilen")
except:
    print("Irgendwas ist gewaltig schief gelaufen")

#Aufgabe 8 
"""
Erweitern Sie den Loesungscode aus Aufgabe 7 fogendermassen:
1) Wenn kein Fehler im try-Block auftritt, kommt das print Statement:
    print("Es gab keine Probleme")
2) Am Ende des Programs soll das folgende print Statement erscheinen unabhaengig
    ob es einen Fehler gibt oder nicht print("Versuchen Sie es nochmal")
"""

#Loesung
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except ValueError:
    print("konnte es nicht in eine Zahl umwandeln")
except ZeroDivisionError:
    print("Kann nicht durch null teilen")
except:
    print("Irgendwas ist gewaltig schief gelaufen")
else:
    print("Es gab keine Probleme")
finally:
    print("Versuchen Sie es nochmal")


#Aufgabe 9
"""
Erstellen Sie eine Funktion aus dem Loesungscode von Aufgabe 8
Die Funktion heisst "bruch" und hat keine Input Parameter.
Die Funktion soll als Output das Ergebniss von der Division a/b liefern
Sie muessen also ein return in die Funktion einbauen. Trotzdem sollen die print 
ausgaben noch funktionieren
"""

#Loesung
def bruch():
    try:
        a = int(input("Tell me one number:"))
        b = int(input("Tell me another number:"))
        return (a/b)
    except ValueError:
        print("konnte es nicht in eine Zahl umwandeln")
    except ZeroDivisionError:
        print("Kann nicht durch null teilen")
    except:
        print("Irgendwas ist gewaltig schief gelaufen")
    else:
        print("Es gab keine Probleme")
    finally:
        print("Versuchen Sie es nochmal")
ergebniss=bruch()
print(ergebniss)  

#Aufgabe 10
"""
Erstellen Sie ein neues leeres Python Skript und kopieren sich den untenstehenden Code.
1) Starten Sie den Debugger (strg+F5), und gehen sie mit "Step" durch ihr Programm
2) Starten Sie den Debugger (strg+F5), und gehen sie mit "Step Into" durch ihr Programm
3) Setzten Sie zwei Breakpoints an einer beliebigen Stelle und starten Sie den 
    Debugger, verwenden sie "Continue" um zum naechsten Breakpoint zu gelangen
4) Wie Aufgabe 3, blos das mindestens ein Breakpoint in einer Funktion ist
    
Bei allen Aufgaben, beobachten Sie im VariablenExplorer wie sich die Variablen 
aendern
"""

def func(x,y,z):
    a=x+y
    b=x-y
    c=z+x
    d=subfun(a,b)
    return (a)

def subfun(s,q):
    l=s*q
    return(l)


x=10
y=11
z=12

d=func(x,y,z)

print(d)

#Aufgabe 11
"""
Gegeben ist unten stehender Code. Dieser ist Fehlerhaft.
Theoretisch hat die Funktion als Inputparameter eine Liste. Die Funktion hat
als Output eine Liste, die in umgekehrter Reihenfolge ist wie die Input liste.
Der Code hat Logische wie auch Syntax Fehler.
Verbessern Sie den Code damit er laeuft. Alternativ koennen Sie eine neue 
Funktion schreiben.

"""
def rev_list_buggy(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)):
        j = len(L) - i
        L[i] = temp
        L[i] = L[j]
        L[j] = L[i]

list1=[1,2,3,4,5]
rev_list=rev_list_buggy(list1)
print(rev_list)

#Loesung
def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        
L = [1,2,3,4]
rev_list(L)
print(L)

#Aufgabe 12
"""
Gegeben ist unten stehender Code. Dieser ist Fehlerhaft.
Theoretisch hat die Funktion als Inputparameter eine ganze Zahl. Die Funktion hat
als Output eine Liste, aller Primzahlen die bis zur Inputzahl gehen.
Verbessern Sie den Code damit er laeuft. Alternativ koennen Sie eine neue 
Funktion schreiben.

"""
def primes_list_buggy(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    if i == 2:
        primes.append(2)
    # go through each elem of primes list
    for i in range(len(primes)):
        # go through each of 2...n
        for j in range(len(n)):
            # check if not divisible by elem of list
            if i%j != 0:
                primes.append(i)
                
#Loesung
def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2) )               
print(primes_list(15)  )      