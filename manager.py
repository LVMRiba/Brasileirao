# LIBRARY
from main_library import *


class ETL(Files):
    def alterate_arena(self):
        self.db_brasileirao['Arena'] = self.db_brasileirao['Arena'].replace({
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
        return self.db_brasileirao['Arena']
    
    
    def alterate_club(self):
        self.db_brasileirao[['Mandante', 'Visitante', 'Vencedor']] = self.db_brasileirao[
            ['Mandante', 'Visitante', 'Vencedor']].replace({
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
        return self.db_brasileirao[['Mandante', 'Visitante', 'Vencedor']]
    
    
    def alterate_hour(self):
        piece_1 = self.db_brasileirao['ID'] == 3248
        piece_2 = (self.db_brasileirao['ID'] > 6409) & (self.db_brasileirao['ID'] < 6420)
        self.db_brasileirao.loc[piece_1, 'Horário'] = self.db_brasileirao.loc[piece_1, 'Horário'].fillna('19h00')
        self.db_brasileirao.loc[piece_2, 'Horário'] = self.db_brasileirao.loc[piece_2, 'Horário'].fillna('17h00')
        
        
    def extract_data(self):
        # ETL
        self.set_options_view()
        self.path_files()
        self.read_files()
        self.db_brasileirao = self.db_brasileirao.drop(
            columns=['Estado Mandante', 'Estado Visitante', 'Estado Vencedor'])
        #self.db_brasileirao = self.db_brasileirao.dropna()
        self.db_brasileirao['Mandante'] = self.db_brasileirao['Mandante'].str.title()
        self.db_brasileirao['Visitante'] = self.db_brasileirao['Visitante'].str.title()
        self.db_brasileirao['Vencedor'] = self.db_brasileirao['Vencedor'].str.title()
        self.db_brasileirao = self.db_brasileirao.loc[self.db_brasileirao['ID'] >= 1054]  # Filtra resultados pós 2002
        self.db_brasileirao[['Mandante', 'Visitante', 'Vencedor']] = self.alterate_club()  # Mudar nome de Clubes
        self.db_brasileirao['Arena'] = self.alterate_arena()  # Mudar nome de Arenas
        self.db_brasileirao = self.db_brasileirao.drop(columns='Vencedor')
        self.db_brasileirao['Result'] = self.gen_column_result()  # Otimizar o resultado da partida
        self.db_brasileirao.insert(1, 'Year', '-')  # Cria e reordena coluna Year
        self.db_brasileirao['Year'] = self.gen_column_year()  # Definir edicao do campeonato
        # FILL: NAN: HOUR
        self.alterate_hour()
        # RETYPE: GOALS

        # DROP: NAN
        self.db_brasileirao = self.db_brasileirao.dropna()
        # GENERATE: LIST
        self.list_club = sorted(self.db_brasileirao['Mandante'].drop_duplicates())
        self.list_arena = sorted(self.db_brasileirao['Arena'].drop_duplicates().dropna())

        """
        print(self.db_brasileirao)
        print(f'\n===CLUBES=== {len(self.list_club)} clubes')
        print(self.list_club)
        print(f'\n===ESTÁDIOS=== {len(self.list_arena)} estádios')
        print(self.list_arena)
        print('Show NAN rows')
        print(self.db_brasileirao[self.db_brasileirao.isna().any(axis=1)])
        """
