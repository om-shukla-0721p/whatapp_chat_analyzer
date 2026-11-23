# Module->4 
# For visualization 
# seeing plots gives better vibes and easier to read data

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud

def apply_chart_theme(fig, ax, grid=True):

    fig.patch.set_facecolor("#101820")
    ax.set_facecolor("#1D2A35")

    ax.tick_params(colors="#AAB8C5")

    ax.xaxis.label.set_color("#AAB8C5")
    ax.yaxis.label.set_color("#AAB8C5")
    ax.title.set_color("#E8EEF2")

    for spine in ax.spines.values():
        spine.set_color("#40515E")

    if grid:
        ax.set_axisbelow(True)
        ax.grid(
            True,
            color="#40515E",
            alpha=0.4,
            linestyle="--"
        )

# def plot_daily_timeline(daily_df):
#     fig,ax=plt.subplots(figsize=(12,5))

#     sns.lineplot(
#         data=daily_df,
#         x=daily_df.index,
#         y="total_messages",
#         ax=ax
#     )

#     ax.set_title("Daily Message Timeline",fontsize=20,color="red")
#     ax.set_xlabel("Date",fontsize=23,color="blue")
#     ax.set_ylabel("Number of Messages",fontsize=25)
#     plt.xticks(rotation=90)
#     fig.tight_layout()

#     return fig
def plot_daily_timeline(daily_df):
    fig, ax = plt.subplots(figsize=(12, 5))

    fig.patch.set_facecolor("#101820")
    ax.set_facecolor("#1D2A35")

    sns.lineplot(
        data=daily_df,
        x=daily_df.index,
        y="total_messages",
        ax=ax,
        color="#45C4B0",
        linewidth=2.5
    )

    ax.set_title(
        "Daily Message Timeline",
        fontsize=18,
        color="#E8EEF2",
        pad=15
    )

    ax.set_xlabel("Date", fontsize=12, color="#AAB8C5")
    ax.set_ylabel("Number of Messages", fontsize=12, color="#AAB8C5")

    ax.tick_params(axis="x", colors="#AAB8C5", rotation=45)
    ax.tick_params(axis="y", colors="#AAB8C5")

    for spine in ax.spines.values():
        spine.set_color("#40515E")

    ax.grid(
        True,
        color="#40515E",
        alpha=0.4,
        linestyle="--"
    )

    fig.tight_layout()

    return fig

# def plot_monthly_timeline(monthly_df):
#     fig,ax=plt.subplots(figsize=(12,5))
#     monthly_df=monthly_df.reset_index()
#     monthly_df["date"]=pd.to_datetime(monthly_df[["year","month"]].assign(day=1))

#     sns.lineplot(
#         data=monthly_df,
#         x="date",
#         y="total_messages",
#         ax=ax
#     )

#     ax.set_title("Monthly Message Timeline",fontsize=20,color="red")
#     ax.set_xlabel("Months",fontsize=23,color="blue")
#     ax.set_ylabel("Number of Messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()
#     return fig

# def plot_weekday_stats(weekday_df):
#     fig,ax=plt.subplots(figsize=(10,5))

#     sns.barplot(
#         weekday_df,
#         x=weekday_df.index,
#         y="total_messages",
#         ax=ax,
#         palette="viridis",
#         hue="total_messages"
#     )
#     ax.set_title("weekdays stats",fontsize=20,color="red")
#     ax.set_xlabel("weekdays",fontsize=23,color="blue")
#     ax.set_ylabel("Number of Messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()
#     return fig


# def plot_hourly_activities(hourly_df):
#     fig,ax=plt.subplots(figsize=(10,5))
    
#     sns.barplot(
#         hourly_df,
#         x=hourly_df.index,
#         y="total_messages",
#         ax=ax,
#         palette="viridis",
#         hue="total_messages"
#     )
#     ax.set_title("Hourly stats",fontsize=20,color="red")
#     ax.set_xlabel("Hour of the day",fontsize=23,color="blue")
#     ax.set_ylabel("Number of Messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()
#     return fig


# def plot_activity_heatmap(heatmap_df):
#     fig,ax=plt.subplots(figsize=(10,5))
        
#     sns.heatmap(
#         heatmap_df,
#         ax=ax,
#         annot=True,
#         fmt="d",
#         cmap="viridis"

