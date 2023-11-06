import requests
import pandas as pd
url = "https://text-analysis12.p.rapidapi.com/sentiment-analysis/api/v1.1"

payload = {
	"language": "english",
	"text": "In the frontline IT pack, Infosys was average performing stock, as it shed close to 16% so far in 2023, and hit a 52-week low in April. From its 52-week high, the stock is down about 24%."
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "902244c5f6mshf1eaa2464e9100fp1993dfjsn610632dea406",
	"X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
}

# response = requests.post(url, json=payload, headers=headers)



# print(response.json())
df = pd.read_csv('article.csv')

for ind in df.index:
	payload = {
		"language": "english",
		"text": f"{df['title'][ind]}. {df['info'][ind]}"
	}
	response = requests.post(url, json=payload, headers=headers)
	response = requests.post(url, json=payload, headers=headers)
	print(response.json())
	break
