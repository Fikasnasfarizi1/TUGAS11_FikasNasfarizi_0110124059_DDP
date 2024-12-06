class gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak(self):

        print(f"ada gempa baru, lokasinya di{self.lokasi}")
        print(f"skala dari gempa ini adalah{self.skala}")
        if self.skala <= 2:
            print("Dampak tidak terasa")
        elif self.skala >= 2 and self.skala <=4:
            print("Dampak bangunan retak-retak")
        elif self.skala > 4 and self.skala <=6:
            print("Dampak gempa bangunan roboh")
        elif self.skala > 6 :
            print("Dampak gempa bangunan roboh juga potensi tsunami!")
        else :
            print("sistem error. tidak dapat dibaca")
