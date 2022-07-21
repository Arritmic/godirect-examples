import logging
  



# from gdx_modules.gdx import gdx_class
# gdx = gdx_class()
#import gdx_modules.gdx


#Are these variable required outside the class? 
# woutput = wtext(text='')
# startbutton = None
# closebutton = None

class ver_vpython:


    closed = False
    running = False
    #period = 100

    def __init__(self):  
        """
        """

    def setup_canvas(self):

        # Can we install the vpython library with godirect?
        #from vpython import canvas, button, box, wtext, checkbox, rate
        from vpython import canvas, box, button

        # if they are using vpython, then create the canvas and start/stop/close buttons
        global startbutton, closebutton
        canvas(width=2, height=2)
        box()
        startbutton = button(text='Start', bind=vp_start_stop)
        canvas.get_selected().append_to_caption('  ')
        closebutton = button(text='Close', bind=vp_closed)


    def print_to_canvas(self):
        """ Discovers all Go Direct devices with a USB connection and opens those devices
        for data collection. 
		"""  
        from vpython import canvas

        canvas.get_selected().append_to_caption('Must specify device channels.')
        canvas.get_selected().caption = 'test caption'
        raise AttributeError('Must specify device channels.')     

    def start_button(self):
        if ver_vpython.running:
            return True
        else:
            return False

    def closed_button(self):
        if ver_vpython.closed:
            return True
        else:
            return False

    
def vp_start_stop(f):
    
    if f.text == 'Start':
        f.text = 'Stop'
        #print("ver python period = ", ver_vpython.period)
        #gdxvp.start(ver_vpython.period)
        # "Change the class variable’s value using the class name only."
        ver_vpython.running = True
        #vp.running = True
    else:
        f.text = 'Start'
        ver_vpython.running = False
        #gdxvp.stop()


def vp_closed():
    from vpython import rate

    ver_vpython.closed = True
    ver_vpython.running = False
    # gdx = gdx_modules.gdx.gdx()
    # #x = ver.readall() # clear things out
    # ver.running = False
    #gdxvp.stop()
    n = 0
    while True: # shut down gracefully
        rate(100)
        n += 1
        if n > 100: break
    #gdxvp.close()
    startbutton.delete()
    closebutton.delete()
    


   