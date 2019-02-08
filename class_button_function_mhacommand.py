from tkinter import*
from replace import*
import os



class Person:

    def __init__(self):
        self.gainbb = 0
        self.ONbb = False
        self.gainbb = 0
        self.fqcybb = 300
        self.gainCoherencebb = 20
        self.gainSCbb = 20
        self.gainfshiftbb = 20
        self.gainHPfilterbb = 0
        self.gainLPfilterbb = 0


    def BtnClick_On(self):

        self.ONbb = True
        # launch the jack server
        os.system('./startdemo.sh')


    def BtnClick_Off(self):

        setVariableNull2()
        self.ONbb = False
        self.gainbb = 0
        self.fqcybb = 0
        self.gainCoherencebb = 20
        self.gainSCbb = 20
        self.gainfshiftbb = 20
        self.gainHPfilterbb = 0
        self.gainLPfilterbb = 0

        # kill the mha program already running
        os.system('killall mha -9')
        # kill the jack server
        os.system('killall jackd -9')
        print('test Off ok')


    def BtnClick_GainOn(self):

        if self.ONbb == True:
            # kill the mha program already running
            os.system('killall mha -9')
            os.system('sleep 1')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:gain_live.cfg cmd=start &')
            print('test Gain On ok')

        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_UpdateGain(self, input_text):

        if self.ONbb == True:
            gainupdate_int = input_text.get()

            if (gainupdate_int > -41) & (gainupdate_int < 51):
                replace_gain2(gainupdate_int)
                self.gainbb = gainupdate_int
                print(self.gainbb)

                # kill the mha program already running
                os.system('killall mha -9')
                os.system('sleep 1')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:gain_live.cfg cmd=start &')

            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_GainUp(self):

        if self.ONbb == True:

            gainup = 5
            self.gainbb = self.gainbb + gainup

            if (self.gainbb > -41) & (self.gainbb < 51):
                replace_gain2(self.gainbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:gain_live.cfg cmd=start &')
                print(self.gainbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_GainDown(self):

        if self.ONbb == True:

            gaindown = 5
            self.gainbb = self.gainbb - gaindown

            if (self.gainbb > -41) & (self.gainbb < 51):
                replace_gain2(self.gainbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:gain_live.cfg cmd=start &')
                print(self.gainbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_CoherenceOn(self):

        if self.ONbb == True:
            # kill the mha program already running
            os.system('killall mha -9')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:coherence_gain_live.cfg cmd=start &')  # check the right name of the file
            print('test Coherence On ok')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_CoherenceGainUp(self):

        if self.ONbb == True:
            gainup = 5
            self.gainCoherencebb = self.gainCoherencebb + gainup

            if (self.gainCoherencebb > -41) & (self.gainCoherencebb < 51):
                replace_SCfiltergain2(self.gainCoherencebb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:coherence_gain_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainCoherencebb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_CoherenceGainDown(self):

        if self.ONbb == True:
            gaindown = 5
            self.gainCoherencebb = self.gainCoherencebb - gaindown

            if (self.gainCoherencebb > -41) & (self.gainCoherencebb < 51):
                replace_Coherencefiltergain2(self.gainCoherencebb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:coherence_gain_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainCoherencebb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_SCNoiseReductionOn(self):

        if self.ONbb == True:
            # kill the mha program already running
            os.system('killall mha -9')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:scdenoising_gain_live.cfg cmd=start &')  # check the right name of the file
            print('test SC Noise Reduction On ok')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_SCNoiseReductionGainUp(self):

        if self.ONbb == True:
            gainup = 5
            self.gainSCbb = self.gainSCbb + gainup

            if (self.gainSCbb > -41) & (self.gainSCbb < 51):
                replace_SCfiltergain2(self.gainSCbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:scdenoising_gain_live.cfg cmd=start &')  # check the right name of the file
                print('test SC Noise Reduction On ok')
                print(self.gainSCbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_SCNoiseReductionGainDown(self):

        if self.ONbb == True:
            gaindown = 5
            self.gainSCbb = self.gainSCbb - gaindown

            if (self.gainSCbb > -41) & (self.gainSCbb < 51):
                replace_SCfiltergain2(self.gainSCbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:scdenoising_gain_live.cfg cmd=start &')  # check the right name of the file
                print('test SC Noise Reduction On ok')
                print(self.gainSCbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_DCOn(self):

        if self.ONbb == True:
            print('test DC On ok')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_FqcyShifting_On(self):

        if self.ONbb == True:
            fqcy_up = 300
            self.fqcybb = self.fqcybb + fqcy_up

            if (self.fqcybb > 0) & (self.fqcybb < 15000):
                replace_fqcyshift(self.fqcybb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:fbc_live.cfg cmd=start &')  # check the right name of the file
                print(self.fqcybb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_FqcyShifting_Update(self, input_text):

        if self.ONbb == True:
            fqcyshift_int = input_text.get()

            if (fqcyshift_int > -1) & (fqcyshift_int < 16000):
                replace_fqcyshift(fqcyshift_int)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:fbc_live.cfg cmd=start &')  # check the right name of the file
                self.fqcybb = fqcyshift_int
                print(self.fqcybb)

            else:
                print('the value of the frequency is outside the bounds [fmin, fmax]')

        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_FqcyShifting_GainUp(self):

        if self.ONbb == True:
            gainup = 5
            self.gainfshiftbb = self.gainfshiftbb + gainup

            if (self.gainfshiftbb > -41) & (self.gainfshiftbb < 51):
                replace_fshiftgain2(self.gainfshiftbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:fbc_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainfshiftbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_FqcyShifting_GainDown(self):

        if self.ONbb == True:
            gaindown = 5
            self.gainfshiftbb = self.gainfshiftbb - gaindown

            if (self.gainfshiftbb > -41) & (self.gainfshiftbb < 51):
                replace_fshiftgain2(self.gainfshiftbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:fbc_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainfshiftbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_LowPassFilterOn(self):

        if self.ONbb == True:
            # kill the mha program already running
            os.system('killall mha -9')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:dc_lowpass_live.cfg cmd=start &')  # check the right name of the file
            print('test LowPass On ok')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_LowPassFilterGainUp(self):

        if self.ONbb == True:
            gainup = 5
            self.gainLPfilterbb = self.gainLPfilterbb  + gainup

            if (self.gainLPfilterbb  > -41) & (self.gainLPfilterbb  < 51):
                replace_LPfiltergain2(self.gainLPfilterbb )
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:dc_lowpass_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainLPfilterbb )
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_LowPassFilterGainDown(self):

        if self.ONbb == True:
            gaindown = 5
            self.gainLPfilterbb  = self.gainLPfilterbb  - gaindown

            if (self.gainLPfilterbb  > -41) & (self.gainLPfilterbb  < 51):
                replace_LPfiltergain2(self.gainLPfilterbb )
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:dc_lowpass_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainLPfilterbb )
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_HighPassFilterOn(self):

        if self.ONbb == True:
            # kill the mha program already running
            os.system('killall mha -9')
            # start to run the config file gain_live.cfg with the updated gain value
            os.system('mha ?read:dc_highpass_live.cfg cmd=start &')  # check the right name of the file
            print('test LowPass On ok')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_HighPassFilterGainUp(self):

        if self.ONbb == True:
            gainup = 5
            self.gainHPfilterbb = self.gainHPfilterbb + gainup

            if (self.gainHPfilterbb > -41) & (self.gainHPfilterbb < 51):
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:dc_highpass_live.cfg cmd=start &')  # check the right name of the file
                replace_HPfiltergain2(self.gainHPfilterbb)
                print(self.gainHPfilterbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')


    def BtnClick_HighPassFilterGainDown(self):

        if self.ONbb == True:
            gaindown = 5
            self.gainHPfilterbb = self.gainHPfilterbb - gaindown

            if (self.gainHPfilterbb > -41) & (self.gainHPfilterbb < 51):
                replace_HPfiltergain2(self.gainHPfilterbb)
                # kill the mha program already running
                os.system('killall mha -9')
                # start to run the config file gain_live.cfg with the updated gain value
                os.system('mha ?read:dc_highpass_live.cfg cmd=start &')  # check the right name of the file
                print(self.gainHPfilterbb)
            else:
                print('the value of the gain is outside the bounds [gmin, gmax]')
        else:
            print('On is not activated, please press On to launch the Jack server')





