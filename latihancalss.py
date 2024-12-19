class orang:
    #variabel
    #nama =""
    #usia = 0
    #jekel =""

    def __init__(self, nama, usia, jekel):
        self.nama = nama
        self.usia = usia
        self.jekel =jekel
        
    #fungsi (method)
    def berjalan(self):
        print("saya berjalan")

    def ngomong(self, kata):
        print("saya berbicara", kata)

#objek1
#supir = orang()
#print(supir.nama)
#supir.berjalan()
#supir.ngomong("jalan yuk")
