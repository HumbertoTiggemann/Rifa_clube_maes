# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pywintypes import *
from win32api import *

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\tigge\OneDrive\Área de Trabalho\HT testes\Rifa_clube_maes\build\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x500")
window.configure(bg="#2B3EEB")
window.title("CRIADOR DE RIFAS by Humberto Tiggemann")





canvas = Canvas(
    window,
    bg="#2B3EEB",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_text(
    30.0,
    20.0,
    anchor="nw",
    text="Criador de RIFAS ou Ações entre Amigos",
    fill="#730E0E",
    font=("Inter ExtraBold", 32 * -1),
)


canvas.create_text(
    90.0,
    394.0,
    anchor="nw",
    text="Números por folha:",
    fill="#730E0E",
    font=("Inter", 30 * -1),
)

canvas.create_text(
    22.0,
    306.0,
    anchor="nw",
    text="Quantidade de prêmios:",
    fill="#730E0E",
    font=("Inter", 30 * -1),
)

canvas.create_text(
    12.0,
    350.0,
    anchor="nw",
    text="Quantidade de números:",
    fill="#730E0E",
    font=("Inter", 30 * -1),
)

canvas.create_text(
    210.0, 262.0, anchor="nw", 
    text="Valor: R$ ", fill="#730E0E", justify= 'right', font=("Inter", 30 * -1)
)

canvas.create_text(
    265.0, 218.0, anchor="nw", text="Local:", fill="#730E0E", font=("Inter", 30 * -1)
)

canvas.create_text(
    150.0,
    174.0,
    anchor="nw",
    text="Dia do Sorteio:",
    fill="#730E0E",
    font=("Inter", 30 * -1),
)

canvas.create_text(
    112.0,
    130.0,
    anchor="nw",
    text="Nome (Subtítulo):",
    fill="#730E0E",
    font=("Inter", 30 * -1),
)

canvas.create_text(
    155.0,
    86.0,
    anchor="nw",
    text="Nome (Título):",
    fill="#730E0E",
    font=("Inter", 30 * -1),
)

canvas.create_rectangle(361.0, 86.0, 693.0, 122.0, fill="#A9C2E7", outline="")

testo1=StringVar()
testo1.set("CLUBE DE MÃES ANA NERI")
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(527.0, 104.0, image=entry_image_1)
entry_1 = Entry(textvariable= testo1, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_1.place(x=363.0, y=88.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 130.0, 693.0, 166.0, fill="#A9C2E7", outline="")

testo2=StringVar()
testo2.set("Ação entre Amigos")
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(527.0, 148.0, image=entry_image_2)
entry_2 = Entry(textvariable= testo2, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_2.place(x=363.0, y=132.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 174.0, 693.0, 210.0, fill="#A9C2E7", outline="")

testo3=StringVar()
testo3.set("09/09/2023")
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(527.0, 192.0, image=entry_image_3)
entry_3 = Entry(textvariable= testo3, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_3.place(x=363.0, y=176.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 218.0, 693.0, 254.0, fill="#A9C2E7", outline="")

testo4=StringVar()
testo4.set("Salão Paroquial ROCA SALES")
entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(527.0, 236.0, image=entry_image_4)
entry_4 = Entry(textvariable= testo4,bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_4.place(x=363.0, y=220.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 262.0, 693.0, 298.0, fill="#A9C2E7", outline="")

testo5=StringVar()
testo5.set("5,00")
entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(527.0, 280.0, image=entry_image_5)
entry_5 = Entry(textvariable= testo5, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_5.place(x=363.0, y=264.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 306.0, 693.0, 342.0, fill="#A9C2E7", outline="")

testo6=StringVar()
testo6.set("Somente número")
entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(527.0, 324.0, image=entry_image_6)
entry_6 = Entry(textvariable= testo6, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_6.place(x=363.0, y=308.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 350.0, 693.0, 386.0, fill="#A9C2E7", outline="")


testo7=StringVar()
testo7.set("Somente número")
entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(527.0, 368.0, image=entry_image_7)
entry_7 = Entry(textvariable= testo7, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_7.place(x=363.0, y=352.0, width=328.0, height=30.0)

canvas.create_rectangle(361.0, 394.0, 693.0, 430.0, fill="#A9C2E7", outline="")

testo8=StringVar()
testo8.set("Somente número")
entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(527.0, 412.0, image=entry_image_8)
entry_8 = Entry(textvariable= testo8, bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0 )
entry_8.place(x=363.0, y=396.0, width=328.0, height=30.0)


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(),                 


            relief="flat",
        )
button_1.place(x=256.0, y=445.0, width=188.03602600097656, height=37.0)



nome_clube = str(testo1.get())
nome_subtitulo = str(testo2.get())
data_sorteio = str(f"DATA DO SORTEIO: {testo3.get()}")							
local_sorteio = str(f"LOCAL: {testo4.get()}")
rifa_valor = str(f"VALOR: {testo5.get()}")
premios_qtd = testo6.get()
#quantidade total de números a venda na rifa 
rifa_total_numeros = testo7.get()
#números de rifa por folha
rifa_qtd_numeros_folha= testo8.get()


# print   (nome_clube,
#         nome_subtitulo,
#         data_sorteio,							
#         local_sorteio,
#         rifa_valor,
#         premios_qtd,
#         rifa_total_numeros,
#         rifa_qtd_numeros_folha)



window.resizable(False, False)
window.mainloop()

nome_clube = str(testo1.get())
nome_subtitulo = str(testo2.get())
data_sorteio = str(f"DATA DO SORTEIO: {testo3.get()}")							
local_sorteio = str(f"LOCAL: {testo4.get()}")
rifa_valor = str(f"VALOR: {testo5.get()}")
premios_qtd = int(testo6.get())
#quantidade total de números a venda na rifa 
rifa_total_numeros = int(testo7.get())
#números de rifa por folha
rifa_qtd_numeros_folha= int(testo8.get())




dados= (testo1.get(), testo2.get(), testo3.get(), testo4.get(), testo5.get(), testo6.get(),testo7.get(), testo8.get())
print(dados)
print   (nome_clube,
        nome_subtitulo,
        data_sorteio,							
        local_sorteio,
        rifa_valor,
        premios_qtd,
        rifa_total_numeros,
        rifa_qtd_numeros_folha)
