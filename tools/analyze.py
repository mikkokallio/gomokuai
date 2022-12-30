import pandas as pd


csv_data = pd.read_csv('tools/study5b.csv')
df = pd.DataFrame(csv_data)
df['b_t_rnd'] = df['b_time'] / df['rounds'] * 2
df['w_t_rnd'] = df['w_time'] / df['rounds'] * 2
print(df.to_string())
for player in df['black'].unique():
    print(f"{player}'s statistics")
    for color in ['black', 'white']:
        print(f'-> {color}')
        my_df = df[df[color] == player]
        time_col = 'b_t_rnd' if color == 'black' else 'w_t_rnd'
        print(my_df[time_col].mean())
        total = dict(my_df['winner'].value_counts())
        wins = total[player] if player in total else 0
        draws = total['draw'] if 'draw' in total else 0
        foes = {key: value for key, value in total.items() if key not in [player, 'draw']}
        losses = sum(foes.values())
        print(f'{wins} wins, {draws} draws, {losses} losses {foes}')
    print('')
