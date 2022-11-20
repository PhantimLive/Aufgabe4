anfang2 = 0
bearbeitungszeit = 0
wartezeit2 = 0
ende1 = 0
ende2 = 0
anfangbearbeitung2 = 0
wartezeitlst = []
time = 0
time_day = 0
i = 0
x = 0
nextpossibleline = []
split2 = 0

def average(x):
    return(f"Durchschnittliche Wartezeit in Minuten: {(sum(x) / len(x))}")


with open('fahrradwerkstatt1.txt') as beispiel:
    lines = [lines.rstrip() for lines in beispiel]

split1 = lines[i].split()
anfang2 = int(split1[0])
bearbeitungszeit = int(split1[1])


while 1 == 1:
    if 540 <= time_day <= 1020:
        if anfang2 <= time:
            bearbeitungszeit = bearbeitungszeit - 1
    if bearbeitungszeit == 0:
        if lines[i] == lines[-1]:
            ende2 = time
            wartezeit2 = ende2 - anfang2
            wartezeitlst.append(wartezeit2)
            break
        else:
            ende2 = time
            wartezeit2 = ende2 - anfang2
            wartezeitlst.append(wartezeit2)
            x = i
            while 1 == 1:
                x = x + 1
                split2 = lines[x].split()
                if int(split2[0]) <= time:
                    nextpossibleline.append(split2[1])
                    print(nextpossibleline)
                    if lines[x] == lines[-1]:
                        break
                else:
                    break
            if len(nextpossibleline) > 0:
                y = i + nextpossibleline.index(min(nextpossibleline)) + 1
            else:
                i = i + 1
                split1 = lines[i].split()
                anfang2 = int(split1[0])
                bearbeitungszeit = int(split1[1])
                nextpossibleline.clear()
                continue
            split2 = lines[y].split()
            split2 = ' '.join(split2)
            lines.remove(split2)
            lines.insert(i, split2)
            i = i + 1
            split1 = lines[i].split()
            anfang2 = int(split1[0])
            bearbeitungszeit = int(split1[1])
            nextpossibleline.clear()
    if time_day == 1440:
        time_day = 0
    time_day = time_day + 1
    time = time + 1


print(wartezeitlst)
print(f"Durchschnittliche Wartezeit in Minuten: {(sum(wartezeitlst) / len(wartezeitlst))}")
print(max(wartezeitlst))
