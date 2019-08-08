from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles
import json

def weighted_genre_metric(json_file):
    f = open(json_file)
    r = f.read()
    dict_ = json.loads(r)
    all_genres = []
    for show, show_dict in dict_.items():
        all_genres.append(show_dict['genre'])

    unique_genres = {i for j in all_genres for i in j}
    unique_genres = set(sorted(unique_genres))

    level_I_genres = {'Crime', 'Action', 'Thriller', 'Drama'}
    level_II_genres = {'Mystery', 'History', 'Adventure'}
    level_III_genres = {'Biography', 'War'}
    level_IV_genres = {'Horror', 'Sport', 'Documentary'}
    level_V_genres = unique_genres - level_I_genres.union(level_II_genres).union(level_III_genres).union(level_IV_genres)
    genre_dict = {}
    for i in level_I_genres:
        genre_dict[i] = 10
    for j in level_II_genres:
        genre_dict[j] = 7.5
    for i in level_III_genres:
        genre_dict[i] = 5
    for i in level_IV_genres:
        genre_dict[i] = 2.5
    for i in level_V_genres:
        genre_dict[i] = 0
    show_rating_dict = {}
    for show, show_dict in dict_.items():
        show_rating_dict[show] = round(sum([genre_dict[i] for i in show_dict['genre'] if i])/len(show_dict['genre']))
    show_rating_dict = dict(sorted(show_rating_dict.items(), key=lambda x : x[1], reverse=True))
    unique_rating = sorted(list({i for _,i in show_rating_dict.items()}))
    plot_dict = {i : sum(1 for m in show_rating_dict if show_rating_dict[m]==i) for i in unique_rating}
    heatmap(all_genres, unique_genres)
    return plot_dict

def heatmap(all_genres, unique_genres):
    import seaborn as sns
    sns.set(rc={'figure.figsize':(16,9)})
    genre_matrix = []
    for i in unique_genres:
        temp = []
        for j in unique_genres:
            s = sum(1  if i in m and j in m and i!=j else 0 for m in all_genres)
            temp.append(s)
        genre_matrix.append(temp)
    genre_matrix = np.array(genre_matrix)
    ax = sns.heatmap(genre_matrix, xticklabels=list(unique_genres), 
            yticklabels=list(unique_genres), annot=True, linewidths=.42, 
            cbar=True, cbar_kws={'label': 'Colorbar'})
    plt.savefig('seaborn_cross_fold_plot.png')
    plt.show()


def bar_plot(plot_dict, show_=False):
    xval = list(plot_dict.values())
    ybars = tuple(plot_dict.keys())
    y_pos = np.arange(len(ybars))
    plt.barh(y_pos, xval)
    plt.yticks(y_pos, ybars)
    plt.xlabel('Number of TV Shows', fontsize=18)
    plt.ylabel('Weighted Rating', fontsize=16)
    plt.savefig('weighted_rating_horizontal_barplot.png')
    if show_:
        plt.show()


if __name__ == '__main__':
    bar_plot(weighted_genre_metric('AllShows.json'))
