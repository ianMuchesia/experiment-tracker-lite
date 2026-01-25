import matplotlib.pyplot as plt
from src.comparison import compare_experiments,get_best_run


all_runs = compare_experiments("./experiments")

#Figure the whole window or image
#axis the specific graph(with x and y coordinates) inside that window
fig, ax = plt.subplots()

#loop through every run in our list
for run in all_runs:
    
    loss_data = run["loss"]
    
    ax.plot(loss_data,label="Loss Data")
    
    