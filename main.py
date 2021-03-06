from gui import AppInicial
import threading
import pytube
from tkinter import ttk
from tkinter import *

class App(AppInicial):
    def __init__(self,) -> None:
        super().__init__()
        self.label_carregando = Label( self, text="Carregando...", 
            font=("MulishRoman Bold", 12 * -1), borderwidth=0, bg="#FFFFFF",
            highlightthickness=0, relief="flat", )
        
        self.progres_1 = ttk.Progressbar(self, orient=HORIZONTAL, length=300, 
                                         mode="indeterminate")
        self.lista_videos = []
        self.position_download = 0
        
    
    def on_progress(self, stream, chunk, bytes_remaining):
        item = self.tree.get_children(0)
        
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.tree.set(item[self.position_download], column=2,
                    value=f"{round(percentage_of_completion, 2)} %")
    
    def downloag_video(self, ):
        chunk_size = 1024
        path_destino = "./assets/download/"
        self.progres_1.start()
        self.progres_1.place(x=26,  y = 470)
        
        for i, x in enumerate(self.lista_videos):
            pos = i + 1
            self.position_download = i
            
            video = x.streams.get_highest_resolution()
            x.register_on_progress_callback(self.on_progress)
         
            video.download(path_destino)
        self.progres_1.stop()
        self.progres_1.place_forget()
        
        
    def download_videos(self,):        
        threading.Thread(target=self.downloag_video).start()
        
        
    def getVideos(self, url):
        self.tree.delete(*self.tree.get_children())
        self.lista_videos = []
        v = pytube.Channel(url)
        for i, yt in enumerate(v.videos):
            #round(resolucao.filesize * 0.000001, 2)
            if i > 3:
                break
            self.lista_videos.append(yt)
            self.tree.insert("", "end",  values=(i, yt.title, "--", 0))

        self.progres_1.stop()
        self.progres_1.place_forget()
        self.label_carregando.place_forget()
        #self.botao_download.place(x=540,  y = 540)
        
        self.button_download.place(
            x=429.0,
            y=450,
            width=111.0,
            height=47.0
        )
        
    def OnDoubleClick(self, event):
        
        item = self.tree.selection()
        #print("you clicked on", self.tree_view.item(item, "values")[0])
    
    def buscar_videos(self, ):
        self.progres_1.start()
        self.progres_1.place(x=26,  y = 470)
        self.label_carregando.place(x=26, y = 450)
        #self.botao_download.place_forget()
        url = self.url_entry.get()
        t = threading.Thread(target=self.getVideos, args=(url,)).start()
        
if __name__ == "__main__":
    App().mainloop()