#     )
#     ax.set_title("Weekly Activity heatmap",fontsize=20,color="red")
#     ax.set_xlabel("Hour of the day",fontsize=15,color="blue")
#     ax.set_ylabel("Weekday",fontsize=25,color="green")
#     fig.tight_layout()
#     return fig



# def plot_sender_activity(activity_df):
#     fig,ax=plt.subplots(figsize=(12,5))
#     activity_df=activity_df.reset_index()
#     activity_df=activity_df.melt(
#         id_vars="hour",
#         var_name="sender",
#         value_name="messages"
#     )
            
#     sns.lineplot(
#         activity_df,
#         x="hour",
#         y="messages",
#         hue="sender",
#         ax=ax,

#     )
#     ax.set_title("Sender Activity by Hour",fontsize=20,color="red")
#     ax.set_xlabel("Hour of the Day",fontsize=23,color="blue")
#     ax.set_ylabel("Number of Messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()

#     return fig
# #n



# def plot_sender_weekday_activity(activity_df):
#     fig,ax=plt.subplots(figsize=(12,5))
#     activity_df=activity_df.reset_index()
#     activity_df=activity_df.melt(
#         id_vars="weekday", # col
#         var_name="sender", # row
#         value_name="messages"
#     )

#     sns.lineplot(
#         activity_df,
#         x="weekday",
#         y="messages",
#         hue="sender",
#         ax=ax,

#     )
#     ax.set_title("Senders Activity by weekday",fontsize=20,color="red")
#     ax.set_xlabel("Weekday",fontsize=23,color="blue")
#     ax.set_ylabel("Number of messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()

#     return fig

# def plot_type_stats(type_df):
#     fig,ax=plt.subplots(figsize=(10,5))

#     type_df=type_df.reset_index()

#     type_df=type_df.melt(
#         id_vars="sender",
#         var_name="type",
#         value_name="messages"
#     )

#     sns.barplot(
#         type_df,
#         x="type",
#         y="messages",
#         hue="sender",
#         palette="viridis",
#         ax=ax
#     )
#     ax.set_title("Type of message stats",fontsize=20,color="red")
#     ax.set_xlabel("Type of message",fontsize=23,color="blue")
#     ax.set_ylabel("Number of messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()

#     return fig

# def plot_subtypes_stat(subtypes_df):
#     fig,ax=plt.subplots(figsize=(15,6))
#     subtypes_df=subtypes_df.reset_index()
#     subtypes_df=subtypes_df.melt(
#         id_vars="sender",
#         var_name="subtype",
#         value_name="messages"
#     )

#     sns.barplot(
#         subtypes_df,
#         x="subtype",
#         y="messages",
#         hue="sender",
#         palette="viridis",
#         ax=ax
#     )

#     ax.set_title("Subtypes stats",fontsize=20,color="red")
#     ax.set_xlabel("Subtypes",fontsize=23,color="blue")
#     ax.set_ylabel("Number of messages",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()

#     return fig


# def plot_word_frequency(word_freq):
#     fig,ax=plt.subplots(figsize=(12,6))
#     top_20=word_freq.most_common(20)
#     word_df=pd.DataFrame(top_20,columns=["word","freq"])

#     sns.barplot(
#         word_df,
#         x="word",
#         y="freq",
#         hue="freq",
#         palette="viridis",
#         ax=ax,
#         legend=False
#                 )
#     ax.set_title("Most Common words",fontsize=20,color="red")
#     ax.set_xlabel("Words",fontsize=23,color="blue")
#     ax.set_ylabel("Frequency",fontsize=25,color="green")
#     plt.xticks(rotation=90)
#     fig.tight_layout()

#     return fig



# def plot_emoji_stats(emoji_freq):
#     fig,ax=plt.subplots(figsize=(10,6))
#     top_30=emoji_freq.most_common(30)
#     top_30=pd.DataFrame(top_30,columns=["emoji","frequency"])

#     sns.barplot(
#         top_30,
#         x="frequency",
#         y="emoji",
#         hue="frequency",
#         palette="viridis",
#         legend=False,
#         ax=ax
#     )
#     ax.set_title("Most Common Emoji",fontsize=20,color="red")
#     ax.set_xlabel("Frequency",fontsize=23,color="blue")
#     ax.set_ylabel("Emojis",fontsize=25,color="green")
#     fig.tight_layout()
#     return fig

# def plot_emoji_stats_df(emoji_freq):
#     top_30=emoji_freq.most_common(30)
#     top_30=pd.DataFrame(top_30,columns=["emoji","frequency"])
#     return top_30


