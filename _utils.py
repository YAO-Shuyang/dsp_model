import pandas as pd
import os
import pickle

DSP_path = r"E:\Data\Dsp_maze"
f2 = pd.read_excel(os.path.join(DSP_path,'dsp_maze_paradigm.xlsx'), sheet_name = 'calcium')

def get_