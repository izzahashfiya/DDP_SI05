from Gempa import *

#membuat objek gempa dengan lokasi dan skala
#objek1
gempa1 = Gempa("Banten", 1.2)

#info gempa1
print("## gempa bumi info ##")
print()
gempa1.dampak() #memanggil method dampak()

#objek2
gempa2 = Gempa("Palu", 6.1)

#info gempa2
print("## gempa bumi info")
print()
gempa2.dampak() #memanggil method dampak()

#objek3
gempa3 = Gempa("Cianjur", 5.6)

#info gempa3
print("## gempa bumi info ##")
print()
gempa3.dampak() #memanggil method dampak()

#objek4
gempa4 = Gempa("Jayapura", 3.3)

#info gempa4
print("## gempa bumi info ##")
print()
gempa4.dampak() #memanggil method dampak()

#objek5
gempa5 = Gempa("Garut", 4.0)

#info gempa5
print("## gempa bumi info ##")
print()
gempa5.dampak() #memanggil method dampak()