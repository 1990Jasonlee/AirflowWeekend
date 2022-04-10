import pandas as pd
from matplotlib import pyplot as plt


def some_script():
    data = pd.read_csv('/Users/jason/dev/AirflowWeekend/data/pokedex.csv')
    df = data[['name', 'type_1']]
    count = df.groupby('type_1')['type_1'].count()

    count.plot.bar()
    plt.title('Number of Pokemon by Primary Types')
    plt.xlabel('Primary Type')
    plt.ylabel('Number of Pokemon')

    plt.savefig(f'/Users/jason/dev/AirflowWeekend/data/1')

    df1 = data[['name', 'generation']]
    bins = [1, 2, 3, 4, 5, 6, 7, 8]
    df1['generation'].hist(bins=bins)
    plt.title('Number of Pokemon by Generation')
    plt.xlabel('Generation')
    plt.ylabel('Number of Pokemon')

    plt.savefig(f'/Users/jason/dev/AirflowWeekend/data/2')
