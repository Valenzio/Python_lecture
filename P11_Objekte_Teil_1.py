# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:31:57 2018

@author: vsolotyc
"""


#Aufgabe 1
""" 
Erstellen Sie ein Dictionary mit dem Namen "polo", das folgende Eigenschaften enthaelt (keys):
    Gewicht, Leistung, Tankfuellung
Die entsprechenden Werte (values) sind:
    2000, 150, 60
 """

#Aufgabe 2
 """ 
 Erstellen Sie eine Funktion mit dem Namen tank_berechnung,
 die als Input das Dictionary aus Aufgabe 1 hat und die gefahrene Strecke. 
 Die Funktion berechnet den Tankinhalt nach der gefahrenen Strecke.
 Am Ende Gibt die Funktion das Dictionary mit dem neuen Tankinhalt zurueck
 Die Formel fuer den Verbrauch kann man folgendermassen berechnen
 
 verbrauch=Gewicht/2*Leistung/4 /5000
 """


#Aufgabe 3
 """
 Gegeben ist der unten stehende String "bsp_str". 
 Wandeln Sie jeden Buchstaben in dem String in einen Grossbuchstaben um. 
 Verwenden Sie dazu die entsprechende Methode. Verwenden Sie google oder dir() 
 um die richtige Methode zu finden
 """
 
 bsp_str="alles klein"
 
#Aufgabe 4
 """
 Gegeben ist die Untenstehende Klassen Definition fuer ein Auto. 
 Erstellen Sie ein neues Objekt der Klasse auto mit dem Namen "polo" und geben 
 Sie das Gewicht in der Konsole aus.
 Aendern Sie nun das Gewicht von dem "polo"-Objekt zu 1200 und geben Sie es wieder aus.
 """
 
class auto:
    Gewicht=2000
    Leistung = 150
    Tankinhalt = 60
    

#Aufgabe 5
 """
 Gegeben ist die Untenstehende Klassen Definition fuer ein Auto. 
 Fuehren Sie den Code aus bis zu den Kommentar. Danach fuehren Sie die letzten 2 Zeilen aus.
 Sie werden sehen es kommt eine Fehlermeldung. 
 Die funktion in der Klasse kann nichts mit dem Variablen Namen "gewicht" anfangen, obwohl wir 
 das Objekt Polo in die Funktion uebergeben. Welche Aenderung muss man vornehmen, damit 
 die Funktion in der Klasse weiss um welche Variablen es sich handelt. Schauen Sie sich 
 dazu Aufgabe 4 nochmal genauer an
 """

class Auto:
    gewicht=2000
    leistung = 150
    tankinhalt = 60
  
    def tank_berechnung(self,strecke):
        verbrauch=gewicht/2*leistung/4 /5000
        tankinhalt = tankinhalt - (verbrauch*strecke/100)
        
    
polo=Auto()
print(polo.tankinhalt)
# Bis hier ausfuehren, danach den rest
polo.tank_berechnung(100)
print(polo.tankinhalt)


#Aufgabe 6
 """
Gegeben ist die untenstehende Klasse. Diese ist fast genauso wie die Klasse die als
Loesung fuer Aufgabe 5 rauskam, mit der Ausnahme das der Tankinhalt nun mit einem Return versehen ist
und kein "self." davor steht. Fuehren Sie den Code aus. Sie werden sehen das sich 
der Tankinhalt nicht aendert. Wie koennte man den neuen Tankinhalt trotzdem ausgeben
ohne das man die Klasse veraendert? """
 class Auto:
    gewicht=2000
    leistung = 150
    tankinhalt = 60
  
    def tank_berechnung(self,strecke):
        verbrauch=self.gewicht/2*self.leistung/4 /5000
        tankinhalt = self.tankinhalt - (verbrauch*strecke/100)
        return (tankinhalt)
        
    
polo=Auto()
print(polo.tankinhalt)
# Bis hier ausfuehren, danach den rest
polo.tank_berechnung(100)
print(polo.tankinhalt)


 

#Aufgabe 7
 """
