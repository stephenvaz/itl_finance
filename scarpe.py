from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

#use session to get the page
r = session.get('https://economictimes.indiatimes.com/reliance-industries-ltd/stocksupdate/companyid-13215.cms')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r.html.render(sleep=1, scrolldown=5)

articleContainer = r.html.find('div.eachStory')
# print(len(articleContainer))

articleList = []

for article in articleContainer:
    try:
        fullTitle = article.find('div.headingText', first=True)
        title = fullTitle.find('h3', first=True).text
        date = article.find('div.storyDate', first=True).text
        info = article.find('p', first=True).text
        article = {
            'title': title,
            'date': date,
            'info': info
        }
        articleList.append(article)
    except:
        pass

# print(articleList[0])

# create a csv file with title, date, info
df = pd.DataFrame(articleList)
df.to_csv('article.csv', index=False)
print(df.head())