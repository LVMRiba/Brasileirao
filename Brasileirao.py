# LIBRARY
import pandas as pd
from datetime import date
import codecs   # HABILITAR UTF-8

# MODULES
import module_alterar
import module_gen

ANO_FIXO = 2006
ANO_ATUAL = date.today().year


def check_file():
    pass


def print_list(list):
    for element in list:
        print(element)


def write_file_campaign(data):
    file = codecs.open('table_campaign.csv', 'a', 'utf-8')

    for i in range(0, 5):
        #print(f"{data[i]['Club']}; {data[i]['Year']}; {data[i]['Mode']}; {data[i]['P']}; {data[i]['V']}; {data[i]['E']}; {data[i]['D']}; {data[i]['GF']}; {data[i]['GS']}")
        file.write(f"{data[i]['Club']};{data[i]['Year']};{data[i]['Mode']};{data[i]['P']};{data[i]['V']};{data[i]['E']};{data[i]['D']};{data[i]['GF']};{data[i]['GS']}\n")

    file.close()


# SET_OPTION
pd.set_option('display.max_columns', 15)
pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 400)

path_brasileirao = "campeonato-brasileiro-full.csv"
path_pontosasterisco = "pontosasterisco.csv"
path_campanhas = "table_campaign.csv"

db_brasileirao = pd.read_csv(path_brasileirao, delimiter=';')
tbl_pontosasterisco = pd.read_csv(path_pontosasterisco, delimiter=';')
tbl_campanhas = pd.read_csv(path_campanhas, delimiter=';')

db_brasileirao = db_brasileirao.drop(columns=['Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])
db_brasileirao['Mandante'] = db_brasileirao['Mandante'].str.title()
db_brasileirao['Visitante'] = db_brasileirao['Visitante'].str.title()
db_brasileirao['Vencedor'] = db_brasileirao['Vencedor'].str.title()
db_brasileirao = db_brasileirao.loc[db_brasileirao['ID'] >= 1054]       # Filtra resultados a partir de 2003
db_brasileirao[['Mandante', 'Visitante', 'Vencedor']] = module_alterar.alterar_clube(db_brasileirao)      # Mudar nome de Clubes
db_brasileirao['Arena'] = module_alterar.alterar_arena(db_brasileirao)    # Mudar nome de Arenas
db_brasileirao['Resultado'] = module_gen.gerar_tabela_resultado(db_brasileirao)    # Otimizar o vencedor da partida
db_brasileirao['Edicao'] = module_gen.gerar_tabela_edicao(db_brasileirao)          # Definir edicao do campeonato

list_club = sorted(db_brasileirao['Mandante'].drop_duplicates())
list_arena = sorted(db_brasileirao['Arena'].drop_duplicates().dropna())

list_club_ano = module_gen.gerar_lista_clube_ano(db_brasileirao)

#gerar_tabela_campanha(db_brasileirao, list_club_ano)

#print(tbl_campanhas)

"""
print(tbl_pontosasterisco)
print(f'===TIPOS DAS COLUNAS===\n{db_brasileirao.dtypes}')     # Tipos das Colunas
print(f'===RESULTADOS===\n{db_brasileirao}')
print(f'\n===CLUBES=== {len(list_club)} clubes')
print_list(list_club)
print(f'\n===ESTÁDIOS=== {len(list_arena)} estádios')
print_list(list_arena)
"""

module_gen.gerar_tabela_agregado(db_brasileirao, list_club_ano)