Nehmen Sie die Klasse die in Aufgabe 5 erstellt wurde. Erstellen Sie ein Objekt 
mit dem Namen "smart" und aendern Sie das Gewicht und Leistung zu 1500 und 100.
Geben Sie den Tankinhalt aus nachdem das Auto eine strecke von 100 gefahren ist.
 """
    

# Aufgabe 8
 """
 Gegegeben ist die untenstehende Klasse. Aendern Sie die Klasse so das man alle drei 
 Parameter (gewicht, leistung, tankinhalt) bei der Initialisierung des Objekts festlegen kann.
 
 """

class Auto:
    def __init__(self,gewicht):
        self.gewicht=gewicht
    
    
    leistung = 150
    tankinhalt = 60
  
    def tank_berechnung(self,strecke):
        verbrauch=self.gewicht/2*self.leistung/4 /5000
        tankinhalt = self.tankinhalt - (verbrauch*strecke/100)

        
    
polo=Auto(1500)
print(polo.tankinhalt)
# Bis hier ausfuehren, danach den rest
polo.tank_berechnung(100)
print(polo.tankinhalt)

# Aufgabe 9
"""
Erstellen Sie nun 2 Objekte der Klasse "Auto"
Verwenden Sie die Klasse "Auto" von Aufgabe 8
Das Erste Objekt heisst "golf" und hat folgende Eigenschaften: 1800, 100, 50
Das Zweite Objekt heist "passat" und hat folgende Eigenschaften: 2200, 120, 60
Berechnen Sie nun die Differenz des Tankinhaltes wenn der golf eine Strecke von 100
und der passat eine Strecke von 150 faehrt
"""

# Aufgabe 10
"""
Aendern Sie die untenstehende Klasse so, das wenn man ein Objekt der Klasse printed,
der Aktuelle Tankinhalt von dem Objekt angezeigt wird
"""

class Auto:
    def __init__(self,gewicht,leistung,tankinhalt):
        self.gewicht=gewicht
        self.leistung=leistung
        self.tankinhalt=tankinhalt
    
    def __str__(self):
            return("Beispiel")

    def tank_berechnung(self,strecke):
        verbrauch=self.gewicht/2*self.leistung/4 /5000
        tankinhalt = self.tankinhalt - (verbrauch*strecke/100)
        return (tankinhalt)
    
# Aufgabe 11
"""
erstellen Sie 2 listen
l1=[1,2,3]
l2=[4,5,6]
verwenden sie das "+" zeichen um die 2 Listen mit einander zu verknuepfen,
speichern sie das Ergebnis in der Variable "sum_list"

machen sie das gleiche nochmal nur anstatt listen verwenden Sie numpy arrays.
n1 und n2, Was ist der Unterschied?

"""        

# Aufgabe 12
"""
Schauen Sie sich den folgenden code an, was genau macht dieser Code.
Hier lernen Sie 2 neue Tools
1. List Comprehensions: Ist eine schnellere Schreibweise wie man eine for loop schreibt
2. zip: verbindet zwei listen zur einer, wenn man darueber iteriert bekommt
man pro iteration eine neue Liste (x) die Zwei Element hat x[0] und x[1].
Aufgabe: Schreiben sie diese List Comprehension in eine "normale" for loop verwenden Sie 
dennoch die zip Funktion
"""
l1=[1,2,3]
l2=[4,5,6]
sum_list=[x[0] + x[1] for x in zip(l1,l2)]


# Aufgabe 13
"""
Schauen Sie sich den folgenden Code an. Hier wird eine neue Objekt-Klasse definiert
Es handelt sich hierbei um ein Objekt das einer Liste aehnelt, nur mit dem 
Unterschied das man die Listen Elementweise addieren kann mit dem "+" Operator.
Aufgabe: Fuegen Sie zu dem Objekt eine neue Methode zu, mit dem Namen 
__sub__, diese Methode subtrahiert die 2 Listen Elementweise. 
"""
class Arrlist:
    def __init__(self,simple_list):
        self.simple_list=simple_list
        
    def __add__(self,other):
        sum_list=[x[0] + x[1] for x in zip(self.simple_list, other.simple_list)]
        return (Arrlist(sum_list))
    
    def __str__(self):
        return(str(self.simple_list))
        
l1=Arrlist([1,2,3])
l2=Arrlist([4,5,6])

l_sum=l1+l2
print(l_sum)



# Aufgabe 14
"""
Verwenden Sie die untenstehende Klasse um 2 Listen Elementweise zu addieren und 
Speichern Sie das Ergebnis in einem neuen Arrlist-Objekt mit dem Namen l_sum.
Verwenden Sie einmal den "+" Opperator und einmal mit der Methode "add"
"""
class Arrlist:
    def __init__(self,simple_list):
        self.simple_list=simple_list
        
    def __add__(self,other):
        sum_list=[x[0] + x[1] for x in zip(self.simple_list, other.simple_list)]
        return (Arrlist(sum_list))
    
    def add(self,other):
        sum_list=[x[0] + x[1] for x in zip(self.simple_list, other.simple_list)]
        return (Arrlist(sum_list))

    def __str__(self):
        return(str(self.simple_list))
        
l1=Arrlist([1,2,3])
l2=Arrlist([4,5,6])

# Aufgabe 15 (Hausaufgabe)
"""
Schauen Sie sich den folgenden Code an und versuchen Sie ihn zu verstehen
"""
class Fraction():
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))


