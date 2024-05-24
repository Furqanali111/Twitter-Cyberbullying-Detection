# importing important libraries for performing different tasks
import pandas as pd
from textblob import TextBlob

# reading file
file_path = "twitter_parsed_dataset.csv"
df = pd.read_csv(file_path)

# reading the tweet column from dataset
Tweet_col = df['Text']
# initializing cyber bulling list
bullying_list = []

# converting the column data to list
tweet_list = Tweet_col.tolist()

# calculating the length of the dataset
length = len(tweet_list)

poscount = 0
negcount = 0
neucount = 0


def sentiment_analysis():
    global poscount, negcount, neucount
    # creating a loop that will run from start of the data set and end on the last value
    for i in range(0, length):
        text = tweet_list[i]
        # checking if the data type is string or not
        if isinstance(text, str):
            analysis = TextBlob(text)

            # Get the sentiment polarity of the text
            polarity = analysis.sentiment.polarity

            # Output the sentiment polarity
            if polarity > 0:
                bullying_list.append("Positive")
                poscount += 1
            elif polarity < 0:
                bullying_list.append("Negative")
                negcount += 1
            else:
                bullying_list.append("Neutral")
                neucount += 1
        else:
            bullying_list.append("Neutral")


if __name__ == '__main__':
    sentiment_analysis()

    df["Cyber_Bullying"] = pd.Series(bullying_list)
    df.to_csv(file_path, mode='w', index=False)

    print("Total Postive tweets = ", poscount)
    print("Total Negative tweets = ", negcount)
    print("Total Neutral tweets = ", neucount)
