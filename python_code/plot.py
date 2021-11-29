# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:46:01 2021

@author: juany
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

class Maquina:
    def __init__(self):
        self.rb = []
        self.al = []
        self.pr = []
        self.fwd = []
        self.rb_tr = []
        self.al_tr = []
        self.pr_tr = []
        self.fwd_tr = []
        
Cliente_1 = Maquina()
Cliente_2 = Maquina()
Cliente_3 = Maquina()
Server_1 =  Maquina()
Server_2 =  Maquina()
Server_3 =  Maquina()
dpdk = []

for i in range(1,4):
    print(i)
    if(i == 1):
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "pr.txt"
        pr = open(file)
        #rb = open("/cliente_"+i+"/rb.txt")
        j = 0
        for row in csv.reader(pr):
            if(j < 300):
                Cliente_1.pr.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "rb.txt"
        rb = open(file)
        j = 0
        for row in csv.reader(rb):
            if(j < 300):
                Cliente_1.rb.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "al.txt"
        al = open(file)
        j = 0
        for row in csv.reader(al):
            if(j < 300):
                Cliente_1.al.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "fwd.txt"
        fwd = open(file)
        j = 0
        for row in csv.reader(fwd):
            if(j < 300):
                Cliente_1.fwd.append(float(row[0])*1000)
                j = j + 1
    if(i == 2):
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "pr.txt"
        pr = open(file)
        #rb = open("/cliente_"+i+"/rb.txt")
        j = 0
        for row in csv.reader(pr):
            if(j < 300):
                Cliente_2.pr.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "rb.txt"
        rb = open(file)
        j = 0
        for row in csv.reader(rb):
            if(j < 300):
                Cliente_2.rb.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "al.txt"
        al = open(file)
        j = 0
        for row in csv.reader(al):
            if(j < 300):
                Cliente_2.al.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "fwd.txt"
        fwd = open(file)
        j = 0
        for row in csv.reader(fwd):
            if(j < 300):
                Cliente_2.fwd.append(float(row[0])*1000)
                j = j + 1
    if(i == 3):
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "rb.txt"
        rb = open(file)
        j = 0
        for row in csv.reader(rb):
            if(j < 300):
                Cliente_3.rb.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "al.txt"
        al = open(file)
        j = 0
        for row in csv.reader(al):
            if(j < 300):
                Cliente_3.al.append(float(row[0])*1000)
                j = j + 1
        direc = Path("results/cliente_"+str(i)+"/")
        file = direc / "fwd.txt"
        fwd = open(file)
        j = 0
        for row in csv.reader(fwd):
            if(j < 300):
                Cliente_3.fwd.append(float(row[0])*1000)
                j = j + 1

for i in range(1,4):
    print(i)
    if(i == 1):
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "pr.txt"
        pr = open(file)
        j = 0
        for row in csv.reader(pr):
            Server_1.pr.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "rb.txt"
        rb = open(file)
        j = 0
        for row in csv.reader(rb):
            Server_1.rb.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "al.txt"
        al = open(file)
        j = 0
        for row in csv.reader(al):
            Server_1.al.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "fwd.txt"
        fwd = open(file)
        j = 0
        for row in csv.reader(fwd):
            Server_1.fwd.append(float(row[0]))
            j = j + 1
    if(i == 2):
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "pr.txt"
        pr = open(file)
        j = 0
        for row in csv.reader(pr):
            Server_2.pr.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "rb.txt"
        rb = open(file)
        j = 0
        for row in csv.reader(rb):
            Server_2.rb.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "al.txt"
        al = open(file)
        j = 0
        for row in csv.reader(al):
            Server_2.al.append(float(row[0]))
            j = j + 1
    if(i == 3):
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "pr.txt"
        pr = open(file)
        j = 0
        for row in csv.reader(pr):
            Server_3.pr.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "rb.txt"
        rb = open(file)
        j = 0
        for row in csv.reader(rb):
            Server_3.rb.append(float(row[0]))
            j = j + 1
        direc = Path("results/server_"+str(i)+"/")
        file = direc / "al.txt"
        al = open(file)
        j = 0
        for row in csv.reader(al):
            Server_3.al.append(float(row[0]))
            j = j + 1

#Sacar datos de cpu de DPDK
direc = Path("results/")
file = direc / "dpdk.txt"
al = open(file)
for row in csv.reader(al):
    dpdk.append(float(row[0]))

#Sacar throughput

#Cliente 1
for i in Cliente_1.rb:
    Cliente_1.rb_tr.append((12657*8)/(i/1000))
for i in Cliente_1.pr:
    Cliente_1.pr_tr.append((12657*8)/(i/1000))
for i in Cliente_1.al:
    Cliente_1.al_tr.append((12657*8)/(i/1000))
for i in Cliente_1.fwd:
    Cliente_1.fwd_tr.append((12657*8)/(i/1000))
    
#Cliente 2
for i in Cliente_2.rb:
    Cliente_2.rb_tr.append((12657*8)/(i/1000))
for i in Cliente_2.pr:
    Cliente_2.pr_tr.append((12657*8)/(i/1000))
