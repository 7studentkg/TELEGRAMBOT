import requests

url = "https://www.film.ru/compilation/luchshie-multfilmy-hayao-miyadzaki"

payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
  'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.google.com/',
  'Connection': 'keep-alive',
  'Cookie': '_ga_BPVGCQN0CF=GS1.1.1698692534.4.1.1698692645.9.0.0; _ga=GA1.2.1461913855.1698489216; cto_bundle=F3USgV9zeVZnRDVidEglMkJCUmI5UGxpRWYwMCUyRmRwR295Rk0wb1lMYUFCZWl0VGpSRUpjZXhyOSUyRmhvUlNPMmJDJTJGVkVpODElMkJvSkNwb2tFYUp5WlBSdUJRRWdaT2k2SDVMaTJKN1dzeW9QUmlFWmslMkY5b1hFTFVpa2cyVU9pb1lvZWp1UXlCTEY2JTJGTE9zelgwJTJGdWg2UUpsRENaRllnJTNEJTNE; _gid=GA1.2.1263783423.1698687351',

}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
