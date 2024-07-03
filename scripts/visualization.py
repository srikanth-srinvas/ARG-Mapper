import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_arg_distribution(arg_data, output_file):
    plt.figure(figsize=(12, 8))
    sns.heatmap(arg_data, cmap="YlGnBu", annot=True)
    plt.title('ARG Distribution Across Samples')
    plt.xlabel('Resistance Gene')
    plt.ylabel('Sample')
    plt.savefig(output_file)
    plt.close()
