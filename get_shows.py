import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pprint import pprint as pp

def get_show_details(show_url):
	show_details = {}
	show_details['show_url'] = show_url
	r = requests.get(show_url)
	if r.status_code == 200:
		soup = bs(r.text, 'html.parser')

		rating_div = soup.find_all('div', class_='ratingValue')
		rating_title = rating_div[0].find_all('strong')[0]['title']
		rating_title = rating_title.split('based')
		rating = int(''.join(k for k in rating_title[0] if k.isnumeric()))/10
		show_details['rating'] = rating
		total_ratings = int(''.join(k for k in rating_title[1] if k.isnumeric()))
		show_details['rating_count'] = total_ratings

		genre_sub_text = soup.find_all('div', class_='subtext')
		genre_sub_text_links = genre_sub_text[0].find_all('a')
		genres = [i.text for i in genre_sub_text_links if 'genre' in i['href']]
		show_details['genre'] = genres
		release_info = [i.text for i in genre_sub_text_links if 'release' in i['href']]
		release_years = release_info[0].split('(')[-1]
		release_years = release_years[:release_years.rfind(')')]
		show_details['duration'] = release_years
		show_details['type'] = 'Mini' if 'mini' in release_info[0].lower() else 'Full' 

		summary_div = soup.find_all('div', class_='summary_text')
		summary_text = summary_div[0].text
		summary_text = "".join(i.strip() for i in summary_text.splitlines())
		show_details['summary'] = summary_text

	return show_details



def main():
	url = 'https://www.imdb.com/chart/toptv/'
	r = requests.get(url)
	if r.status_code == 200:
		soup = bs(r.text, 'html.parser')
		shows_table = soup.find_all('td', class_='titleColumn')
		shows_links_title_dict = {i.find_all('a')[0].text : 'https://www.imdb.com'+i.find_all('a')[0]['href'] for i in shows_table}
		shows_all_details = {k : get_show_details(v) for k,v in list(shows_links_title_dict.items())[:6]}


if __name__ == '__main__':
	main()