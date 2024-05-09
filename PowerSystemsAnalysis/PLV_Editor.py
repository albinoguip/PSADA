from . NTW_Reader import *
import pandas as pd
import numpy as np


class PLV_Editor():

    def __init__(self, report_path):

        self.ND  = NTW_Reader(report_path)
        self.bus = self.ND.bus_data
        self.gen = self.ND.gen_data

        # print(self.gen.iloc[100:150])
        # print(self.gen.columns)

        self.vars  = []
        self.plots = []
        self.names = []

    def new_variable(self, var, tipo, barra1, eqp1=0, barra2=0, eqp2=0, multiplier=1):

        self.vars.append(f'{len(self.vars)+1:4} {tipo:4} \'{var:<10}\' {barra1:4} {eqp1:4} {barra2:4} {eqp2:4} {multiplier:8.5f} \'            \' \'            \' / \n')
        print(f'Variable number {len(self.vars)} added')

    def new_plot(self, name, variable_number):

        variable_number = variable_number if type(variable_number) == list else [variable_number]

        self.names.append(name)
        self.plots.append(variable_number)


    def append(self, name, variable_number):

        variable_number = variable_number if type(variable_number) == list else [variable_number]

        idx = self.names.index(name)
        for var in variable_number:
            self.plots[idx].append(var)

    def save(self, save_path):

      file = [f'          -1 \n']

      for var in self.vars: file.append(var)

      file.append(' -9 /\n')
      file.append('\'\' /\n')

      for idx in range(len(self.names)):

        file.append(f'\'{self.names[idx] : <30}\'     0.00000    0.00000    0    0 \'N\' / \n')

        for num in self.plots[idx]:
            file.append(f'        {num:3}  0 / \n')

        file.append(' -9 /\n')
      
      file.append(' -99 /\n')

      with open(save_path, 'w') as f:
            for line in file:
                f.write(line)
        