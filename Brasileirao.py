import pandas as pd
from datetime import date
import codecs   # HABILITAR UTF-8

ANO_FIXO = 2006
ANO_ATUAL = date.today().year


def alterar_arena(db_brasileirao):
    db_brasileirao['Arena'] = db_brasileirao['Arena'].replace({
        'A Campanella': 'Anacleto Campanella',
        'Arena Corinthians': 'Itaqueirão',
        'Beira Rio': 'Beira-Rio',
        'Benedito Teixeira': 'Teixeirão',
        'Boca do Jacaré': 'Serejão',
        'Cláudio Moacyr': 'Moacyrzão',
        'Durival de Brito': 'Vila Capanema',
        'Eduardo José Farah': 'Prudentão',
        'Estrela Solitária': 'Engenhão',
        'Itaipava Arena Fonte Nova': 'Fonte Nova',
        'Juiz de Fora': 'Municipal Juiz de Fora',
        'Kyocera Arena': 'Arena da Baixada',
        'Mário Helênio': 'Limeirão',
        'Mj José Levi Sobrinho': 'Municipal Juiz de Fora',
        'Neo Química Arena': 'Itaqueirão',
        'Nilton Santos (Engenhão)': 'Engenhão',
        'Papa J.Paulo II': 'Vail Chaves',
        'Pedro Pedrossian': 'Morenão',
        'Plácido Castelo': 'Castelão',
        'Parque Antártica': 'Palestra Itália',
        'Pq. Antarctica': 'Palestra Itália',
        'Romildo Ferreira': 'Vail Chaves',
        'Romildão': 'Vail Chaves',
        'Wilson de Barros': 'Vail Chaves'
    })

    return db_brasileirao['Arena']


def alterar_clube(db_brasileirao):
    db_brasileirao[['Mandante', 'Visitante', 'Vencedor']] = db_brasileirao[['Mandante', 'Visitante', 'Vencedor']].replace({
        'América-Mg': 'América-MG',
        'América-Rn': 'América-RN',
        'Athlético-Pr': 'Athlético-PR',
        'Athletico-Pr': 'Athlético-PR',
        'Atlético-Go': 'Atlético-GO',
        'Atlético-Mg': 'Atlético-MG',
        'Botafogo-Rj': 'Botafogo',
        'Grêmio Prudente': 'Barueri',
        'Csa': 'CSA',
    })

    return db_brasileirao[['Mandante', 'Visitante', 'Vencedor']]


def gerar_tabela_campanha(db_brasileirao, list_club_ano):
    """
    P: PM + PV + PP
    Ps: Pontos Asteriscos
    V: Vitórias (VM + VV)
    E: Empates (EM + EV)
    D: Derrotas (DM + DV)

    PM: Pontos como Mandante
    PV: Pontos como Visitante
    VM: Vitórias como Mandante
    VV: Vitórias como Visitante
    EM: Empates como Mandante
    EV: Empates como Visitante
    DM: Derrotas como Mandante
    DV: Derrotas como Visitante
    GFM: Gols feitos como Mandante
    GSM: Gols sofridos como Mandante
    GFV: Gols feitos como Visitante
    GSV: Gols sofridos como Visitante

    PO: Pontos obtidos no Turno 1
    PE: Pontos obtidos no Turno 2
    VO: Vitórias no Turno 1
    VE: Vitórias no Turno 2
    EO: Emaptes no Turno 1
    EE: Empates no Turno 2
    DO: Derrotas no Turno 1
    DE: Derrotas no Turno 2
    GFO: Gols feitos no Turno 1
    GSO: Gols sofridos no Turno 2
    GFE: Gols feitos no Turno 1
    GSE: Gols sofridos no Turno 2
    """

    for i in range(2003, ANO_ATUAL):
        print(f'Edição {i}')
        if i in [2003, 2004]:
            round_med = int(23) # São 23 jogos por turno
        elif i == 2005:
            round_med = int(21) # São 21 jogos por turno
        else:
            round_med = int(19) # São 19 jogos por turno

        for club in list_club_ano[str(i)]:
            # DATA: HOME & AWAY
            VH = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'M')].count())
            VA = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'V')].count())
            EH = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'E')].count())
            EA = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'E')].count())
            DH = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'V')].count())
            DA = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'M')].count())
            V = VH + VA
            E = EH + EA
            D = DH + DA

            PH = 3*VH + EH
            PA = 3*VA + EA
            P = PH + PA

            GFH = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Mandante'] == club)].sum())
            GSH = int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                             (db_brasileirao['Mandante'] == club)].sum())
            GFA = int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                             (db_brasileirao['Visitante'] == club)].sum())
            GSA = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Visitante'] == club)].sum())
            GF = GFH + GFA
            GS = GSH + GSA

            # DATA: OPENING & ENDING
            VO = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'M')].count()) + \
                 int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'V')].count())
            VE = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'M')].count()) + \
                 int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'V')].count())
            EO = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'E')].count()) + \
                 int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'E')].count())
            EE = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'E')].count()) + \
                 int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'E')].count())
            DO = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'V')].count()) + \
                 int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'M')].count())
            DE = int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                     (db_brasileirao['Mandante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'V')].count()) + \
                 int(db_brasileirao['Resultado'].loc[(db_brasileirao['Edicao'] == i) &
                                                     (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                     (db_brasileirao['Visitante'] == club) &
                                                     (db_brasileirao['Resultado'] == 'M')].count())

            PO = 3*VO + EO
            PE = 3*VE + EE

            GFO = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                            (db_brasileirao['Mandante'] == club)].sum()) + \
                  int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                            (db_brasileirao['Visitante'] == club)].sum())
            GSO = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                            (db_brasileirao['Visitante'] == club)].sum()) + \
                  int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                            (db_brasileirao['Mandante'] == club)].sum())
            GFE = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                            (db_brasileirao['Mandante'] == club)].sum()) + \
                  int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                            (db_brasileirao['Visitante'] == club)].sum())
            GSE = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                            (db_brasileirao['Visitante'] == club)].sum()) + \
                  int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['Edicao'] == i) &
                                                            (db_brasileirao['Rodada'].astype(int) > round_med) &
                                                            (db_brasileirao['Mandante'] == club)].sum())

            campaign = []
            campaign_lg = {'Club': club, 'Year': i, 'Mode': 'LG', 'P': P, 'V': V, 'E': E, 'D': D, 'GF': GF, 'GS': GS}
            campaign_hm = {'Club': club, 'Year': i, 'Mode': 'HM', 'P': PH, 'V': VH, 'E': EH, 'D': DH, 'GF': GFH, 'GS': GSH}
            campaign_aw = {'Club': club, 'Year': i, 'Mode': 'AW', 'P': PA, 'V': VA, 'E': EA, 'D': DA, 'GF': GFA, 'GS': GSA}
            campaign_op = {'Club': club, 'Year': i, 'Mode': 'OP', 'P': PO, 'V': VO, 'E': EO, 'D': DO, 'GF': GFO, 'GS': GSO}
            campaign_ed = {'Club': club, 'Year': i, 'Mode': 'ED', 'P': PE, 'V': VE, 'E': EE, 'D': DE, 'GF': GFE, 'GS': GSE}

            campaign.append(campaign_lg)
            campaign.append(campaign_hm)
            campaign.append(campaign_aw)
            campaign.append(campaign_op)
            campaign.append(campaign_ed)

            write_file(campaign)


