import pandas as pd 
import numpy as np

students = pd.read_csv('./part3/students.csv')

students.GPA.plot.bar(0)