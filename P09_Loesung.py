

# Aufgabe 1
"""Gegeben ist die Liste mit dem Namen "list1"
Berechnen sie den Cosinus wert von jedem Eintrag in der liste und speichern sie
das Ergebnis in "list2"
Bonus fuer die Pros: Verwenden Sie keine for-Schleife
"""
import math
list1 = [1, 2, 3.14, 3.14/2]
list2 = []
for ii in list1:
    list2.append(math.cos(ii))

# Aufgabe 2
""" Erstellen sie einen numpy-array so wie er auf der Powerpoint Folie 
abgebildet ist
"""

#Loesung
import numpy as np
mat1 = np.array([[5.2,3.0,4.5], [9.1,0.1,0.3]])
# Form der Matix
np.shape(b)

# Aufgabe 2.1
"""
Verwenden Sie den numpy-array aus Aufgabe 2 und berechnen Sie den Cosinus Wert
von jedem Element.
"""

#Loesung
np.cos(mat1)

# Aufgabe 3
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (3,5)
Jedes Element des Arrays = 0 """

#Loesung
mat2= np.zeros([3,5])

# Aufgabe 4
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (2,5)
Jedes Element des Arrays = 1 """
#Loesung
mat3= np.ones([2,5])

# Aufgabe 5
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (2,5)
Jedes Element des Arrays = 6 """
#Loesung
mat4 = np.ones([2,5]) * 6

# Aufgabe 6
""" Erstellen sie einen numpy-array mit folgenden Dimensionen (3,3)
Das erste Element ist 0, das zweite 1, das dritte 2 usw. Gehen sie wie folgt 
vor:
1) Verwenden sie die numpy Funktion arange (np.arrange) um eine Zahlenfolge 
    im numpy Format zu erstellen
2) Verwenden Sie die numpy Funktion reshape um aus dem 1D array einen array
    mit Dimension (3,3) zu ersetllen"""

#Loesung
vec1= np.arange(9)
mat5= np.reshape(vec1, [3,3])

mat5= np.reshape(np.arange(9), [3,3]) #gleiche in Gruen in einer Zeile

# Aufgabe 7
""" Gegeben ist der Untenstehende 1D array "bsp_array1", aendern sie das 
Element das die Zahl 7 hat in die Zahl 17 um"""

#Loesung
bsp_array1=np.arange(8)
bsp_array1[7] = 17

# Aufgabe 8
""" Gegeben ist der Untenstehende 2D array "bsp_array2", aendern sie das 
Element das die Zahl 7 hat, in die Zahl 17 um"""
bsp_array2=np.reshape(np.arange(8),[4,2])
bsp_array2[3,1] = 17

# Aufgabe 9
""" Gegeben ist der Untenstehende 3D array "bsp_array3", aendern sie das 
Element das die Zahl 7 hat in die Zahl 17 um"""
bsp_array3=np.reshape(np.arange(24),[4,3,2])

#Loesung
bsp_array3[1,0,1]=17
bsp_array3[2]
bsp_array3

# Aufgabe 10
""" Gegeben ist der Untenstehende 1D array "bsp_array4", Erstellen Sie einen 
neuen 1D array "sub_array4" der die letzten 3 Elemente von "bsp_array 4"
beinhaltet
"""
#Loesung
bsp_array4=np.reshape(np.arange(16),[16,1])
sub_array4 = bsp_array4[-3:]

# Aufgabe 11
""" Gegeben ist der Untenstehende 3D array "bsp_array5", 
 Erstellen Sie einen neuen 1D array "sub_array5" der die Elemente 
 [ 4, 10, 16, 22] beinhaltet. Erstellen Sie den sub_array5 in abhaengigkeit von
 bsp_array5 Verwenden sie die slicing Methode
"""
bsp_array5=np.reshape(np.arange(24),[4,3,2])
#Loesung
sub_array5 = bsp_array5[:,2,0]

# Aufgabe 12
""" Multiplizieren Sie die 2 Matrizen "mat1" und "mat2" mit einander
"""
mat1=np.reshape(np.arange(0,6),[2,3])
mat2=np.reshape(np.arange(6,18),[3,4])

#Loesung
mat_sol=np.matmul(mat1,mat2)

# Aufgabe 13
""" Multiplizieren Sie die 2 Matrizen "mat3" und "mat4" Elementweise mit 
einander
"""
mat3=np.reshape(np.arange(0,6),[2,3])
mat4=np.reshape(np.arange(6,12),[2,3])

#Loesung
mat_sol1= mat3*mat4

# Aufgabe 14
""" Mulitplizieren Sie jede Zeile von "mat5" Elementweise mit dem Vector "vec1"
"""
mat5=np.reshape(np.arange(12),[3,4])
vec1=np.reshape(np.arange(4),[1,4])

#Loesung
mat_sol2= mat5*vec1


# Aufgabe 15
"""
Aufgabe fuer die Pros:
Gegeben ist die untenstehende Matrix. Berechnen Sie die Eigenwerte und 
Eigenvektoren fuer diese Matrix.

"""
mat6=np.reshape(np.arange(9),[3,3])