def gerar_tabela_edicao(db_brasileirao):
    """
    O Brasileirao de pontos corridos atualmente possui 20 clubes, mas em suas primeiras edições este número variou:
    Brasileirao 2003: [1054, 1605] - 24 clubes
    Brasileirao 2004: [1606, 2157] - 24 clubes
    Brasileirao 2005: [2158, 2619] - 22 clubes
    """
    db_brasileirao.loc[db_brasileirao['ID'] < 1054, 'Edicao'] = -1   # Antes de 2003 ?
    db_brasileirao.loc[(db_brasileirao['ID'] > 1053) & (db_brasileirao['ID'] < 1606), 'Edicao'] = 2003   # 2004 ?
    db_brasileirao.loc[(db_brasileirao['ID'] > 1606) & (db_brasileirao['ID'] < 2158), 'Edicao'] = 2004   # 2005 ?
    db_brasileirao.loc[(db_brasileirao['ID'] > 2158) & (db_brasileirao['ID'] < 2620), 'Edicao'] = 2005   # 2006 ?

    for i in range(0, ANO_ATUAL - ANO_FIXO + 1):
        Y = 380
        db_brasileirao.loc[(db_brasileirao['ID'] > 2619 + i * Y) &
                           (db_brasileirao['ID'] <= 2619 + (i + 1) * Y), 'Edicao'] = 2006 + i  # Pós 2006 ?

    return db_brasileirao['Edicao']


def gerar_tabela_resultado(db_brasileirao):
    db_brasileirao.loc[db_brasileirao['Mandante Placar'] > db_brasileirao['Visitante Placar'], 'Resultado'] = 'M'
    db_brasileirao.loc[db_brasileirao['Mandante Placar'] < db_brasileirao['Visitante Placar'], 'Resultado'] = 'V'
    db_brasileirao.loc[db_brasileirao['Mandante Placar'] == db_brasileirao['Visitante Placar'], 'Resultado'] = 'E'

    return db_brasileirao['Resultado']


def gerar_lista_clube_ano(db_brasileirao):
    clubs = {}
    for i in range(2003, ANO_ATUAL):
        ano = f'{i}'
        clubs[ano] = sorted(db_brasileirao['Mandante'].loc[(db_brasileirao['Edicao'] == i)].drop_duplicates())

    return clubs


def print_list(list):
    for element in list:
        print(element)


def write_file(data):
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
db_brasileirao[['Mandante', 'Visitante', 'Vencedor']] = alterar_clube(db_brasileirao)      # Mudar nome de Clubes
db_brasileirao['Arena'] = alterar_arena(db_brasileirao)                 # Mudar nome de Arenas
db_brasileirao['Resultado'] = gerar_tabela_resultado(db_brasileirao)    # Otimizar o vencedor da partida
db_brasileirao['Edicao'] = gerar_tabela_edicao(db_brasileirao)          # Definir edicao do campeonato

list_club = sorted(db_brasileirao['Mandante'].drop_duplicates())
list_arena = sorted(db_brasileirao['Arena'].drop_duplicates().dropna())

list_club_ano = gerar_lista_clube_ano(db_brasileirao)

#gerar_tabela_campanha(db_brasileirao, list_club_ano)

print(tbl_campanhas)

"""
print(tbl_pontosasterisco)
print(f'===TIPOS DAS COLUNAS===\n{db_brasileirao.dtypes}')     # Tipos das Colunas
print(f'===RESULTADOS===\n{db_brasileirao}')
print(f'\n===CLUBES=== {len(list_club)} clubes')
print_list(list_club)
print(f'\n===ESTÁDIOS=== {len(list_arena)} estádios')
print_list(list_arena)
"""
