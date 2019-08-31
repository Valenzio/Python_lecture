# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:31:57 2018

@author: vsolotyc
"""

#Aufgabe 1
""" Erstellen Sie einen Pandas Datenframe. Verwenden Sie dazu das unten stehende Beispiel. Aendern Sie das Beispiel so das Sie dem
 existierenden Dataframe eine Zeile und eine Spalte hinzufuegen, es ist Ihnen ueberlassen welche Daten sie einfuegen"""
import pandas as pd

df=pd.DataFrame([[3,4,5],[4,5,3],[3,1,5]], index=[1,2,3],columns=["a","b","c"])

#Aufgabe 2 
""" Erstellen Sie einen Pandas Datenframe mit hilfe der gegebenen 3 Numpy array. Der  array "data" ist eine Matrix fuer die Daten.
Array "ind" sind die Indizies
Array "col" sind die Spalten Namen 
"""
import numpy as np
data =np.array([[3,4,5],[4,5,3],[3,1,5]])
ind= np.array([1,2,3])
col= np.array(["a","b","c"])

#Aufgabe 3
""" Erstellen Sie den gleichen Pandas Dataframe wie in Aufgabe 2, aber definieren
sie nicht den Index und Spaltennamen. Loeschen Sie dazu das Feld "index" und "column" aus der Dataframe Definition.
Welche Werte nemhen der Index und Spaltennamen ein?
"""


#Aufgabe 4
""" Erstellen Sie einen Pandas Dataframe mit der Hilfe des Dictionaries. 
Achten Sie darauf welcher Spaltenbezeichnung genommen wird, obwohl wir keine Spalten bezeichnung definiert haben.
"""

data = {'Country': ['Belgium', 'India', 'Brazil'], 'Capital': ['Brussels', 'New Delhi', 'Brasilia'],'Population': [11190846, 1303171035, 207847528]}

#Aufgabe 5
""" Erstellen Sie einen aehnlichen Pandas Dataframe wie in Aufgabe 4 nur das Sie die Spaltenbezeichnung manuell aendern in ["Hauptstadt", "Land", "Einwohner"].
"""

# Aufgabe 6
"""Gegeben ist der unten stehende Pandas Dataframe. Speichern Sie die 2 letzten Spalten in einen neuen Pandas Dataframe, mit dem namen df_temp ab.
"""

data = {'Country': ['Belgium', 'India', 'Brazil'], 'Capital': ['Brussels', 'New Delhi', 'Brasilia'],'Population': [11190846, 1303171035, 207847528]}
df=pd.DataFrame(data, index=["a","b","c"])

# Aufgabe 7
"""Nehmen Sie den Dataframe von Aufgabe 6. Speichern Sie die 2 letzten Spalten und 2 letzten Reihen (also 2x2) in einen neuen Pandas Dataframe, mit dem namen df_temp2 ab.
"""


#Aufgabe 8
"""Nehmen Sie den Dataframe von Aufgabe 6. Loeschen Sie zunaechst die erste Zeile, danach die Letzte Spalte. Am schluss fuegen Sie eine neue Spalte hinzu mit dem Spaltennamen "Continent" und den Werten ["Asia","America"]
"""

#Aufgabe 9
"""Laden sie sich die Excel Datei census.xlsx runter und speichern Sie sie an einem beliebigen Ort
Importieren Sie Datei in einen Pandas Dataframe mit dem namen "df_census".
"""

#Aufgabe 10
"""Exportieren Sie den Pandas Dataframe "df_census" aus Aufgabe 10 in eine Excel Datei, mit einem anderen Namen (den Namen koennen Sie bestimmen). Nach dem Export oeffnen Sie die Datei. Welchen unterschied stellen Sie fest zu der Originaldatei census.xlsx?
"""

#Aufgabe 11
""" Verwenden Sie den Dataframe den Sie in Aufgabe 9 erstellt haben. Rufen Sie die untenstehende Zeile auf. Diese Reduziert den Dataframe. Bilden Sie den Mittelwert von der Spalte "CENSUS2010POP", und speichern Sie diesen in einer Variablen mit einem Namen Ihrer Wahl ab.
"""

df_red=df.iloc[0:10,4:8].append(df.iloc[500:510,4:8])

#Aufgabe 12
""" Verwenden Sie den Dataframe "df_red" den Sie in Aufgabe 11 erstellt haben. Sortieren Sie den Dataframe zuerst nach der Spalte "STNAME" und dann nach der Spalte "CENSUS2010POP". Speichern Sie den sortierten Dataframe unter den Namen df_sort ab.
"""

#Aufgabe 13
""" Verwenden Sie den Dataframe "df_red" den Sie in Aufgabe 11 erstellt haben. Filtern Sie die  Spalte "CENSUS2010POP" so das nur Eintraege uebrig bleiben die grosser als 50000 sind. Zusaetlich Filtern Sie noch die Spalte "COUNTY" so das nur Eintraege uebrig bleiben die grosser als 200 sind. Verwenden sie Boolesche Operatoren. Speichern Sie den gefilterten Dataframe unter den Namen df_filt ab.
"""

#Aufgabe 14
""" Verwenden Sie den Dataframe "df_red" den Sie in Aufgabe 11 erstellt haben. Gruppieren Sie die Daten auf die Spalte ["STNAME"] und bilden sie den Durchschnitt von jeder Gruppe. Speichern Sie den gefilterten Dataframe unter den Namen df_group ab.
"""


