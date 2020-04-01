from sqlalchemy import create_engine

import pandas as pd
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

import json

        



def extractStars(row):
    """Lambda function to extract number of stars left in rating"""
    return float(row.split(' ')[0]) 

def extractHelpful(row):
    """Lambda function to extract number of upvotes on Amazon"""
    rev = row.split(' ')[0]
    
    if(rev.isnumeric()):
        return int(rev)
    elif(rev=="one"):
        return 1
    else:
        return 0
    
def extractDate(row):
    """Lambda function to convert string into datetime object"""
    date = pd.to_datetime(row[33:])
    return date

def convertTime(rev):
    """Lambda function to abstract datetime object per month for groupby"""
    corr_date = rev-pd.offsets.MonthBegin(1) 
    return corr_date

def countWords(rev):
    """Lambda function to count all words in a particular review"""
    return len(word_tokenize(rev))



# define function to read data from PostgreSQL server
def readData(table="eucerin_intensive_lotion", 
         engine=create_engine("postgresql://postgres:postgres@localhost/CPG")):
    
    # connect engine
    conn = engine.connect()
    
    # try making query asked for
    try:
        query = f"SELECT * FROM {table}"
        # attempt to read table queried
        data = pd.read_sql(query,conn)
    except:
        # output default data
        query = "SELECT * FROM eucerin_intensive_lotion"
        data = pd.read_sql(query,conn)
    
    return data


# perform data loading and transforming in one function
def read_transform(table="eucerin_intensive_lotion",
                   engine=create_engine("postgresql://postgres:postgres@localhost/CPG")):
    """Docstring: makes query to PostgreSQL database using the table defined.
    Performs all transformations, including cleaning prior to returning dataframe"""
    
    # read in raw data from PostgreSQL
    data = readData(table,engine)
    
    # transformations
    data["stars"] = data.apply(lambda x: extractStars(x["stars"]),axis=1)
    data["helpful"] = data.apply(lambda x: extractHelpful(x["helpful"]),axis=1)
    data["review_date"] = data.apply(lambda x: extractDate(x["review_date"]),axis=1)
    data["corr_date"] = data.apply(lambda x: convertTime(x["review_date"]),axis=1)
    data["word_count"] = data.apply(lambda x: countWords(x["review"]),axis=1)
    
    # perform groupby on month to get aggregate data
    gb = data.groupby('corr_date')["stars"].mean()
    
    # populate dictionary containing all data to pass back to route
    ratings_dict = {}
    ratings_dict["review_date"] = list(data["review_date"])
    ratings_dict["gb_date"] = gb.index.tolist()
    ratings_dict["avg_monthly_rating"] = list(gb)
    ratings_dict["histogram_rating_values"] = np.histogram(data["stars"], bins=[1,2,3,4,5,6])[0].tolist()
    ratings_dict["histogram_rating_bins"] = np.histogram(data["stars"], bins=[1,2,3,4,5,6])[1].tolist()
    
    
    return data, ratings_dict












# def text_emotion(df,column):
    
#     new_df = df.copy()
    
#     filepath = ('data/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt')  
    
#     emolex_df = pd.read_csv(filepath, names=["word", "emotion", "association"], sep='\t')
#     emolex_words = emolex_df.pivot(index='word',
#                                    columns='emotion',
#                                    values='association').reset_index()
#     emotions = emolex_words.columns.drop('word')
    
#     emo_df = pd.DataFrame(0,index=df.index, columns=emotions)
    
#     stemmer = SnowballStemmer("english")
    
#     for i in range(0, len(new_df)):
#         row = new_df[column][i]
#         document = word_tokenize(row)
        
#         for word in document:
#             word = stemmer.stem(word.lower())
            
#             emo_score = emolex_words[emolex_words.word == word]
            
#             if not emo_score.empty:
#                 for emotion in list(emotions):
#                     emo_df.at[i,emotion] += emo_score[emotion]
#         new_df = pd.concat([new_df, emo_df], axis=1)
    
#     return new_df

# def monthlyEmotionAvg(df):
#     # calculate date
#     df['YearMonth'] = df['review_date'] - pd.offsets.MonthBegin(1)
#     date = list(df["YearMonth"]) ## HAVE TO HAVE THIS FCN
    
#     # calculate emotional response
#     emotion_df = text_emotion(df,"review")
    
#     # take row sums
#     emotion_df["anger_sum"] = emotion_df["anger"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["anticipation_sum"] = emotion_df["anticipation"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["disgust_sum"] = emotion_df["disgust"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["fear_sum"] = emotion_df["fear"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["joy_sum"] = emotion_df["joy"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["negative_sum"] = emotion_df["negative"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["positive_sum"] = emotion_df["positive"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["sadness_sum"] = emotion_df["sadness"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["surprise_sum"] = emotion_df["surprise"].sum(axis=1)/len(emotion_df["review"])
#     emotion_df["trust_sum"] = emotion_df["trust"].sum(axis=1)/len(emotion_df["review"])
    
#     # take just sums
#     emotion_df = emotion_df.iloc[:,-10:]
    
#     # store emotional response for all 10 vectors in dictionary
#     month_avg = {}
#     for col in emotion_df.columns:
#         emotions = list(emotion_df[col])
#         col_name = col[:-4]
#         # pd dataframe is not json serializable
#         month_avg[col_name] = list(pd.DataFrame({"Date": date, "Emotion": emotions}).groupby("Date").mean()["Emotion"])#.plot(kind="line") 
    
#     return json.dumps(month_avg) # this is just returning a dictionary, not list of dictionary which is needed for JS

