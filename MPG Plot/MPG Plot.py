# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:09:43 2018

@author: Harsh Kava
"""
import pandas as pd
import matplotlib.pyplot as plt

"""
Reads the auto-mpg.csv
Plots a line chart (with multiple lines) to show the mpg trend over the years by origin.
"""

def mpg_plot():
    
    # read auto-mpg.csv
    df = pd.read_csv('auto-mpg.csv', header=0)
    
    #line chart to show mpg trend over the years by origin
    df.groupby(['model_year','origin']).mean()['mpg'].unstack().plot(title='avg mpg by origin over years',kind='line',figsize=(8,4)).legend(loc='center left', bbox_to_anchor=(1, 0.5));
    
    #plot graph
    plt.show()
    
    
if __name__ == "__main__":
    mpg_plot()