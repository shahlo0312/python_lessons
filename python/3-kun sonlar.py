kun = input("Bugun qanday kun?>>>")
harorat = float(input("Havo harorati qanday?>>>"))
if kun.lower()=="shanba" or kun.lower()=="yakshanba" and harorat>=30:
    print("Ketdik cho`milishga")
elif kun.lower()=="yakshanba" and harorat<30:
    print("Uyda dam olamiz.")
 
