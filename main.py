from tkinter import *
from tkinter import messagebox
from NaiveBayesClassifier import NaiveBayesClassifier

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.__trainer = NaiveBayesClassifier()
        self.__create_widgets()
        self.grid(column=0,row=0, sticky=('n', 'w', 'e', 's') )
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.pack(pady = 15, padx = 15)
        self.pack()

    def __create_widgets(self):
        # insert Luas Bangunan
        Label(self, text="Luas Bangunan").grid(row=0, sticky='w', padx = 4, pady = 4)
        LB = Entry(self)
        LB.grid(row=0, column=2, sticky="e", padx = 4, pady = 4)

        # insert Bahan Bakar Memasak
        Label(self, text="Bahan Bakar Memasak").grid(row=1, sticky='w', padx = 4, pady = 4)
        BBM_choices = {'kayu bakar', 'gas lpg', 'kompor listrik'}
        BBM = StringVar(self)
        BBM.set('kayu bakar')
        BBM_options = OptionMenu(self, BBM, *BBM_choices)
        BBM_options.grid(row = 1, column = 2, sticky="w", padx = 4, pady = 4)

        # insert Jenis Lantai
        Label(self, text="Jenis Lantai").grid(row=2, sticky='w')
        JL_choices = {'ubin', 'plester', 'tanah'}
        JL = StringVar(self)
        JL.set('ubin')
        JL_options = OptionMenu(self, JL, *JL_choices)
        JL_options.grid(row=2, column=2, sticky="w", padx = 4, pady = 4)

        # insert Frekuensi Makan Daging
        Label(self, text="Frekuensi Makan Daging").grid(row=3, sticky='w', padx = 4, pady = 4)
        FMD = Entry(self)
        FMD.grid(row=3, column=2, sticky="e", padx = 4, pady = 4)

        # Get class button
        button = Button(self, text='Tentukan Class', fg="green", command=lambda: self.__generateClass(LB.get(), BBM.get(), JL.get(), FMD.get()))
        button.grid(row=5, column = 2, sticky="e", ipady=5)

    def __generateClass(self, LB, BBM, JL, FMD):
        try:
            LB = float(LB)
            FMD = float(FMD)
        except:
            self.__alert("Input Error", "Luas Bangunan dan Frekuensi Makan Daging harus diisi beruapa angka")
        result = self.__trainer.getClassOf([LB, BBM, JL, FMD])
        content = ""
        for index, key in enumerate(result):
            content += str(key) + ": " + str(result[key]) + "\n"
        self.__alert(title="Class", content= "Hasil klasifikasi\n"+ content)

    def __alert(self, title = "Warning", content = "Something went wrong"):
        messagebox.showinfo(title, content)

root = Tk()
root.title("Naive Bayes Classification")
app = Application(master=root)
app.mainloop()
