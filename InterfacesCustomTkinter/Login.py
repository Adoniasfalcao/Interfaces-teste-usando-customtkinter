import customtkinter as ctk
import tkinter.messagebox as tkmb


def create_login():
    if usuario_entry.get().strip() == "":
        tkmb.showwarning(title="Aviso!",message="Campo usuário não pode ser vazio")

    elif senha_entry.get().strip() == "":
        tkmb.showwarning(title="Aviso!",message="Campo senha não pode ser vazio")

    else:
        tkmb.showinfo(title="Encerrado!",message="Logado com sucesso!")
        window.destroy()


#Configurações da janela
window = ctk.CTk()
window.title("Login page")
window.geometry("340x500")
window.resizable(0,0)


#Título
title_label = ctk.CTkLabel(window,text="Login",font=ctk.CTkFont(size=20,weight="bold"))
title_label.pack(padx=20,pady=(20,20))


#Frame principal
login_frame = ctk.CTkFrame(window,width=300,height=320,corner_radius=15)
login_frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)


#Texto do frame
frame_labeltext = ctk.CTkLabel(login_frame,text="Logar na sua conta")
frame_labeltext.place(x=100,y=10)


#Entrada de dados
usuario_entry = ctk.CTkEntry(login_frame, width=220, placeholder_text='Usuário')
usuario_entry.place(x=40, y=110)

senha_entry = ctk.CTkEntry(login_frame, width=220, placeholder_text='Senha',show="*")
senha_entry.place(x=40, y=140)


#Login
login_button = ctk.CTkButton(login_frame, width=220, text="Login", command=create_login, corner_radius=6)
login_button.place(x=40, y=240)


window.mainloop()
