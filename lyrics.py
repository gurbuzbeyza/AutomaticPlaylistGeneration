import pandas as pd

songs_df = pd.read_csv('msd_genre_dataset.csv')

# print (songs_df)

f = open('mxm_dataset_train.txt', 'r')
lines = [x for x in f.readlines() if not x.startswith('#')]
top_words = lines[0][1:].split(',')
splitted_lines = [x.split(',') for x in lines[1:]]
song_word_counts = {x[0]:{top_words[int(y.split(':')[0])-1]:int(y.split(':')[1]) for y in x[2:]} for x in splitted_lines[1:]}
song_names = [x[0] for x in splitted_lines]
song_name_df = pd.DataFrame(song_names, columns=['track_id'])
word_count_df = pd.DataFrame(song_word_counts)
word_count_df = word_count_df.transpose()
# word_count_df.index.name = 'track_id'
word_count_df.reset_index()
print (word_count_df)
# result = pd.merge(songs_df, song_name_df, on='track_id')
# print (result)

# print (result.shape)