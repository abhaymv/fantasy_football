import csv
import yaml
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import sys
import json

def initials(str):
    sol = ''
    for s in str.split():
        sol += s[0]
    return sol

def main(**args):
    if len(sys.argv) > 1:
        exclude = sys.argv[1].split()
    else:
        exclude = []
    sns.set(font_scale=.75)
    with open('resources/predraft.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        output = list()
        df = pd.read_csv(csvfile)
        T = df['T']
        df = df.dropna(axis='columns').sort_values(by=['VAL'], ascending=False)
        df['T'] = T
        df['INIT'] = df['NAME'].apply(initials)
        for pos in exclude:
            df = df[df['POS'] != pos]
        print(df.columns.values)
        ind = 0
        count = 0
        while ind < len(df):
            fig, ax1 = plt.subplots()
            s = sns.catplot('INIT', 'VAL', hue='POS',ax=ax1, data=df[ind: min(ind + 25, (len(df)))])
            ax2 = ax1.twinx()
            s = sns.catplot('INIT', 'T', color='magenta', alpha=.7, ax=ax2, data=df[ind: min(ind + 25, (len(df)))])
            ax2.invert_yaxis()
            ax2.set(ylabel='Tier')
            s.set(xlabel='Initials')
            fig.savefig(f'fantasy_viz{count}.png')
            count += 1
            ind += 25
        file = open('dump.json', 'w')
        json.dump(df.to_dict('index'), file, indent=4)
        return
        for row in reader:
            if True:
                if row['T'] != '#N/A':
                    pass
                    output.append((row['\ufeffNAME'], row['T'], row['VAL'], row['PS']))
        output = sorted(output, key=lambda x:float(x[2]), reverse = True)
        output = sorted(output, key=lambda x:int(x[1]))
        # output=output[60:]
        plt.figure()

        plt.savefig('fantasy_viz.png')
        print(output)
        yaml.dump(output, file, default_flow_style=False)



if __name__ == '__main__':
    main()
