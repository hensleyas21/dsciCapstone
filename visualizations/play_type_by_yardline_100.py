import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../cleaned_data.csv')

plt.figure(figsize=(10,7))

plot = sns.histplot(data=df, x='yardline_100', hue='play_type', multiple='stack', discrete=True, edgecolor='none', palette={'run': '#a3221d', 'pass': '#5799c7', 'punt': '#4da24d', 'field_goal': '#d98032', 'qb_kneel': '#8c5fa4'}, alpha=1.0)
plot.set_title("Play Type by Yardline 100", fontsize=24)
plt.xlabel("Yardline 100", fontsize=16)
plt.xlim(0, 100)
plt.xticks(fontsize=12)
legend = plot.legend_
plt.legend(handles=legend.legend_handles, labels=[t.get_text().replace('_', ' ').title().replace('Qb', 'QB') for t in legend.texts], 
            title="Play Type", loc='upper left', fontsize=12, title_fontsize=16)
plt.ylabel('Number of Plays', fontsize=16)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('charts/play_type_by_yardline_100.svg')
plt.show()