# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:57:24 2019

@author: Silvi
"""
import pandas as pd
from scipy import stats
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
from pro_data import *
medidas = pro_data()


#from json_20190723 import json
#medidas.select_data(json)
#medidas.plot_force()

'''Medidas de impedancia eléctrica probetas 1 a 7'''
#from json_20190814 import json
#medidas.select_data(json)
#medidas.plot_Z()

'''Medidas de impedancia eléctrica probetas 8 a 13'''
#from json_20190910 import json
#medidas.select_data(json)
#medidas.plot_Z()

#from json_20190928 import json
#medidas.select_data(json)
#medidas.plot_Z()
#medidas.plot_ocp()

'''Medidas de impedancia eléctrica probetas 14 a 17'''
#from json_20191013 import json
#medidas.select_data(json)
#medidas.plot_Z()

'''Medidas de OCP-force probetas 1 a 7'''
# from json_20190916 import json
# medidas.select_data(json)
#medidas.plot_force()
#medidas.plot_Z()
#medidas.plot_ocp()
# medidas.plot_ocp_force()

'''Medidas de OCP-force probetas 8 a 17'''
# from json_20191016 import json
# medidas.select_data(json)
#medidas.plot_force()
#medidas.plot_Z()
#medidas.plot_ocp()
# medidas.plot_ocp_force()

#from json_20191029 import json
#medidas.select_data(json)
#medidas.plot_Z()

#from json_20191105 import json
#medidas.select_data(json)
#medidas.plot_Z()

#from json_20191106 import json
#medidas.select_data(json)
#medidas.plot_Z()

#from json_20200118 import json
#medidas.select_data(json)
#medidas.plot_Z()

#from json_20200205 import json
#medidas.select_data(json)
#medidas.plot_Z()

#from json_20200619 import json
#medidas.select_data(json)
#medidas.plot_Z()
#medidas.plot_ocp()

'''Medidas en probetas con AuNPs'''
# from AuNP import json
# medidas.select_data(json)
# medidas.plot_Z()
# medidas.plot_ocp()

'''Medidas en probetas con NTC'''
# from NTC import json
# medidas.select_data(json)
# medidas.plot_Z()
# medidas.plot_ocp()
# t_integra = 10
# plt.figure()
# medidas.plotC_mu_ti(ti = t_integra, color = '.b', n=1)
# C = medidas.getC_mu_ti(ti =t_integra)[2]
# V = medidas.getC_mu_ti(ti =t_integra)[0]
# C = C[1:9]
# V = V[1:9]
# from scipy import stats
# print(stats.linregress(V, C))

# from NTC_dis import json
# medidas.select_data(json)
# medidas.plot_Z()

# from NTC_1_12 import json
# json['is'] = []
# data = pd.read_excel('Medidas_data.xlsx')

# probeta = data.loc[data['sample'] == 'p62']
# # #probeta = data.loc[data['solvent'] == 'Agua tipo I + EUCON']
# path_list = probeta.path
# for j in probeta.index:
#     json['is'].append({'path':(path_list[j])})#('data/' + path_list[j])})

# medidas.select_data(json)

# freq = medidas.freq
# Zc = np.array(medidas.Z_re)-1j*np.array(medidas.Z_im)

# from semiCirclesEISModel import *
# import xlsxwriter

# ax_x = np.linspace(0,2*np.pi,1000)
# a = []
# for j in range(0,len(freq),1):
#     fit = semiCirclesEISModel(freq[j],Zc[j])   
#     # Algoritmo de busqueda de máximos y minimos-----------
#     l = np.int16(np.linspace(0, fit.real.size-1, 30))
#     der = np.gradient(fit.imag[l])/np.gradient(fit.real[l])
#     real_min = []
#     real_max = []
#     for j1 in np.arange(len(der)-2):
#         if (der[j1]*der[j1+1]<0) & (der[j1]*der[j1+2]<0):
#             if der[j1]<0:
#                 s = der == der[j1]
#                 real_min.append(fit.real[l][s][0])
#             elif der[j1]>0:
#                 s = der == der[j1]
#                 real_max.append(fit.real[l][s][0])
#     #------------------------------------------------------
#     #-fitting first dispersion and copy circle parameters
#     p1 = fit.optCircleParameters(real_min=0, real_max=real_min[0])
#     fit.plotNyquist(show_title=False)
#     #---------------------------------------------------------------------------
#     #-fitting second dispersion and copy circle parameters in xlsx, if there is
#     if len(real_min)>=2:
#         p2 = fit.optCircleParameters(real_min=real_min[0], real_max=real_min[1])
#         fit.plotNyquist(show_title=False)
#     #---------------------------------------------------------------------------
#     #-fitting constant phase element and copy linear parameters in xlsx
#     s1 = fit.real[l] > real_min[-1]
#     lin_re = stats.linregress(fit.real[l][s1], fit.imag[l][s1])
#     plt.plot(fit.real[l][s1], lin_re[0]*fit.real[l][s1]+lin_re[1], 'k:')
#     plt.xlim(-2500, 30000)
#     plt.ylim(-2500, 30000)


    # probeta.loc[probeta.index[j],'fig_fit_geometric']
    # data.loc[probeta.index[j],'params_fit_geometric']=str(p)
# writer = pd.ExcelWriter('Medidas(respuestas).xlsx', engine='xlsxwriter')
# data.to_excel(writer, sheet_name='Sheet1', startrow=0, index=None)
# writer.save()

# medidas.plot_Z()
# medidas.plot_C_is()


# plt.figure()
# for i in np.arange(0,len(medidas.f_charge),1):
#     label = medidas.path_is[i]
#     plt.subplot(2,1,1)
#     plt.plot(medidas.freq[i], medidas.Z_im[i]*1e-3, '.')#, label=label)
#     plt.xscale('log')
#     plt.xlabel(r'Frequency [Hz]', fontsize=18)
#     plt.ylabel(r'Z´´ [$k\Omega$]', fontsize=18)
#     plt.legend()
#     plt.subplot(2,1,2)
#     plt.plot(medidas.freq[i], medidas.Z_re[i]*1e-3, '.')#, label=label)
#     plt.xscale('log')
#     plt.xlabel(r'Frequency [Hz]', fontsize=18)
#     plt.ylabel(r'Z´ [$k\Omega$]', fontsize=18)
#     plt.legend()

'''Capacitance curves'''    
# plt.figure()
# for i in np.arange(0,len(medidas.f_charge),1):
#     Zc = medidas.Z_re[i] - 1j*medidas.Z_im[i]
#     C = 1/(2*np.pi*medidas.freq[i]*Zc[i])
#     label = medidas.path_is[i]
#     plt.subplot(3,1,1)
#     plt.plot(medidas.freq[i], C.imag*1e6, '.')#, label=label)
#     plt.xscale('log')
#     plt.xlabel(r'Frequency [Hz]', fontsize=18)
#     plt.ylabel(r'C´´ [$\mu F$]', fontsize=18)
#     plt.legend()
#     plt.subplot(3,1,2)
#     plt.plot(medidas.freq[i], C.real*1e6, '.')#, label=label)
#     plt.xscale('log')
#     plt.xlabel(r'Frequency [Hz]', fontsize=18)
#     plt.ylabel(r'C´ [$\mu F$]', fontsize=18)
#     plt.legend()
#     plt.subplot(3,1,3)
#     plt.plot(C.real*1e6, C.imag*1e6, '.')#, label=label)
#     plt.xlabel(r'C´ [$\mu F$]', fontsize=18)
#     plt.ylabel(r'C´´ [$\mu F$]', fontsize=18)
#     plt.legend()

'''Medidas en probetas con GO'''
from GO import json
medidas.select_data(json)
medidas.plot_Z()
# medidas.plot_ocp()

'''Medidas probetas de grafito'''
# from grafite import json
# medidas.select_data(json)
# medidas.plot_Z()
#t_integra = 10.0
#plt.figure()
#medidas.plotC_mu_ti(ti = t_integra, color = '.b', n=1)


# filter_sample = data.loc[data['sample'] == 'p59']
# path_list = filter_sample.path

# R0 = filter_sample["params_fit_geometric_r0"]
# meassurement_date = filter_sample["measurement_date"]
# time = meassurement_date - meassurement_date[mea_date.index[0]]
# days = time.convert_dtypes(convert_integer=True)*1e-9/(60*60*24)
# plt.plot(days, R0, '.b')
