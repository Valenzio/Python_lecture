# Aufgabe 1 (Ausfuehren von Mathematischen Funktionen auf Listenelemente)
"""Gegeben ist die Liste mit dem Namen "list1"
Berechnen sie den Cosinus Wert von jedem Eintrag in der liste und speichern sie
das Ergebnis in "list2"
Bonus fuer die Pros: Verwenden Sie keine for-Schleife."""
list1 = [1, 2, 3.14, 3.14/2]


# Aufgabe 2
""" Erstellen sie einen numpy-array so wie er auf der Powerpoint Folie 
abgebildet ist"""

# Aufgabe 2.1
"""Verwenden Sie den numpy-array aus Aufgabe 2 und berechnen Sie den Cosinus 
Wert von jedem Element."""


# Aufgabe 3 (Erstellen einer Matrix)
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (3,5)
Jedes Element des Arrays/Matrix hat den Wert 0 """


# Aufgabe 4 
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (2,5)
Jedes Element des Arrays/Matrix hat den Wert 1 """


# Aufgabe 5
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (2,5)
Jedes Element des Arrays/Matrix hat den Wert 6 """


# Aufgabe 6 (Reshape)
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (3,3)
Das erste Element ist 0, das zweite 1, das dritte 2 usw. Gehen sie wie folgt 
vor:
1) Verwenden sie die numpy Funktion arange um eine Zahlenfolge 
    im numpy Format zu erstellen
2) Verwenden Sie die numpy Funktion reshape um aus dem 1D array einen array
    mit Dimension (3,3) zu ersetllen"""
    

# Aufgabe 7 (Array manipulation)
""" Gegeben ist der Untenstehende 1D array "bsp_array1", aendern sie das 
Element das die Zahl 7 hat in die Zahl 17 um"""
bsp_array1=np.arange(8)


# Aufgabe 8 
""" Gegeben ist der Untenstehende 2D array "bsp_array2", aendern sie das 
Element das die Zahl 7 hat, in die Zahl 17 um"""
bsp_array2=np.reshape(np.arange(8),[4,2])


# Aufgabe 9
""" Gegeben ist der Untenstehende 3D array "bsp_array3", aendern sie das 
Element das die Zahl 7 hat in die Zahl 17 um"""
bsp_array3=np.reshape(np.arange(24),[4,3,2])


# Aufgabe 10 (Array slicing)
""" Gegeben ist der Untenstehende 1D array "bsp_array4", Erstellen Sie einen 
neuen 1D array "sub_array4" der die letzten 3 Elemente von "bsp_array4"
beinhaltet"""
bsp_array4=np.arange(16)


# Aufgabe 11
""" Gegeben ist der Untenstehende 3D array "bsp_array5", 
 Erstellen Sie einen neuen 1D array "sub_array5" der die Elemente 
 [ 4, 10, 16, 22] beinhaltet. Erstellen Sie den sub_array5 in abhaengigkeit von
 bsp_array5 Verwenden sie die slicing Methode"""
bsp_array5=np.reshape(np.arange(24),[4,3,2])


# Aufgabe 12 (Matrix multiplication)
""" Multiplizieren Sie die 2 Matrizen "mat1" und "mat2" mit einander"""
mat1=np.reshape(np.arange(0,6),[2,3])
mat2=np.reshape(np.arange(6,18),[3,4])


# Aufgabe 13
""" Multiplizieren Sie die 2 Matrizen "mat3" und "mat4" Elementweise mit 
einander
"""
mat3=np.reshape(np.arange(0,6),[2,3])
mat4=np.reshape(np.arange(6,12),[2,3])


# Aufgabe 14
""" Mulitplizieren Sie jede Zeile von "mat5" Elementweise mit dem Vector "vec1"
"""
mat5=np.reshape(np.arange(12),[3,4])
vec1=np.reshape(np.arange(4),[1,4])


# Aufgabe 15
"""Aufgabe fuer die Pros:
Gegeben ist die untenstehende Matrix. Berechnen Sie die Eigenwerte und 
Eigenvektoren fuer diese Matrix."""
mat6=np.reshape(np.arange(9),[3,3])



