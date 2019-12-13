#Aufgabe 1 (Import von einem Modul)
""" Berechnen sie den Sinus von 45° = pi/4
Importieren Sie dazu das "math" modul und verwenden sie die richtige Funktion 
von diesem Modul"""
#Loesung
import math
sin45 = math.sin(3.14/4)

# Aufgabe 2 (Import eines Moduls mit Alias)
""" Berechnen sie den Sinus von 45° = pi/4 wie in Aufgabe 1, nur mit dem 
Unterschied, dass sie diesmal dem "math" Modul einen Alias zuweisen, der Ihnen 
ueberlassen ist"""
#Loesung
import differential_equation
sin45 = differential_equation.sin(3.14/4)

# Aufgabe 3 (Import einer einzelnen Funktion aus einem Modul mit Alias)
""" Berechnen sie den Sinus von 45° = pi/4 wie in Aufgabe 1, mit dem 
Unterschied das sie sich diesmal nur die Sinus Funktion aus dem math modul 
holen und diese mit einen Alias versehen, der Ihnen ueberlassen ist"""
#Loesung
from math import sin as sinus
sin45 = sinus(3.14/4)

# Aufgabe 4 (Erstellen einer einfachen Funktion)
"""Erstellen sie eine Funktion mit dem namen "addition", 
die Funktion hat 2 input argumente. Als output wird die Summe von den 2 input 
Arguemten ausgegeben. Rufen Sie die Funktion mit 2 beliebigen Zahlen auf und 
testen Sie ob das richtige Ergebnis raus kommt"""
#Loesunbg
def addition(a,b):
    return(a+b)
beispiel = addition(1,2)
# Aufgabe 5 (Abspeichern der Funktion in eine seperate Datei)
"""Erstellen Sie eine neue Python Datei (File->Newfile). 
Kopieren Sie sich die Funktion aus Aufgabe 4 in die Datei.
Speichern Sie die Datei unter dem Namen "beispiel_funktion" in einen beliebigen
Ordner (File-> Save as)"""


# Aufgabe 6 (Importieren der erstellten Funktion)
""" Wir wollen jetzt ein Python Skript erstellen, welches auf eine Funktion von
einer anderen Datei zugreift. Erstellen Sie deshalb eine neue Python Datei mit 
dem namen "main" und speichern Sie es in den gleichen Ordner wie die Datei aus 
Aufgabe 5 (File->Newfile und dann File-> Save as)
Und schreiben sie folgendes hinein"""
import beispiel_funktion
""" fuehren Sie diese Zeile aus, was passiert, warum?? 
Tip: Fuehren Sie folgenden Code aus:"""
import sys
sys.path


#Aufgabe 7 (Ausfuehren der main Python Datei)
""" Oeffnen Sie die Datei aus Aufgabe 6, stellen sie sicher das sich die "main" 
und "beispiel_funktion" datei im 
gleichen Ordner befinden Wenn Sie die "main" Datei geoeffnet haben druecken sie
F5 Was passiert? Gab es wieder einen Fehler warum nicht? 
Tip: fuehren Sie wieder folgenden Code aus:"""
import sys
sys.path


#Aufgabe 8 (Hinzufuegen von Ordner Stukturen)
""" Kopieren Sie die Datei "beispiel_funktion" in einen beliebigen Ordner.
Aendern sie den Namen der Datei zu "beispiel_funktion2"
Fuegen sie den Ordner (in dem die Datei liegt) zu sys.path hinzu, in dem Sie 
folgende Zeilen ergaenzen. Versuchen Sie nun die Datei "beispiel_funktion2" zu 
importieren und fuehren sie die Funktion "addition" aus."""
import sys
import os


#Diese Zeile muss von Ihnen angepasst werden
sys.path.append(os.path.abspath(r"D:\FOM\Industrielle Informationstechnik\Vorlesung\Python\P08\unter_ordner"))