for i in Cliente_2.al:
    Cliente_2.al_tr.append((12657*8)/(i/1000))
for i in Cliente_2.fwd:
    Cliente_2.fwd_tr.append((12657*8)/(i/1000))
    
#Cliente 3
for i in Cliente_3.rb:
    Cliente_3.rb_tr.append((12657*8)/(i/1000))
for i in Cliente_3.al:
    Cliente_3.al_tr.append((12657*8)/(i/1000))
for i in Cliente_3.fwd:
    Cliente_3.fwd_tr.append((12657*8)/(i/1000))
## Plot Client 1
x = np.linspace(0,len(Cliente_1.rb), len(Cliente_1.rb))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Cliente_1.rb,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Cliente_1.pr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Cliente_1.fwd,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Cliente_1.al,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Tiempo de respuesta Cliente 1', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Paquetes", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Respuesta (ms)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Cliente_1.png')
plt.show()

## Plot Client 2
x = np.linspace(0,len(Cliente_2.rb), len(Cliente_2.rb))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Cliente_2.rb,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Cliente_2.pr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Cliente_2.fwd,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Cliente_2.al,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Tiempo de respuesta Cliente 2', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Paquetes", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Respuesta (ms)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Cliente_2.png')
plt.show()

## Plot Client 3
x = np.linspace(0,len(Cliente_3.rb), len(Cliente_3.rb))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Cliente_3.rb,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Cliente_3.fwd,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Cliente_3.al,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Tiempo de respuesta Cliente 3', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Paquetes", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Respuesta (ms)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Cliente_3.png')
plt.show()

## Plot Server 1
x = np.linspace(0,len(Server_1.rb), len(Server_1.rb))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Server_1.rb,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Server_1.pr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Server_1.fwd,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Server_1.al,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Consumo de CPU Server 1', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Tiempo (s/10)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Carga en CPU (%)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Server_1.png')
plt.show()

## Plot Server 2
x = np.linspace(0,len(Server_2.rb), len(Server_2.rb))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Server_2.rb,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Server_2.pr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Server_2.al,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Consumo de CPU Server 2', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Tiempo (s/10)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Carga en CPU (%)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Server_2.png')
plt.show()

## Plot Server 3
x = np.linspace(0,len(Server_1.rb), len(Server_1.rb))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Server_3.rb,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Server_3.pr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Server_3.al,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Consumo de CPU Server 3', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Tiempo (s/10)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Carga en CPU (%)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Server_3.png')
plt.show()

## Plot DPDK
x = np.linspace(0,len(dpdk), len(dpdk))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, dpdk,color = 'tab:blue', marker = 'o')
ax.set_title('Consumo de CPU Nodo DPDK', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Tiempo (s/10)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Carga en CPU (%)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
plt.savefig('DPDK.png')
plt.show()

## Plot Client 1 throughput
x = np.linspace(0,len(Cliente_1.rb_tr), len(Cliente_1.rb_tr))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Cliente_1.rb_tr,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Cliente_1.pr_tr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Cliente_1.fwd_tr,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Cliente_1.al_tr,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Throughput Cliente 1', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Paquetes", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Throughput (bps)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Cliente_1_th.png')
plt.show()

## Plot Client 2 throughput
x = np.linspace(0,len(Cliente_2.rb_tr), len(Cliente_2.rb_tr))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Cliente_2.rb_tr,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Cliente_2.pr_tr,color = 'tab:green', marker = 'o', label = 'Honey bee foraging')
ax.plot(x, Cliente_2.fwd_tr,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Cliente_2.al_tr,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Throughput Cliente 2', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Paquetes", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Throughput (bps)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Cliente_2_th.png')
plt.show()

## Plot Client 3 throughput
x = np.linspace(0,len(Cliente_3.rb_tr), len(Cliente_3.rb_tr))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Cliente_3.rb_tr,color = 'tab:blue', marker = 'o', label = 'Round Robin')
ax.plot(x, Cliente_3.fwd_tr,color = 'tab:red', marker = 'o', label = 'No Balancing')
ax.plot(x, Cliente_3.al_tr,color = 'tab:orange', marker = 'o', label = 'Active Monitoring')
ax.set_title('Throughput Cliente 3', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Paquetes", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Throughput (bps)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Cliente_3_th.png')
plt.show()

## Plot Active monitoring servers
x = np.linspace(0,len(Server_1.al), len(Server_1.al))
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
fig.set_dpi(100)
ax.plot(x, Server_1.al,color = 'tab:blue', marker = 'o', label = 'Server 1')
ax.plot(x, Server_2.al,color = 'tab:green', marker = 'o', label = 'Server 2')
ax.plot(x, Server_3.al,color = 'tab:orange', marker = 'o', label = 'Server 3')
ax.set_title('Consumo de CPU en active monitoring de los servidores', loc = "center", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_xlabel("Tiempo (s/10)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.set_ylabel("Carga en CPU (%)", fontdict = {'fontsize':25, 'fontweight':'bold', 'color':'k'})
ax.legend(loc = 'upper right')
plt.savefig('Active_Monitoring.png')
plt.show()
