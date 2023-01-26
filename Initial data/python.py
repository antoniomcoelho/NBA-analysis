from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests


def load_web_page():
    # URL to scrape
    url = "https://www.basketball-reference.com/playoffs/"
    #url = "https://www.transfermarkt.com/premier-league/transfers/wettbewerb/GB1/"

    # collect HTML data
    #html = urlopen(url)
            
    # create beautiful soup object from HTML
    #soup1 = BeautifulSoup(html, features="lxml")


    page = requests.get(url)
    with open('C:\\Users\\amfcc\\MyDocuments\\Data Engineering\\1 - MyProject - NBA\\saving.html', 'wb+') as f:
        f.write(page.content)


def main():

    # Get soup from web or load it
    if 0:
        soup1 = load_web_page()
    else:
        with open('C:\\Users\\amfcc\\MyDocuments\\Data Engineering\\1 - MyProject - NBA\\saving.html', 'rb') as f:
            soup = BeautifulSoup(f.read(), 'lxml')

    # use getText()to extract the headers into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    print([th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')])
    print("")

    # get rows from table
    rows = soup.findAll('tr')[2:]
    rows_data = [[td.getText() for td in rows[i].findAll('td')]
                        for i in range(len(rows))]# if you print row_data here you'll see an empty row
    print(rows_data[0:38])
    print("")

    # so, remove the empty row
    rows_data.pop(20)# for simplicity subset the data for only 39 seasons
    rows_data = rows_data[0:38]
    print(rows_data)
    print("")

    # we're missing a column for years
    # add the years into rows_data
    last_year = 2020
    for i in range(0, len(rows_data)):
        rows_data[i].insert(0, last_year)
        last_year -=1
    print(rows_data)
    print("")

    # create the dataframe
    nba_finals = pd.DataFrame(rows_data, columns = headers)# export dataframe to a CSV 
    nba_finals.to_csv("C:\\Users\\amfcc\\MyDocuments\\Data Engineering\\1 - MyProject - NBA\\nba_finals_history.csv", index=False)






def load_web_page_standings(year_init, year_final):

    for year in range(year_init, year_final):
        # URL to scrape
        url = f'http://webcache.googleusercontent.com/search?q=cache:https://www.basketball-reference.com/leagues/NBA_{year}_standings.html'
        #url = "https://www.transfermarkt.com/premier-league/transfers/wettbewerb/GB1/"

        # collect HTML data
        #html = urlopen(url)
                
        # create beautiful soup object from HTML
        #soup1 = BeautifulSoup(html, features="lxml")


        page = requests.get(url)
        with open(f'C:\\Users\\amfcc\\MyDocuments\\Data Engineering\\1 - MyProject - NBA\\standings\\standings_{year}.html', 'wb+') as f:
            f.write(page.content)

def main_standings(year_init, year_final):

    for year in range(year_init, year_final):
        print(f'______________ Year {year} ___________________ ')

        # Get soup from web or load it
        if 0:
            soup1 = load_web_page()
        else:
            with open(f'C:\\Users\\amfcc\\MyDocuments\\Data Engineering\\1 - MyProject - NBA\\standings\\standings_{year}.html', 'rb') as f:
                soup = BeautifulSoup(f.read(), 'lxml')

        # Use getText()to extract the headers into a list
        headers  = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
        headers.insert(0, 'year')

        # Get rows from table
        rows = soup.findAll('tr')[2:]
        rows_data = [[td.getText() for td in rows[i].findAll('td')] 
                            for i in range(len(rows))] # Get statistics
        rows_data_team = [[td.getText() for td in rows[i].findAll('a')] 
                            for i in range(len(rows))] # Get team name

        # Check the number of teams    
        number_teams = len(rows_data)
        for i in range(0, len(rows_data)):
            for j in range(0, len(rows_data[i])):
                if  rows_data[i][j].find("Division Standings") > 0:
                    number_teams = i

        # Select the data related to the first standing table
        rows_data = [[td.getText() for td in rows[i].findAll('td')]
                            for i in range(number_teams)]
        rows_data_team = [[td.getText() for td in rows[i].findAll('a')]
                            for i in range(number_teams)]

        # Delete empty rows
        flag_cycle = len(rows_data)
        while i < flag_cycle:
            if rows_data[i] == []:
                print(rows_data[i])
                rows_data.pop(i)
                i = i - 1
                flag_cycle = flag_cycle - 1
            else:
                i = i + 1

        # Add the years into rows_data
        for i in range(0, len(rows_data)):
            try:
                rows_data[i].insert(0, year)
                rows_data[i].insert(1, rows_data_team[i][0])
            except:
                1

        # Create the dataframe
        nba_finals = pd.DataFrame(rows_data, columns = headers)# export dataframe to a CSV 
        nba_finals.to_csv(f'C:\\Users\\amfcc\\MyDocuments\\Data Engineering\\1 - MyProject - NBA\\standings_csv\\nba_standings_{year}.csv', index=False)

        1

if __name__ == '__main__':
    #main()
    #load_web_page_standings(2000, 2020)
    #load_web_page_standings(2009, 2020)
    main_standings(2000, 2020)
