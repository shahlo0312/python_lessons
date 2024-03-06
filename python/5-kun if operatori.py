mahsulot = ["ketmon", "lapatka", "dazmol", "likopcha", "kosa", "tabaq", "qozon", "kapkir", "qoshiq", "vilka", "chashka"]
savat = []
print("Mahsulot kiriting")
for soro in range(0,5):
    savat.append(input(f"{soro+1}-mahsulotingizni kiriting>>>"))
print(savat)
for sor in savat:
    if sor in mahsulot:
        print(f"Bu {sor} mahsuloti mavjud")
    else:
        print("Mavjud emas")                   
