from pathlib import Path

working_directory = Path(__file__).absolute().parent

wartezeit2 = 0
anfang2 = 0
ende1 = 0
ende2 = 0
anfangbearbeitung2 = 0
lst = []
i = 0

#function um durchschnitt einer Liste zu berechnen
def average(x):
    print(f"Durchschnittliche Wartezeit in Minuten: {(sum(x) / len(x))}")

#Datei öffnen
with open('C:/Users/firep/OneDrive/Desktop/Bwinf/Aufgabe4/fahrradwerkstatt0.txt') as beispiel:
    lines = [line.rstrip() for line in beispiel]

#anfang/ende 2 ist der Anfang/Ende des Auftrags von dem man die Wartezeit berechnet
#ende1 ist das Ende des vorherigen Auftrages
while i < len(lines):
    if i == 0:
        split1 = lines[i].split()
    else:
        split1 = lines[i-1].split()
    if i == 0:
        ende1 = int(split1[0])
    split2 = lines[i].split()
    if i == 0:
        anfang2 = int(split1[0])
    else:
        anfang2 = int(split2[0])
    if ende1 > anfang2:
        anfangbearbeitung2 = ende1
    else:
        anfangbearbeitung2 = anfang2
    if i == 0:
        ende2 = int(split1[1]) + anfangbearbeitung2
    else:
        ende2 = int(split2[1]) + anfangbearbeitung2
    wartezeit2 = ende2 - anfang2
    lst.append(wartezeit2)
    ende1 = ende2
    if lines[-1] == lines[i]:
        break
    i = i + 1


print(lst)
average(lst)