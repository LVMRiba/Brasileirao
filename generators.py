# LIBRARY
from main_library import *

# CONSTANTS & REFERENCES
ANO_FIXO = 2006
ANO_ATUAL = date.today().year


# GENERATORS
class Gens(Files):
    # GENERATE: COLUMN: RESULT
    def gen_column_result(self):
        self.db_brasileirao.loc[self.db_brasileirao['Mandante Placar'] >
                                self.db_brasileirao['Visitante Placar'], 'Result'] = 'M'
        self.db_brasileirao.loc[self.db_brasileirao['Mandante Placar'] <
                                self.db_brasileirao['Visitante Placar'], 'Result'] = 'V'
        self.db_brasileirao.loc[self.db_brasileirao['Mandante Placar'] ==
                                self.db_brasileirao['Visitante Placar'], 'Result'] = 'E'

        return self.db_brasileirao['Result']

    # GENERATE: COLUMN: YEAR
    def gen_column_year(self):
        """
        O Brasileirao de pontos corridos atualmente possui 20 clubes, mas em suas primeiras edições este número variou:
        Brasileirao 2003: [1054, 1605] - 24 clubs
        Brasileirao 2004: [1606, 2157] - 24 clubs
        Brasileirao 2005: [2158, 2619] - 22 clubs
        """
        self.db_brasileirao.loc[self.db_brasileirao['ID'] < 1054, 'Year'] = -1  # Before 2003 ?
        self.db_brasileirao.loc[
            (self.db_brasileirao['ID'] > 1053) & (self.db_brasileirao['ID'] < 1606), 'Year'] = int(2003)  # 2004 ?
        self.db_brasileirao.loc[
            (self.db_brasileirao['ID'] > 1606) & (self.db_brasileirao['ID'] < 2158), 'Year'] = int(2004)  # 2005 ?
        self.db_brasileirao.loc[
            (self.db_brasileirao['ID'] > 2158) & (self.db_brasileirao['ID'] < 2620), 'Year'] = int(2005)  # 2006 ?

        for i in range(0, ANO_ATUAL - ANO_FIXO + 1):
            Y = 380
            self.db_brasileirao.loc[(self.db_brasileirao['ID'] > 2619 + i * Y) &
                                    (self.db_brasileirao['ID'] <= 2619 + (i + 1) * Y), 'Year'] = int(2006+i)  # Pós 2006 ?

        return self.db_brasileirao['Year']

    # GENERATE: LIST: CLUBS
    def gen_list_club(self):
        self.path_list_club = "list_club"
        self.list_club = []
        # READ: LIST: CLUBS
        with codecs.open(self.path_list_club, 'r', 'utf-8') as file:
            self.list_club.append('')
            for line in file:
                #print(line, end='')
                self.list_club.append(line)

    # GENERATE: LIST: ARENA
    def gen_list_arena(self):
        self.path_list_arena = "arenas"
        self.list_arena = []
        # READ: LIST: CLUBS
        with codecs.open(self.path_list_arena, 'r', 'utf-8') as file:
            self.list_arena.append('')
            for line in file:
                #print(line, end='')
                self.list_arena.append(line)
