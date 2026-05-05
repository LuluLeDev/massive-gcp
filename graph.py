import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def clean_time(x):
    if isinstance(x, str):
        return float(x.replace('ms', '').strip())
    return float(x)

print("Génération des graphiques en cours")

# Graphique de la Concurrence (conc.csv)
if os.path.exists('out/conc.csv'):
    df_conc = pd.read_csv('out/conc.csv', sep=',')

    df_conc['AVG TIME'] = df_conc['AVG TIME'].apply(clean_time)

    plt.figure(figsize=(10, 6))

    sns.barplot(data=df_conc, x='PARAM', y='AVG TIME', errorbar='sd', capsize=0.1, color='cornflowerblue', edgecolor='black')
    
    plt.title('Temps moyen par requête selon la concurrence')
    plt.xlabel("Nombre d'utilisateurs concurrents")
    plt.ylabel('Temps moyen par requête (ms)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig('conc.png')
    print("Graphique conc.png généré avec succès !")
else:
    print("Le fichier out/conc.csv n'existe pas encore ou est vide.")

# Graphique du Fanout (fanout.csv)
if os.path.exists('out/fanout.csv'):
    df_fanout = pd.read_csv('out/fanout.csv', sep=',')

    col_time = 'AVG_TIME' if 'AVG_TIME' in df_fanout.columns else 'AVG TIME'
    df_fanout[col_time] = df_fanout[col_time].apply(clean_time)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_fanout, x='PARAM', y=col_time, errorbar='sd', capsize=0.1, color='coral', edgecolor='black')
    
    plt.title('Temps moyen par requête selon le fanout')
    plt.xlabel('Nombre de followees')
    plt.ylabel('Temps moyen par requête (ms)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig('fanout.png')
    print("Graphique fanout.png généré avec succès !")
else:
    print("Le fichier out/fanout.csv n'existe pas encore ou est vide.")