
#重要・URLを判定してページに合った関数を実行させる役割のurl_check(url)関数。
def url_check(url):
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
url_check("https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=cead00336/?dmmref=actress_1008785&i3_ref=list&i3_ord=49")

def actress(url):
	pass

def genru(url):
	pass

def sakuhin_list(url):
	pass

def video_page(url):
	pass

	