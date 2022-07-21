#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

import numpy as np
import re
import matplotlib as mpl
# mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


def change_job_title(title):
    #------------------ FONT_setup ----------------------
    font = {'family' : 'Arial',
        'color'  : 'black',
        'weight' : 'normal',
        'size' : 13.0,
        }

    #------------------- Data Read ----------------------
    Greek_alphabets=['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta', 'Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Pega']
    group_labels=[];xtick=[]
    with open("KLABELS",'r') as reader:
        lines=reader.readlines()[1:]
    for i in lines:
        s=i.encode('utf-8')#.decode('latin-1')
        if len(s.split())==2 and not s.decode('utf-8','ignore').startswith('*'):
            klabel=str(s.decode('utf-8','ignore').split()[0])
            for j in range(len(Greek_alphabets)):
                if (klabel.find(Greek_alphabets[j].upper())>=0):
                    latex_exp=r''+'$\\'+str(Greek_alphabets[j])+'$'
                    # print(latex_exp)
                    klabel=klabel.replace(str(Greek_alphabets[j].upper()),str(latex_exp))
            if (klabel.find('_')>0):
               n=klabel.find('_')
               klabel=klabel[:n]+'$'+klabel[n:n+2]+'$'+klabel[n+2:]
            group_labels.append(klabel)
            xtick.append(float(s.split()[1]))
    for label in range(len(group_labels)):
        if re.search('(?i)Gamma',  str(group_labels[label])):
            group_labels[label] = '$\Gamma$'
    datas=np.loadtxt("REFORMATTED_BAND_UP.dat",dtype=np.float64)
    data2=np.loadtxt("REFORMATTED_BAND_DW.dat",dtype=np.float64)



    fig, ax = plt.subplots(2, 2, sharex=False, sharey=True, figsize=(12, 8))
    fig.suptitle(title, fontsize=font['size']+5, fontweight='bold')


    #--------------------- PLOTs ------------------------
    axe = ax[0, 0]
    axe.axhline(y=0, xmin=0, xmax=1,linestyle= '--',linewidth=0.5,color='0.5')
    for i in xtick[1:-1]:
        axe.axvline(x=i, ymin=0, ymax=1,linestyle= '--',linewidth=0.5,color='0.5')
    colormaps='blue'
    axe.plot(datas[:,0],datas[:,1:],linewidth=1.0,color=colormaps)
    axe.set_ylabel(r'$\mathrm{E} - \mathrm{E_f}$ (eV)',fontdict=font)
    axe.set_xticks(xtick)
    axe.set_xticklabels(group_labels, rotation=0,fontsize=font['size']-2,fontname=font['family'])
    axe.set_xlim((xtick[0], xtick[-1]))
    axe.axis(ymin=-2, ymax=2) # set y limits manually
    axe.set_yticks(range(-2,2))
    axe.set_title('Band Structure (Up)', fontsize=font['size'])

    axi = ax[1, 0]
    axi.axhline(y=0, xmin=0, xmax=1,linestyle= '--',linewidth=0.5,color='0.5')
    for j in xtick[1:-1]:
        axi.axvline(x=j, ymin=0, ymax=1,linestyle= '--',linewidth=0.5,color='0.5')
    colormaps='blue'
    axi.plot(data2[:,0],data2[:,1:],linewidth=1.0,color=colormaps)
    axi.set_ylabel(r'$\mathrm{E} - \mathrm{E_f}$ (eV)',fontdict=font)
    axi.set_xticks(xtick)
    axi.set_xticklabels(group_labels, rotation=0,fontsize=font['size']-2,fontname=font['family'])
    axi.set_xlim((xtick[0], xtick[-1]))
    axi.axis(ymin=-2, ymax=2) # set y limits manually
    axi.set_yticks(range(-2,2))
    axi.set_title('Band Structure (Down)', fontsize=font['size'])

    def readfile2(filename):
        energy = filename[:, 0]
        state_choose = filename[:, 1]
        return energy, state_choose

    def readfile10(filename):
        energy = filename[:, 0]
        state_Total = filename[:, 10]
        return energy, state_Total

    def readfileTotal(filename):
        energy = filename[:, 0]
        state_up = filename[:, 1]
        state_dw = filename[:, 2]
        return energy, state_up, state_dw



    x1, y1, y2 = readfileTotal(np.loadtxt("TDOS.dat"))
    # x2, y2 = readfile10(np.loadtxt("PDOS_SUM_UP.dat"))

    ax1  = ax[0, 1]
    ax1.plot(y1, x1, label = "Spin down", linewidth=1.0)
    ax1.plot(y2, x1, label = "Spin up", linewidth=1.0)
    # plt.ylabel('Energy (eV)')
    # plt.xlabel('', rotation=0,fontsize=font['size']-2,fontname=font['family'])
    # plt.ylim(-6,0)
    ax1.axis(ymin=-2, ymax=2)
    ax1.axis(xmin=-100,xmax=100)
    ax1.axvline(x=0, color = "black", ls= ":")
    legend = ax1.legend(shadow=True, fontsize=font['size']-4)
    ax1.set_title('Density of States', fontsize=font['size'])
    ax1.get_yaxis().set_visible(False)

    ax2 = ax[1,1]
    ax2.plot(y1, x1, label = "Spin down", linewidth=1.0)
    ax2.plot(y2, x1, label = "Spin up", linewidth=1.0)
    # plt.ylabel('Energy (eV)')
    # plt.xlabel('', rotation=0,fontsize=font['size']-2,fontname=font['family'])
    # plt.ylim(-6,0)
    ax2.axis(ymin=-2, ymax=2)
    ax2.axis(xmin=-100,xmax=100)
    ax2.axvline(x=0, color = "black", ls= ":")
    legend = ax2.legend(shadow=True, fontsize=font['size']-4)
    ax2.set_title('Density of States', fontsize=font['size'])
    ax2.get_yaxis().set_visible(False)

    fig = plt.gcf()
    plt.rcParams["font.family"] = "Arial"
    # plt.show()
    # fig.set_size_inches(50, 40)
    plt.savefig(title+'.png',dpi= 300)

if __name__ == "__main__":
    change_job_title(sys.argv[1])