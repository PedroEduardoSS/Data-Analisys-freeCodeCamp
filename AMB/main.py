import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from dearpygui.core import *
from dearpygui.simple import *

#main-code

arquivo = pd.read_csv(r"Dados-Oficiais - Página1.csv")
y = arquivo['Doença/Sintomas']  # variavel alvo
x = arquivo.drop('Doença/Sintomas', axis=1)  # variavel preditora
# criando os conjuntos de dados de treino
x_treino = x[:15]
y_treino = y[:15]

modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

result = " "
def mainFuction(sender, data):
    diceased = []
    diceased.append(var)
    previsao = modelo.predict(diceased)
    if previsao == [['AIDS']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: AIDS")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Asma']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Asma")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Catapora']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Catapora")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Chikungunya']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Chikungunya")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Coronavírus']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Coronavírus")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Dengue']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Dengue")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Gripe']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Gripe")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Hantavirose']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Hantavirose")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Hipertensão']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Hipertensão")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Leptospirose']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Leptospirose")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Malária']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Malária")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Raiva']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Raiva")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Rotavírus']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Rotavírus")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Sarampo']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Sarampo")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    elif previsao == [['Zika Vírus']]:
        with window("Resultado", no_close=True):
            add_text("Sua doença é: Zika Vírus")
            add_button("Fechar", callback=lambda:delete_item("Resultado"))
    else:
        result = "INCONCLUSIVO"

def sintomaFun():
    var.pop(0)
    var.insert(0, 1)

def sintoma2Fun():
    var.pop(1)
    var.insert(1, 1)

def sintoma3Fun():
    var.pop(2)
    var.insert(2, 1)

def sintoma4Fun():
    var.pop(3)
    var.insert(3, 1)

def sintoma5Fun():
    var.pop(4)
    var.insert(4, 1)

def sintoma6Fun():
    var.pop(5)
    var.insert(5, 1)

def sintoma7Fun():
    var.pop(6)
    var.insert(6, 1)

def sintoma8Fun():
    var.pop(7)
    var.insert(7, 1)

def sintoma9Fun():
    var.pop(8)
    var.insert(8, 1)

def sintoma10Fun():
    var.pop(9)
    var.insert(9, 1)

def sintoma11Fun():
    var.pop(10)
    var.insert(10, 1)

def sintoma12Fun():
    var.pop(11)
    var.insert(11, 1)

def sintoma13Fun():
    var.pop(12)
    var.insert(12, 1)

def sintoma14Fun():
    var.pop(13)
    var.insert(13, 1)

def sintoma15Fun():
    var.pop(14)
    var.insert(14, 1)

def sintoma16Fun():
    var.pop(15)
    var.insert(15, 1)

def sintoma17Fun():
    var.pop(16)
    var.insert(16, 1)

def sintoma18Fun():
    var.pop(17)
    var.insert(17, 1)

def sintoma19Fun():
    var.pop(18)
    var.insert(18, 1)

def sintoma20Fun():
    var.pop(19)
    var.insert(19, 1)

def sintoma21Fun():
    var.pop(20)
    var.insert(20, 1)


#interface
set_main_window_size(800, 850)
set_main_window_title("Assistente Medica")
with window("AMB", width=799, height=820, x_pos=0, y_pos=0, no_close=True):
    
    add_text("Marque apenas os sintomas que sentiu nos últimos dias", bullet=True)

    add_separator()
    add_spacing(count=5)

    with group("row1"):
        add_same_line(spacing=100)
        add_checkbox("Calafrios", callback=sintomaFun)
        add_same_line(spacing=100)
        add_checkbox("Emagrecimento", callback=sintoma8Fun)
        add_same_line(spacing=100)
        add_checkbox("Perda de Paladar", callback=sintoma15Fun)

    with group("row2"):
        add_spacing(count=10)
        add_same_line(spacing=100)
        add_checkbox("Diarreia", callback=sintoma2Fun)
        add_same_line(spacing=108)
        add_checkbox("Febre", callback=sintoma9Fun)
        add_same_line(spacing=155)
        add_checkbox("Perda de Olfato", callback=sintoma16Fun)
    
    with group("row3"):
        add_spacing(count=10)
        add_same_line(spacing=100)
        add_checkbox("Dor de cabeça", callback=sintoma3Fun)
        add_same_line(spacing=73)
        add_checkbox("Mal-estar", callback=sintoma10Fun)
        add_same_line(spacing=127)
        add_checkbox("Sangramento Nasal", callback=sintoma17Fun)

    with group("row4"):
        add_spacing(count=10)
        add_same_line(spacing=100)
        add_checkbox("Dor Geral", callback=sintoma4Fun)
        add_same_line(spacing=102)
        add_checkbox("Má Respiração", callback=sintoma11Fun)
        add_same_line(spacing=98)
        add_checkbox("Tosse", callback=sintoma18Fun)

    with group("row5"):
        add_spacing(count=10)
        add_same_line(spacing=100)
        add_checkbox("Dor de Garganta", callback=sintoma5Fun)
        add_same_line(spacing=60)
        add_checkbox("Manchas Vermelhas", callback=sintoma12Fun)
        add_same_line(spacing=70)
        add_checkbox("Tosse Seca", callback=sintoma19Fun)

    with group("row6"):
        add_spacing(count=10)
        add_same_line(spacing=100)
        add_checkbox("Dor Tórax/Peito", callback=sintoma6Fun)
        add_same_line(spacing=60)
        add_checkbox("Náuseas", callback=sintoma13Fun)
        add_same_line(spacing=140)
        add_checkbox("Tontura", callback=sintoma20Fun)

    with group("row7"):
        add_spacing(count=10)
        add_same_line(spacing=100)
        add_checkbox("Dor nos Olhos", callback=sintoma7Fun)
        add_same_line(spacing=75)
        add_checkbox("Olhos vermelhos", callback=sintoma14Fun)
        add_same_line(spacing=82)
        add_checkbox("Vômitos", callback=sintoma21Fun)
    
    add_spacing(count=5)
    add_separator()

    add_spacing(count=5)
    add_same_line(spacing=325)
    add_button("Verificar", callback=mainFuction)
    add_spacing(count=5)

start_dearpygui()