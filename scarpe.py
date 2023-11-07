from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

r = session.get('https://economictimes.indiatimes.com/reliance-industries-ltd/stocksupdate/companyid-13215.cms')

r.html.render(sleep=1, scrolldown=5)

articleContainer = r.html.find('div.eachStory')

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

df = pd.DataFrame(articleList)
df.to_csv('article.csv', index=False)
print(df.head())