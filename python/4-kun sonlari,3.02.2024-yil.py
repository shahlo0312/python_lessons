narh = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False
if choy:
    print("Mijoz choy oldi")
    narh = narh + 3000
if salat:
    print("Mijoz salat oldi")
    narh = narh + 5000
if non:
    print("Mijoz non oldi")
    narh = narh + 2500
if kompot:
    print("Mijoz kompot oldi")
    narh = narh + 7000
if assorti:
    print("Mijoz assorti oldi")
    narh = narh + 12000
print(f"Jami {narh} narh")