# def plot_wordcloud(word_freq):
#     wc=WordCloud(
#         width=1000,
#         height=500,
#         background_color="#18232D",
#         colormap="winter",
#         min_font_size=10,

#     ).generate_from_frequencies(word_freq)

#     fig,ax=plt.subplots(figsize=(12,6))

#     ax.imshow(
#         wc,
#         interpolation="bilinear",
#     )
#     ax.axis("off")
#     ax.set_title("Most Freuently used words",fontsize=16)

#     return fig 


# def plot_participant_comparision(comparision_stats,column,title,ylabel):
#     fig,ax=plt.subplots(figsize=(10,5))

#     sns.barplot(
#         data=comparision_stats,
#         x="sender",
#         y=column,
#         ax=ax,
#         hue="sender",
#         palette="viridis"
#     )

#     ax.set_title(title)
#     ax.set_xlabel("Pariticipants")
#     ax.set_ylabel(ylabel)

#     plt.xticks(rotation=15)
#     plt.tight_layout()
#     return fig




def plot_monthly_timeline(monthly_df):
    fig,ax=plt.subplots(figsize=(12,5))
    monthly_df=monthly_df.reset_index()
    monthly_df["date"]=pd.to_datetime(monthly_df[["year","month"]].assign(day=1))

    sns.lineplot(
        data=monthly_df,
        x="date",
        y="total_messages",
        ax=ax,
        color="#45C4B0",
        linewidth=2.5
    )

    ax.set_title("Monthly Message Timeline",fontsize=18,pad=15)
    ax.set_xlabel("Months",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)
    ax.tick_params(axis="x",rotation=45)

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_weekday_stats(weekday_df):
    fig,ax=plt.subplots(figsize=(10,5))

    sns.barplot(
        data=weekday_df,
        x=weekday_df.index,
        y="total_messages",
        ax=ax,
        palette="crest",
        hue="total_messages",
        legend=False
    )

    ax.set_title("Weekday Activity",fontsize=18,pad=15)
    ax.set_xlabel("Weekdays",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)
    ax.tick_params(axis="x",rotation=45)

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_hourly_activities(hourly_df):
    fig,ax=plt.subplots(figsize=(10,5))

    sns.barplot(
        data=hourly_df,
        x=hourly_df.index,
        y="total_messages",
        ax=ax,
        palette="crest",
        hue="total_messages",
        legend=False
    )

    ax.set_title("Hourly Activity",fontsize=18,pad=15)
    ax.set_xlabel("Hour of the Day",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_activity_heatmap(heatmap_df):
    fig,ax=plt.subplots(figsize=(10,5))

    sns.heatmap(
        heatmap_df,
        ax=ax,
        annot=True,
        fmt="d",
        cmap="mako",
        linewidths=0.5,
        linecolor="#304452",
        annot_kws={"color":"white"}
    )

    ax.set_title("Weekly Activity Heatmap",fontsize=18,pad=15)
    ax.set_xlabel("Hour of the Day",fontsize=12)
    ax.set_ylabel("Weekday",fontsize=12)

    apply_chart_theme(fig,ax,grid=False)
    fig.tight_layout()
    return fig


def plot_sender_activity(activity_df):
    fig,ax=plt.subplots(figsize=(12,5))
    activity_df=activity_df.reset_index()

    activity_df=activity_df.melt(
        id_vars="hour",
        var_name="sender",
        value_name="messages"
    )

    sns.lineplot(
        data=activity_df,
        x="hour",
        y="messages",
        hue="sender",
        ax=ax,
        palette="crest",
        linewidth=2.5
    )

    ax.set_title("Sender Activity by Hour",fontsize=18,pad=15)
    ax.set_xlabel("Hour of the Day",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)

    ax.legend(
        title="Participants",
        facecolor="#1D2A35",
        labelcolor="#E8EEF2",
        title_fontsize=10
    )

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_sender_weekday_activity(activity_df):
    fig,ax=plt.subplots(figsize=(12,5))
    activity_df=activity_df.reset_index()

    activity_df=activity_df.melt(
        id_vars="weekday",
        var_name="sender",
        value_name="messages"
    )

    sns.lineplot(
        data=activity_df,
        x="weekday",
        y="messages",
        hue="sender",
        ax=ax,
        palette="crest",
        linewidth=2.5
    )

    ax.set_title("Sender Activity by Weekday",fontsize=18,pad=15)
    ax.set_xlabel("Weekday",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)

    ax.legend(
        title="Participants",
        facecolor="#1D2A35",
        labelcolor="#E8EEF2"
    )

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_type_stats(type_df):
    fig,ax=plt.subplots(figsize=(10,5))

    type_df=type_df.reset_index()

    type_df=type_df.melt(
        id_vars="sender",
        var_name="type",
        value_name="messages"
    )

    sns.barplot(
        data=type_df,
        x="type",
        y="messages",
        hue="sender",
        palette="crest",
        ax=ax
    )

    ax.set_title("Message Type Distribution",fontsize=18,pad=15)
    ax.set_xlabel("Type of Message",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)
    ax.tick_params(axis="x",rotation=45)

    ax.legend(
        title="Participants",
        facecolor="#1D2A35",
        labelcolor="#E8EEF2"
    )

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_subtypes_stat(subtypes_df):
    fig,ax=plt.subplots(figsize=(15,6))
    subtypes_df=subtypes_df.reset_index()

    subtypes_df=subtypes_df.melt(
        id_vars="sender",
        var_name="subtype",
        value_name="messages"
    )

    sns.barplot(
        data=subtypes_df,
        x="subtype",
        y="messages",
        hue="sender",
        palette="crest",
        ax=ax
    )

    ax.set_title("Message Subtype Distribution",fontsize=18,pad=15)
    ax.set_xlabel("Subtypes",fontsize=12)
    ax.set_ylabel("Number of Messages",fontsize=12)
    ax.tick_params(axis="x",rotation=45)

    ax.legend(
        title="Participants",
        facecolor="#1D2A35",
        labelcolor="#E8EEF2"
    )

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_word_frequency(word_freq):
    fig,ax=plt.subplots(figsize=(12,6))
    top_20=word_freq.most_common(20)
    word_df=pd.DataFrame(top_20,columns=["word","freq"])

    sns.barplot(
        data=word_df,
        x="word",
        y="freq",
        hue="freq",
        palette="crest",
        ax=ax,
        legend=False
    )

    ax.set_title("Most Frequently Used Words",fontsize=18,pad=15)
    ax.set_xlabel("Words",fontsize=12)
    ax.set_ylabel("Frequency",fontsize=12)
    ax.tick_params(axis="x",rotation=45)

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_emoji_stats(emoji_freq):
    fig,ax=plt.subplots(figsize=(10,6))
    top_30=emoji_freq.most_common(30)
    top_30=pd.DataFrame(top_30,columns=["emoji","frequency"])

    sns.barplot(
        data=top_30,
        x="frequency",
        y="emoji",
        hue="frequency",
        palette="crest",
        legend=False,
        ax=ax
    )

    ax.set_title("Most Common Emojis",fontsize=18,pad=15)
    ax.set_xlabel("Frequency",fontsize=12)
    ax.set_ylabel("Emojis",fontsize=12)

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig


def plot_emoji_stats_df(emoji_freq):
    top_30=emoji_freq.most_common(30)
    top_30=pd.DataFrame(top_30,columns=["emoji","frequency"])
    return top_30


def plot_wordcloud(word_freq):
    wc=WordCloud(
        width=1000,
        height=500,
        background_color="#18232D",
        colormap="winter",
        min_font_size=10
    ).generate_from_frequencies(word_freq)

    fig,ax=plt.subplots(figsize=(12,6))
    fig.patch.set_facecolor("#101820")
    ax.set_facecolor("#101820")

    ax.imshow(
        wc,
        interpolation="bilinear"
    )

    ax.axis("off")
    ax.set_title(
        "Most Frequently Used Words",
        fontsize=18,
        color="#E8EEF2",
        pad=15
    )

    fig.tight_layout()
    return fig


def plot_participant_comparision(comparision_stats,column,title,ylabel):
    fig,ax=plt.subplots(figsize=(10,5))

    sns.barplot(
        data=comparision_stats,
        x="sender",
        y=column,
        ax=ax,
        hue="sender",
        palette="crest",
        legend=False
    )

    ax.set_title(title,fontsize=18,pad=15)
    ax.set_xlabel("Participants",fontsize=12)
    ax.set_ylabel(ylabel,fontsize=12)
    ax.tick_params(axis="x",rotation=15)

    apply_chart_theme(fig,ax)
    fig.tight_layout()
    return fig







