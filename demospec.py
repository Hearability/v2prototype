from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy import signal

def getSpec(filename):
    fs, data = wavfile.read(filename)
    ch1 = data[:,0]
    ch2 = data[:,1]
    freq, ch1w = signal.welch(ch1, fs, nperseg=8000)
    freq, ch2w = signal.welch(ch2, fs, nperseg=8000)
    return freq, ch1w, ch2w

def getTime(filename):
    fs, data = wavfile.read(filename)
    ch1 = data[:,0]
    ch2 = data[:,1]
    N = len(ch1)
    T = 1.0 / fs # sample spacing
    xarr = np.linspace(0.0, N*T, N) # time array (beginning, end, number of points)
    return xarr, ch1, ch2

"""
f_ref, ch1_ref, ch2_ref = getSpec('noisepaulOn.wav')
f_dn, ch1_dn, ch2_dn = getSpec('noisepaulOn_dn.wav')
f_dngain, ch1_dngain, ch2_dngain = getSpec('noisepaulOn_dn_gain.wav')
f_noise, ch1_noise, ch2_noise = getSpec('whitenoiseOn.wav')

fig, ax = plt.subplots()

ax.plot(f_ref, ch1_ref, 'r', label='ch1', linewidth=2.0)
ax.plot(f_ref, ch2_ref, 'b', label='ch2', linewidth=2.0)
#ax.plot(f_dn, ch1_dn, 'darkcyan', label='ch1 denoised', linewidth=2.0)

ax.plot(f_noise, ch1_noise, 'dimgrey', linewidth=3.0, label='ch1 noise')
ax.plot(f_noise, ch2_noise, 'darkgrey', linewidth=3.0, label='ch2 noise')

leg = plt.legend()
plt.xlabel("Frequency (Hz)", fontsize=18)
plt.ylabel("Power Spectral Density", fontsize=18)
plt.xlim([0, 1200])

fig.savefig('talkSpecDN2.png')

"""

fig2, ax2 = plt.subplots()
#x, ch1x, ch2x = getTime('whitenoiseOn.wav')
xn, ch1xn, ch2xn = getTime('noisepaulOn.wav')
#xdn, ch1xdn, ch2xdn = getTime('noisepaulOn_dn.wav')

ax2.plot(xn, ch1xn, 'red', label='ch1')
#ax2.plot(xn, ch2xn, 'blue', label='ch2')
#ax2.plot(x, ch1x, 'grey', label='ch1 noise')
#ax2.plot(x, ch2x, 'black', label='ch2 noise')

#ax2.plot(xdn, ch1xdn, 'darkcyan', label='ch1 denoised')

leg = plt.legend(loc='upper left')
plt.xlabel("Time (s)", fontsize=18)
plt.ylabel("Amplitude (a.u.)", fontsize=18)

#fig2.savefig('timeSpecDN2.png')

plt.show()


"""

f_ref, ch1_ref, ch2_ref = getSpec('noisepaulOn.wav')
f_dn, ch1_dn, ch2_dn = getSpec('noisepaulOn_dn.wav')
f_dngain, ch1_dngain, ch2_dngain = getSpec('noisepaulOn_dn_gain.wav')

fig, ax = plt.subplots()

#ax.plot(f_ref, ch1_ref, 'r', label='ch1', linewidth=2.0)
#ax.plot(f_dn, (10.0*ch1_dn-ch1_dngain), 'darkcyan', label='ch1 denoised', linewidth=2.0)

ax.plot(f_dn, (10.0*ch1_dn), 'darkcyan', label='ch1 denoised * 10.0', linewidth=1.0)
ax.plot(f_dngain, ch1_dngain, 'red', label='ch1 denoised+gain 10 dB', linewidth=1.0)

ax.plot(f_dngain, (10.0*ch1_dn)-ch1_dngain, 'black', label='Difference', linewidth=2.0)

leg = plt.legend()
plt.xlabel("Frequency (Hz)", fontsize=18)
plt.ylabel("Power Spectral Density", fontsize=18)
plt.xlim([0, 1500])

fig.savefig('talkSpecDN_gain_comp.png')

"""


"""
f_ref, ch1_ref, ch2_ref = getSpec('1speaker_diffNoise_2ch.wav')
f_dn, ch1_dn, ch2_dn = getSpec('1speaker_diffNoise_2ch_OUT.wav')
fig, ax = plt.subplots()
ax.plot(f_ref, 1000*ch1_ref, 'r', label='ch1', linewidth=2.0)
ax.plot(f_ref, 1000*ch2_ref, 'b', label='ch2', linewidth=2.0)
ax.plot(f_dn, 1000*ch1_dn, 'darkcyan', label='ch1 denoised', linewidth=2.0)
ax.plot(f_dn, 1000*ch2_dn, 'green', label='ch2 denoised', linewidth=2.0)
leg = plt.legend()
plt.xlabel("Frequency (Hz)", fontsize=18)
plt.ylabel("Power Spectral Density (a.u.)", fontsize=18)
plt.xlim([0, 3000])
fig.savefig('specDN_openMHArecording.png')

fig2, ax2 = plt.subplots()
x, ch1x, ch2x = getTime('1speaker_diffNoise_2ch.wav')
xn, ch1xn, ch2xn = getTime('1speaker_diffNoise_2ch_OUT.wav')
ax2.plot(xn, ch1x, 'red', label='ch1')
ax2.plot(xn, ch2x, 'blue', label='ch2')
ax2.plot(x, ch1xn, 'cyan', label='ch1 denoised')
ax2.plot(x, ch2xn, 'green', label='ch2 denoised')
plt.xlabel("Time (s)", fontsize=18)
plt.ylabel("Amplitude (a.u.)", fontsize=18)
leg = plt.legend()
fig2.savefig('timeSpecDN_openMHArecording.png')
"""

### for 2D plotting

#fig = plt.figure(figsize=(20, 20), dpi=80)
#plt.hist2d(qleading, countList, bins=(2000, 20), range=[[-10000, -6000], [0, 20]], norm=LogNorm())
#plt.colorbar()
#plt.title("QTC Leading Edge", fontsize=30)
#plt.xlabel('Channel Number for the Edge', fontsize=30)
#plt.ylabel('Number of Edges in Region', fontsize=30)
#plt.tick_params(labelsize=25)
#fig.savefig("lead_num.png")
