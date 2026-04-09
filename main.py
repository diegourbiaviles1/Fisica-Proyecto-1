import tkinter as tk
from Interfaz import AplicacionCoulomb

def main():
    raiz = tk.Tk()
    app = AplicacionCoulomb(raiz)
    raiz.mainloop()

if __name__ == "__main__":
    main()