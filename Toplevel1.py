import sys
import tkinter as tk
import tkinter.ttk as ttk
import ColorCovid_support
import Functionalities as fnc

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])
        top.geometry("561x403+255+104")
        top.minsize(120, 1)
        top.maxsize(1370, 729)
        top.resizable(1, 1)
        top.title("ColorCovid 2020")
        top.configure(background="#d9d9d9")
        self.root = top
        
        fnc_obj = fnc.Functionalities(self)
        
        # Menu bar
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="File")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="Exit")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Settings")
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                foreground="#000000",
                label="Help")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="Help")
        self.sub_menu12.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="About")

        # Notebook tab
        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Setup",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Acquisition", compound="left", underline="-1",)
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        #                                       Panel 1 (Setting)
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        
        # Labelframe
        self.VideoCaptionFrame = tk.LabelFrame(self.TNotebook1_t1)
        self.VideoCaptionFrame.place(relx=0.054, rely=0.053, height=250, width=170)
        self.VideoCaptionFrame.configure(relief='groove')
        self.VideoCaptionFrame.configure(foreground="black")
        self.VideoCaptionFrame.configure(text='''Available cameras''')
        self.VideoCaptionFrame.configure(background="#d9d9d9")

        # Listbox
        self.CameraListBox = tk.Listbox(self.VideoCaptionFrame)
        self.CameraListBox.place(relx=0.083, rely=0.152, relheight=0.8, relwidth=0.8, bordermode='ignore')
        self.CameraListBox.configure(activestyle="none")
        self.CameraListBox.configure(background="white")
        self.CameraListBox.configure(disabledforeground="#a3a3a3")
        self.CameraListBox.configure(font="TkFixedFont")
        self.CameraListBox.configure(foreground="#000000")
        self.CameraListBox.configure(justify='right')
        self.CameraListBox.configure(selectmode='single')
        self.CameraListBox.bind('<<ListboxSelect>>', fnc_obj.cameraListBoxSelectionChange)
        
        
        self.CameraImageHolderFrame = tk.LabelFrame(self.TNotebook1_t1)
        self.CameraImageHolderFrame.place(relx=0.198, rely=0.052, height=530, width=700)
        self.CameraImageHolderFrame.configure(relief='groove')
        self.CameraImageHolderFrame.configure(foreground="black")
        self.CameraImageHolderFrame.configure(text='''Camera frame''')
        self.CameraImageHolderFrame.configure(background="#d9d9d9")

        # Label for test image
        self.CameraImageHolder = tk.Label(self.CameraImageHolderFrame)
        self.CameraImageHolder.place(relx=0.5, rely=0.5, height=490, width=650, anchor=tk.CENTER)
        #self.CameraImageHolder.configure(background="#d9d9d9")
        #self.CameraImageHolder.configure(disabledforeground="#a3a3a3")
        #self.CameraImageHolder.configure(foreground="#000000")
        #self.CameraImageHolder.pack(padx=10, pady=10)

        # Test frame button
        self.TestSnapshotButton = tk.Button(self.TNotebook1_t1)
        self.TestSnapshotButton.place(relx=0.054, rely=0.743, height=34, width=117)
        self.TestSnapshotButton.configure(activebackground="#ececec")
        self.TestSnapshotButton.configure(activeforeground="#000000")
        self.TestSnapshotButton.configure(background="#d9d9d9")
        self.TestSnapshotButton.configure(disabledforeground="#a3a3a3")
        self.TestSnapshotButton.configure(foreground="#000000")
        self.TestSnapshotButton.configure(highlightbackground="#d9d9d9")
        self.TestSnapshotButton.configure(highlightcolor="black")
        self.TestSnapshotButton.configure(pady="0")
        self.TestSnapshotButton.configure(text='''Test''')
        self.TestSnapshotButton.configure(command=fnc_obj.getTestFrame)
        self.TestSnapshotButton.configure(state=tk.DISABLED)
        
        # Get cameras list button
        self.GetAvailableCamerasButton = tk.Button(self.TNotebook1_t1)
        self.GetAvailableCamerasButton.place(relx=0.054, rely=0.637, height=34, width=117)
        self.GetAvailableCamerasButton.configure(activebackground="#ececec")
        self.GetAvailableCamerasButton.configure(activeforeground="#000000")
        self.GetAvailableCamerasButton.configure(background="#d9d9d9")
        self.GetAvailableCamerasButton.configure(disabledforeground="#a3a3a3")
        self.GetAvailableCamerasButton.configure(foreground="#000000")
        self.GetAvailableCamerasButton.configure(highlightbackground="#d9d9d9")
        self.GetAvailableCamerasButton.configure(highlightcolor="black")
        self.GetAvailableCamerasButton.configure(pady="0")
        self.GetAvailableCamerasButton.configure(text='''Get cameras''')
        self.GetAvailableCamerasButton.configure(command=fnc_obj.getAvailableCameras)
        
        # Turn camera ON button
        self.TurnCameraON = tk.Button(self.TNotebook1_t1)
        self.TurnCameraON.place(relx=0.054, rely=0.477, height=24, width=117)
        self.TurnCameraON.configure(activebackground="#ececec")
        self.TurnCameraON.configure(activeforeground="#000000")
        self.TurnCameraON.configure(background="#d9d9d9")
        self.TurnCameraON.configure(disabledforeground="#a3a3a3")
        self.TurnCameraON.configure(foreground="#000000")
        self.TurnCameraON.configure(highlightbackground="#d9d9d9")
        self.TurnCameraON.configure(highlightcolor="black")
        self.TurnCameraON.configure(pady="0")
        self.TurnCameraON.configure(text='''Turn ON''')
        self.TurnCameraON.configure(state=tk.DISABLED)
        self.TurnCameraON.configure(command=fnc_obj.openCamera)
        
        # Turn camera OFF button
        self.TurnCameraOFF = tk.Button(self.TNotebook1_t1)
        self.TurnCameraOFF.place(relx=0.054, rely=0.557, height=24, width=117)
        self.TurnCameraOFF.configure(activebackground="#ececec")
        self.TurnCameraOFF.configure(activeforeground="#000000")
        self.TurnCameraOFF.configure(background="#d9d9d9")
        self.TurnCameraOFF.configure(disabledforeground="#a3a3a3")
        self.TurnCameraOFF.configure(foreground="#000000")
        self.TurnCameraOFF.configure(highlightbackground="#d9d9d9")
        self.TurnCameraOFF.configure(highlightcolor="black")
        self.TurnCameraOFF.configure(pady="0")
        self.TurnCameraOFF.configure(text='''Turn OFF''')
        self.TurnCameraOFF.configure(state=tk.DISABLED)
        self.TurnCameraOFF.configure(command=fnc_obj.closeCamera)
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        #                                       Panel 2 (Acquisition)
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------