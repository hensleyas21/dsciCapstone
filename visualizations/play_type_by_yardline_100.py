import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../cleaned_data.csv')

plot = sns.histplot(data=df, x='yardline_100', hue='play_type', multiple='stack', discrete=True)
plot.set_title("Play Type by Yardline 100")
plt.xlabel("Yardline 100")
plt.xlim(0, 100)
legend = plot.legend_
plt.legend(handles=legend.legend_handles, labels=[t.get_text().replace('_', ' ').title().replace('Qb', 'QB') for t in legend.texts], 
            title="Play Type", loc='upper left')
plt.ylabel('Number of Plays')
plt.savefig('charts/play_type_by_yardline_100.svg')
plt.show()