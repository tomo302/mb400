import os
import requests
from bs4 import BeautifulSoup
import re
import json



#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cead00336/?dmmref=actress_1008785&i3_ref=list&i3_ord=31"





url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cead00427/?dmmref=actress_26225&i3_ref=list&i3_ord=25"
def soup2(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	
	age_check_url = soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
	
	res2 = requests.get(age_check_url)
	
	soup2 = BeautifulSoup(res2.text, 'html.parser')
	
	return soup2

url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=mide00981/"

url2 = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=huw002/"

soup2 = soup2(url2)

# サンプル画像（大）のURLとビデオタイトルを返す関数
def get_sample_large_url(soup2):
	video_title = soup2.find("h1", id = "title").text

	try:
		for _ in soup2.find("div", id="sample-image-block").find_all("a"):
			print(_['href'])
	except KeyError:
		print("サンプル画像（大）はありません")

	get_sample_tag = soup2.find_all('img', class_ ="mg-b6")
	small_sample_urls = []
	for img in get_sample_tag:
		small_sample_urls.append(img['src'])
	large_sample_urls = []
	add_word = "jp-"
	for url in small_sample_urls:
		split_url = url.split('-')
		large_sample_urls.append(split_url[0] + add_word + split_url[1])
	return large_sample_urls, video_title


large_sample_urls, video_title = get_sample_large_url(soup2)


print(large_sample_urls)

print(video_title)


"""
<a name="sample-image" id="sample-image2" href="https://pics.dmm.co.jp/digital/video/mide00981/mide00981jp-2.jpg" class="crs_full"><img src="https://pics.dmm.co.jp/digital/video/mide00981/mide00981-2.jpg" border="0" alt="電撃専属 汁・汗・潮・液・唾・涎 体液ダダ漏れ性交SPECIAL 深田えいみ" class="mg-b6"></a>
<div id="sample-image-block"

"""
# try:
# 	for _ in soup2.find("div", id="sample-image-block").find_all("a"):
# 		print(_['href'])
# except KeyError:
# 	print("サンプル画像はありません")

for _ in soup2.find_all('img', class_ = "mg-b6"):
	print(_['src'])
	print(_['alt'])
	file_name = _['alt'].replace(' ', '_') + '_' + _['src'].split('-')[-1]
	print(file_name)

print()
print()
# 作品タイトル取得パターン
print(soup2.find('img', class_ = "mg-b6")['alt'])
print(soup2.find("meta", property="og:title")['content'])

print(soup2.find("div", id="sample-video").a['href'])

def get_json_data(soup2):
	json_2 = soup2.find('script', type="application/ld+json")
	json_text = json_2.text

	
	json_dict = json.loads(json_2.text) #pickle作成時と混同しないこと！！
	print()
	print(json_dict['name'])
	print()
	json_dict['description']
	print()
	json_dict['sku']
	print()
	 json_dict['image']
	print()
	json_dict['subjectOf']['contentUrl']
	print()
	print(json_dict['subjectOf']['actor']['name'])
	print()
	print(json_dict['subjectOf']['actor']['alternateName'])