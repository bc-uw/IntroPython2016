import os

for i in os.listdir():
    print i

with open("file.txt", rb) as source:
    with open("file2.txt", wb) as dest:
        for line in source:
            dest.write(line)

with open("students.txt") as students:
          langlist = []
          students.readline()
          for line in students:
                  langs = line.rsplit(':')[1]
                  langlist.append(langs)
          strippedlist = [i.strip().replace(',', ' ').replace('and', ' ').split() for i in langlist]
          uniqueset = set(noquotelist)
