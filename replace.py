import fileinput

number_from_gain = 0
counter_gain = 0
gainFilename = ""

number_from_fqcyshift = 0
counter_fqcyshift = 0
fqcyshiftFilename = ""

number_from_Coherencefiltergain = 0
counter_Coherencefiltergain = 0
CoherencefiltergainFilename = ""

number_from_SCfiltergain = 0
counter_SCfiltergain = 0
SCfiltergainFilename = ""

number_from_fshiftgain = 0
counter_fshiftgain = 0
fshiftgainFilename = ""


number_from_LPfiltergain = 0
counter_LPfiltergain = 0
LPfiltergainFilename = ""

number_from_HPfiltergain = 0
counter_HPfiltergain = 0
HPfiltergainFilename = ""


def setVariableNull2():

    global counter_gain
    global counter_fqcyshift
    global counter_Coherencefiltergain
    global counter_SCfiltergain
    global counter_fshiftgain
    global counter_HPfiltergain
    global counter_LPfiltergain

    global number_from_gain
    global number_from_fqcyshift
    global number_from_Coherencefiltergain
    global number_from_SCfiltergain
    global number_from_fshiftgain
    global number_from_HPfiltergain
    global number_from_LPfiltergain

    replace_gain2(0)
    counter_gain = 0
    number_from_gain = 0

    replace_fqcyshift(300)
    counter_fqcyshift = 0
    number_from_fqcyshift = 0

    replace_Coherencefiltergain2(20)
    counter_Coherencefiltergain = 0
    number_from_Coherencefiltergain = 0

    replace_SCfiltergain2(20)
    counter_SCfiltergain = 0
    number_from_SCfiltergain = 0

    replace_fshiftgain2(20)
    counter_fshiftgain = 0
    number_from_fshiftgain = 0

    replace_HPfiltergain2(0)
    counter_HPfiltergain = 0
    number_from_HPfiltergain = 0

    replace_LPfiltergain2(0)
    counter_LPfiltergain = 0
    number_from_LPfiltergain = 0


def replace_value_file(variableFrom, variableTo, Filename) :

    with fileinput.FileInput(Filename,
                             inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(variableFrom,
                               variableTo), end='')



#------------------------------------------------------------------------------------------------------------------
#gain
#------------------------------------------------------------------------------------------------------------------

def generate_stringFile_gain_counter0(number_to):

    global gainFilename
    variable_counterNULL_from = "mha.gain.gains = [ " + str(0) + " " + str(0) + " ]"
    variable_to = "mha.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
    gainFilename = 'gain_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_gain(number_to):

    variable_from = "mha.gain.gains = [ " + str(number_from_gain) + " " + str(number_from_gain) + " ]"
    variable_to = "mha.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"

    return variable_from, variable_to


def replace_gain2(number_to):

    global counter_gain
    global number_from_gain
    global gainFilename

    if counter_gain == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_gain_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, gainFilename)
        number_from_gain = number_to

    else :

        variable_from, variable_to = generate_stringFile_gain(number_to)
        replace_value_file(variable_from, variable_to, gainFilename)
        number_from_gain = number_to

    counter_gain = counter_gain + 1
    print("counter_gain = ", counter_gain)


#------------------------------------------------------------------------------------------------------------------
#end gain
#------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------
#fqcyshift
#------------------------------------------------------------------------------------------------------------------

def generate_stringFile_fqcyshift_counter0(number_to):

    global fqcyshiftFilename
    variable_counterNULL_from = "mha.mhachain.fshift.df = " + str(300)
    variable_to = "mha.mhachain.fshift.df = " + str(number_to)
    fqcyshiftFilename = 'fbc_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_fqcyshift(number_to):

    variable_from = "mha.mhachain.fshift.df = " + str(number_from_fqcyshift)
    variable_to = "mha.mhachain.fshift.df = " + str(number_to)

    return variable_from, variable_to


def replace_fqcyshift(number_to):

    global counter_fqcyshift
    global number_from_fqcyshift
    global fqcyshiftFilename

    if counter_fqcyshift == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_fqcyshift_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, fqcyshiftFilename)
        number_from_fqcyshift = number_to

    else :

        variable_from, variable_to = generate_stringFile_fqcyshift(number_to)
        replace_value_file(variable_from, variable_to, fqcyshiftFilename)
        number_from_fqcyshift = number_to

    counter_fqcyshift = counter_fqcyshift + 1
    print("counter_fqcyshift = ", counter_fqcyshift)


#frequencyshift upgrade gain------------------------------------------------------------------------


def generate_stringFile_fshiftgain_counter0(number_to):

    global fshiftgainFilename
    variable_counterNULL_from = "mha.mhachain.altplugs.gain.gains = [ " + str(20) + " " + str(20) + " ]"
    variable_to = "mha.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
    fshiftgainFilename = 'fbc_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_fshiftgain(number_to):

    variable_from = "mha.mhachain.altplugs.gain.gains = [ " + str(number_from_fshiftgain) + " " + str(number_from_fshiftgain) + " ]"
    variable_to = "mha.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"

    return variable_from, variable_to


def replace_fshiftgain2(number_to):

    global counter_fshiftgain
    global number_from_fshiftgain
    global fshiftgainFilename

    if counter_fshiftgain == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_fshiftgain_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, fshiftgainFilename)
        number_from_fshiftgain = number_to

    else :

        variable_from, variable_to = generate_stringFile_fshiftgain(number_to)
        replace_value_file(variable_from, variable_to, fshiftgainFilename)
        number_from_fshiftgain = number_to

    counter_fshiftgain = counter_fshiftgain + 1
    print("counter_fshiftgain = ", counter_fshiftgain)



