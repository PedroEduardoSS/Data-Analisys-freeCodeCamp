"""Bibliotecas"""
import pandas as pd #Leitura Do Arquivo
from sklearn.ensemble import ExtraTreesClassifier #Código de Machine learning

"""Leitura do arquivo"""
arquivo = pd.read_csv(r"Dados-Oficiais - Página1.csv")
y = arquivo['Doença/Sintomas']  # variavel alvo
x = arquivo.drop('Doença/Sintomas', axis=1)  # variavel preditora
# criando os conjuntos de dados de treino
x_treino = x[:15]
y_treino = y[:15]

"""Interação com o usuário (Sem Interface Gráfica)"""
l1 = list()
l2 = list()
s = ['Calafrios', 'Diarreia', 'Dor de cabeça', 'Dor Geral', 'Dor de garganta', 'Dor no tórax/peito', 'Dor nos Olhos',
     'Emagrecimento', 'Febre', 'Mal-estar', 'Má Respiração', 'Man Vermelhas', 'Nausea', 'Olhos Vermelhos',
     'Perda Paladar', 'Perda Olfato', 'Sangue Nasal', 'Tosse', 'Tosse seca', 'Tontura', 'Vomitos']
print("Responda as perguntas a seguir como 0 para NÃO e 1 para SIM.")
for sintom in s:
    l2.append(int(input(f"Teve {sintom}?")))

l1.append(l2)

"""Criação do modelo para treinar o conteúdo do arquivo.CSV:"""
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

"""
Previsão dos parâmetros dados pelo usuário
com base no modelo criado anteriormente 
"""
previsao = modelo.predict(l1)
if previsao == [['Rotavírus']]:
    print('Rotavírus')