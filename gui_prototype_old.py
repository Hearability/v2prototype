from tkinter import*
from research import*
import os
#==================================================================
# simple functions just to test if the gui interface work fine. This section must be commented afterwords, and the next one should be filled
# with the right file names and uncommented


root = Tk()
ON = False
gainb = 0
input_text = IntVar()

"""
def btnClick_On():

    global ON
    ON = True
    print('test On ok')


def btnClick_Off():

    global ON
    global counter
    global gainb

    ON = False
    setVariableNull()
    gainb = 0
    print('test Off ok')


def btnClick_GainOn():

    global ON
    if ON == True :
        print('test Gain On ok')

    else:
        print('On is not activated, please press On to launch the Jack server')


def btnClick_UpdateGain():

    global gainb
    global input_text
    global input
    global ON

    if ON == True:
        # gainupdate_int = int("input_text")
        gainupdate_int = input_text.get()

        if (gainupdate_int > -41) & (gainupdate_int < 51):
            replace_gain(gainupdate_int)
            gainb = gainupdate_int
            # gainnew = gainb + gainupdate_int
            print(gainb)

        else:
            print('the value of the gain is outside the bounds [gmin, gmax]')

    else:
        print('On is not activated, please press On to launch the Jack server')



def btnClick_GainUp():

    global ON
    if ON == True :
        global gainb
        gainup = 5
        gainb = gainb + gainup

        if (gainb > -41) & (gainb < 51):
            replace_gain(gainb)
            print(gainb)
        else:
            print('the value of the gain is outside the bounds [gmin, gmax]')
    else:
        print('On is not activated, please press On to launch the Jack server')


def btnClick_GainDown():

    global ON
    if ON == True:
        global gainb
        gaindown = 5
        gainb = gainb - gaindown

        if (gainb > -41) & (gainb < 51):
            replace_gain(gainb)
            print(gainb)
        else:
            print('the value of the gain is outside the bounds [gmin, gmax]')
    else:
        print('On is not activated, please press On to launch the Jack server')


def btnClick_CoherenceOn():

    global ON
    if ON == True :
        print('test Coherence On ok')
    else:
        print('On is not activated, please press On to launch the Jack server')


def btnClick_SCNoiseReductionOn():

    global ON
    if ON == True :
        print('test SC Noise Reduction On ok')
    else:
        print('On is not activated, please press On to launch the Jack server')


def btnClick_DCOn():

    global ON
    if ON == True :
        print('test DC On ok')
    else:
        print('On is not activated, please press On to launch the Jack server')



#==================================================================
# end of the test gui interface
"""



#==================================================================
# definition of the function for the buttons, which call the openMHA cfg files


def btnClick_On():
    
    global ON
    ON = True
    #launch the jack server
    os.system('./startdemo.sh')


def btnClick_Off():

    global ON
    global counter
    global gainb
    
    ON = False
    # kill the mha program already running
    os.system('killall mha -9')
    # kill the jack server
    os.system('killall jackd -9')
    setVariableNull()
    gainb = 0
    print('test Off ok')


def btnClick_GainOn():
    
    global ON
    if ON == True :

        # go to the directory where the config file gain_live.cfg is
        #os.system('cd ./filepath/')
        # kill the mha program already running
        os.system('killall mha -9')
        # start to run the config file gain_live.cfg with the updated gain value
        os.system('mha ?read:gain_live.cfg cmd=start &')

    else:
        print('On is not activated, please press On to launch the Jack server')



def btnClick_UpdateGain():

    global gainb
    global input_text
    global input
    global ON

    if ON == True:
        # gainupdate_int = int("input_text")
        gainupdate_int = input_text.get()

        if (gainupdate_int > -41) & (gainupdate_int < 51):
            replace_gain(gainupdate_int)
            gainb = gainupdate_int
            # gainnew = gainb + gainupdate_int
            print(gainb)
            
            # go to the directory where the config file gain_live.cfg is
            #os.system('cd ./filepath/')
            # kill the mha program already running
            os.system('killall mha -9')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:gain_live.cfg cmd=start &')

        else:
            print('the value of the gain is outside the bounds [gmin, gmax]')

    else:
        print('On is not activated, please press On to launch the Jack server')
       

def btnClick_GainUp():

    global ON
    
    if ON == True :
        global gainb
        gainup = 5
        gainb = gainb + gainup

        if (gainb > -41) & (gainb < 51):  # values should be replaced by the values of gmin and gmax in the file gain_live.cfg
            
            replace_gain(gainb)
            print(gainb)
            # go to the directory where the config file gain_live.cfg is
            #os.system('cd ./filepath/')
            # kill the mha program already running
            os.system('killall mha -9')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:gain_live.cfg cmd=start &')

        else:
            print('the value of the gain is outside the bounds [gmin, gmax]')

    else:
        print('On is not activated, please press On to launch the Jack server')



