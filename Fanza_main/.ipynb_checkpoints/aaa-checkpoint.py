from soup2 import soup2, page_kind, get_maxPage, make_pageNationUrlList


# URLサンプル
# 50音ページ
# https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=a/page=1/
#ジャンルページ
# https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=1001/page=1/
# 出演作品一覧ページ
# https://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=1039047/page=1/  枢木あおい(くるるぎあおい)



# 使用するURLを指定
#url = "https://www.dmm.co.jp/digital/videoa/-/actress/=/keyword=si/"
#url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=keyword/id=1001/"
url = "https://www.dmm.co.jp/digital/videoa/-/list/=/article=actress/id=1008785/" #篠田ゆう


soup2 = soup2(url)

#######################################################################################
#出演作品一覧ページ 取得値：「article=actress」
#page_kind = str(soup2.find_all('li', class_ = 'terminal')[1]).split('/')[6]

#ジャンルページ 取得値： 「article=keyword」
#page_kind = str(soup2.find_all('li', class_ = 'terminal')[1]).split('/')[6]

#５０音ページ 取得値： 「actress」
#page_kind = str(soup2.find_all('li', class_ = 'terminal')[1]).split('/')[6]
########################################################################################

#max_page = soup2.find_all('li', class_ = 'terminal')
#max_page = int(str(max_page[1]).split('/')[-4].split('=')[1])
max_page = get_maxPage(soup2)

print("最大ページは：" + str(max_page))





# max_page = int(str(max_page[1]).split('/')[-4].split('=')[1])



page_kind = str(page_kind(soup2))

print("このページは：" + page_kind + "です")

make_pageNationUrlList(max_page, page_kind)