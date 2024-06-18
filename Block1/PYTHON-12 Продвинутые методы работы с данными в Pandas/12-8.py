import re 
import pandas as pd

def get_year_release(arg):
    candidates = re.findall(r'\(\d{4}\)', arg)  
    if len(candidates) > 0:
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        return None
rating=pd.read_csv('data/ratings_movies.csv')
rating_df=rating.copy()
rating_df['year']=get_year_release(rating_df['title'])