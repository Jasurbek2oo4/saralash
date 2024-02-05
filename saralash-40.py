import random
ismlar = ["lutfullo", "hayrullo", "sayfullo", "rahmatullo", "murodillo", "saydullo","haydullo", "sofiya", "roziya", "oysha", "fotima", "dilafruz", "hadicha"]
familiyalar = ["akramov", "karimov", "a'zamov", "sultonov", "mirziyoyev", "nasrullayev", "bekmirzayev", "bekmurodov", "to'rayev"]
soni = 60

studentlar = []
for i in range(soni):
    ism = random.choice(ismlar)
    familiya = random.choice(familiyalar)
    ball = random.randint(57,189)
    student = {"ism":ism, "familiya":familiya, "ball":ball}
    studentlar.append(student)
# print(studentlar)

g1,g2,g3=[],[],[]

for student in studentlar:
    # print(student)
    # print(studentlar.pop())
    talaba = studentlar.pop()
    g1.append(talaba)
    talaba = studentlar.pop()
    g2.append(talaba)
    talaba = studentlar.pop()
    g3.append(talaba)

print(g1,"\n")
print(g2,"\n")
print(g3,"\n")