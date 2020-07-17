from tkinter import *


class Application:
    def __init__(self, master=None):
        self.mainfont = ("Arial", "10")
        self.firstCont = Frame(master)
        self.firstCont["pady"] = 10
        self.firstCont.pack()

        self.secondCont = Frame(master)
        self.secondCont["padx"] = 20
        self.secondCont.pack()

        self.thirdCont = Frame(master)
        self.thirdCont["padx"] = 20
        self.thirdCont.pack()

        self.fourthCont = Frame(master)
        self.fourthCont["padx"] = 20
        self.fourthCont.pack()

        self.fifthCont = Frame(master)
        self.fifthCont["pady"] = 20
        self.fifthCont.pack()

        self.title = Label(self.firstCont, text="Entre com os dados")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.fixedLabel = Label(self.secondCont,
                                text="Taxa Fixa: ", font=self.mainfont)
        self.fixedLabel.pack(side=LEFT)

        self.fixed = Entry(self.secondCont)
        self.fixed["width"] = 30
        self.fixed["font"] = self.mainfont
        self.fixed.pack(side=LEFT)

        self.perparcelLabel = Label(self.thirdCont,
                                    text="Taxa por Parcela: ", font=self.mainfont)
        self.perparcelLabel.pack(side=LEFT)

        self.perparcel = Entry(self.thirdCont)
        self.perparcel["width"] = 30
        self.perparcel["font"] = self.mainfont
        self.perparcel.pack(side=LEFT)

        self.parcelsLabel = Label(self.fourthCont,
                                  text="Quantidade de Parcelas: ", font=self.mainfont)
        self.parcelsLabel.pack(side=LEFT)

        self.parcels = Entry(self.fourthCont)
        self.parcels["width"] = 30
        self.parcels["font"] = self.mainfont
        self.parcels.pack(side=LEFT)

        self.calculate = Button(self.fifthCont)
        self.calculate["text"] = "Calcular"
        self.calculate["font"] = ("Calibri", "8")
        self.calculate["width"] = 12
        self.calculate["command"] = self.mesure
        self.calculate.pack()

        self.messageLabel = Label(self.fifthCont,
                                  text="", font=self.mainfont)
        self.messageLabel.pack()

    def mesure(self):
        x = float(self.fixed.get())
        y = float(self.perparcel.get())
        z = 1
        message = [""]
        parcel = int(self.parcels.get())
        while z < parcel:
            a = (((1 + (x/100))*(1 + (y/100))**(z))-1)*100
            toappend = "Para {} Parcelas: {} % \n".format(z, a)
            message.append(toappend)
            print("For ", z, " Parcels: ", a, "%")
            z = z + 1
        self.messageLabel["text"] = message


root = Tk()
Application(root)
root.mainloop()
