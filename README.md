# Au-NPs-cement-composites
Four python modules are presented to analyze measured data from mechanical and electrical characterizations.

Module.py instance the class pro_data that al

20210128 update python 2 code to python 3 code 
We change dictionary.has_key('key'): for 'key' in dictionary:
20210129 We need to change the attribute join from python 2.0 instead attribute in python 3.0
    name = '' # Name of experiment
    date = strftime('%c')
    F = [] #Force in N
    ds = [] #deformation in m
    mec_rate = [] #rate change of the force in time
    f_charge = []
    path_m = [] #file name of mechanical proofs
    path_is = [] #file name of impedance proofs
    path_ocp = [] #file name of OCP proofs
    freq = [] #frequency in Hz
    Z_re = [] #real part of impedance in Ohm
    Z_im = [] #imaginary part of impedance in Ohm
    Z = [] #magnitude of impedance in Ohm
    phase = [] #phase of impedance
    V_ocp = [] #open circuit potential
    t_ocp = [] #time ocp measurement
    t_force = [] #time of compression test
    scvPhi = []  # External potential for SCV experiment
    t = [] # Time step
    V = [] # Potential difference
    I = [] # Current
"""
