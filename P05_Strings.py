#Aufgabe 1 (len-Funktion)
"""Erstellen Sie ein Skript, welches eine Eingabe von dem User auffordert. Die 
Eingabe kann ein beliebiger Satz sein. Verwenden sie die 'len' Funktion um die
Laenge des Satzes (Anzahl aller Zeichen) mit einer print() Funktion auszugeben.
Bonus fuer die Pros: Geben Sie die Satzlaenge ohne Leerzeichen an
"""
sen=input("Geben Sie einen beliebigen Satz in der Konsole ein\n")
#Loesung
print(len(sen))

#Aufgabe 2 (Untersuchen ob ein Buchstabe in einem String vorkommt)
""" Erstellen Sie eine Variable mit dem Namen "sen" und weisen Sie Ihr den 
string "Hello World" zu. Untersuchen Sie ob der Buchstabe "o" in dem string 
enthalten ist.
Bonus fuer die Pros: Geben Sie die Postionen an, wo der Buchstabe "o" in dem 
String vorkommt. Verwenden Sie nicht die "find" funktion."""
#Loesung
sen = "Hello World"
print("o" in sen)

#Aufgabe 3 (find Funktion fuer Strings)
""" Erstellen Sie eine Variable mit dem Namen "sen" und weisen Sie Ihr den 
string "Hello World" zu. Benutzten sie die find Funktion um die Postion des
 ersten Buchstabens "o" zu finden.
Hier ist ein Beispiel wie man das erste Auftreten des Buchstabens "e" auffindet
Bonus fuer die Pros: Wie wuerden Sie die Position des zweiten "o" finden"""
sen = "Hello World"
position = sen.find("e")
print(position)
#Loesung
sen = "Hello World"
position = sen.find("o")
print(position)

# Aufgabe 4 (Ausgabe von einzelnen Zeichen in einem String)
""" Erstellen Sie eine Variable mit dem Namen "sen" und weisen Sie Ihr den 
string "Hello World" zu. Geben Sie anschliessend den vorletzten Buchstaben des
 Strings mit einer print() Ausgabe wieder. 
Hier ist ein Beispiel wie man den Ersten Buchstaben von einem string bekommt.
Bonus fuer die Pros: Zaehlen Sie wie oft der Buchstabe "o" in dem String 
vorkommt und speichern Sie diese Zahl in einer neuen Variable. """
sen="Hallo World"
print(sen[0])
#Loesung
sen = "Hello World"
print(sen[-2])

#Aufgabe 5 (String slicing)
""" Erstellen Sie eine Funktion mit dem Namen "last_letters" die als Input ein 
beliebiegen String einliesst und dann die letzten 3 Buchstaben mit einer 
print() Ausgabe ausgibt. Zusaetlich soll die Funktion die letzten 3 Buchstaben 
selber ausgeben mit return(), so das man diese 3 Buchstaben einer neuen 
Variabel zuweisen kann.
Hier ist ein Beispiel wie man sich den letzten Buchstaben von einem String 
in eine neue Variable speichern kann
Bonus fuer die Pros: Schneiden Sie die ersten 2 und letzten 2 Buchstaben 
von dem String ab und geben Sie Ihn aus."""
satz="Hello World"
last2=satz[-2:]

#Loesung
def last_letters(sen):
    last3 = sen [-3:]
    print(last3)
    return(last3)
last_letters(satz)


#Aufgabe 6 (Integer vs String)
"""Gegeben ist der untenstehende code. Fuehren Sie diesen aus. Warum kommt es 
zu einem Fehler?
Aendern Sie den Code so, dass der Fehler behoben wird
und die Addition funktioniert. """
string = "123456789"
result = string + 10
#Loesung
string = 123456789
result = string + 10

#Aufgabe 7 (String Concatenation)
"""Gegeben ist der untenstehende code. Fuehren Sie diesen aus. Was kommt raus?
Bonus fuer die Pros: Aendern Sie den Code so, dass string2 genau in der Mitte 
von string1 eingefuegt wird. Ueberlegen Sie sich eine Regel, falls string1 
eine ungerade Anzahl an Zeichen hat. """
string1 = "123456789"
string2 = "10"
result = string1 + string2
print(result)


#Aufgabe 8 (String manupilation)
"""Gegeben ist der untenstehende string. Erstellen Sie einen string mit der 
umgekehrten Reihenfolge von Zeichen und das immer nur das zweite Zeichen 
genommen wird. Am Ende sollte der neue string wie folgt aussehen: "97531"
Bonus fuer die Pros: Summieren Sie die einzelnen Zahlen auf, also in dem
Beispiel waere das 9+7+5+3+1
"""
#Loesung
string="0123456789"
print(string[-1::-2])


#Aufgabe 9
""" Gegeben ist folgender string
text = "X-DSPAM-Confidence:    0.8475"
Ihre Aufgabe ist es nun die Zahl 0.8475 in eine float Variable abzuspeichern. 
Schritt 1: Suchen Sie die Postion des Doppelpunktes (:) in dem String, und 
    speichern Sie die Postion als eine Variable ab, mit dem Namen "pos"
Schritt 2: Erstellen Sie eine neue Variable mit dem Namen "num_str" die die 
    Zahl in dem string "text" beinhaltet. Benutzten sie die variable "pos" dazu
Schritt 3: Wandeln Sie den String "num_str" in ein float um und speichern 
    diesen unter dem variablen Namen "num_float". Die Funktion float wandelt 
    strings in floats um und loescht automatisch Leerzeichen, die vor oder nach 
    der eigentlichen Zahl stehen.
Hier ist ein Beispiel wie man einen String in einen float umwandelt"""
num_str="     0.23456"
num_float=float(num_str)

#Loesung
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":") + 1
num_text= text[pos:]
num_float = float(num_text)
print(num_float)

#Aufgabe 10
""" Erstellen Sie eine Funktion mit dem Namen print_string die einen beliebigen
 string als input hat. Die Funktion gibt jeden einzelnen Buchstaben mit der 
 print() Funktion aus. Verwenden Sie eine for-schleife"""
#Loesung
def print_string (sen):
    for ii in sen:
        print(ii)

print_string("Ein beliebiger Satz")


#Aufgabe 11
""" Erstellen Sie einen string str1 = "Hello" und einen 
string str2 = "World". Verbinden Sie beide Strings zu einem neuen String, der 
beide strings vereint. Einmal mit Leerzeichen (str3_space) und einmal ohne 
(str3_nospace)"""
str1="Hello"
str2="World"
#Loesung
str3_nospace = str1+str2
str3_space = str1 + " " + str2


#Aufgabe 12 (Hausaufgabe)
""" Erstellen Sie eine Funktion mit dem Namen ltor die 
einen beliebigen string als input hat. 
Die Funktion geht durch den string durch und ersetzt 
jedes "l" mit dem Buchstaben "r"
Schritt 1: Definieren Sie die Funktion
Schritt 2: Erstellen Sie einen leeren string, z.B.: empty=""
Schritt 3: Starten sie eine for-Schleife die durch jeden buchstaben durchgeht
Schritt 4: Ueberpruefen Sie ob der Buchstabe ein "l" ist oder nicht, falls ja 
    aendern sie den Buchstaben entsprechend (if-else Abfrage)
Schritt 5: Haengen Sie den Buchstaben an den leeren String an
Bonus fuer die Pros: Loesen Sie die Aufgabe ohne for-Scheife"""

        
    
