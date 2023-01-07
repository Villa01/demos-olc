class temp:
    contador = 1
    contador_labels = 1

    def __init__(self):
        self.C3D = ""
        self.TMP = "t"+str(temp.getContador())
 
    @classmethod
    def getContador(cls):
        return cls.contador

    def new_label_v(self):
        self.LV = ""
        self.LV += "L"+ str(temp.contador_labels) + " "
        temp.contador_labels += 1

    def new_label_f(self):
        self.LF = ""
        self.LF += "L"+ str(temp.contador_labels) + " "
        temp.contador_labels += 1

    @classmethod
    def nuevo_temp(cls):
        cls.contador += 1