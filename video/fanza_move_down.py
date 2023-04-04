from bs4 import BeautifulSoup
import itertools
import requests
import re
import json
import time
#これ以降のコードは１本のビデオのURLでダウンロードするコード。
#url2 = 'https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ssni00299/?dmmref=recommend6_detail&i3_ref=recommend&i3_ord=12'#一つのアドレスで動画ダウンロードテスト
url2 = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=1stars00668/?dmmref=keyword_6965&i3_ref=list&i3_ord=3"
res3 = requests.get(url2)

soup3 = BeautifulSoup(res3.text, 'html.parser')

url3 = soup3.find('a', class_ ="ageCheck__link ageCheck__link--r18")['href']
# END 作品ページ取得ここまで
#リダイレクトを突破したURLでスクレイピング開始。
res4 = requests.get(url3)

soup4 = BeautifulSoup(res4.text, 'html.parser')
#動画URLサンプル：：https://cc3001.dmm.co.jp/litevideo/freepv/h/hmn/hmn00160/hmn00160_mhb_w.mp4
# 抽出したいタグ・・・・<script type="application/ld+json">　ターゲットはこれ！！
#以降参考にしたサイト：https://teratail.com/questions/295808
#動画タイトルとURLが存在するタグをまるごと抽出。多分簡素に直接、タイトルとURLを取得できるかもしれないが、全体像を知っておいたほうが今後の為になるはず・・
json_2= soup4.find("script", {"type": "application/ld+json"})
print(type(json_2))
#bs4のノードからテキストを取り出す。type:str
data = json_2.text
#テキストからjsonとしてパースする。type:dict
json_dict = json.loads(data)	# 文字列をjsonとして辞書型で読み込む
print(json_dict)

#動画のURL取得 720x404 mhb , sm 320X180 取得できるのは smなので、urlないのsmをmhbに置換して大きいサイズをダウンロードしている。

json_dict['subjectOf']['name']

move_url = (json_dict['subjectOf']['contentUrl']).replace('sm', 'mhb')
#move_url = (json_dict['subjectOf']['contentUrl'])
print((move_url))

#動画のタイトル取得。保存ファイル名に使用する。

move_title = (json_dict['name'])

print(type(move_title))
if len(move_title) > 50:
    title = move_title[:35] + '＊＊＊＊' + move_title[-15:]

#動画ダウンロード成功だが、保存ファイル名は、動画タイトルを使用。
response = requests.get(move_url)

# 開始 sleep時間をカウントしない処理時間
start_time = time.process_time()
response = requests.get(move_url)
#サンプル動画に大きいサイズのURLが存在した場合ダウンロードする
if response.status_code == 200:
    with open('/Users/i3-12100/git/mb400/video/' + move_title + '.mp4', 'wb') as saveFile:
        saveFile.write(response.content)
else:
    move_url = (json_dict['subjectOf']['contentUrl']).replace('sm', 'dmb')
    response = requests.get(move_url)
    with open('/Users/i3-12100/git/mb400/video/' + move_title + '.mp4', 'wb') as saveFile:
        saveFile.write(response.content)

    # ダミー処理
    #time.sleep(1)

    # 修了
    end_time = time.process_time()

    # 経過時間を出力(秒)
    elapsed_time = end_time - start_time
    print(elapsed_time)
    print("終了しました")
    print("ステータスコード：　" + str(response.status_code))
