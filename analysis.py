# Module 3 
# analyzing the data we have
# and we will make new cols in data for better analysis

import pandas as pd
import re
import emoji
import nltk

try :
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords",quiet=True)
from nltk.corpus import stopwords

from collections import Counter

def create_useful_columns(df):
    # df["date"]=pd.to_datetime(df["date"], 
    #                           format="%d/%m/%y",
    #                           errors="coerce")
    # normalizing date
    df["date"]=pd.to_datetime(df["date"],format="mixed",dayfirst=True,errors="coerce")

    # normalizing time 
    if (df["period"]=="").all():
        df["time"]=pd.to_datetime(
                       df["time"],
                       format="mixed",
                       errors= "coerce"
                                ).dt.time
    else: 
        df["time"] = pd.to_datetime(
                        df["time"] + " " + df["period"],
                        format="mixed",
                        errors="coerce"
                                ).dt.time




    df["hour"]=df["time"].apply(lambda x:x.hour)
    df["day"]=df["date"].dt.day
    df["month_name"]=df["date"].dt.month_name()
    df["month"]=df["date"].dt.month
    df["weekday"]=df["date"].dt.day_name()
    df["year"]=df["date"].dt.year
    df["word_count"]=df["message"].str.split().str.len()
    df["message_length"]=df["message"].str.len()
    return df  

def fetch_basic_stats(df): # nn
    ans={}
    ans["total_messages"]=df["message"].count()
    ans["total_participant"]=df["sender"].nunique()
    ans["total_words"]=df["word_count"].sum()
    ans["avg_words"]=(df["word_count"].mean())
    ans["avg_message_length"]=(df["message_length"].mean())
    ans["total_link"]=(df["type"]=="Link").sum()
    ans["total_media"]=(df["type"]=="Media").sum()
    ans["total_text_msg"]=(df["type"]=="Text").sum()
    return ans

# def fetch_sender_stats(df):
#     ans={}

#     for sender in df["sender"].dropna().unique():
#         curr_df=df[df["sender"]==sender]
#         ans[sender]={
#         "total_message":curr_df["message"].count(),
#         "total_words":curr_df["word_count"].sum(),
#         "avg_words":curr_df["word_count"].mean(),
#         "avg_message_length":curr_df["message_length"].mean(),
#         "media_count":(curr_df["type"]=="Media").sum(),
#         "links_count":(curr_df["type"]=="Link").sum(),
#         "message_percentage":(len(curr_df)/len(df))*100}
#     return ans

def fetch_sender_stats(df): # nn
    grouped=df.groupby("sender")

    ans=grouped.agg(
        total_messages=("message","count"),
        total_words=("word_count","sum"),
        avg_words=("word_count","mean"),
        avg_message_length=("message_length","mean"),

    )

    ans["media_count"]=grouped["type"].apply(lambda x:(x=="Media").sum())
    ans["links_count"]=grouped['type'].apply(lambda x:(x=="Link").sum())
    ans["text_count"]=grouped["type"].apply(lambda x:(x=="Text").sum())
    ans["message_percentage"]=(ans["total_messages"]/ans["total_messages"].sum())*100



    return ans    


def fetch_daily_timeline(df):
    grouped=df.groupby(["date"])
    ans=grouped.agg(
        total_messages=("message","count")
    )
    return ans


def fetch_monthly_timeline(df):
    grouped=df.groupby(["year","month"])
    ans=grouped.agg(
        total_messages=("message","count")
        )
    return ans


def fetch_weekday_stats(df):
    week_order=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    grouped=df.groupby("weekday")
    ans=grouped.agg(
        total_messages=("message","count")
    )
    ans=ans.reindex(week_order,fill_value=0)

    return ans


def fetch_hourly_timeline(df):
    grouped=df.groupby("hour")
    h=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    ans=grouped.agg(
        total_messages=("message","count")
    )
    ans=ans.reindex(h,fill_value=0)
    return ans


def fetch_activity_heatmap(df):
    week_order=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    hour_order=list(range(24))

    ans=pd.pivot_table(
        df,
        values="message",
        index="weekday",
        columns="hour",
        aggfunc="count",
        fill_value=0
    )
    ans=ans.reindex(index=week_order,columns=hour_order,fill_value=0)
    return ans


def fetch_most_active_dates(df): # nn
    daily=fetch_daily_timeline(df)
    ans=daily.sort_values(by="total_messages",ascending=False).head(10)
    return ans


def fetch_sender_activity(df):
    h=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    ans=pd.pivot_table(
        df,
        columns="sender",
        index="hour",
        values="message",
        aggfunc="count",
        fill_value=0
    )
    ans=ans.reindex(index=h,fill_value=0)
    return ans


def fetch_activity_by_weekday(df):
    week_order=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    ans=pd.pivot_table(
        df,
        columns="sender",
        index="weekday",
        values="message",
        aggfunc="count",
        fill_value=0
    )
    ans=ans.reindex(index=week_order,fill_value=0)
    return ans


def fetch_type_stats(df):
    type_order=["Text","Media","Link","Call"]
    ans=pd.pivot_table(
        df,
        columns="type",
        index="sender",
        values="message",
        aggfunc="count",
        fill_value=0
    )
    ans=ans.reindex(columns=type_order,fill_value=0)
    return ans


def fetch_subtypes_stats(df):
    subtype_order = [
    "Text",
    "URL",
    "Image",
    "Video",
    "Audio",
    "Voice_message",
    "Sticker",
    "PDF",
    "Other",
    "Unspecified",
    "Unknown"
              ]
    ans=pd.pivot_table(
        df,
        columns="subtype",
        index="sender",
        values="message",
        aggfunc="count",
        fill_value=0
    )
    ans=ans.reindex(columns=subtype_order,fill_value=0)
    return ans




# stage 2
# NLP

def fetch_word_freq(df):
    temp=df[df["type"]=="Text"].copy()
    text=" ".join(temp["message"].dropna())
    text=text.lower()

    # Remove punctuation and special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Split the string into individual words
    words = text.split()

    # stopwords
    stop_words=set(stopwords.words("english"))

    # custom hindi stop words
    stop_words.update([
        "hai", "hain", "tha", "thi", "the",
    "nahi", "nai", "ni", "kya", "kyu",
    "ka", "ki", "ke", "ko", "se",
    "me", "mein", "mai", "aur", "toh",
    "bhi", "ye", "yeh", "woh", "wo",
    "iska", "uska", "ek", "hi", "he",
    "h", "hu", "hun", "hain",
    "bhai", "tu", "rha", "raha", "rhi", "rahi",
    "nhi", "nahi", "nai",
    "kr", "kar", "k", "ho", "hu",
    "na", "haa", "haan",
    "de", "le", "gya", "gaya",
    "ab", "abhi", "aaj", "kal",
    "kuch", "tere", "tera", "tko", "mko",
    "vo", "woh", "abe", "ok",
    "sab", "theek", "lia", "liya",
    "hua", "mat", "krna", "dunga", "dia",
    "aa", "bas", "maine", "baat", "mere","omitted","edited","message","deleted","mt","ne",
    "fir","koi","media"
    ])

    words=[word for word in words if word not in stop_words]

    word_freq=Counter(words)
    return word_freq


def fetch_emoji_stats(df):
    temp=df[df['type']=="Text"].copy()
    text=" ".join(temp["message"].dropna())

    emojis=emoji.emoji_list(text) # makes a dict of dicts
    emoji_list=[item["emoji"] for item in emojis] # just list comprehension

    emoji_freq=Counter(emoji_list)
    return emoji_freq