#end frequencyshift upgrade gain------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#end fqcyshift
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#Coherence filter upgrade gain
#------------------------------------------------------------------------------------------------------------------



def generate_stringFile_Coherencefiltergain_counter0(number_to):

    global CoherencefiltergainFilename
    variable_counterNULL_from = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(20) + " " + str(20) + " ]"
    variable_to = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
    CoherencefiltergainFilename = 'coherence_gain_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_Coherencefiltergain(number_to):

    variable_from = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_from_Coherencefiltergain) + " " + str(number_from_Coherencefiltergain) + " ]"
    variable_to = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"

    return variable_from, variable_to


def replace_Coherencefiltergain2(number_to):

    global counter_Coherencefiltergain
    global number_from_Coherencefiltergain
    global CoherencefiltergainFilename

    if counter_Coherencefiltergain == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_Coherencefiltergain_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, CoherencefiltergainFilename)
        number_from_Coherencefiltergain = number_to

    else :

        variable_from, variable_to = generate_stringFile_Coherencefiltergain(number_to)
        replace_value_file(variable_from, variable_to, CoherencefiltergainFilename)
        number_from_Coherencefiltergain = number_to

    counter_Coherencefiltergain = counter_Coherencefiltergain + 1
    print("counter_Coherencefiltergain = ", counter_Coherencefiltergain)


#------------------------------------------------------------------------------------------------------------------
#End coherence filter upgrade gain
#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
#SC noise reduction filter upgrade gain
#------------------------------------------------------------------------------------------------------------------



def generate_stringFile_SCfiltergain_counter0(number_to):

    global SCfiltergainFilename
    variable_counterNULL_from = "mha.mhachain.altplugs.gain.gains = [ " + str(20) + " " + str(20) + " ]"
    variable_to = "mha.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
    SCfiltergainFilename = 'scdenoising_gain_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_SCfiltergain(number_to):

    variable_from = "mha.mhachain.altplugs.gain.gains = [ " + str(number_from_SCfiltergain) + " " + str(number_from_SCfiltergain) + " ]"
    variable_to = "mha.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"

    return variable_from, variable_to


def replace_SCfiltergain2(number_to):

    global counter_SCfiltergain
    global number_from_SCfiltergain
    global SCfiltergainFilename

    if counter_SCfiltergain == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_SCfiltergain_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, SCfiltergainFilename)
        number_from_SCfiltergain = number_to

    else :

        variable_from, variable_to = generate_stringFile_SCfiltergain(number_to)
        replace_value_file(variable_from, variable_to, SCfiltergainFilename)
        number_from_SCfiltergain = number_to

    counter_SCfiltergain = counter_SCfiltergain + 1
    print("counter_SCfiltergain = ", counter_SCfiltergain)



#------------------------------------------------------------------------------------------------------------------
#end SC noise reduction upgrade gain
#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
#High pass filter gain
#------------------------------------------------------------------------------------------------------------------


def generate_stringFile_HPfiltergain_counter0(number_to):

    global HPfiltergainFilename
    variable_counterNULL_from = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(0) + " " + str(0) + " ]"
    variable_to = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
    HPfiltergainFilename = 'dc_highpass_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_HPfiltergain(number_to):

    variable_from = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_from_HPfiltergain) + " " + str(number_from_HPfiltergain) + " ]"
    variable_to = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"

    return variable_from, variable_to


def replace_HPfiltergain2(number_to):

    global counter_HPfiltergain
    global number_from_HPfiltergain
    global HPfiltergainFilename

    if counter_HPfiltergain == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_HPfiltergain_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, HPfiltergainFilename)
        number_from_HPfiltergain = number_to

    else :

        variable_from, variable_to = generate_stringFile_HPfiltergain(number_to)
        replace_value_file(variable_from, variable_to, HPfiltergainFilename)
        number_from_HPfiltergain = number_to

    counter_HPfiltergain = counter_HPfiltergain + 1
    print("counter_HPfiltergain = ", counter_HPfiltergain)



#------------------------------------------------------------------------------------------------------------------
#High pass filter gain
#------------------------------------------------------------------------------------------------------------------




#------------------------------------------------------------------------------------------------------------------
#Low pass filter gain
#------------------------------------------------------------------------------------------------------------------




def generate_stringFile_LPfiltergain_counter0(number_to):

    global LPfiltergainFilename
    variable_counterNULL_from = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(0) + " " + str(0) + " ]"
    variable_to = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
    LPfiltergainFilename = 'dc_lowpass_live.cfg'

    return variable_counterNULL_from, variable_to


def generate_stringFile_LPfiltergain(number_to):

    variable_from = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_from_LPfiltergain) + " " + str(number_from_LPfiltergain) + " ]"
    variable_to = "mha.overlapadd.mhachain.altplugs.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"

    return variable_from, variable_to


def replace_LPfiltergain2(number_to):

    global counter_LPfiltergain
    global number_from_LPfiltergain
    global LPfiltergainFilename

    if counter_LPfiltergain == 0:

        variable_counterNULL_from, variable_to = generate_stringFile_LPfiltergain_counter0(number_to)
        replace_value_file(variable_counterNULL_from, variable_to, LPfiltergainFilename)
        number_from_LPfiltergain = number_to

    else :

        variable_from, variable_to = generate_stringFile_LPfiltergain(number_to)
        replace_value_file(variable_from, variable_to, LPfiltergainFilename)
        number_from_LPfiltergain = number_to

    counter_LPfiltergain = counter_LPfiltergain + 1
    print("counter_LPfiltergain = ", counter_LPfiltergain)




#------------------------------------------------------------------------------------------------------------------
#end Low pass filter gain
#------------------------------------------------------------------------------------------------------------------