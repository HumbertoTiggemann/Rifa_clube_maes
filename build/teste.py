# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\tigge\OneDrive\Área de Trabalho\HT testes\Rifa_clube_maes\build\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

premio_valor= int(10)


window = Tk()
ii= ((premio_valor * 20) + 120)
iii= f"700x{ii}"
window.geometry(iii)
window.configure(bg="#4285F4")
window.title("LISTA DE PRÊMIOS")

canvas = Canvas(
    window,
    bg="#4285F4",
    height= (premio_valor * 20) + 120.0,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)

canvas.create_text(
    175.0,
    8.0,
    anchor="nw",
    text="Descrição dos Prêmios:",
    fill="#16730E",
    font=("Inter ExtraBold", 30 * -1),
)


# premio_valor= int(5)
# def criarpremios(premio_valor):
i= 1
lista_premios= list()
while i <= premio_valor:
    altura= float((i * 20) + 27.0)
    canvas.create_text(15.0, altura, anchor="nw", text=F"{i}º Prêmio:", fill="#17740E", font=("Inter", 13 * -1), justify= 'right')
    x=i-1
    lista_premios.append(f"{i}º Prêmio:")
    i= 1 + i
    # return

print(lista_premios)

i= 1    
while i <= premio_valor:
    altura_inic= float((i * 20) + 27.0)
    altura_final= float((i * 20) + 42.0)
    canvas.create_rectangle(86.0, altura_inic , 692.0, altura_final , fill="#A9C2E7", outline="")
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(389.0, 55.0, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
    entry_1.place(x=88.0, y=altura_inic+2, width=602.0, height=10.0)
    i= 1 + i


premios_nr = ("1º premio","2º premio","3º premio")
premios_sorteio = ("premio grande","premio medio","premio pequeno",)
def dicionario_premios(x,y):
    dicionario_p=dict(zip(x, y, strict=True))
    return dicionario_p

altura_inic= float((premio_valor * 20) + 20 + 27.0)
altura_final= float((premio_valor * 20) + 20 + 42.0)


canvas.create_text(
    11.0, altura_inic, anchor="nw", text="Observação:", fill="#17740E", font=("Inter", 13 * -1)
)

altura_inic2= float((premio_valor * 20) + 40 + 27.0)
canvas.create_text(
    12.0,
    altura_inic2,
    anchor="nw",
    text="A observação vai localizada embaixo dos prêmios.\n O nome do arquivo é Rifa_data do sorteio.pdf.",
    fill="#17250E",
    font=("Inter", 12 * -1,'bold'),
)


canvas.create_rectangle(86.0, altura_inic, 692.0, altura_final, fill="#A9C2E7", outline="")

entry_image_21 = PhotoImage(file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(389.0, 455.0, image=entry_image_21)
entry_21 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_21.place(x=88.0, y=altura_inic+2, width=602.0, height=10.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=382.0, y=altura_inic+20, width=204.0, height=25.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(lista_premios),
    relief="flat",
)
button_2.place(x=629.0, y=altura_inic+20, width=63.0, height=25.0)

window.resizable(False, False)
window.mainloop()