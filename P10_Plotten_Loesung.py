
# Aufgabe 1
""" Erstellen sie einen einfachen Datensatz mit x, y und z
x= 0 bis 10 mit einer Schrittweite von 2
Verwenden sie numpy.arange dazu, googlen sie wie man die Schrittweite auf 2 
aendert. Verwenden Sie x um y und z zu erstellen.
y=x^2
z=x^3
"""
import numpy as np
#Loesung
x= np.arange(0,11,2)
y= x**2
z= x**3


# Aufgabe 2
""" Nehmen Sie die 2 Arrays aus Aufgabe 1 und plotten Sie diese in einem Line
 plot. Verwenden Sie dazu die matplotlib Bibliothek, indem Sie folgendes 
 importieren"""
import matplotlib.pyplot as plt
#Loesung
plt.plot(x,y)

# Aufgabe 3
""" Nehmen Sie die 2 Arrays aus Aufgabe 1 und plotten Sie diese in einem 
Scatter plot.
Diesmal soll der Plot aber in einem neuen Fenster erscheinen.
Aendern Sie dazu die Einstellungen"""

#Loesung
plt.scatter(x,y)

# Aufgabe 4
""" Erstellen sie ein leeres Bild mit Breite 19 und Hoehe 9
weisen sie dem Bild die variable "fig" zu
Wenn Sie dies erstellt haben koennen sie mit der Breite und Hoehe ein wenig 
experimentieren.
"""
#Loesung
fig = plt.figure(figsize = (6,3))

# Aufgabe 5
"""
Fuegen Sie dem Bild das Sie in Aufgabe 4 erstellt haben ein Koordinaten System 
(KS) hinzu
Mit folgenden Eigenschaften
X-Position des KS Ursprungs: 0.2
Y-Position des KS Ursprungs: 0.6
Breite des KS: 0.3
Hoehe des KS: 0.2
"""
#Loesung
ax = plt.axes([0.2, 0.6, .2, .2])

# Aufgabe 6
"""
Fuegen Sie dem KS, dass Sie in Aufgabe 5 erstellt haben einen Graphen hinzu
x=np.arange(0,12,2)
y=x**2
"""

x=np.arange(0,12,2)
y=x**2
plt.plot(x,y)

# Aufgabe 6.1
"""
Fuegen Sie dem KS das Sie in Aufgabe 6 erstellt haben noch einen Graphen hinzu
Hier ist die Funktion:
x=np.arange(0,12,2)
y=x**3
"""
x=np.arange(0,12,2)
y=x**3
plt.plot(x,y)

# Aufgabe 7
"""
Fuegen Sie dem Bild aus Aufgabe 6 ein neues KS hinzu. Mit folgenden 
Eigenschaften:
X-Position des KS Ursprungs: 0.6
Y-Position des KS Ursprungs: 0.6
Breite des KS: 0.3
Hoehe des KS: 0.2
"""
#Loesung
ax2 = plt.axes([0.6, 0.6, .3, .2])


# Aufgabe 8
"""
Fuegen Sie dem KS das Sie in Aufgabe 7 erstellt haben 2 Graphen hinzu
x=np.arange(0,12,2)
y=x**2
und 
y=x**3
"""

#Loesung
x=np.arange(0,12,2)
y2=x**2 
z=x**3
plt.plot(x,y)
plt.plot(x,z)

# Aufgabe 9
""" Erstellen Sie ein Komplett neues Bild das fast genauso aussieht wie das
erstellte Bild in Aufgabe 8 (2 KS mit jeweils 2 Graphen). Nur das das neue Bild
im linken KS nur noch einen Graphen hat anstatt 2. Sie koennen sich auswaehlen 
welchen Graphen Sie loeschen
Tipp: Verwenden Sie Copy Paste von den vorherigen aufgaben
"""

#Loeschen
fig=plt.figure(figsize=(10,5))
ax = plt.axes([0.2,0.6,0.3,0.2])
plt.plot(x,y2)
ax1 = plt.axes([0.6,0.6,0.3,0.2])
plt.plot(x,y1)
plt.plot(x,y2)


# Aufgabe 10
""" Erstellen Sie ein Bild und unterteilen Sie es in 6 Sektoren indem Sie
das Bild in 3 Spalten und 2 Zeilen unterteilen
Plotten Sie einen Graphen in den 6 Sektoren (unten rechts)
x=np.arange(0,12,2)
y=x**2
"""
#Loesung
fig=plt.figure(figsize=(10,5))
plt.subplot(3,2,6)
plt.plot(x,y)


# Aufgabe 11
""" Fuegen Sie dem Bild aus Aufgabe 10 einen Graphen in den 4ten Sektor hinzu
x=np.arange(0,12,2)
y=x**3
"""
#Loesung
x=np.arange(0,12,2)
y=x**3
plt.subplot(3,2,4)
plt.plot(x,y)

# Aufgabe 12
""" Erstellen Sie ein Bild mit einem Graphen
x=np.arange(0,12,2)
y=x**3
Die Linie des Graphen soll folgende Eigenschaften haben:
Farbe: Gruen (g)
Linestyle: (-.)
Dicke der Linie: 3
"""
#Loesung
fig=plt.figure(figsize=(10,5))
plt.plot(x,y)