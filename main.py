# LIBRARY
from main_library import *

root = Tk()

# FUNCTIONS
class Funcs():
    def select_list_match(self):
        self.list_match.delete(*self.list_match.get_children())
        db_rows = self.db_brasileirao.to_numpy().tolist()
        for row in db_rows:
            self.list_match.insert("", "end", values=row)
    def search_match(self):
        #self.connect_db()
        #self.list_match.delete(*self.listaCli.get_children())
        #self.entry_name.insert(END, '%')
        club = self.entry_club.get()
        self.cursor.execute(""" SELECT code, client_name, telephone, city FROM clients 
            WHERE client_name LIKE '%s' ORDER BY client_name ASC """ % name)
        search_club = self.cursor.fetchall()
        for i in search_club:
            self.list_match.insert("", END, values=i)
        #self.disconnect_db()

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
        # LABEL: CLUB_NAME
        self.lbl_club_name = ttk.Label(self.frame_1, text="Rival", justify="left")
        self.lbl_club_name.place(relx=0.21, rely=0.02, relwidth=0.20, relheight=0.1)
        # LABEL: ARENA
        self.lbl_arena_name = ttk.Label(self.frame_1, text="Arena", justify="left")
        self.lbl_arena_name.place(relx=0.01, rely=0.42, relwidth=0.20, relheight=0.1)

        # COMBOBOX: LIST: CLUB
        self.combo_list_club = ttk.Combobox(self.frame_1, value=self.list_club)
        self.combo_list_club.current(0)
        self.combo_list_club.place(relx=0.01, rely=0.12, relwidth=0.20, relheight=0.1)
        # COMBOBOX: LIST: RIVAL
        self.combo_list_rival = ttk.Combobox(self.frame_1, value=self.list_club)
        self.combo_list_rival.current(0)
        self.combo_list_rival.place(relx=0.21, rely=0.12, relwidth=0.20, relheight=0.1)
        # COMBOBOX: LIST: ARENA
        self.combo_list_arena = ttk.Combobox(self.frame_1, value=self.list_arena)
        self.combo_list_arena.current(0)
        self.combo_list_arena.place(relx=0.01, rely=0.52, relwidth=0.20, relheight=0.1)

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
        self.btn_search.place(relx=0.9, rely=0.85, relwidth=0.1, relheight=0.15)
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
        self.list_match.heading('#7', text="Club Home")
        self.list_match.heading('#8', text="Club Away")
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

        # SCROLLBAR: LIST: MATCH
        self.scroolbar_list_match = Scrollbar(self.frame_2, orient='vertical')
        self.list_match.configure(yscroll=self.scroolbar_list_match.set)
        self.scroolbar_list_match.config(command=self.list_match.yview)
        self.scroolbar_list_match.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        #self.list_match.bind("<Double-1>", self.OnDoubleClick)

Main()
