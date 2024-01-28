import requests

from pprint import pprint
import datetime
from bs4 import BeautifulSoup
import pandas as pd

def crawl():
	cookies = {
		'sp': 'adba7bd0-16e4-461f-9c1f-7826b59336b0',
		'_scid': 'b751155b-0d2a-4540-a1cc-95b71249b411',
		'xp_session_identifier': 'th7j41rsoem',
		'_gcl_au': '1.1.742260922.1699251999',
		'_strava_cbv3': 'true',
		'_fbp': 'fb.1.1699713403296.1821153676',
		'elevate_desktop_promo_hidden': 'true',
		'_sctr': '1%7C1705420800000',
		'_strava4_session': 'gp03e1lepsncc7por51t1avhud0v7r8u',
		'_gid': 'GA1.2.838242471.1705756311',
		'CloudFront-Key-Pair-Id': 'APKAIDPUN4QMG7VUQPSA',
		'elevate_daily_connection_done': 'true',
		'fbm_284597785309': 'base_domain=.www.strava.com',
		'CloudFront-Policy': 'eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vaGVhdG1hcC1leHRlcm5hbC0qLnN0cmF2YS5jb20vKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcwNjcxNjM0OX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzA1NDkyMzQ5fX19XX0_',
		'CloudFront-Signature': 'GOaG4t2yRxlG4z1mo00XRqc43Vec8pUc7JgpAaWgERcy00D51aBHi1D5BOBznwO8yFquCT2uAKDWoPI3kpBNI6qaHO3II~Pg7edQkvTuI2abDiZFR9gZynmAJjB6uFKjQ816bYqBBijMk8enZaKhKSMowAnnE~6QhoetodApwO2ju4nPLNlnnKB8wL7P8Ir-omc0WxuMlG7XtXEgDGvR-onxPmiqt3z2RM5ht~BfoaI3dXsFBApTN9kXvRwCGFU~o3JncwFbSee9CdPLiIBJqMxgCPle~W2SV7ySC6uAJatTweNvUC49-LKKOs18HPxYoVNRkzj5eZac2YwdGBOY0g__',
		'_sp_ses.047d': '*',
		'fbsr_284597785309': 'RcFUChBqAYDl17jEE4WN3rx0DHfAvcwiPGj3jzWzfkU.eyJ1c2VyX2lkIjoiMzIzNTE5NjkxMDEzNzk4MiIsImNvZGUiOiJBUUEwNkMyVHE4Z3VGMS1aejN2N2VNOHNTQ2IwLUg2N3lPVk1Ba3RhdUxOSmVrd2dzWG9QQ0ZTZktsZGk1SzhLaFB0bVd2eXpUeVExaEx2M1hVVmFJY3NyMjZqTnBDdVVwYkRuWDhNcGZNbXZDU3V4QTBmSTlNVFhpT3doeUtXRkY3LVkyTEoxRGoxYWdPdEZQOWExT1BROFFjYUNUSGJxNzh5N3Iyd2k4cUd6RlNNbDA0NFVGelctTlcyTGV2akQyUUlFeUdvaU0yNG43V09vQ1pLVlBZSFI3NXNtU2tPcXkycDRnU2RkcFBaRWIxRnlHbzlQZmhXQWkwcTdiOWtvODJiWlZfWl9NNEdDY2t2bTFhaFFQdndjbDFyOU9BdXNYSzFSTVFuOFlNclFCZER6MkxlakpoT1VBeVFiVVNnTGxnajNLZE5MM3lrVVRxRExlYkVsZll4OCIsIm9hdXRoX3Rva2VuIjoiRUFBQUFRa05aQWt0MEJPejdDR0tURk9Wd1pCUGlObzh2ZmZwTFpCUTYzTVpDTjU3REZMWFpCNFdkUTVWenBObzVNWWtMejdpWVZRU2FKeUNWRlpDSWZMRDdaQjBEOW9sWWFsM1JlQjl6MWJtOGpKSUFCREVScWRXUTFmSEFZYWZFVDBXSGRhem5aQWVka2k2NmFMc0VDeWw3MWVXNUdZUlQwakhkS3liVXdtb0JWVVEzcE5aQWEyd0NuaHdDSExneVpDQ1d5MmN6b1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MDU4OTI5MjJ9',
		'fbsr_284597785309': 'yrtuDBOogUZdL969B5b5EzjvXlQ0MnFtuEV7aI7N2A4.eyJ1c2VyX2lkIjoiMzIzNTE5NjkxMDEzNzk4MiIsImNvZGUiOiJBUUR3em5lTW41WVIxMTNQZHMtWmx3NlRRbXBEb0t6N280WUtRc2sxV2FYUlFrZ0dJWFJnemFjMjk3RWUxVWozMWRNR0NGVVpfTndmT3A3UjRTdkM2bnVoTm1wSDNLbng4XzhjOTJ4LUxIS1VuTEtmQ0tfX2l0a3NDTXhVMmtWcWJjd1JSQjRFXzJpSnQ0Qk9ENFBCSlJoa2duRHJzVjNZb083UVZKdGlfbVZlUlNBelZKYUo1ZGlZQ3NSNUpGbTAyLS11dTdUMGlfOUxJbnV4YnlkazU4SXdfRTE1SU83OWVvN3dOaTBTUV9YZWdqZ0ZwZDBrUl95UG9LTTNSQzh3STJZY0FaZS1seW1IY1VVdi1jWHVfM2xReV9CRG1vV29wUk0xU1ZqQ3Z2NWJmTzhyZm95QVZNTWlKREx3OXVYM3hucFByQ1JZdU1wTk1pa0xodmN3dE9ESCIsIm9hdXRoX3Rva2VuIjoiRUFBQUFRa05aQWt0MEJPejdDR0tURk9Wd1pCUGlObzh2ZmZwTFpCUTYzTVpDTjU3REZMWFpCNFdkUTVWenBObzVNWWtMejdpWVZRU2FKeUNWRlpDSWZMRDdaQjBEOW9sWWFsM1JlQjl6MWJtOGpKSUFCREVScWRXUTFmSEFZYWZFVDBXSGRhem5aQWVka2k2NmFMc0VDeWw3MWVXNUdZUlQwakhkS3liVXdtb0JWVVEzcE5aQWEyd0NuaHdDSExneVpDQ1d5MmN6b1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MDU4OTMwNTB9',
		'_dc_gtm_UA-6309847-24': '1',
		'_gat': '1',
		'_ga_ESZ0QKJW56': 'GS1.1.1705892922.94.1.1705894189.56.0.0',
		'_ga': 'GA1.2.2128658248.1691402014',
		'_sp_id.047d': '3c1bf0b9-4f68-4c41-a588-a36816a8ec86.1691401989.101.1705894190.1705853953.119b2cb1-c00a-49d9-a25f-28e196f94577',
		'_ga_8W80LVBJ1W': 'GS1.2.1705892922.79.1.1705894189.0.0.0',
		'_scid_r': 'b751155b-0d2a-4540-a1cc-95b71249b411',
	}

	headers = {
		'authority': 'www.strava.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
		'cache-control': 'max-age=0',
		# 'cookie': 'sp=adba7bd0-16e4-461f-9c1f-7826b59336b0; _scid=b751155b-0d2a-4540-a1cc-95b71249b411; xp_session_identifier=th7j41rsoem; _gcl_au=1.1.742260922.1699251999; _strava_cbv3=true; _fbp=fb.1.1699713403296.1821153676; elevate_desktop_promo_hidden=true; _sctr=1%7C1705420800000; _strava4_session=gp03e1lepsncc7por51t1avhud0v7r8u; _gid=GA1.2.838242471.1705756311; CloudFront-Key-Pair-Id=APKAIDPUN4QMG7VUQPSA; elevate_daily_connection_done=true; fbm_284597785309=base_domain=.www.strava.com; CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vaGVhdG1hcC1leHRlcm5hbC0qLnN0cmF2YS5jb20vKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcwNjcxNjM0OX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzA1NDkyMzQ5fX19XX0_; CloudFront-Signature=GOaG4t2yRxlG4z1mo00XRqc43Vec8pUc7JgpAaWgERcy00D51aBHi1D5BOBznwO8yFquCT2uAKDWoPI3kpBNI6qaHO3II~Pg7edQkvTuI2abDiZFR9gZynmAJjB6uFKjQ816bYqBBijMk8enZaKhKSMowAnnE~6QhoetodApwO2ju4nPLNlnnKB8wL7P8Ir-omc0WxuMlG7XtXEgDGvR-onxPmiqt3z2RM5ht~BfoaI3dXsFBApTN9kXvRwCGFU~o3JncwFbSee9CdPLiIBJqMxgCPle~W2SV7ySC6uAJatTweNvUC49-LKKOs18HPxYoVNRkzj5eZac2YwdGBOY0g__; _sp_ses.047d=*; fbsr_284597785309=RcFUChBqAYDl17jEE4WN3rx0DHfAvcwiPGj3jzWzfkU.eyJ1c2VyX2lkIjoiMzIzNTE5NjkxMDEzNzk4MiIsImNvZGUiOiJBUUEwNkMyVHE4Z3VGMS1aejN2N2VNOHNTQ2IwLUg2N3lPVk1Ba3RhdUxOSmVrd2dzWG9QQ0ZTZktsZGk1SzhLaFB0bVd2eXpUeVExaEx2M1hVVmFJY3NyMjZqTnBDdVVwYkRuWDhNcGZNbXZDU3V4QTBmSTlNVFhpT3doeUtXRkY3LVkyTEoxRGoxYWdPdEZQOWExT1BROFFjYUNUSGJxNzh5N3Iyd2k4cUd6RlNNbDA0NFVGelctTlcyTGV2akQyUUlFeUdvaU0yNG43V09vQ1pLVlBZSFI3NXNtU2tPcXkycDRnU2RkcFBaRWIxRnlHbzlQZmhXQWkwcTdiOWtvODJiWlZfWl9NNEdDY2t2bTFhaFFQdndjbDFyOU9BdXNYSzFSTVFuOFlNclFCZER6MkxlakpoT1VBeVFiVVNnTGxnajNLZE5MM3lrVVRxRExlYkVsZll4OCIsIm9hdXRoX3Rva2VuIjoiRUFBQUFRa05aQWt0MEJPejdDR0tURk9Wd1pCUGlObzh2ZmZwTFpCUTYzTVpDTjU3REZMWFpCNFdkUTVWenBObzVNWWtMejdpWVZRU2FKeUNWRlpDSWZMRDdaQjBEOW9sWWFsM1JlQjl6MWJtOGpKSUFCREVScWRXUTFmSEFZYWZFVDBXSGRhem5aQWVka2k2NmFMc0VDeWw3MWVXNUdZUlQwakhkS3liVXdtb0JWVVEzcE5aQWEyd0NuaHdDSExneVpDQ1d5MmN6b1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MDU4OTI5MjJ9; fbsr_284597785309=yrtuDBOogUZdL969B5b5EzjvXlQ0MnFtuEV7aI7N2A4.eyJ1c2VyX2lkIjoiMzIzNTE5NjkxMDEzNzk4MiIsImNvZGUiOiJBUUR3em5lTW41WVIxMTNQZHMtWmx3NlRRbXBEb0t6N280WUtRc2sxV2FYUlFrZ0dJWFJnemFjMjk3RWUxVWozMWRNR0NGVVpfTndmT3A3UjRTdkM2bnVoTm1wSDNLbng4XzhjOTJ4LUxIS1VuTEtmQ0tfX2l0a3NDTXhVMmtWcWJjd1JSQjRFXzJpSnQ0Qk9ENFBCSlJoa2duRHJzVjNZb083UVZKdGlfbVZlUlNBelZKYUo1ZGlZQ3NSNUpGbTAyLS11dTdUMGlfOUxJbnV4YnlkazU4SXdfRTE1SU83OWVvN3dOaTBTUV9YZWdqZ0ZwZDBrUl95UG9LTTNSQzh3STJZY0FaZS1seW1IY1VVdi1jWHVfM2xReV9CRG1vV29wUk0xU1ZqQ3Z2NWJmTzhyZm95QVZNTWlKREx3OXVYM3hucFByQ1JZdU1wTk1pa0xodmN3dE9ESCIsIm9hdXRoX3Rva2VuIjoiRUFBQUFRa05aQWt0MEJPejdDR0tURk9Wd1pCUGlObzh2ZmZwTFpCUTYzTVpDTjU3REZMWFpCNFdkUTVWenBObzVNWWtMejdpWVZRU2FKeUNWRlpDSWZMRDdaQjBEOW9sWWFsM1JlQjl6MWJtOGpKSUFCREVScWRXUTFmSEFZYWZFVDBXSGRhem5aQWVka2k2NmFMc0VDeWw3MWVXNUdZUlQwakhkS3liVXdtb0JWVVEzcE5aQWEyd0NuaHdDSExneVpDQ1d5MmN6b1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MDU4OTMwNTB9; _dc_gtm_UA-6309847-24=1; _gat=1; _ga_ESZ0QKJW56=GS1.1.1705892922.94.1.1705894189.56.0.0; _ga=GA1.2.2128658248.1691402014; _sp_id.047d=3c1bf0b9-4f68-4c41-a588-a36816a8ec86.1691401989.101.1705894190.1705853953.119b2cb1-c00a-49d9-a25f-28e196f94577; _ga_8W80LVBJ1W=GS1.2.1705892922.79.1.1705894189.0.0.0; _scid_r=b751155b-0d2a-4540-a1cc-95b71249b411',
		'referer': 'https://www.strava.com/athlete/segments/starred?page=2&page_uses_modern_javascript=true',
		'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Linux"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
	}

	params = {
		'page': '1',
		'page_uses_modern_javascript': 'true',
		'per_page': '1000'
	}

	response = requests.get('https://www.strava.com/athlete/segments/starred', params=params, cookies=cookies, headers=headers)

	soup=BeautifulSoup(response.content, 'html.parser')
	return str(soup)
