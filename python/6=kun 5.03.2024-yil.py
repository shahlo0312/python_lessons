mahsulotlar= ["pomidor", "bodiring", "kartoshka", "piyoz", "chesnok", "banan", "qozon"]
savat = []
print("bemalol hohlagan turdagi 5 ta mahsulotingizni kiriting, do`kon mahsulotlarini")
for i in range(5):
    savat.append(input(f"{i+1}-mahsulotingizni kiriting: "))

bor_mahsulotlar = []
mavjud_emas = []
for j in savat:
    if j in mahsulotlar:
        bor_mahsulotlar.append(j)
    else:
        mavjud_emas.append(j)
if bor_mahsulotlar in mahsulotlar:
    print(f"Ha albatta, bunday mahsulotlarimiz {bor_mahsulotlar} do`konda mavjud")
else:
    print(f"Uzr bizni kechiring, bu mahsulotlar {mavjud_emas mavjud emas ekan")
