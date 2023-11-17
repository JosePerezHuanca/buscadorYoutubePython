import wx;
from googleapiclient.discovery import build;
import subprocess;
from dotenv import load_dotenv;
import os;

load_dotenv();


clabeapi =os.getenv('API_KEY');

youtube = build('youtube', 'v3', developerKey=clabeapi)

class mainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(mainWindow, self).__init__(*args, **kw)
        self.panel = wx.Panel(self)
        caja = wx.BoxSizer(wx.VERTICAL)
        labelbuscar = wx.StaticText(self.panel, label='Busca algo')
        caja.Add(labelbuscar, 0, wx.ALL, 5)
        self.textobusqueda = wx.TextCtrl(self.panel)
        caja.Add(self.textobusqueda, 0, wx.ALL, 5)
        buscarboton = wx.Button(self.panel, label='Buscar')
        buscarboton.Bind(wx.EVT_BUTTON, self.buscarMethod)
        caja.Add(buscarboton, 0, wx.ALL, 5)
        labelLista = wx.StaticText(self.panel, label='Resultados')
        caja.Add(labelLista, 0, wx.ALL, 5)

        # Cuadrícula con dos columnas: Videos y Reproducir
        grid_sizer = wx.GridBagSizer(vgap=5, hgap=5)
        self.resultadosLista = wx.ListCtrl(self.panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.resultadosLista.InsertColumn(0, 'Videos', width=200)
        grid_sizer.Add(self.resultadosLista, pos=(0, 0), flag=wx.EXPAND)
        caja2 = wx.BoxSizer(wx.VERTICAL)
        self.boton_reproducir = wx.Button(self.panel, label='Reproducir', size=(100, -1))
        self.boton_reproducir.Bind(wx.EVT_BUTTON, self.reproducirMethod)
        caja2.Add(self.boton_reproducir, 0, wx.ALL, 5)
        grid_sizer.Add(caja2, pos=(0, 1), flag=wx.EXPAND)
        caja.Add(grid_sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(caja)
        self.urls = []
        self.reproductor=None;

    def buscarMethod(self, event):
        try:
            texto = self.textobusqueda.GetValue()
            searchRequest = youtube.search().list(q=texto, type='video', part='id,snippet', maxResults=100).execute()
            self.resultadosLista.DeleteAllItems()
            self.boton_reproducir.Enable(False)
            self.urls = []
            for idx, result in enumerate(searchRequest.get('items', [])):
                videotitle = result['snippet']['title']
                self.resultadosLista.InsertItem(idx, videotitle)
                video_url = f'https://youtube.com/watch?v={result["id"]["videoId"]}'
                self.urls.append(video_url)
                self.boton_reproducir.Enable(True)
        except Exception as e:
            wx.MessageBox(str(e));

    def reproducirMethod(self, event):
        try:
            seleccion = self.resultadosLista.GetFirstSelected()
            if seleccion != -1:
                video_url = self.urls[seleccion]
                if(self.reproductor):
                    self.reproductor.terminate();
                # Abre el enlace de YouTube en el reproductor
                self.reproductor=subprocess.Popen(['PotPlayerMini64', video_url]);
            else:
                wx.MessageBox('Se produjo un error al reproducir el video');
        except Exception as e:
            wx.MessageBox(str(e));

app = wx.App()
mainwindow = mainWindow(None, title='Buscador de YouTube')
mainwindow.Show()
app.MainLoop()
