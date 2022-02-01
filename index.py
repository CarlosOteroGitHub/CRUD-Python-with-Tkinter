import sys
import winsound
from tkinter import *
from tkinter import messagebox

class CuentaUsuario:

    def __init__(self, id_usuario, nombre, constrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.constrasena = constrasena

    def get_idUsuario(self):
        return self.id_usuario

    def set_idUsuario(self, id_usuario):
        self.id_usuario=id_usuario

    def get_Nombre(self):
        return self.nombre

    def set_Nombre(self, nombre):
        self.nombre=nombre
        
    def get_Contrasena(self):
        return self.constrasena

    def set_Contrasena(self, constrasena):
        self.constrasena=constrasena

class Login:
    
    def __init__(self, frame):
        self.frame = frame
        frame.title("Login")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x370")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.lista = []
        self.lista.append(CuentaUsuario(1, "admin", "admin123"))
        self.lista.append(CuentaUsuario(2, "user1", "123"))
        self.lista.append(CuentaUsuario(3, "user2", "123"))

        self.img1 = PhotoImage(file="F:\\xampp\\htdocs\\AppPersonal\\My Folders\\Programming\\2. Desarrollo de Proposito General\\2. Python\\9. Programas Finales\\2. Programación Visual\\login.png")
        self.label1 = Label(frame, text="", image=self.img1)
        self.label1.place(x=102, y=5, width=241, height=86)
        self.label1.configure(background='white')

        self.label2 = Label(frame, text="Email*")
        self.label2.place(x=160, y=110, width=130, height=30)
        self.label2.configure(background='white')

        self.label3 = Label(frame, text="Contraseña*")
        self.label3.place(x=160, y=190, width=130, height=30)
        self.label3.configure(background='white')

        self.entry1 = Entry(frame)
        self.entry1.place(x=100, y=140, width=250, height=30)

        self.entry2 = Entry(frame, show="*")
        self.entry2.place(x=100, y=220, width=250, height=30)

        self.img2 = PhotoImage(file="F:\\xampp\\htdocs\\AppPersonal\\My Folders\\Programming\\2. Desarrollo de Proposito General\\2. Python\\9. Programas Finales\\2. Programación Visual\\acep_norm.png")
        self.button1 = Button(frame, text="Aceptar", image=self.img2, command=self.aceptar)
        self.button1.place(x=50, y=280, width=103, height=35)

        self.img3 = PhotoImage(file="F:\\xampp\\htdocs\\AppPersonal\\My Folders\\Programming\\2. Desarrollo de Proposito General\\2. Python\\9. Programas Finales\\2. Programación Visual\\canc_norm.png")
        self.button2 = Button(frame, text="Aceptar", image=self.img3, command=self.salir)
        self.button2.place(x=260, y=280, width=103, height=35)

    def sonido(tono):
        winsound.PlaySound('F:\\xampp\\htdocs\\AppPersonal\\My Folders\\Programming\\2. Desarrollo de Proposito General\\2. Python\\9. Programas Finales\\2. Programación Visual\\' + tono, winsound.SND_FILENAME) 

    def busquedaID(self, nombre, contrasena):
        row = 0
        bandera = False
        for i in range(0, len(self.lista), 1):
            if(nombre == self.lista[i].get_Nombre() and contrasena == self.lista[i].get_Contrasena()):
                row = i
                bandera = True

        if bandera != False:
            row = self.lista[row].get_idUsuario()
        return row

    def aceptar(self):
        if len(self.entry1.get()) == 0 and len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Campos de Texto Vacios")
        elif len(self.entry1.get()) == 0 or len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Uno de los Campo de Texto está Vacio")
        else:
            id_obtain = self.busquedaID(self.entry1.get(), self.entry2.get())
            if(id_obtain != 0):
                if(self.entry1.get() == self.lista[id_obtain-1].get_Nombre() and self.entry2.get() == self.lista[id_obtain-1].get_Contrasena()):
                    if self.lista[id_obtain-1].get_Nombre() == "admin" and self.lista[id_obtain-1].get_Contrasena() == "admin123":
                        Login.sonido("login.wav")
                        self.frame.destroy()
                        objeto = Tk()
                        Admin(objeto, self.lista)
                        objeto.mainloop()
                    else:
                        Login.sonido("login.wav")
                        self.frame.destroy()
                        objeto = Tk()
                        Usuario(objeto, id_obtain, self.lista)
                        objeto.mainloop()
            else:
                Login.sonido("error.wav")
                messagebox.showwarning("Mensaje de Advertencia", "Cuenta de Usuario no Encontrada")


    def salir(self):
        choise = messagebox.askquestion("Salír", "¿Estas seguro de salír?")
        if choise == 'yes':
            sys.exit()


class Admin:

    def __init__(self, frame, lista = []):
        self.frame = frame
        self.lista = lista
        frame.title("Administrador")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x370")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.img1 = PhotoImage(file="F:\\xampp\\htdocs\\AppPersonal\\My Folders\\Programming\\2. Desarrollo de Proposito General\\2. Python\\9. Programas Finales\\2. Programación Visual\\administrador.png")
        self.label1 = Label(frame, text="", image=self.img1)
        self.label1.place(x=-20, y=30, width=240, height=200)
        self.label1.configure(background='white')

        self.label2 = Label(frame, text="Administrador")
        self.label2.place(x=220, y=100, width=240, height=35)
        self.label2.configure(background='white')
        self.label2.config(font=("Tahoma", 25))

        self.button1 = Button(frame, text="Mostrar Cuentas de Usuario", command=self.mostrarCuentas)
        self.button1.place(x=100, y=240, width=250, height=35)

        self.button2 = Button(frame, text="Agregar Cuenta de Usuario", command=self.agregarCuenta)
        self.button2.place(x=100, y=290, width=250, height=35)

        self.menu1 = Menu(frame)
        self.menuBar1 = Menu(self.menu1, tearoff=0)
        self.menuBar1.add_command(label="Salír", command=self.salir)
        self.menu1.add_cascade(label="Archivo", menu=self.menuBar1)
        frame.config(menu=self.menu1)

    def mostrarCuentas(self):
        mensaje=""
        for i in range(1, len(self.lista), 1):
            mensaje+="\nNombre: " + self.lista[i].get_Nombre() + " y Constraseña: " + self.lista[i].get_Contrasena()
        messagebox.showwarning("Mensaje de Información", "Las Cuentas de Usuario del Sistema se Muestran a Continuación: " + mensaje)

    def agregarCuenta(self):
        self.frame.destroy()
        objeto = Tk()
        AgregarUsuario(objeto, self.lista)
        objeto.mainloop()

    def salir(self):
        choise = messagebox.askquestion("Salír", "¿Estas seguro de salír?")
        if choise == 'yes':
            sys.exit()


class AgregarUsuario:

    def __init__(self, frame, lista = []):
        self.frame = frame
        self.lista = lista
        frame.title("Agregar Usuario")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x300")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.label1 = Label(frame, text="Email*")
        self.label1.place(x=150, y=10, width=130, height=30)
        self.label1.configure(background='white')

        self.entry1 = Entry(frame)
        self.entry1.place(x=90, y=40, width=250, height=30)

        self.label2 = Label(frame, text="Contraseña*")
        self.label2.place(x=150, y=90, width=130, height=30)
        self.label2.configure(background='white')

        self.entry2 = Entry(frame, show="*")
        self.entry2.place(x=90, y=120, width=250, height=30)

        self.button1 = Button(frame, text="Agregar Usuario", command=self.agregarUsuario)
        self.button1.place(x=90, y=180, width=250, height=35)

        self.menu1 = Menu(frame)
        self.menuBar1 = Menu(self.menu1, tearoff=0)
        self.menuBar1.add_command(label="Regresar", command=self.regresar)
        self.menu1.add_cascade(label="Archivo", menu=self.menuBar1)
        frame.config(menu=self.menu1)

    def busquedaUsuario(self, cadena):
        bandera = False
        for i in range(0, len(self.lista), 1):
            if(cadena == self.lista[i].get_Nombre()):
                bandera = True
                break
        return bandera

    def agregarUsuario(self):
        if len(self.entry1.get()) == 0 and len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Campos de Texto Vacios")
        elif len(self.entry1.get()) == 0 or len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Uno de los Campo de Texto está Vacio")
        else:
            if(self.busquedaUsuario(self.entry1.get()) == True):
                Login.sonido("error.wav")
                messagebox.showerror("Mensaje de Advertencia", "Ya Existe la Cuenta de Usuario.")
            else:
                self.lista.append(CuentaUsuario(3, self.entry1.get(), self.entry2.get()))
                Login.sonido("add.wav")
                self.frame.destroy()
                objeto = Tk()
                Admin(objeto, self.lista)
                objeto.mainloop()

    def regresar(self):
        self.frame.destroy()
        objeto = Tk()
        Admin(objeto, self.lista)
        objeto.mainloop()


class Usuario:

    def __init__(self, frame, id_usuario, lista = []):
        self.frame = frame
        self.lista = lista
        self.id_usuario = id_usuario
        frame.title("Usuario")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x370")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.img1 = PhotoImage(file="F:\\xampp\\htdocs\\AppPersonal\\My Folders\\Programming\\2. Desarrollo de Proposito General\\2. Python\\9. Programas Finales\\2. Programación Visual\\usuario.png")
        self.label1 = Label(frame, text="", image=self.img1)
        self.label1.place(x=10, y=10, width=180, height=180)
        self.label1.configure(background='white')

        self.label2 = Label(frame, text=self.lista[id_usuario-1].get_Nombre())
        self.label2.place(x=220, y=100, width=240, height=35)
        self.label2.configure(background='white')
        self.label2.config(font=("Tahoma", 25))

        self.button1 = Button(frame, text="Editar mis Datos", command=self.editarCuenta)
        self.button1.place(x=100, y=210, width=250, height=35)

        self.menu1 = Menu(frame)
        self.menuBar1 = Menu(self.menu1, tearoff=0)
        self.menuBar1.add_command(label="Salír", command=self.salir)
        self.menu1.add_cascade(label="Archivo", menu=self.menuBar1)
        frame.config(menu=self.menu1)

    def editarCuenta(self):
        self.frame.destroy()
        objeto = Tk()
        EditarUsuario(objeto, self.id_usuario, self.lista)
        objeto.mainloop()

    def salir(self):
        choise = messagebox.askquestion("Salír", "¿Estas seguro de salír?")
        if choise == 'yes':
            sys.exit()


class EditarUsuario:

    def __init__(self, frame, id_usuario, lista = []):
        self.frame = frame
        self.lista = lista
        self.id_usuario = id_usuario
        frame.title("Editar Usuario")
        frame.configure(background='white')
        frame.resizable(False, False)
        frame.geometry("450x300")
        frame.update_idletasks() 
        w = frame.winfo_screenwidth() 
        h = frame.winfo_screenheight() 
        size = tuple(int(_) for _ in frame.geometry().split('+')[0].split('x')) 
        x = w/2 - size[0]/2 
        y = h/2 - size[1]/2 
        frame.geometry("%dx%d+%d+%d" % (size + (x, y)))

        self.label1 = Label(frame, text="Email*")
        self.label1.place(x=150, y=10, width=130, height=30)
        self.label1.configure(background='white')

        self.entry1 = Entry(frame)
        self.entry1.place(x=90, y=40, width=250, height=30)

        self.label2 = Label(frame, text="Contraseña*")
        self.label2.place(x=150, y=90, width=130, height=30)
        self.label2.configure(background='white')

        self.entry2 = Entry(frame, show="*")
        self.entry2.place(x=90, y=120, width=250, height=30)

        self.button1 = Button(frame, text="Editar Usuario", command=self.editarUsuario)
        self.button1.place(x=90, y=180, width=250, height=35)

        self.menu1 = Menu(frame)
        self.menuBar1 = Menu(self.menu1, tearoff=0)
        self.menuBar1.add_command(label="Regresar", command=self.regresar)
        self.menu1.add_cascade(label="Archivo", menu=self.menuBar1)
        frame.config(menu=self.menu1)

    def busquedaUsuario(self, cadena):
        bandera = False
        for i in range(0, len(self.lista), 1):
            if(cadena == self.lista[i].get_Nombre()):
                bandera = True
                break
        return bandera

    def editarUsuario(self):
        if len(self.entry1.get()) == 0 and len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Campos de Texto Vacios")
        elif len(self.entry1.get()) == 0 or len(self.entry2.get()) == 0:
            messagebox.showwarning("Mensaje de Advertencia", "Uno de los Campo de Texto está Vacio")
        else:
            if(self.busquedaUsuario(self.entry1.get()) == True):
                Login.sonido("error.wav")
                messagebox.showerror("Mensaje de Advertencia", "Ya Existe la Cuenta de Usuario.")
            else:
                self.lista[self.id_usuario-1].set_Nombre(self.entry1.get())
                self.lista[self.id_usuario-1].set_Contrasena(self.entry2.get())
                Login.sonido("add.wav")
                self.frame.destroy()
                objeto = Tk()
                Usuario(objeto, self.id_usuario, self.lista)
                objeto.mainloop()

    def regresar(self):
        self.frame.destroy()
        objeto = Tk()
        Usuario(objeto, self.id_usuario, self.lista)
        objeto.mainloop()


class MainClass:
    objeto = Tk()
    Login(objeto)
    objeto.mainloop()


"""

Programa Visual que Gestiona las Cuentas de Usuarios desde una Cuenta Administrador.

"""