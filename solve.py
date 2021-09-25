from tkinter import Tk, Label, Button, Entry, Frame
from tkinter.ttk import Combobox
import math

size_modifier = 0.5
method_names = ["Middle Rect", "Left Rect", "Right Rect", "Simpson"]


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#a = float(eval(input('Введите а = ')))
#b = float(eval(input('Введите b = ')))
#eps = float(eval(input('Введите eps = ')))

def f(x):
	return math.exp(x)

def fEnter(fStr, x):
	if (fStr == 'f'): 
		return f(x)
	else:
		return float(eval(fStr.replace("x",str(x))))

def middleRect(A, h, N, funcF, fStr):
	ans = 0
	for i in range(0, N):
		ans += funcF(fStr, A + h/2 + h*i)
	return ans*h

def leftRect(A, h, N, funcF, fStr):
	ans = 0
	for i in range(0, N):
		ans += funcF(fStr, A + h*i)
	return ans*h

def rightRect(A, h, N, funcF, fStr):
	ans = 0
	for i in range(0, N):
		ans += funcF(fStr, A + h + h*i)
	return ans*h
    
def fSimpson(A, h, N, funcF, fStr):
	ans = 0
	for i in range(0, N):
		ans += funcF(fStr, (A + h*i)) + 4*funcF(fStr,(A + h/2 + h*i)) + funcF(fStr,(A + h + h*i))
	return ans*h/6


methods = {
    'Middle Rect':[middleRect, 2], 
    'Left Rect':[leftRect, 1], 
    'Right Rect':[rightRect, 1],
    'Simpson':[fSimpson, 3]
    }


def getR(q1, q2,  m):
	return (q2 - q1)/(1-1/pow(2, m+1))

def getIntegral(A, B, Eps, methFunct, funcF, fStr):
    h1 = B - A
    n = 1
    q1 = methFunct[0](A, h1, n, funcF, fStr)
    print('--------------------')
    print('\n• step 1:')
    print('q1')
    print(q1)
    R = 1
    i = 1
    while abs(R)>Eps:
        i += 1
        print('\n• step ' + str(i) + ':')
        h1 = h1/2
        n = n*2
        q2 = methFunct[0](A, h1, n, funcF, fStr)
        print('q2')
        print(q2)
        R = getR(q1, q2, methFunct[1])
        print('N = ')
        print(n)
        print('R = ')
        print(R)
        print('I = ')
        print(q1+R)
        q1 = q2
    return toFixed(q1+R, len(str(Eps))-1)

#getIntegral(a, b, eps)

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title_label = Label(self, bd=40*size_modifier, text="A simple approximation Integral finder " + chr(8747)) 
        self.title_label.pack()

        self.methFrm = Frame(self)
        self.methFrm.pack()
        Label(self.methFrm, bd=5*size_modifier, text="Method: ").pack(side='left')
        self.methCombo = Combobox(self.methFrm, values=method_names)
        self.methCombo.pack(side='left')
        self.methCombo.current(0)


        self.iEnterFrm = Frame(self, bd=40*size_modifier)
        self.iEnterFrm.pack()
        self.iFrm = Frame(self.iEnterFrm, bd=30*size_modifier)
        self.iFrm.pack(side='left')
        self.funcEntry = Entry(self.iEnterFrm)
        self.funcEntry.pack(side='left')
        self.funcEntry.insert(0, "x")
        self.aFrm = Frame(self.iFrm, bd=4*size_modifier)
        self.bFrm = Frame(self.iFrm, bd=4*size_modifier)

        Label(self.bFrm, text='b = ').pack(side='left')
        self.bEntry = Entry(self.bFrm, width=5)
        self.bEntry.pack(side='left')
        self.bEntry.insert(0, "1")
        self.bFrm.pack(side='top')

        Label(self.iFrm, text=chr(8747), font="Times 17").pack(side = 'top')

        Label(self.aFrm, text='a = ').pack(side='left')
        self.aEntry = Entry(self.aFrm, width=5)
        self.aEntry.pack(side='top')
        self.aEntry.insert(0, "0")
        self.aFrm.pack(side='top')

        self.epsFrm = Frame(self, bd=4*size_modifier)
        Label(self.epsFrm, font="Times 8", text='eps = ').pack(side='left')
        self.epsEntry = Entry(self.epsFrm, width=7)
        self.epsEntry.pack(side='left')
        self.epsFrm.pack()
        self.epsEntry.insert(0, "0.001")

        self.label = Label(self, text="")
        self.label.pack()
        self.button = Button(self, text="Compute", bd = 20*size_modifier, command=self.onclick)
        self.button.pack()

    def onclick(self):
        func = self.funcEntry.get()
        print('\n--------------------')
        print(self.methCombo.get())
        self.label.configure(text=str(getIntegral(float(self.aEntry.get()), float(self.bEntry.get()), float(self.epsEntry.get()), methods[self.methCombo.get()], fEnter, func)))


root = Root()
root.mainloop()