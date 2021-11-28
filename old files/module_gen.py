# LIBRARY
from datetime import date

ANO_FIXO = 2006
ANO_ATUAL = date.today().year

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

            write_file_campaign(campaign)


def gerar_tabela_agregado(db_brasileirao, list_club_ano):
    """
    club_1: Clube 1
    club_2: Clube 2
    ID_1: ID da partida do Turno 1 entre Clube 1 e Clube 2
    ID_2: ID da partida do Turno 2 entre Clube 1 e Clube 2
    G_1M: Gols do Clube 1 como Mandante
    G_1V: Gols do Clube 1 como Visitante
    G_2M: Gols do Clube 2 como Mandante
    G_2V: Gols do Clube 2 como Visitante
    G_1: Gols do Clube 1 (G_1M + G_1V)
    G_2: Gols do Clube 2 (G_2M + G_2V)
    """

    for i in range(2003, 2004):
        print(f'Edição {i}')
        if i in [2003, 2004]:
            round_med = int(23) # São 23 jogos por turno
        elif i == 2005:
            round_med = int(21) # São 21 jogos por turno
        else:
            round_med = int(19) # São 19 jogos por turno

        for club_1 in list_club_ano[str(i)]:
            print(club_1)
            list_club_2 = db_brasileirao['Visitante'].loc[(db_brasileirao['Edicao'] == i) &
                                                          (db_brasileirao['Rodada'].astype(int) <= round_med) &
                                                          (db_brasileirao['Mandante'] == club_1)]

            for club_2 in list_club_2:
                ID_1 = int(db_brasileirao['ID'].loc[(db_brasileirao['Edicao'] == i) &
                                                    (db_brasileirao['Mandante'] == club_1) &
                                                    (db_brasileirao['Visitante'] == club_2)])
                ID_2 = int(db_brasileirao['ID'].loc[(db_brasileirao['Edicao'] == i) &
                                                    (db_brasileirao['Mandante'] == club_2) &
                                                    (db_brasileirao['Visitante'] == club_1)])
                G_1M = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['ID'] == ID_1)])
                G_1V = int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['ID'] == ID_2)])
                G_2M = int(db_brasileirao['Visitante Placar'].loc[(db_brasileirao['ID'] == ID_1)])
                G_2V = int(db_brasileirao['Mandante Placar'].loc[(db_brasileirao['ID'] == ID_2)])
                G_1 = G_1M + G_1V
                G_2 = G_2M + G_2V

                if G_1 > G_2:
                    Result = 'C1' # Clube 1 fez mais gols no agregado
                elif G_1 < G_2:
                    Result = 'C2' # Clube 2 fez mais gols no agregado
                else:
                    if G_1V > G_2V:
                        Result = 'C1A' # Clube 1 fez mais gols como visitante
                    elif G_1V < G_2V:
                        Result = 'C2A' # Clube 2 fez mais gols como visitante
                    else:
                        Result = 'C0' # Empate com mesmo número de gols em ambos os jogos

                print(f'{club_2:15}\t{ID_1}\t{ID_2}\t{G_1M}x{G_2V}\t{G_2M}x{G_1V}\t{G_1} {G_2}\t{Result}')

            """
            database = {'ID_1', 'ID_2', 'Club_1', 'Club_2', 'Placar_1', 'Placar_2', 'Result'}
            """

    pass


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
