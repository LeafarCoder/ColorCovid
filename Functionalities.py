import cv2
import tkinter as tk
from tkinter import messagebox
import Toplevel1 as tl
from PIL import Image, ImageTk

class Functionalities:
    
    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.activeCameraIndex = -1 # non connected yet
        self.activeCamera = None  # active camera object
        
    def getAvailableCameras(self):
        index = 0
        arr = []
        # iterate to get all cameras connected to the computer
        while True:
            cap = cv2.VideoCapture(index,cv2.CAP_DSHOW)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release() # close connection to camera
            index += 1
        
        self.toplevel.CameraListBox.delete(0,tk.END)
        for idx in arr:
            self.toplevel.CameraListBox.insert(tk.END, "Cam. {}".format(idx))
        
        if(len(arr)==0):
            messagebox.showinfo("Information","There no cameras available.")
            # deactivate buttons
            self.toplevel.TurnCameraOFF.configure(state=tk.DISABLED)
            self.toplevel.TurnCameraON.configure(state=tk.DISABLED)
        else:
            # unlock buttons
            self.toplevel.TestSnapshotButton.configure(state=tk.ACTIVE)
            self.toplevel.CameraListBox.selection_set(0)
            self.cameraListBoxSelectionChange(0)
            selection = int(self.toplevel.CameraListBox.get(self.toplevel.CameraListBox.curselection()).split(" ")[1])
            if(self.activeCameraIndex == selection):
                self.toplevel.TurnCameraON.configure(state=tk.DISABLED)
                self.toplevel.TurnCameraOFF.configure(state=tk.ACTIVE)
            else:
                self.toplevel.TurnCameraON.configure(state=tk.ACTIVE)
                self.toplevel.TurnCameraOFF.configure(state=tk.DISABLED)
               
            if(len(arr)==1):
                #messagebox.showinfo("Information","There is only one camera (default) available.")
                pass
            else:
                #messagebox.showinfo("Information","There are {} cameras available".format(len(arr)))
                pass

    def getTestFrame(self):
        
        selection_str = self.toplevel.CameraListBox.get(self.toplevel.CameraListBox.curselection())
        selection_idx = selection_str.split(" ")[1] # Cam + idx (keep idx)
        print(selection_idx)
        #self.toplevel.Label1.configure(image=img)
        vc = cv2.VideoCapture(selection_idx)
        # try to get the first frame
        rval, frame = vc.read()
        self.toplevel.Label1.configure(image=frame)
        vc.release()
        
    def openCamera(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        # try to get the first frame
        rval, frame = vc.read()

        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
        cv2.destroyWindow("preview")
        vc.release()

    def takeSnap(self):
        return 0
    
    def cameraListBoxSelectionChange(self, evt):
        selection_str = self.toplevel.CameraListBox.get(self.toplevel.CameraListBox.curselection())
        self.toplevel.TurnCameraOFF.configure(text="{}: Turn OFF".format(selection_str))
        self.toplevel.TurnCameraON.configure(text="{}: Turn ON".format(selection_str))
        
        selection = int(self.toplevel.CameraListBox.get(self.toplevel.CameraListBox.curselection()).split(" ")[1])
        if(self.activeCameraIndex == selection):
            self.toplevel.TurnCameraON.configure(state=tk.DISABLED)
            self.toplevel.TurnCameraOFF.configure(state=tk.ACTIVE)
        else:
            self.toplevel.TurnCameraON.configure(state=tk.ACTIVE)
            self.toplevel.TurnCameraOFF.configure(state=tk.DISABLED)
    
    def openCamera(self):
        selection = int(self.toplevel.CameraListBox.get(self.toplevel.CameraListBox.curselection()).split(" ")[1])
        if(self.activeCameraIndex != selection):
            self.activeCamera = cv2.VideoCapture(selection)
            self.activeCameraIndex = selection
            self.cameraListBoxSelectionChange(0)
            self.toplevel.GetAvailableCamerasButton.configure(state=tk.DISABLED)
            self.videoLoop()
    
    def videoLoop(self):
        if(self.activeCamera == None):
            return
        
        ok, frame = self.activeCamera.read()  # read frame from video stream
        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image))  # convert image for tkinter
            self.toplevel.CameraImageHolder.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.toplevel.CameraImageHolder.config(image=imgtk)  # show the image
            self.toplevel.root.after(100, self.videoLoop)  # repeat in loop

        
    def closeCamera(self):
        if(self.activeCamera!= None):
            self.activeCamera.release()
            self.activeCamera = None
            self.activeCameraIndex = -1
            self.toplevel.GetAvailableCamerasButton.configure(state=tk.ACTIVE)
            self.toplevel.CameraImageHolder.config(image=None)  # show the image
        self.cameraListBoxSelectionChange(0)