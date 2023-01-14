class Film:
    def __init__(self, sorok):
        self.cim = sorok[0]
        self.rendezo = sorok[1]
        self.foszereplo = sorok[2]
        self.ev = int(sorok[3])
        self.perc = int(sorok[4])