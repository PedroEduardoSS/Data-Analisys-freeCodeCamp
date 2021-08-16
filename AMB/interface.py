import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from dearpygui.dearpygui import *

setup_viewport()
set_viewport_title(title='Assistente Medica')
set_viewport_width(500)
set_viewport_height(800)

l = ['anorexia', 'bolhas no corpo', 'calafrios',
       'cansaço', 'coriza', 'chiado no peito', 'diarreia', 'dor abdominal',
       'dor de cabeça', 'dor de garganta', 'dor Geral', 'dor lombar',
       'dor nas juntas', 'dor no tórax/peito', 'dor nos Olhos',
       'dores musculares', 'emagrecimento', 'febre >38', 'febre baixa',
       'fraqueza', 'inquietude', 'mal-estar', 'má Respiração',
       'manchas vermelhas', 'nausea', 'olhos vermelhos', 'perda de apetite',
       'perda paladar', 'perda olfato', 'sangue nasal',
       'sintomas gastrointestinais', 'sudorese', 'suores Noturnos', 'tosse',
       'tosse seca', 'tontura', 'vomitos', 'zumbido no ouvido',
       'consumo de álcool', '>60 anos ',
       'contato com animais selvagens ou com raiva', 'diabetes',
       'dieta rica em sal', 'falta de seneamento básico na região', 'gravidez',
       'parente asmático', 'obesidade', 'puérpera até duas semanas do parto',
       'sedentarismo']

def procurar(sender):
    # get value from input box
    filter_string = get_value(sender)
    # set value of filter set
    set_value(filter_id, filter_string)

with window(label="Filtro de lista", width=499, height=799):
    add_input_text(label="Pesquisar", callback=procurar)
    with filter_set() as filter_id:
        d1 = add_checkbox(label="anorexia", filter_key="anorexia")
        d2 = add_checkbox(label="bolhas no corpo", filter_key="bolhas no corpo")
        d3 = add_checkbox(label="calafrios", filter_key="calafrios")
        d4 = add_checkbox(label="cansaço", filter_key="cansaço")
        d5 = add_checkbox(label="coriza", filter_key="coriza")
        d6 = add_checkbox(label="chiado no peito", filter_key="chiado no peito")
        d7 = add_checkbox(label="diarreia", filter_key="diarreia")
        d8 = add_checkbox(label="dor abdominal", filter_key="dor abdominal")
        d9 = add_checkbox(label="dor de cabeça", filter_key="dor de cabeça")      

start_dearpygui()