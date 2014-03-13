#!/usr/bin/env python
"""
Tkinter GUI for PiPark setup.

Allows the user to perform all setup tasks including: mark parking spaces, set
control points and register the car park with the server. The main PiPark
program can be invoked from the menu.

Author: Nicholas Sanders
Version: 0.1 [2014/03/12]

"""
import os
import Tkinter as tk
import tkMessageBox
from PIL import Image, ImageTk

import imageread
import main
import settings as s

# ==============================================================================
#
#   Application Class
#
# ==============================================================================
class Application(tk.Frame):

    # --------------------------------------------------------------------------
    #   Instance Attributes
    # --------------------------------------------------------------------------
    
    # print messages to the terminal?
    __is_verbose = False
    
    # image load/save locoations
    SETUP_IMAGE = "./images/setup.jpeg"
    DEFAULT_IMAGE = "./images/default.jpeg"
    
    
    # --------------------------------------------------------------------------
    #   Constructor Method
    # --------------------------------------------------------------------------
    def __init__(self, master = None):

        # run super constructor method
        tk.Frame.__init__(self, master)
        
        # set alignment inside the frame
        self.grid()
        
        # create widgets
        self.createDisplay()
        self.createMenu()
            
        # if setup image exists then load it, otherwise load the default image
        # TODO: Add load setup image functionality.
        # if not loadImage(self.SETUP_IMAGE, self.display): 
        #   loadImage(self.DEFAULT_IMAGE, self.display)
        
    
    # --------------------------------------------------------------------------
    #   Load Setup Image
    # --------------------------------------------------------------------------
    def loadImage(image_address = "./", canvas = None):
        """
        Load image at image_address. If the load is successful then return True,
        otherwise return False.
        
        Keyword Arguments:
        image_address -- The address of the image to be loaded (default = './').
        canvas -- The Tkinter Canvas into which the image is loaded.
        
        Returns:
        Boolean -- True if load successful, False if not.
        
        """
        
        try:
            # guard against incorrect datatypes
            if not isinstance(canvas, tk.Canvas): raise TypeError
            if not isinstance(image_address, str): raise TypeError
            
            # load the image into the canvas
            # TODO: load the image into the canvas.
            
            return True
        
        # TODO: Complete loadImage() exception handling.
        except TypeError:
            # image failed to load
            if self.__is_verbose: 
                print "ERROR: loadImage(" + image_address + ") failed to load."
            return False
        except:
            return False


    # --------------------------------------------------------------------------
    #   Key Press Handler
    # --------------------------------------------------------------------------
    def returnPressHandler(self, event):
        return True
        
        
    # --------------------------------------------------------------------------
    #   Take New Setup Image
    # --------------------------------------------------------------------------
    def newSetupImage(self):
        """
        Instruct the user to take a new setup image. Then save the image
        to the specified location 'SETUP_IMAGE_ADDRESS', and finally load the
        new image into the GUI.

        """
        # show quick dialogue box with basic instruction
        tkMessageBox.showinfo(title = "",
            message = "Press the ENTER key to take a new setup image.")

        # initialise the camera using the settings in the imageread module
        try:
            camera = imageread.setup_camera(is_fullscreen = False)
            camera.start_preview()
        except:
            tkMessageBox.showerror(title = "Error!",
                message = "Error: Failed to setup and start PiCam.")
        
        # capture and save a new setup image when the ENTER key is pressed
        # FIXME: Ensure focus isn't lost when camera is initialised.
        while True:
            if self.bind(<Return>, returnPressHandler): 
                camera.capture(self.SETUP_IMAGE_ADDRESS)
                break
        
        # end the preview and close the camera.
        camera.stop_preview()
        camera.close()

    
    # --------------------------------------------------------------------------
    #   Button Handlers
    # --------------------------------------------------------------------------
    def clickQuit(self):
        """Quit terminate the application. """
        
        # TODO: Add yes/no option after seleciton.
        self.quit()
        self.master.destroy()

    def clickSpaces(self):
        """Add/remove parking-space bounding boxes. """
        
        print "ACTION: Clicked 'Add/Remove Spaces'"
        # add spaces with two clicks (start & end corner points)
        # removal of spaces whilst holding CTRL and click in box

    def clickCPs(self):
        """Add/remove control points. """
        
        print "ACTION: Clicked 'Add/Remove Control Points'"
        # add CPs with single click
        # removal of CPs whilst holding CTRL and click

    def clickRegister(self):
        """Register the car park with the server. """
        
        print("ACTION: Clicked 'Register'")
        # register with the server as per CLI setup

    def clickNewImage(self):
        """Use PiCam to take new 'setup image' for PiPark setup. """
        
        # clear the current image in the GUI, then take a new image using the
        # PiCam, then load the new image into the GUI
        # TODO: clear current image in GUI
        self.newSetupImage()
        # TODO: load new setup image into GUI

    def clickStart(self):
        """
        Close the current setup application, then initiate the main
        PiPark program.

        """

        # if the user is positive, close the setup and run the main program
        if tkMessageBox.askyesno(title = "Setup Complete",
                message = "Are you ready to leave setup and run PiPark?"):
            self.quit_button.invoke()
            main.run_main()

    def clickAbout(self):
        """Open the README file for instructions on GUI use. """
        
        # load external README from command line
        os.system("leafpad " + "./SETUP_README.txt")
        

    # --------------------------------------------------------------------------
    #   Create Image Display Canvas
    # --------------------------------------------------------------------------
    def createDisplay(self):
        self.display = tk.Canvas(self, width = 960, height = 540)
        self.display.grid(row = 1, column = 0, columnspan = 7)


    # --------------------------------------------------------------------------
    #   Create Options Menu
    # --------------------------------------------------------------------------
    def createMenu(self):
        PADDING = 10;

        # draw a background for the menu on a new canvas
        self.bg = tk.Canvas(self, width = 960, height = 40)
        self.bg.grid(row = 0, column = 0, columnspan = 7)
        self.bg.create_rectangle(0, 0, 960, 50, fill = "grey")
        
        # about button - display information about PiPark
        self.about_button = tk.Button(self, text = "Open README",
            command = self.clickAbout, padx = PADDING)
        self.about_button.grid(row = 0, column = 5)

        # add/remove spaces button
        self.spaces_button = tk.Button(self, text = "Add/Remove Spaces",
            command = self.clickSpaces, padx = PADDING)
        self.spaces_button.grid(row = 0, column = 3)

        # add/remove control points button
        self.cps_button = tk.Button(self, text = "Add/Remove Control Points",
            command = self.clickCPs, padx = PADDING)
        self.cps_button.grid(row = 0, column = 4)

        # take new setup image button
        self.image_button = tk.Button(self, text = "Take New Setup Image",
            command = self.clickNewImage, padx = PADDING)
        self.image_button.grid(row = 0, column = 1)

        # register the car park button
        self.register_button = tk.Button(self, text = "Register",
            command = self.clickRegister, padx = PADDING)
        self.register_button.grid(row = 0, column = 2)

        # start the main program
        self.start_button = tk.Button(self, text = "Start PiPark",
            command = self.clickStart, padx = PADDING)
        self.start_button.grid(row = 0, column = 0)

        # quit setup
        self.quit_button = tk.Button(self, text = "Quit",
            command = self.clickQuit, padx = PADDING)
        self.quit_button.grid(row = 0, column = 6)


    # --------------------------------------------------------------------------
    #   Get/Set Is Verbose?
    # --------------------------------------------------------------------------
    def getIsVerbose():
        return self.__is_verbose
    
    def setIsVerbose(value):
        if isinstance(value, bool): __is_verbose = value


# ==============================================================================
#
#   Run Main Program
#
# ==============================================================================  
if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.master.title("PiPark Setup")
    app.mainloop()