def btnClick_GainDown():

    global ON
    if ON == True :

        global gainb
        gaindown = 5
        gainb = gainb - gaindown

        if (gainb > -41) & (gainb < 51):  # values should be replaced by the values of gmin and gmax in the file gain_live.cfg
            
            replace_gain(gainb)
            print(gainb)
            # go to the directory where the config file gain_live.cfg is
            #os.system('cd ./filepath/')
            # kill the mha program already running
            os.system('killall mha -9')
            # replace the variable of the gain of the cfg file by increasing it by the gain entered in parameters
            #os.system('mha ?addsubst:<gains = [10 10]> <gains = [gainb gainb]>')  # if accepted...
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:gain_live.cfg cmd=start &')

        else:
            print('the value of the gain is outside the bounds [gmin, gmax]')

    else:
        print('On is not activated, please press On to launch the Jack server')



def btnClick_CoherenceOn():

    global ON
    if ON == True :

        # go to the directory where the config file coherence_live.cfg is
        #os.system('cd ./filepath/')
        # kill the mha program already running
        os.system('killall mha -9')
        # start to run the config file gain_live.cfg with the updated gain value
        os.system('mha ?read:coherence_gain_live.cfg cmd=start &')  # check the right name of the file

    else:
        print('On is not activated, please press On to launch the Jack server')



def btnClick_SCNoiseReductionOn():

    global ON
    if ON == True :

        # go to the directory where the config file SCNoiseReduction_live.cfg is
        #os.system('cd ./filepath/')
        # kill the mha program already running
        os.system('killall mha -9')
        # start to run the config file gain_live.cfg with the updated gain value
        os.system('mha ?read:denoising.cfg cmd=start &')  # check the right name of the file

    else:
        print('On is not activated, please press On to launch the Jack server')


def btnClick_DCOn():

    global ON
    if ON == True :

        # ideally one should at first place load the gain table 'gcdata' of the user profile retrieve with the ma gui interface
        # then change the value of the gain table'gc_data' in the config file dynamic_compression_live.cfg by this new 'gcdata'
        # for that one can use the mha command "os.system('mha ?addsubst:<gains = [10 10]> <gains = [gainb gainb]>')"
        # go to the directory where the config file dynamic_compression_live.cfg is
        #os.system('cd ./filepath/')
        # kill the mha program already running
        os.system('killall mha -9')
        # start to run the config file gain_live.cfg with the updated gain value
        #os.system('mha ?read:dynamic_compression_live.cfg cmd=start &')  # check the right name of the file

    else:
        print('On is not activated, please press On to launch the Jack server')



#-----------------------------------------------------------------------------------------------------------
# end of the defintion of the functions


#-----------------------------------------------------------------------------------------------------------
# gui interface



root.title("Openmha GUI")

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

#f1 = Frame(root, width=300, height=700, bg="powder blue", relief=SUNKEN)
#f1.pack(side=RIGHT)

f2 = Frame(root, width=1200, height=1200, bg="powder blue", relief=SUNKEN)
f2.pack(side=LEFT)

#f3 = Frame(root, width=1200, height=700, bg="powder blue", relief=SUNKEN)
#f3.pack(side=TOP)

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="OpenMHA control command", fg="Steel blue", bd=10, anchor="w")
lblInfo.grid(row = 0, column = 0)

txtDisplay = Entry(f2, font=("Arial", 20, "bold"), bd=30, insertwidth = 4, bg='powder blue', justify  ='right')
txtDisplay.grid(columnspan=4)

input_frame = Frame(txtDisplay, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT).pack()



btn1 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="On", bg = "powder blue",
              command=lambda:btnClick_On()).grid(row = 3, column=150)

btn2 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="Off", bg = "powder blue",
              command=lambda:btnClick_Off()).grid(row = 4, column=150)

btn3 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="Gain On", bg = "powder blue",
              command=lambda:btnClick_GainOn()).grid(row = 1, column=0)

btn4 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="+", bg = "powder blue",
              command=lambda:btnClick_GainUp()).grid(row = 1, column=1)

btn5 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="-", bg = "powder blue",
              command=lambda:btnClick_GainDown()).grid(row = 1, column=2)

btn6 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="Coherence filter On", bg = "powder blue",
              command=lambda:btnClick_CoherenceOn()).grid(row = 2, column=1)

btn7 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="SC Noise Reduction On", bg = "powder blue",
              command=lambda:btnClick_SCNoiseReductionOn()).grid(row = 3, column=1)

btn8 = Button(f2, padx = 16, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="Dynamic compression On", bg = "powder blue",
              command=lambda:btnClick_DCOn()).grid(row = 4, column=1)

btn9 = Button(f2, padx = 32, pady = 16, bd =18, fg = "black", font=('arial', 20, 'bold'), text="update gain", bg = "powder blue",
              command=lambda:btnClick_UpdateGain()).grid(row =0, column=100)
#----------------------------------------------------------------------------------------------------------------------------
#end gui interface

root.mainloop()




