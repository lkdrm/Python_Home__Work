"""
count = 0
count_2 = 0
for i in range(100,999):
        a = i
        b = str(a)
        if b[0] == b[1] and b[1] == b[2]:
                print("All 3 values are same:",b,sep="\n")
                count+=1
        if b[1] == b[2]:
                print("All 2 values are same:",b,sep="\n")
                count_2+=1

print("All numbs which have 3 same values:",count)
print("All numbs which have only 2 same values:",count_2)
"""
count = 0

for i in range(100,999):
        a = i
        b = str(a)
        if b[0] != b[1] and b[1] != b[2] and b[2] != b[0]:
                count+=1

print("All values are:",count) 