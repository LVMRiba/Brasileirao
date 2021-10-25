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