import fanza_getSoup2
from fanza_getSoup2 import get_maxPage

#<title>篠田ゆう2枚組ハイパーベスト8時間 - エロ動画・アダルトビデオ - FANZA動画</title>
#ビデオURL
#url = "https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cead00336/?dmmref=actress_1008785&i3_ref=list&i3_ord=49"

#ジャンル 女子大生：1019
#url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=1019/"

#ジャンル アスリート：6965
url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=6965/"

#女優「し」
#url = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=si/"

#出演作品一覧ページ：id=10758 椎名あきら
#url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=10758/"


"""
20220707追記 最大ページを計算で取得するパターン
５０音ページネーション
<div class="list-boxcaptside list-boxpagenation group">
<p>215人中　1～100人　全3ページ中　1ページ目を表示</p>

ジャンルページネーション
<div class="list-boxcaptside list-boxpagenation">
<p>457タイトル中　1～120タイトル　1ページ目を表示</p>

出演作品一覧ページネーション
<div class="list-boxcaptside list-boxpagenation">
<p>1,681タイトル中　1～120タイトル　1ページ目を表示</p>
"""

"""
ページネーション最大ページ数をタグから抽出
５０音ページ
<li class="terminal">
<a href="https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=a/page=12/">最後へ</a></li>

ジャンルページ
<li class="terminal">
<a href="/digital/videoa/-/list/=/article=keyword/id=1001/page=88/">最後へ</a></li>

出演作品一覧ページ
<li class="terminal">
<a href="/digital/videoa/-/list/=/article=actress/id=1008785/page=15/">最後へ</a></li>

３ページとも同じタグ構造
soup2.find('li', class_ = 'terminal').a.split('/')

"""

soup2 = fanza_getSoup2.soup2(url)
page_title = soup2.title
#print(page_title)
print(url)
if "d/i" in url:
    print("ジャンルページです")
    #ジャンルページ用の関数を実行
elif "a/-/a" in url:
    print("５０音ページです")
    #５０音ページ用の関数を実行
elif "t&" in url:
    print("ビデオページです")
    #ビデオページ用の関数を実行
elif "s/i" in url:
    print("出演一覧ページ")
    #出演一覧ページ用の関数を実行
print(soup2.title)


get_maxPage(soup2)
