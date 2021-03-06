# Aufgabe 1
"""Gegeben ist die Klasse "Auto".
1. Erstellen Sie ein Objekt mit dem Namen "polo" und initialisieren Sie bei der
Erstellung des Objektes das Gewicht mit 1500
2. Geben Sie das Gewicht mit dem Punktoperator in der Konsole aus
3. Aendern Sie das Gewicht mit dem Punktoperator zu 1200
4. Geben Sie das Gewicht mit dem Punktoperator in der Konsole aus"""
class Auto:

    def __init__(self,gewicht):
        self.gewicht= gewicht


# Aufgabe 2 (public vs privat)
"""Gegeben ist die Klasse "Auto2".
Was ist der Unterschied zur Klasse "Auto" von Aufgabe 1?
1. Erstellen Sie ein Objekt mit dem Namen "polo" und initialisieren Sie bei der
Erstellung des Objektes das Gewicht mit 1500
2. Geben Sie das Gewicht mit dem Punktoperator in der Konsole aus
3. Aendern Sie das Gewicht mit dem Punktoperator zu 1200
4. Geben Sie das Gewicht mit dem Punktoperator in der Konsole aus"""

class Auto2:

    def __init__(self,gewicht):
        self.__gewicht = gewicht
        
        
#Aufgabe 3
"""Gegeben ist die Klasse "Auto3".
1. Erstellen Sie ein Objekt mit dem Namen "polo" und initialisieren Sie bei der
Erstellung des Objektes das Gewicht mit 1500
2. Geben Sie das Gewicht in der Konsole aus, schauen sie sich dazu die 
Funktionen in der Klasse an, welche koennte die richtige sein fuer diese 
Aufgabe?
3. Aendern Sie das Gewicht von dem Objekt "polo" zu 1200, 
suchen Sie sich die Funktion die das erledigen koennte
4. Geben Sie das Gewicht in der Konsole aus, schauen sie sich dazu die 
Funktionen in der Klasse an, welche koennte die richtige sein fuer diese 
Aufgabe?"""
class Auto3:

    def __init__(self,gewicht):
        self.__gewicht = gewicht

    def get_gewicht(self):
        return self.__gewicht

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht


#Aufgabe 3.1
"""Gegeben ist die Klasse "Auto3".
Im Prinzip handelt es sich um die gleiche Aufgabe wie Aufgabe 3. Doch es gibt
nur eine Aenderung, welche?
1. Erstellen Sie ein Objekt mit dem Namen "polo" und initialisieren Sie bei der
Erstellung des Objektes das Gewicht mit 1500
2. Geben Sie das Gewicht in der Konsole aus, schauen sie sich dazu die Funktionen 
in der Klasse an, welche koennte die richtige sein fuer diese Aufgabe?
3. Aendern Sie das Gewicht von dem Objekt "polo" zu 1200, 
suchen Sie sich die Funktion die das erledigen koennte
4. Geben Sie das Gewicht in der Konsole aus, schauen sie sich dazu die Funktionen 
in der Klasse an, welche koennte die richtige sein fuer diese Aufgabe?
Tipp: Schauen Sie sich die Initialisierung an """
class Auto3:

    def __init__(self,gewicht):
        self.set_gewicht(gewicht)

    def get_gewicht(self):
        return self.__gewicht

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht


# Aufgabe 4
"""Gegeben ist wieder die Klasse "Auto" von Aufgabe 1. 
Wir wollen nun das jedes Objekt das mit einem maximalen Gewicht von 1200 
initialisiert wird. Das heisst wenn wir ein Objekt mit ueber 1200 Gewicht 
initialisieren, wird das Gewicht automatisch auf 1200 gesetzt
1. Erstellen Sie ein Objekt mit dem Namen "polo" und initialisieren Sie das 
Objekt mit einem Gewicht von 1100
2. Geben Sie das Gewicht in der Konsole aus mit dem print Befehl
3. Erstellen Sie ein neues Objekt mit dem Namen "golf" und initialisieren Sie
das Objekt mit einem Gewicht von 1300
4. Geben Sie das Gewicht von dem Objekt "golf" in der Konsole aus
5. Weisen Sie dem Objekt "golf" ein neues Gewicht mit dem Punktoperator zu, von 
1300
6. Geben Sie das Gewicht von dem Objekt "golf" in der Konsole wieder
War das Sinn und zweck des Objektes?"""
class Auto:

    def __init__(self,gewicht):
        if gewicht>1200:
            self.gewicht=1200
        else:
            self.gewicht= gewicht


#Aufgabe 5
"""Gegeben ist wieder die Klasse "Auto3" von Aufgabe 3. 
Wir wollen nun das jedes Objekt das mit einem maximalen Gewicht von 1200 
initialisiert wird. Das heisst wenn wir ein Objekt mit ueber 1200 Gewicht 
initialisieren, wird das Gewicht automatisch auf 1200 gesetzt.
1. Erstellen Sie ein Objekt mit dem Namen "polo" und initialisieren Sie das 
Objekt mit einem Gewicht von 1100
2. Geben Sie das Gewicht in der Konsole aus
3. Erstellen Sie ein neues Objekt mit dem Namen "golf" und initialisieren Sie
das Objekt mit einem Gewicht von 1300
4. Geben Sie das Gewicht von dem Objekt "golf" in der Konsole wieder
5. Weisen Sie dem Objekt "golf" ein neues Gewicht mit der setter Funktion, von 
1300
6. Geben Sie das Gewicht von dem Objekt "golf" in der Konsole wieder
War das Sinn und zweck des Objektes?"""
class Auto3:

    def __init__(self,gewicht):
        self.set_gewicht(gewicht)

    def get_gewicht(self):
        return self.__gewicht

    def set_gewicht(self, gewicht):
        if gewicht>1200:
            self.__gewicht=1200
        else:
            self.__gewicht= gewicht

        
