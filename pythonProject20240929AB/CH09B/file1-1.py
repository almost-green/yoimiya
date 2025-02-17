no=1
scores=dict()
while True:
    score = int(input('請輸入第'+str(no)+'號的成績:(-1結束)'))
    if score == -1: break;
    scores[no] = score
    no += 1
file = open('score.txt', 'w', encoding='utf-8')
file.write(str(scores))
#資料如何開啟與寫入