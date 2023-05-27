import customtkinter as ctk
import tkinter.messagebox as tkmb


#Lista com os objetos do tipo checkbox
check_box_list = []


def delete_task():
    
    try:
        check_box_list[-1].pack_forget()
        check_box_list.pop()

    except:
        tkmb.showwarning(title="Aviso!",message="Não foi possível apagar a tarefa")



def create_task():
    task = entry_data.get()
    
    if task.strip() != "":
        entry_data.delete(0,ctk.END)

        check_var = ctk.StringVar(value="off")
        checkbox = ctk.CTkCheckBox(scrollable_frame,text=task,variable=check_var,onvalue="on",offvalue="off",checkbox_height=18,checkbox_width=18) 
        checkbox.pack(padx=10)

        check_box_list.append(checkbox)
        
    else:
        tkmb.showwarning(title="Aviso!", message="O campo não pode ser vazio")
    


#Configurações da janela
window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.geometry("340x500")
window.resizable(0,0)
window.title("To-do app")


#Labels
title_label = ctk.CTkLabel(window,text="Tarefas",font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=20,pady=(40,20))


#Frame de scroll
scrollable_frame = ctk.CTkScrollableFrame(window,width=300,height=200)
scrollable_frame.pack()


#Botões
add_button = ctk.CTkButton(window,text="Adicionar",width=300,command=create_task)
add_button.pack(pady=10)

remove_button = ctk.CTkButton(window,text="Remover",width=300,hover_color="red",border_color="red",command=delete_task)
remove_button.pack()


#Entrada de dados
entry_data = ctk.CTkEntry(scrollable_frame,placeholder_text="Digite o nome da tarefa")
entry_data.pack(fill="x")


#Inicialização
window.mainloop()