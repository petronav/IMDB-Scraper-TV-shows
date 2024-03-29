# Top TV shows scraper
This repository is for scraping the top 250 TV shows based on IMDB rating listed [here](https://www.imdb.com/chart/toptv/). Here is a sample TV-show details scraped :

```
'Breaking Bad': {'duration': '2008–2013',
                  'genre': ['Crime', 'Drama', 'Thriller'],
                  'rating': 9.5,
                  'rating_count': 1232141,
                  'show_url': 'https://www.imdb.com/title/tt0903747/',
                  'summary': 'A high school chemistry teacher diagnosed with '
                             'inoperable lung cancer turns to manufacturing '
                             'and selling methamphetamine in order to secure '
                             "his family's future.",
                  'type': 'Full'},
```

## Run instruction

Run as `python3 get_shows.py` to save the json.
Run as `python3 visualize.py` to visualize the heatmap of related genres.

### Heatmap plot

From the top 250 TV-series genre types, here is a cross fold heatmap for all the genres in all the TV-shows :

![heatmap](seaborn_cross_fold_plot.png)
