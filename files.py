# LIBRARY
from main_library import *


# FILES
class Files():

    # SET: OPTIONS: VIEW
    def set_options_view(self):
        pd.set_option('display.max_columns', 15)
        pd.set_option('display.min_rows', 50)
        pd.set_option('display.max_rows', 50)
        pd.set_option('display.width', 400)

    # PATH: FILES
    def path_files(self):
        # PATH: FILES
        self.path_brasileirao = "campeonato-brasileiro-full.csv"
        self.path_estatisticas = "campeonato-brasileiro-estatisticas-full.csv"
        self.path_pontosasterisco = "pontosasterisco.csv"
        self.path_campaigns = "table_campaign.csv"

    # READ: FILES
    def read_files(self):
        # READ: FILES
        self.db_brasileirao = pd.read_csv(self.path_brasileirao, delimiter=';')
        self.db_estatiscas = pd.read_csv(self.path_estatisticas, delimiter=';')
        self.tbl_pontosasterisco = pd.read_csv(self.path_pontosasterisco, delimiter=';')
        self.tbl_campaigns = pd.read_csv(self.path_campaigns, delimiter=';')
