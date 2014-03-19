# coding:utf-8
# 盒內塔範例
# 計算 N 個碟子從 s 位置移動到 d 位置需要移動幾次。
# 並且記錄一棟步驟。

# 思考方式為反向思考，先不要想程式細節部分，打個比方來說
# 如果要移動 3 層的盒內塔：
# 	1.必動要先移動好2層的盒內塔到暫存器
# 	2.再把來原的最後一個盤子移到目的地
# 	3.再把站存器的盤子移到目的地

# 同理可推：
	# function move('碟子數量', '來原', '目的地', '站存器'){
	# 	function('碟子數量-1', '來原', '站存器' ,'目的地')  	# 使用目的地當作站存器來移動把碟子全數移到站存器
	# 	print '來原', 'move to', '目的地'						# 把最底下那個大碟子從來原怡到目的地
	# 	function('碟子數量-1', '站存器', '目的地', '來原')  	# 把站存器所有的碟子移動到目的地，完工！
	# }

	# 近一步要思考判斷當碟子數量為 1 的時候怎麼做....

	# function move('碟子數量', '來原', '目的地', '站存器'){
	# 	if 碟子數量 == 1
	# 		print '來原', 'move to', '目的地'					# 要是帶到底下那個區塊就搞笑了 -1 會造成無窮遞迴(遞迴的終止條件)
	# 	else
	# 		function('碟子數量-1', '來原', '站存器' ,'目的地')  # 使用目的地當作站存器來移動把碟子全數移到站存器
	# 		print '來原', 'move to', '目的地'					# 把最底下那個大碟子從來原怡到目的地
	# 		function('碟子數量-1', '站存器', '目的地', '來原')  # 把站存器所有的碟子移動到目的地，完工！
	# 	end
	# }

# 注意：寫遞迴程式一定要做終止條件不然就無窮迴圈了！

# |
# ||
# |||
# 's'	't'	'd'

# level 3
# def move(s, d, t):
# 	print s,'to',d
# 	print s,'to',t
# 	print d,'to',t
# 	print s,'to',d
# 	print t,'to',s
# 	print t,'to',d
# 	print s,'to',d

# 展示範例(以 Python 實作)
count = 0
def move(n, s, d, t):
	global count
	if n==1:
		print s, 'move to', d
		count +=1
	else:
		move(n-1, s, t, d)
		print s, 'move to', d
		count +=1
		move(n-1, t, d, s)

	return count

if __name__ == '__main__':
	print move(3, 's', 'd', 't')