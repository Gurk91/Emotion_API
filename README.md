# Emotion_API

*** README ***

So far, this bot has been trained only on 300 lines of dialogue

I have cleaned and prepared an additional 40000 in movie_dataset.txt.
To train the bot on this, take the 'from.txt' and 'to.txt' files and put them in 
'conversation_data' or 'conversation_data_neg' folder, depending on the bot you want to train.

You would use 'conversation_data' to train the bot in 'chatbot_logic.py' and 'conversation_data_neg' to train the bot in 'negative_bot.py'.

I think the Cornell Movie dialogue corpus has about 100,000 lines of dialogue, so if you want to use all 100,000, go to 'movie_dataset', 'cornell_cleaner.py' and change the 40000 to 100,000. The code should be fine.

Run emotion_api.py to run the program

The positive chatbot is in 'chatbot_logic.py' and the negative chatbot is in 'negative_bot.py'. Sentiment analysis is done in 'sentiment_analyzer.py'. 
