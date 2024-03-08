---
marp: true
theme: uncover
_class: invert
---
<!-- paginate: true -->
# Python 🐍 Kurs für Anfänger
Jochen Leeder

---
# Was ist Python?
- Python ist eine hochgradig lesbare Programmiersprache.
- Sie ist einfach zu erlernen und vielseitig einsetzbar.
- Wird für Webentwicklung, Datenanalyse, KI und mehr verwendet.
---
# Warum Python?
- Klare, einfache Syntax, die die Programmierung verständlicher macht.
- Große Community und umfangreiche Bibliotheken.
- Plattformunabhängig: Läuft auf Windows, Mac und Linux.
---
# Python installieren
1. Gehe zu [python.org](https://python.org)
2. Lade den Installer für dein Betriebssystem herunter.
3. Führe den Installer aus und folge den Anweisungen.
---
# Dein erstes Python-Programm
- Öffne einen Texteditor.
- Schreibe:
 ```python
 print("Hallo Welt!")
 ```
- Speichere die Datei als `hallo.py`.
- Führe sie im Terminal mit `python hallo.py` aus.
---

# Variablen
- Speichern von Daten für die spätere Verwendung.
```python
# Variable als string
name = "Welt"  
# Variable als Integer damit kann man rechnen!
alter = 30     

print(name)
print(alter)
 ```
 ---
 # Grundlegende Datentypen
- Ganzzahlen (Integer) `5`
- Fließkommazahlen (Float) `5.7`
- Zeichenketten (Strings) `"Hallo Welt"`
- Boolesche Werte (Boolean) `"True" , "False"`

```python
a = 5 # Datentyp Integer (Damit kann man rechnen)
b = "5" #Datentyp String (damit kann man nicht rechnen)
c = "5.8" #Datentyp String (damit kann man nicht rechnen)
d = int(a) # jetzt kann man mit c rechnen , da der Datentyp geändert wurde!
e = float(b) # e ist jetzt eine Fließkommazahl, wichtig ist einen . zu setzen und kein Komma ,
bool_value_1 = True
bool_value_2 = False
```

---
# Operatoren
- Addition: `+`
- Subtraktion: `-`
- Multiplikation: `*`
- Division: `/`
---
# Beispiele zu Operatoren

```python
a = 5
b = 3
c = a + b

print (c)

d = a * b

print (d)

```
---
# Input Befehle

Der Input Befehl wird genutzt, wenn man User etwas eingeben soll
z.b. sein Alter?

```python

alter = int(input("Wie alt bist du?: "))

```

---
# Bedingungen
- `if`, `elif`, `else`
- Beispiel:
```python
if alter > 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")
```
---




