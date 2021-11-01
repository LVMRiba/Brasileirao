# LIBRARY
import pandas as pd         # BIBLIOTECA DE ANÁLISE DE DADOS
from datetime import date   # BIBLIOTECA DE TEMPO
import codecs               # HABILITAR UTF-8
from tkinter import *       # BIBLIOTECA DE INTERFACE GRÁFICA
from tkinter import ttk     # BIBLIOTECA PARA COMBOBOX

root = Tk()

# CONSTANTS & REFERENCES
RELX_C_1 = 0.02     # RELATION X - COLUMN 0
RELY_C_1 = 0.02     # RELATION Y - COLUMN 0

ANO_FIXO = 2006
ANO_ATUAL = date.today().year


# FUNCTIONS: ALTER
class Alts():
    def alterate_arena(self):
        self.db_brasileirao['Arena'].replace({
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

    def alterate_club(self):
        self.db_brasileirao[['Mandante', 'Visitante', 'Vencedor']].replace({
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


# FILES
class Files():
    # SET: OPTIONS: VIEW
    def set_options_view(self):
        pd.set_option('display.max_columns', 15)
        pd.set_option('display.min_rows', 50)
        pd.set_option('display.max_rows', 50)
        pd.set_option('display.width', 400)
    def path_files(self):
        # PATH: FILES
        self.path_brasileirao = "campeonato-brasileiro-full.csv"
        self.path_estatisticas = "campeonato-brasileiro-estatisticas-full.csv"
        self.path_pontosasterisco = "pontosasterisco.csv"
        self.path_campaigns = "table_campaign.csv"
    def read_files(self):
        # READ: FILES
        self.db_brasileirao = pd.read_csv(self.path_brasileirao, delimiter=';')
        self.db_estatiscas = pd.read_csv(self.path_estatisticas, delimiter=';')
        self.tbl_pontosasterisco = pd.read_csv(self.path_pontosasterisco, delimiter=';')
        self.tbl_campaigns = pd.read_csv(self.path_campaigns, delimiter=';')

# FUNCTIONS
class Funcs():
    def select_list_match(self):
        self.list_match.delete(*self.list_match.get_children())
        db_rows = self.db_brasileirao.to_numpy().tolist()
        for row in db_rows:
            self.list_match.insert("", "end", values=row)


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


# MAIN
class Main(Funcs, Gens, ETL):
    def __init__(self):
        self.root = root
        self.read_data()
        self.screen()
        self.screen_frames()
        self.widget_frame_1()
        self.treeview_frame_2()
        self.select_list_match()
        root.mainloop()
    def read_data(self):
        self.extract_data()
        #self.gen_list_club()
        #self.gen_list_arena()
    def screen(self):
        self.root.title("Brasileirão")
        self.root.configure(background='darkgreen')
        self.root.geometry("1024x768")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=640, height=360)
    def screen_frames(self):
        # FRAME 1
        self.frame_1 = Frame(self.root, bd=4, bg='orange', highlightbackground='#B0C4DE', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.9, relheight=0.45)
        # FRAME 2
        self.frame_2 = Frame(self.root, bd=4, bg='orange', highlightbackground='#B0C4DE', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.9, relheight=0.45)
    def widget_frame_1(self):
        # LABEL: CLUB_NAME
        self.lbl_club_name = ttk.Label(self.frame_1, text="Club", justify="left")
        self.lbl_club_name.place(relx=0.01, rely=0.02, relwidth=0.20, relheight=0.1)
        # LABEL: ARENA
        self.lbl_arena_name = ttk.Label(self.frame_1, text="Arena", justify="left")
        self.lbl_arena_name.place(relx=0.01, rely=0.22, relwidth=0.20, relheight=0.1)

        # COMBOBOX: LIST: CLUB
        self.combo_list_club = ttk.Combobox(self.frame_1, value=self.list_club)
        self.combo_list_club.current(0)
        self.combo_list_club.place(relx=0.01, rely=0.12, relwidth=0.20, relheight=0.1)
        # COMBOBOX: LIST: ARENA
        self.combo_list_arena = ttk.Combobox(self.frame_1, value=self.list_arena)
        self.combo_list_arena.current(0)
        self.combo_list_arena.place(relx=0.01, rely=0.32, relwidth=0.20, relheight=0.1)

        # INTERVAL: BY DATE
            # DROPDOWN: YEAR MIN
            # DROPDOWN: YEAR MAX
        # INTERVAL: BY ROUND
            # DROPDOWN: YEAR MIN
            # DROPDOWN: YEAR MAX
        # INTERVAL: BY YEAR
            # DROPDOWN: YEAR MIN
            # DROPDOWN: YEAR MAX
        # CHECK LIST: RESULTS: Victories, Draw, Loses
        # CHECK LIST: Home, Away


        ### BUTTON: SEARCH
        self.btn_search = Button(self.frame_1, text="Search", bd=5, bg='green', fg='white')
        self.btn_search.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
    def treeview_frame_2(self):
        # TREEVIEW: LIST: MATCH
        self.list_match = ttk.Treeview(self.frame_2, height=3,
                                       column=('col1', 'col2', 'col3', 'col4', 'col5',
                                               'col6', 'col7', 'col8', 'col9', 'col10',
                                               'col11', 'col12'))
        self.list_match.heading('#0', text="")
        self.list_match.heading('#1', text="Code")
        self.list_match.heading('#2', text="Year")
        self.list_match.heading('#3', text="Round")
        self.list_match.heading('#4', text="Date")
        self.list_match.heading('#5', text="Hour")
        self.list_match.heading('#6', text="Day")
        self.list_match.heading('#7', text="Club H")
        self.list_match.heading('#8', text="Club A")
        self.list_match.heading('#9', text="Arena")
        self.list_match.heading('#10', text="Goals H")
        self.list_match.heading('#11', text="Goals A")
        self.list_match.heading('#12', text="Result")

        self.list_match.column('#0', width=1)
        self.list_match.column('#1', width=6)
        self.list_match.column('#2', width=4)
        self.list_match.column('#3', width=2)
        self.list_match.column('#4', width=10)
        self.list_match.column('#5', width=5)
        self.list_match.column('#6', width=14)
        self.list_match.column('#7', width=18)
        self.list_match.column('#8', width=18)
        self.list_match.column('#9', width=20)
        self.list_match.column('#10', width=2)
        self.list_match.column('#11', width=2)
        self.list_match.column('#12', width=1)

        self.list_match.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolList = Scrollbar(self.frame_2, orient='vertical')
        self.list_match.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        #self.list_match.bind("<Double-1>", self.OnDoubleClick)

Main()
