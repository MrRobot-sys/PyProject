import dialog
from tkinter import *
from Plotting import Graphics
#from dialog import DialogWindows

global window, COUNTFUNCTIONS
window = Tk()
COUNTFUNCTIONS = 16
graph = Graphics()
#dialogWin = DialogWindows()


def Screen():
    # Widget initialization
    # Inscriptions with numbering
    lbl_title = Label(window, relief='groove', width=30)
    lbls = []
    for i in range(COUNTFUNCTIONS):
        lbls.append(Label(window, relief='groove', width=3))
    # Buttons with functions
    btns = []
    for i in range(COUNTFUNCTIONS):
        btns.append(Button(window, width=15))

    # Accommodation
    lbl_title.grid(row=1, column=1, columnspan=2)
    for i in range(COUNTFUNCTIONS):
        lbls[i].grid(row=(i + 2), column=1)
    for i in range(COUNTFUNCTIONS):
        btns[i].grid(row=(i + 2), column=2)

    # Constants
    window.title('Стандартные графики функций')
    lbl_title.configure(text='Выберите функцию из списка')
    for i in range(COUNTFUNCTIONS):
        lbls[i].configure(text=f'{i + 1}')
    btns[0].configure(text='f(x) = x')
    btns[1].configure(text='f(x) = |x|')
    btns[2].configure(text='f(x) = x^2')
    btns[3].configure(text='f(x) = x^3')
    btns[4].configure(text='f(x) = 1 / x')
    btns[5].configure(text='f(x) = x^(1/2)')
    btns[6].configure(text='f(x) = exp^x')
    btns[7].configure(text='f(x) = ln(x)')
    btns[8].configure(text='f(x) = sin(x)')
    btns[9].configure(text='f(x) = cos(x)')
    btns[10].configure(text='f(x) = tg(x)')
    btns[11].configure(text='f(x) = ctg(x)')
    btns[12].configure(text='f(x) = arcsin(x)')
    btns[13].configure(text='f(x) = arccos(x)')
    btns[14].configure(text='f(x) = arctg(x)')
    btns[15].configure(text='f(x) = arcctg(x)')

    btns[0].configure(command=dialog.X)
    btns[1].configure(command=graph.AbsX)
    btns[2].configure(command=graph.SqrX)
    btns[3].configure(command=graph.CubeX)
    btns[4].configure(command=graph.DivisionX)
    btns[5].configure(command=graph.SqrtX)
    btns[6].configure(command=graph.ExpX)
    btns[7].configure(command=graph.LnX)
    btns[8].configure(command=graph.SinX)
    btns[9].configure(command=graph.CosX)
    btns[10].configure(command=graph.TanX)
    btns[11].configure(command=graph.CtgX)
    btns[12].configure(command=graph.ArcsinX)
    btns[13].configure(command=graph.ArccosX)
    btns[14].configure(command=graph.ArctgX)
    btns[15].configure(command=graph.ArcctgX)

    # Handling window events
    window.mainloop()


def Main():
    Screen()
    pass


if __name__ == '__main__':
    Main()
