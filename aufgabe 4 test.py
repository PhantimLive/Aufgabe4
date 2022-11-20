from pathlib import Path

working_directory = Path(__file__).absolute().parent

wartezeit2 = 0
anfang2 = 0
ende1 = 0
ende2 = 0
bearbeitungszeit = 0
anfangbearbeitung2 = 0
wartezeitlst = []
i = 0

def average(x):
    print(f"Durchschnittliche Wartezeit in Minuten: {(sum(x) / len(x))}")

with open('C:/Users/firep/OneDrive/Desktop/Bwinf/Aufgabe4/fahrradwerkstatt3.txt') as beispiel:
    lines = [line.rstrip() for line in beispiel]

print(lines)

while i < len(lines):
    for line in lines:
        if line.strip():
            split1 = lines[i].split()
            if i == 0:
                anfang2 = int(split1[0])
                bearbeitungszeit = int(split1[1])
                ende2 = anfang2 + bearbeitungszeit
                wartezeit2 = ende2 - anfang2
                ende1 = ende2
            else:
                anfang2 = int(split1[0])
                bearbeitungszeit = int(split1[1])
                if ende1 < anfang2:
                    anfangbearbeitung2 = anfang2
                else:
                    anfangbearbeitung2 = ende1
                ende2 = anfangbearbeitung2 + bearbeitungszeit
                wartezeit2 = ende2 - anfang2
                ende1 = ende2
            wartezeitlst.append(wartezeit2)
            i = i + 1
        else:
            i = i + 1

print(wartezeitlst)
average(wartezeitlst)
print(max(wartezeitlst))