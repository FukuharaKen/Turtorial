while True:
    try:
        x = int(input('数字を入れて下さい:'))
        break
    except (TypeError,ValueError,NameError):
        print("数字じゃ無いじゃん")