#Aufgabe 6
"""Gegeben ist die Klasse "Auto4". Vergleichen Sie es mit der Klasse "Auto3" 
aus Aufgaben 5, was ist der Unterschied?
Tipp: Schauen Sie sich die Initialisierung an. 
1. Erstellen Sie ein Objekt mit dem Namen "polo" ohne das Sie das Gewicht 
initialisieren
2. Geben Sie das Gewicht in der Konsole des Objekts "polo" aus
3. Erstellen Sie ein Objekt mit dem Namen "golf" und weisen Sie das gewicht 
1200 bei der Initialiesierung des Objektes zu.
4. Geben Sie das Gewicht in der Konsole des Objekts "golf" aus"""
class Auto4:

    def __init__(self,gewicht=1000):
        self.set_gewicht(gewicht)

    def get_gewicht(self):
        return self.__gewicht

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht
        

#Aufgabe 7
"""Schauen sie sich die Klasse "Auto4" an und vergleichen Sie diese mit der aus 
Aufgabe 6. Der Einzige Unterschied ist das hier die Klasse "Auto4" die 
Eigentschaften von der Klasse "object" erbt. 
Dies war noetig in Python 2 um spezielle Klassen Features bereit zustellen
In Python 3 sind deswegen automatisch alle Features von der Klasse "object" in
jeder neuen Klasse enthalten. 
Es macht also keinen Unterschied ob die Klasse "object" vererbt wird oder nicht
(koennte fuer die Pruefung relevant sein)"""
class Auto4(object):

    def __init__(self,gewicht=1000):
        self.set_gewicht(gewicht)

    def get_gewicht(self):
        return self.__gewicht

    def set_gewicht(self, gewicht):
        self.__gewicht = gewicht
        
        
#Aufgabe 8
"""1.Laden Sie die Klasse "Auto4" aus Aufgabe 7 in den Arbeitsspeicher. 
2.Danach Laden Sie die Klasse "Motorrad" (siehe unten) in den Arbeitsspeicher. 
3.Erstellen Sie nun ein neues Objekt der Klasse "Motorrad" mit dem Namen 
"hornet" und initialisieren Sie es mit 150 als Gewicht.
4.Geben Sie das Gewicht von dem Objekt "hornet" in der Konsole aus (hier gibt 
es 2 Optionen wie man das anstellt)"""
class Motorrad(Auto4):
    def farbe(self):
        print("Blau")
    def __str__(self):
        return("Mein Motorrad wiegt " +str(self.get_gewicht())+"kg")


#Aufgabe 9 
"""Wir wollen die "Motorrad" Klasse aus Aufgabe 8 erweitern indem wir die Farbe 
des Motorrad Objektes in der Initialisierung vorgeben.
1. Fuegen sie den setter "set_farbe" zu der Klasse "Motorrad" hinzu
2. Fuegen sie den setter "get_farbe" zu der Klasse "Motorrad" hinzu"""
class Motorrad(Auto4):
    def __init__(self,gewicht,farbe):
        Auto4.__init__(self,gewicht) #initiierung von Auto4
        self.set_farbe(farbe)   #neue initiierung
        
    def set_farbe():
        
        
    def get_farbe():
        
        
    def __str__(self):
        return("Mein Motorrad wiegt " +str(self.get_gewicht())+"kg")

hornet=Motorrad(150,"blau")
print(hornet.get_farbe())


#Aufgabe 10
"""Vervollstaendigen Sie die Klasse "roller" damit man das Objekt "schwalbe" 
mit 3 Argumenten initialisieren kann: gewicht, farbe, Leistung. Laden Sie sich
zuvor die Klasse Motorrad aus Aufgabe 9 in den Arbeitsspeicher."""
class Roller(Motorrad):
    
    def __init__(self,gewicht,farbe,leistung):
         #initiierung von Motorrad
         #neue initiierung
        
    def set_leistung(self,leistung):
        self.__leistung=leistung
        
    def get_leistung(self):
        return(self.__leistung)

schwalbe=Roller(120,"orange",3)
print(schwalbe.get_farbe())
print(schwalbe.get_leistung())
print(schwalbe)


#Aufgabe 11
"""In Aufgabe 10 haben sie gesehen, das wenn sie den Befehl 
print(schwalbe) ausfuehren, ein text kommt der nicht zu ihrem Objekt passt.
(Da eine Schwalbe keine Motorrad ist, sondern eher ein Roller)
Aendern Sie die Klasse "Roller" so das der Text zum Objekt passt."""
class Roller(Motorrad):
    
    def __init__(self,gewicht,farbe,leistung):
        Motorrad.__init__(self,gewicht,farbe) #initiierung von Motorrad
        self.set_leistung(leistung)   #neue initiierung
        
    def set_leistung(self,leistung):
        self.__leistung=leistung
        
    def get_leistung(self):
        return(self.__leistung)

schwalbe=Roller(120,"orange",3)
print(schwalbe)






