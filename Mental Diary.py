#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import Markdown, display

display(Markdown("<span style='font-family: Comic Sans Ms; font-size: 22px; color: darkblue;'>This is Your Mental Health Diary</span>"))
display(Markdown("<span style='font-family: Comic Sans Ms; font-size: 18px; color: darkblue;'>Write on good and bad days to track what works and what doesn't!</span>"))
display(Markdown("<span style='font-family: Comic Sans Ms; font-size: 14px; color: darkblue;'>Every evening, (6pm - 12pm), enter in this diary</span>"))
display(Markdown("<span style='font-family: Comic Sans Ms; font-size: 14px; color: darkblue;'>Rate questions out of 10</span>"))

questions = ["Date", "Happiness", "Confidence", "Productivity"]

while True:
    with open("diary.txt", 'a') as external_file:
        all_content = []
        for question in questions:
            content = input(f"{question} (press Enter to finish):\n")
            if len(content) == 0:
                break
            all_content.append(content)
        if len(content) == 0:
            break
        comments = input("Comments (press Enter to finish):\n")
        if len(comments) == 0:
            break
        all_content.append(comments)
        external_file.write(",".join(all_content) + "\n")
    if len(content) == 0:
        break

print("Content added to the file successfully.")


# In[13]:


import os
import pandas as pd

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully.")
    except FileNotFoundError:
        print(f"{filename} not found.")

delete_file('diary.csv')
print("work1")

def convert_txt_to_csv(txt_filename, csv_filename):
    with open(txt_filename, 'r') as txt_file:
        lines = txt_file.readlines()
    with open(csv_filename, 'w', newline='') as csv_file:
        for line in lines:
            csv_file.write(line)

convert_txt_to_csv('diary.txt', 'diary.csv')
print("work2")

df = pd.read_csv('diary.csv')
df.head()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_line_and_trend_from_csv(csv_filename):
    df = pd.read_csv(csv_filename)
    date = df['Date']
    happiness = df['Happiness']
    plt.scatter(date, happiness, marker='o')
    
    plt.plot(date, happiness, color='lightcoral', linestyle='-', linewidth=1)

    plt.xlabel('Date')
    plt.ylabel('Happiness')
    plt.title('Range of Happiness')
  
    plt.ylim(1, 10)
    
    plt.grid(True)
    plt.show()

plot_line_and_trend_from_csv('diary.csv')

def plot_line_and_trend_from_csv(csv_filename):
    df = pd.read_csv(csv_filename)
    date = df['Date']
    productivity = df['Productivity']
    plt.scatter(date, productivity, marker='o')
    
    plt.plot(date, productivity, color='lightcoral', linestyle='-', linewidth=1)

    plt.xlabel('Date')
    plt.ylabel('Productivity')
    plt.title('Range of Productivity')
  
    plt.ylim(1, 10)
    
    plt.grid(True)
    plt.show()

plot_line_and_trend_from_csv('diary.csv')


# In[15]:


def plot_line_and_trend_from_csv(csv_filename):
    # Read data from the CSV file
    df = pd.read_csv(csv_filename)

    confidence = df['Confidence']
    happiness = df['Happiness']

    plt.scatter(happiness, confidence, marker='o')
    slope, intercept = np.polyfit(happiness, confidence, 1)
    trend_line = slope * happiness + intercept

    plt.plot(happiness, trend_line, color='red', linestyle='-', linewidth=2, label='Trend Line')

    plt.xlabel('Happiness')
    plt.ylabel('Confidence')
    plt.title('Happiness vs Confidence')
    plt.legend()

    plt.xlim(1, 10)  
    plt.ylim(1, 10)
    
    plt.grid(True)
    plt.show()

plot_line_and_trend_from_csv('diary.csv')

def plot_line_and_trend_from_csv(csv_filename):
    df = pd.read_csv(csv_filename)
    productivity = df['Productivity']
    happiness = df['Happiness']
    plt.scatter(happiness, productivity, marker='o')

    slope, intercept = np.polyfit(happiness, productivity, 1)
    trend_line = slope * happiness + intercept
    
    plt.plot(happiness, trend_line, color='red', linestyle='-', linewidth=2, label='Trend Line')

    plt.xlabel('Happiness')
    plt.ylabel('Productivity')
    plt.title('Happiness vs Productvity')
    plt.legend()

    plt.xlim(1, 10)  
    plt.ylim(1, 10)
    
    plt.grid(True)
    plt.show()

plot_line_and_trend_from_csv('diary.csv')


# In[ ]:





# In[ ]:




