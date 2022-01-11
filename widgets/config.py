from tkinter import *
from tkinter import ttk

screen_w = 800
screen_h = 600


class AppInicial(Tk):
    def __init__(self,) -> None:
        super().__init__()
        self.label_url = None
        self.canvas = None
        self.url_entry = None
        self.botao_buscar = None
        self.botao_download = None
        self.tree_view = None
        self.img_button = PhotoImage(file=f"assets/button.png")
        
        
        self.iconbitmap("assets/icon_windows.ico")
        
        self.configWindows()
        
    def handle_click(self, event):
        if self.tree_view.identify_region(event.x, event.y) == "separator":
            return "break"
    
    def download_videos(self,):
        pass

    def configWindows(self, ):
        self.minsize(screen_w, screen_h)
        self.resizable(False, False)
        self.title("Youtuber Download Free")
        self.canvas = Canvas(
            self, bg="#f2f0f9", height=screen_h, width=screen_w, bd=0,
            highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y = 0)
        
        self.label_url = Label( self, text="URL", font="Helvetica 14", borderwidth=0,
            highlightthickness=0, relief="flat", bg="#F1F1F1",)
        self.label_url.place(x=20, y = 35)
        
        self.url_entry = Entry( self, bd=0, bg="#fffafa",
            highlightthickness=0, font="Helvetica 14", )
        
        self.url_entry.place(x=80, y = 20, width=450, height=54)
        
        self.botao_buscar = Button( self, image=self.img_button,  borderwidth=0, 
                                   highlightthickness=0, relief="flat", command=self.buscar_videos)
        
        self.botao_buscar.place(x=560,  y = 20)
        
        self.botao_download = Button( self, image=self.img_button,  borderwidth=0, 
                                   highlightthickness=0, relief="flat", command=self.download_videos)
        
        
        columns = ("c1", "c2", "c3", "c4")
        self.tree_view = ttk.Treeview(self, columns=columns, show="headings", height=20,)
        self.tree_view.heading("c1", text="Id")
        self.tree_view.heading("c2", text="Título")
        self.tree_view.heading("c3", text="Tamanho")
        self.tree_view.heading("c4", text="Resolução")
        self.tree_view.column("c1", minwidth=50, width=50, stretch= False) 
        self.tree_view.column("c2", minwidth=450, width=450, stretch= True) 
        self.tree_view.column("c3", minwidth=50, width=85, stretch= True) 
        self.tree_view.column("c4", minwidth=50, width=85, stretch= True) 
        self.tree_view.place(x= 80, y = 100)
        self.tree_view.tag_configure("ood", background="red")
        self.tree_view.tag_configure("ddd", background="blue")
        self.tree_view.bind('<Button-1>', self.handle_click)
        self.tree_view.bind("<Double-1>", self.OnDoubleClick)
    
    def OnDoubleClick(self, event):
        pass
           
    def buscar_videos(self, ):
        pass