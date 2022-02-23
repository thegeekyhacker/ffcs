import re
nc = int(input("Enter number of courses : "))
courses = []
selectedslots = []
timetable ={}
ftimetable = {}
for i in range(nc):
    cname = input("Enter the course name : ")
    courses.append(cname)
    f = open(f"{cname}.txt","w")
    f.close()
print(courses)
for i in range(len(courses)):
    slots = []
    aslots = []
    mslots = []
    f1 = open(f"{courses[i]}.txt","w")
    sname = input(f"Enter the slots for {courses[i]} course : ")
    slots.append(sname)
    sname = sname.split(", ")
    for j in range(len(sname)):
        tname = input(f"Enter Faculty names for {courses[i]}'s {sname[j]} slot : ")
        f1.write(f"{sname[j]} :- {tname}\n")
    f1.flush()
    f1.close()
    for j in range(len(sname)):
        if '2' in sname[j]:
            aslots.append(sname[j])
        elif '1' in sname[j]:
            mslots.append(sname[j])
    for j in range(len(aslots)-1,-1,-1):
        x = 0
        if "+" in aslots[j]:
            aslots[j] = aslots[j].split("+")
            for l in aslots[j]:
                if any(l in word for word in selectedslots) == True:
                    x += 1
                    break
            else:
                selectedslots.append("+".join(aslots[j]))
                break
        else:
            if any(aslots[j] in word for word in selectedslots) == False:
                selectedslots.append(aslots[j])
                break
    timetable[courses[i]] = selectedslots[i]
    for c in timetable:
        fst = ''
        f2 = open(f"{c}.txt","r")
        data = f2.readlines()
        for a in data:
            if timetable[c] in a:
                a = a[len(timetable[c])+3:]
                a = a.split(", ")
                a.sort(key= lambda z : list(map(int, re.findall(r'\d+',z)))[0])
                st = a[-1]
                st = st.split(" - ")
                fst = st[0]
                break
        ftimetable[courses[i]] = selectedslots[i] + ' by :- ' + fst
print(ftimetable)