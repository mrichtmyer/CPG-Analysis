import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

## Lambda functions ##
## ---------------- ##

def star(rev):
    return int(rev[0])

def helpful(rev):
    rev = rev.split(' ')[0]
    
    try:
        # the first element of the list is a number and we can directly return it
        num = int(rev)
        return num
    
    except:
        # the first element of the list is the string 'one'
        if rev == "One":
            return 1
        # the list contains 'report abuse' which means there were no upvotes for
        # this review
        else:
            return 0
        None
def date(rev):
    return pd.to_datetime(rev[33:])

def word_count(rev):
    # tokenize
    return len(word_tokenize(rev))



# def star(rev):
#     try:
#         num = int(rev[0])
#         return num
#     except:
#         None
    
# def helpful(rev):
#     try:
#         rev = rev.split(' ')[0]
#         # the first element of the list is a number and we can directly return it
#         num = int(rev)
#         return num
    
#     except:
#         # the first element of the list is the string 'one'
#         if rev == "One":
#             return 1
#         # the list contains 'report abuse' which means there were no upvotes for
#         # this review
#         else:
#             return 0
#         None

# def date(rev):
#     try:
#         abc = pd.to_datetime(rev[33:])
#         return abc
#     except:
#         None

# def word_count(rev):
#     # tokenize
#     return len(word_tokenize(rev))


# def convTime(rev):
#     try:
#         corr_date = rev-pd.offsets.MonthBegin(1)
#         return corr_date
#     except:
#         None

def etl(data):

    # clean up dataframe with lambda functions defined above
    data["stars"] = data.apply(lambda x: star(x["stars"]), axis=1)
    data["helpful"] = data.apply(lambda x: helpful(x["helpful"]),axis=1)
    data["review_date"] = data.apply(lambda x: date(x["review_date"]), axis=1)
    data["word_count"] = data.apply(lambda x: word_count(x["review"]),axis=1)
    #data['YearMonth'] = data.apply(lambda x: convTime(x["review_date"]),axis=1)

    data['YearMonth'] = data['review_date'] - pd.offsets.MonthBegin(1)


    return data

def text_emotion(df,column):
    
    new_df = df.copy()
    
    filepath = ('data/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt')  
    
    emolex_df = pd.read_csv(filepath, names=["word", "emotion", "association"], sep='\t')
    emolex_words = emolex_df.pivot(index='word',
                                   columns='emotion',
                                   values='association').reset_index()
    emotions = emolex_words.columns.drop('word')
    
    emo_df = pd.DataFrame(0,index=df.index, columns=emotions)
    
    stemmer = SnowballStemmer("english")
    
    for i in range(0, len(new_df)):
        row = new_df[column][i]
        document = word_tokenize(row)
        
        for word in document:
            word = stemmer.stem(word.lower())
            
            emo_score = emolex_words[emolex_words.word == word]
            
            if not emo_score.empty:
                for emotion in list(emotions):
                    emo_df.at[i,emotion] += emo_score[emotion]
        new_df = pd.concat([new_df, emo_df], axis=1)
    
    return new_df

def monthlyEmotionAvg(df):
    # calculate date
    df['YearMonth'] = df['review_date'] - pd.offsets.MonthBegin(1)
    date = list(df["YearMonth"]) ## HAVE TO HAVE THIS FCN
    
    # calculate emotional response
    emotion_df = text_emotion(df,"review")
    
    # take row sums
    emotion_df["anger_sum"] = emotion_df["anger"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["anticipation_sum"] = emotion_df["anticipation"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["disgust_sum"] = emotion_df["disgust"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["fear_sum"] = emotion_df["fear"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["joy_sum"] = emotion_df["joy"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["negative_sum"] = emotion_df["negative"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["positive_sum"] = emotion_df["positive"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["sadness_sum"] = emotion_df["sadness"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["surprise_sum"] = emotion_df["surprise"].sum(axis=1)/len(emotion_df["review"])
    emotion_df["trust_sum"] = emotion_df["trust"].sum(axis=1)/len(emotion_df["review"])
    
    # take just sums
    emotion_df = emotion_df.iloc[:,-10:]
    
    # store emotional response for all 10 vectors in dictionary
    month_avg = {}
    for col in emotion_df.columns:
        emotions = list(emotion_df[col])
        col_name = col[:-4]
        # pd dataframe is not json serializable
        month_avg[col_name] = list(pd.DataFrame({"Date": date, "Emotion": emotions}).groupby("Date").mean()["Emotion"])#.plot(kind="line") 
    
    
    return month_avg # this is just returning a dictionary, not list of dictionary which is needed for JS

