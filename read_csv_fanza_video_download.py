# 出演作品一覧ページのCSVファイルからサンプルビデオのURLを抽出してすべての動画をダウンロードするコード。
# ASRockPCで、期待通りに動作確認。20221010
import csv
import requests
from bs4 import BeautifulSoup
import json
filename = '猫村ゆゆ(ねこむらゆゆ) _4_.csv'
with open(filename, encoding='utf8', newline='') as f:
	csvreader = csv.reader(f)
	video_url = []
	# 作品ページのURL取得
	for row in csvreader:
		#print(row[2])
		video_url.append(row[2])
	print(video_url)

def soup2(video_url):
	res = requests.get(video_url)
	soup = BeautifulSoup(res.text, 'html.parser')
	
	age_check_url = soup.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
	
	res2 = requests.get(age_check_url)
	
	soup2 = BeautifulSoup(res2.text, 'html.parser')
	
	return soup2    

def get_move(url):
	json_dict = None
	res3 = requests.get(url)
	soup3 = BeautifulSoup(res3.text, 'html.parser')
	url3 = soup3.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
	res4 = requests.get(url3)
	soup4 = BeautifulSoup(res4.text, 'html.parser')
	json_2= soup4.find("script", {"type": "application/ld+json"})
	data = json_2.text
	#サンプル動画が存在しないと['subjectOf']キーが無いってエラーが出るのでサンプル動画があったら処理をする。
	if "subjectOf" in data and "contentUrl" in data:
		json_dict = json.loads(data)
		#print(json_dict)
		move_url = (json_dict['subjectOf']['contentUrl']).replace('sm', 'mhb')
		move_title = (json_dict['name'])
		print(move_url)
		#動画タイトル名をファイル名に使用するので長すぎるとエラーになるので５０文字以上なら短く加工する処理
		if len(move_title) > 50:
			#タイトルの先頭から３５文字に＊＊＊＊をつなげてタイトル末尾１５文字を連結してファイル名を作成。
			move_title = move_title[:35] + '＊＊＊＊' + move_title[-15:]
		#動画タイトルの中に「/」スラッシュが入っていると、動画保存するパスが変わってしまうので置換処理。
		move_title = move_title.replace('/', '_')
		response = requests.get(move_url)
		print(response.status_code)
	
		if response.status_code == 200:
				
			pass
		else:
			move_url = move_url.replace('mhb', 'dmb')
			response = requests.get(move_url)
		
		with open('/Users/i3-12100/fanza/' + move_title + '.mp4', 'wb') as saveFile:
			saveFile.write(response.content)

for url in video_url:
	get_move(url)
	
	

