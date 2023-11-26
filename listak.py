


import random

#Listák, ciklusok, programozási tételek


nyertesSzamok = []

for i in range(0,5,1):
	randomSzam = random.randint(1,100)
	if randomSzam in nyertesSzamok:
		pass
	else:
		nyertesSzamok.append(randomSzam)



def NyertesSzamok():
	return nyertesSzamok










# Nézzük meg a lottószámok átlagát
def LottoAtlag():
	osszeg = 0
	for szam in nyertesSzamok:
		osszeg += szam
	atlag = osszeg / 5
	return atlag









# Hány 50-nél nagyobb szám van közte
def OtvennelNagyobb():
	szamlalo = 0
	for szam in nyertesSzamok:
		if szam > 50:
			szamlalo += 1
	return szamlalo









# Melyik a legnagyobb szám 
def Legnagyobb():
	legnagyobb = 0
	for szam in nyertesSzamok:
		if szam > legnagyobb:
			legnagyobb = szam
	return legnagyobb












# Hányadiknak generáltuk a a legnagyobb számot
def LegnagyobbIndexe():
	index = nyertesSzamok.index(max(nyertesSzamok)) + 1
	return index










# Melyik a legkisebb szám 
def Legkisebb():
	legkisebb = min(nyertesSzamok)
	return legkisebb










# A legkisebb és a legnagyobb szám közti különbség
def NagyKicsiKulonbseg():
	kulonbseg = max(nyertesSzamok) - min(nyertesSzamok)
	return kulonbseg










# Kérj be a felhasználótól egy számot, és döntsd el, hogy szerepel -e a szám a húzott számok között 
def SzamBekeres():
	valasz = "nincs benne"
	bekert = int(input("Kérek egy egész számot: "))
	for szam in nyertesSzamok:
		if bekert == szam:
			valasz = "benne van"
	return valasz






#NEHEZEK
# Kérj be a felhasználótól 5 számot, és döntsd el, hogy van-e találata
def OtszorBekeres():
	bekertLista = []
	talalat = "Nincs találat"

	for szam in range(0,5,1):
		bekert = int(input("Kérek egy egész számot: "))
		bekertLista.append(bekert)

	for szam in nyertesSzamok:
		for bekert in bekertLista:
			if szam == bekert:
				talalat = "Van találat"

	return talalat






# Kérj be a felhasználótól 5 számot, és a program mondja meg, hány találata van az illetőnek
def HanyTalalat():
	bekertLista = []
	talalatLista = 0

	for szam in range(0,5,1):
		bekert = int(input("Kérek egy egész számot: "))
		bekertLista.append(bekert)

	for szam in nyertesSzamok:
		for bekert in bekertLista:
			if szam == bekert:
				talalatLista += 1

	return talalatLista









# A húzott véletlen számok ne lehessenek azonosak!
# alapbol ugy irtam a kód elején







# A felhasználótól addig kérd be a számokat, amíg 5 különbözőt ad meg!
def KulonbozoBekeres():
	bekert = 0
	bekertLista = []

	while bekert != 5:
		szam = int(input("Kérek egy egész számot: "))
		if szam not in bekertLista:
			bekertLista.append(szam)
			bekert += 1
	return bekertLista







































