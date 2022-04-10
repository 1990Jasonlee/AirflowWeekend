import pandas as pd
#import matplotlib
#matplotlib.use('Agg')
#from matplotlib import pyplot as plt
import plotly.express as px

def some_script():
    data = pd.read_csv('/Users/jason/dev/AirflowWeekend/data/pokedex.csv')
    df = data[['name', 'type_1']]
    count = df.groupby('type_1')['type_1'].count()

    count.plot.bar()
    #plt.title('Number of Pokemon by Primary Types')
    #plt.xlabel('Primary Type')
    #plt.ylabel('Number of Pokemon')
    #plt.savefig(f'/Users/jason/dev/AirflowWeekend/data/1')

    fig = px.bar(count, y='type_1')
    fig.update_layout(xaxis_title='Types',
                      yaxis_title='Number of Pokemon',
                      title='Pokemon by Types')
    fig.write_image(f'/Users/jason/dev/AirflowWeekend/data/1')

    df1 = data[['name', 'generation']]
    bins = [1, 2, 3, 4, 5, 6, 7, 8]
    df1['generation'].hist(bins=bins)
    #plt.title('Number of Pokemon by Generation')
    #plt.xlabel('Generation')
    #plt.ylabel('Number of Pokemon')
    #plt.savefig(f'/Users/jason/dev/AirflowWeekend/data/2')

    fig1 = px.histogram(data_frame=df1,
                        x='generation')
    fig1.update_layout(xaxis_title='Generation',
                       yaxis_title='Number of Pokemons',
                       title='Pokemon by Generations')
    fig.write_image(f'/Users/jason/dev/AirflowWeekend/data/2')