import requests
from Keys import line_notify_key
url='https://notify-api.line.me/api/notify'
print('請留意token是你的不是老師的')
token=line_notify_key
headers={'Authorization':'Bearer '+token}
data={
    'message':'Python',
    'imageThumbnail':'https://www.google.com/imgres?q=%E8%B7%91%E8%B7%91%E8%96%91%E9%A4%85%E4%BA%BA%20%E8%87%89%E6%9B%B8&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D1802821323295761&imgrefurl=https%3A%2F%2Fzh-tw.facebook.com%2Fcookierunzh%2Fposts%2F%25E8%25B7%2591%25E8%25B7%2591%25E5%25B0%258F%25E5%258F%25AE%25E5%259A%2580%25E4%25BA%258B%25E5%2589%258D%25E7%25B6%2581%25E5%25AE%259A%25E4%25BD%25A0%25E7%259A%2584%25E9%2581%258A%25E6%2588%25B2%25E7%25B4%2580%25E9%258C%2584%25E4%25BF%259D%25E8%25AD%25B7%25E4%25BD%25A0%25E7%259A%2584%25E8%25B7%2591%25E8%25B7%2591%25E8%2596%2591%25E9%25A4%2585%25E4%25BA%25BAios%25E7%25B3%25BB%25E7%25B5%25B11-%25E5%2589%258D%25E5%25BE%2580%25E6%2589%258B%25E6%25A9%259F%25E8%25A3%259D%25E7%25BD%25AE%25E8%25A8%25AD%25E5%25AE%259A-game-center-%25E4%25B8%25AD%25E7%2599%25BB%25E5%2585%25A5game-center%25E5%25B8%25B3%25E8%2599%259F2-%25E6%2589%2593%25E9%2596%258B%25E8%25B7%2591%25E8%25B7%2591%25E8%2596%2591%25E9%25A4%2585%25E4%25BA%25BA%25E7%2583%25A4%25E7%25AE%25B1%25E5%25A4%25A7%2F1802821323295761%2F&docid=x7hl_thBFU9uSM&tbnid=ajYVaryITQyP2M&vet=12ahUKEwj46-StopeKAxXNh68BHZcMAtkQM3oECGUQAA..i&w=1200&h=1200&hcb=2&ved=2ahUKEwj46-StopeKAxXNh68BHZcMAtkQM3oECGUQAA',
    'imageFullsize':'https://www.google.com/imgres?q=%E8%B7%91%E8%B7%91%E8%96%91%E9%A4%85%E4%BA%BA%20%E8%87%89%E6%9B%B8&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D1802821323295761&imgrefurl=https%3A%2F%2Fzh-tw.facebook.com%2Fcookierunzh%2Fposts%2F%25E8%25B7%2591%25E8%25B7%2591%25E5%25B0%258F%25E5%258F%25AE%25E5%259A%2580%25E4%25BA%258B%25E5%2589%258D%25E7%25B6%2581%25E5%25AE%259A%25E4%25BD%25A0%25E7%259A%2584%25E9%2581%258A%25E6%2588%25B2%25E7%25B4%2580%25E9%258C%2584%25E4%25BF%259D%25E8%25AD%25B7%25E4%25BD%25A0%25E7%259A%2584%25E8%25B7%2591%25E8%25B7%2591%25E8%2596%2591%25E9%25A4%2585%25E4%25BA%25BAios%25E7%25B3%25BB%25E7%25B5%25B11-%25E5%2589%258D%25E5%25BE%2580%25E6%2589%258B%25E6%25A9%259F%25E8%25A3%259D%25E7%25BD%25AE%25E8%25A8%25AD%25E5%25AE%259A-game-center-%25E4%25B8%25AD%25E7%2599%25BB%25E5%2585%25A5game-center%25E5%25B8%25B3%25E8%2599%259F2-%25E6%2589%2593%25E9%2596%258B%25E8%25B7%2591%25E8%25B7%2591%25E8%2596%2591%25E9%25A4%2585%25E4%25BA%25BA%25E7%2583%25A4%25E7%25AE%25B1%25E5%25A4%25A7%2F1802821323295761%2F&docid=x7hl_thBFU9uSM&tbnid=ajYVaryITQyP2M&vet=12ahUKEwj46-StopeKAxXNh68BHZcMAtkQM3oECGUQAA..i&w=1200&h=1200&hcb=2&ved=2ahUKEwj46-StopeKAxXNh68BHZcMAtkQM3oECGUQAA'
}
data=requests.post(url,headers=headers,data=data)
print(data)