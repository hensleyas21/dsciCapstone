import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../cleaned_data.csv')

plot = sns.histplot(data=df, x='down', hue='play_type', multiple='stack', discrete=True)
plot.set_title("Play Type by Down")
plt.xlabel("Down")
plt.xticks([1, 2, 3, 4])
legend = plot.legend_
plt.legend(handles=legend.legend_handles, labels=[t.get_text().replace('_', ' ').title().replace('Qb', 'QB') for t in legend.texts], 
            title="Play Type", loc='upper right')
plt.ylabel('Number of Plays')
plt.savefig('charts/play_type_by_down.svg')
plt.show()