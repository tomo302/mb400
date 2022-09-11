#このコードはFANZAのページの種類を取得するコード
def page_kind(soup2):

	pk = str(soup2.find_all('li', class_ = 'terminal')[1]).split('/')[6]

	if pk == "article=actress":
		print("出演作品一覧ページです")
		pk = sakuhin
	elif pk == "article=keyword":
		print("ジャンルページです")
		pk = "genru"
	elif pk == "actress":
		print("５０音ページです")
		pk = "50on"
	return pk