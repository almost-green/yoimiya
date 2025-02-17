while True:
    print("1.猜數字遊戲")
    print("0.離開程式")
    user = int(input("請選擇:"))
    list = user
    if user == 0:
        break
    elif user == 1:
        import Gjun.game.guessNumber as game
        game.play()
print("歡迎下次再玩")
