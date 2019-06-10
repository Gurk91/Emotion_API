from negative_bot import neg_predict

while True:
    try:
        user = input()
        print(neg_predict(user))
    except:
        KeyboardInterrupt
        break

