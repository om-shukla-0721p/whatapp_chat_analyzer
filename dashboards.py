import streamlit as st
from analysis import *
from visualization import * 
import matplotlib.pyplot as plt


# def overall_analysis(df): self
#     st.header("Overall Analysis")

#     basic_stats=fetch_basic_stats(df)
#     st.subheader("Chat Statistics")
#     col1,col2,col3,col4=st.columns(4)
#     col1.metric("Total Messages",basic_stats["total_messages"])
#     col2.metric("Participants",basic_stats["total_participant"])
#     col3.metric("Total Words",basic_stats["total_words"])
#     col4.metric("Avg Words/message",round(basic_stats["avg_words"],2))

#     st.subheader("Daily Message Timeline")
#     daily_df=fetch_daily_timeline(df)
#     fig=plot_daily_timeline(daily_df)
#     st.pyplot(fig)

#     st.subheader("Monthly Message Timeline")
#     monthly_df=fetch_monthly_timeline(df)
#     fig=plot_monthly_timeline(monthly_df)
#     st.pyplot(fig)

#     st.subheader("Weekday Activity")
#     weekday_df=fetch_weekday_stats(df)
#     fig=plot_weekday_stats(weekday_df)
#     st.pyplot(fig)

#     st.subheader("Hourly Activity")
#     hourly_df=fetch_hourly_timeline(df)
#     fig=plot_hourly_activities(hourly_df)
#     st.pyplot(fig)

#     st.subheader("Activity Heatmap")
#     heatmap_df=fetch_activity_heatmap(df)
#     fig=plot_activity_heatmap(heatmap_df)
#     st.pyplot(fig)


#     # sender wise
#     st.subheader("Sender Activity")
#     sender_activity=fetch_sender_activity(df)
#     fig=plot_sender_activity(sender_activity)
#     st.pyplot(fig)

#     st.subheader("Sender Avtivity by Weekday")
#     weekday_activity=fetch_activity_by_weekday(df)
#     fig=plot_sender_weekday_activity(weekday_activity)
#     st.pyplot(fig)

#     # message types + subtypes
#     st.subheader("Message Type Distribution")
#     type_df=fetch_type_stats(df)
#     fig=plot_type_stats(type_df)
#     st.pyplot(fig)

#     st.subheader("Subtypes Distribution")
#     subtype_df=fetch_subtypes_stats(df)
#     fig=plot_subtypes_stat(subtype_df)
#     st.pyplot(fig)

#     # word frequency + emoji analysis

#     st.subheader("Most Frequenctly Used Words")
#     word_freq=fetch_word_freq(df)
#     fig=plot_word_frequency(word_freq)
#     st.pyplot(fig)

#     st.subheader("Most Frequently Used Emojis")
#     emoji_freq=fetch_emoji_stats(df)

#     col1,col2=st.columns([2,1])
#     with col1:
#         fig=plot_emoji_stats(emoji_freq)
#         st.pyplot(fig)

#     with col2:
#         emoji_df=plot_emoji_stats_df(emoji_freq)
#         st.dataframe(emoji_df,use_container_width=True)

#     st.subheader("Word Cloud")
#     fig=plot_wordcloud(word_freq) # word_freq used from above
#     st.pyplot(fig)

def overall_analysis(df): # used char gpt for btter visuals
    st.header("Overall Analysis")
    st.caption("Explore conversation activity, participant behaviour and message content.")

    # 1. Chat Statistics
    basic_stats = fetch_basic_stats(df)

    st.subheader("Chat Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Messages", basic_stats["total_messages"])
    col2.metric("Participants", basic_stats["total_participant"])
    col3.metric("Total Words", basic_stats["total_words"])
    col4.metric("Avg Words/message", round(basic_stats["avg_words"], 2))

    st.divider()

    # 2. Message Activity
    st.subheader("Message Activity")
    st.caption("Track how conversation activity changes over time.")

    daily_df = fetch_daily_timeline(df)
    fig = plot_daily_timeline(daily_df)
    st.pyplot(fig)
    plt.close(fig)

    monthly_df = fetch_monthly_timeline(df)
    fig = plot_monthly_timeline(monthly_df)
    st.pyplot(fig)
    plt.close(fig)

    st.divider()

    # 3. Activity Patterns
    st.subheader("Activity Patterns")
    st.caption("Discover which days and hours are the busiest.")

    col1, col2 = st.columns(2)

    with col1:
        weekday_df = fetch_weekday_stats(df)
        fig = plot_weekday_stats(weekday_df)
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        hourly_df = fetch_hourly_timeline(df)
        fig = plot_hourly_activities(hourly_df)
        st.pyplot(fig)
        plt.close(fig)

    st.caption("The heatmap combines weekdays and hours to reveal activity patterns.")

    heatmap_df = fetch_activity_heatmap(df)
    fig = plot_activity_heatmap(heatmap_df)
    st.pyplot(fig)
    plt.close(fig)

    st.divider()

    # 4. Participant Activity
    st.subheader("Participant Activity")
    st.caption("Compare when different participants are active.")

    sender_activity = fetch_sender_activity(df)
    fig = plot_sender_activity(sender_activity)
    st.pyplot(fig)
    plt.close(fig)

    weekday_activity = fetch_activity_by_weekday(df)
    fig = plot_sender_weekday_activity(weekday_activity)
    st.pyplot(fig)
    plt.close(fig)

    st.divider()

    # 5. Message Composition
    st.subheader("Message Composition")
    st.caption("Understand the types of messages shared in the conversation.")

    col1, col2 = st.columns(2)

    with col1:
        type_df = fetch_type_stats(df)
        fig = plot_type_stats(type_df)
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        subtype_df = fetch_subtypes_stats(df)
        fig = plot_subtypes_stat(subtype_df)
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    word_freq=fetch_word_freq(df)
    # 6. Language and Expressions
    st.subheader("Language & Expressions")
    st.caption("Explore commonly used words and emojis.")
    if len(word_freq)==0:
        st.info("No text message available for word analysis")
    else:    
        word_freq = fetch_word_freq(df)

        fig = plot_word_frequency(word_freq)
        st.pyplot(fig)
        plt.close(fig)

        fig = plot_wordcloud(word_freq)
        st.pyplot(fig)
        plt.close(fig)

    emoji_freq = fetch_emoji_stats(df)

    if len(emoji_freq)==0:
        st.info("No emojis found in this chat")
    else:
        st.subheader("Emoji Analysis")

        col1, col2 = st.columns([2, 1])

        with col1:
            fig = plot_emoji_stats(emoji_freq)
            st.pyplot(fig)
            plt.close(fig)

        with col2:
            emoji_df = plot_emoji_stats_df(emoji_freq)
            st.dataframe(emoji_df, use_container_width=True)



# def individual_analysis(df):
#     st.header("Individual Participant Analysis")
#     participants=df["sender"].dropna().unique().tolist()
#     selected_user=st.selectbox("Select Participant",participants)

#     user_df=df[df["sender"]==selected_user].copy()

#     user_stats=fetch_basic_stats(user_df)
#     st.subheader(f"Statistics for {selected_user}")

#     col1,col2,col3,col4=st.columns(4)

#     col1.metric(
#         "Message Sent",user_stats["total_messages"]
#     )
#     col2.metric(
#                 "Total words",user_stats["total_words"]
#             )
#     col3.metric(
#                 "Average words/messages",round(user_stats["avg_words"],2)
#             )
#     col4.metric(
#                 "Avg Message length",round(user_stats["avg_message_length"],2)
#             )
    
#     st.divider()
#     st.subheader("Activity Patterns")

#     # daily activity
#     daily_df=fetch_daily_timeline(user_df)
#     fig=plot_daily_timeline(daily_df)
#     st.pyplot(fig)

#     # monthly activty
#     monthly_df=fetch_monthly_timeline(user_df)
#     fig=plot_monthly_timeline(monthly_df)
#     st.pyplot(fig)

#     # weekday activity
#     weekday_df=fetch_weekday_stats(user_df)
#     fig=plot_weekday_stats(weekday_df)
#     st.pyplot(fig)

#     # hourly activity
#     hourly_df=fetch_hourly_timeline(user_df)
#     fig=plot_hourly_activities(hourly_df)
#     st.pyplot(fig)

#     # activity heatmap
#     heatmap_df=fetch_activity_heatmap(user_df)
#     fig=plot_activity_heatmap(heatmap_df)
#     st.pyplot(fig)


#     st.divider()
#     st.subheader("Content Analysis")

#     # word frequency
#     word_freq=fetch_word_freq(user_df)
#     fig=plot_word_frequency(word_freq)
#     st.pyplot(fig)

#     # Word Cloud
#     fig=plot_wordcloud(word_freq)
#     st.pyplot(fig)

#     # emoji analysis
#     emoji_freq=fetch_emoji_stats(user_df)

#     col1,col2=st.columns([2,1])

#     with col1 :
#         fig=plot_emoji_stats(emoji_freq)
#         st.pyplot(fig)
#     with col2:
#         emoji_df=plot_emoji_stats_df(emoji_freq)
#         st.dataframe(emoji_df,use_container_width=True)


def individual_analysis(df):
    st.header("Individual Participant Analysis")
    st.caption("Explore the messaging habits and activity of an individual participant.")

    # 1. Participant Selection
    participants = df["sender"].dropna().unique().tolist()

    selected_user = st.selectbox(
        "Select Participant",
        participants
    )

    user_df = df[df["sender"] == selected_user].copy()

    # 2. Participant Statistics
    user_stats = fetch_basic_stats(user_df)

    st.subheader(f"Statistics for {selected_user}")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Messages Sent", user_stats["total_messages"])
    col2.metric("Total Words", user_stats["total_words"])
    col3.metric("Avg Words/message", round(user_stats["avg_words"], 2))
    col4.metric("Avg Message Length", round(user_stats["avg_message_length"], 2))

    st.divider()

    # 3. Activity Patterns
    st.subheader("Activity Patterns")
    st.caption("Understand when this participant is most active.")

    # Daily Activity
    daily_df = fetch_daily_timeline(user_df)
    fig = plot_daily_timeline(daily_df)
    st.pyplot(fig)
    plt.close(fig)

    # Monthly Activity
    monthly_df = fetch_monthly_timeline(user_df)
    fig = plot_monthly_timeline(monthly_df)
    st.pyplot(fig)
    plt.close(fig)

    # Weekday and Hourly Activity
    col1, col2 = st.columns(2)

    with col1:
        weekday_df = fetch_weekday_stats(user_df)
        fig = plot_weekday_stats(weekday_df)
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        hourly_df = fetch_hourly_timeline(user_df)
        fig = plot_hourly_activities(hourly_df)
        st.pyplot(fig)
        plt.close(fig)

    # Activity Heatmap
    st.caption("Explore the relationship between weekdays and messaging hours.")

    heatmap_df = fetch_activity_heatmap(user_df)
    fig = plot_activity_heatmap(heatmap_df)
    st.pyplot(fig)
    plt.close(fig)

    st.divider()

    # 4. Content Analysis
    st.subheader("Content Analysis")
    st.caption("Discover the words and emojis frequently used by this participant.")

    # Word Frequency
    word_freq = fetch_word_freq(user_df)
    if len(word_freq)==0:
        st.info("No text messages available for word analysis")
    else:
        st.markdown("**Frequently Used Words**")
        fig = plot_word_frequency(word_freq)
        st.pyplot(fig)
        plt.close(fig)

        # Word Cloud
        st.markdown("**Word Cloud**")
        fig = plot_wordcloud(word_freq)
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    # 5. Emoji Analysis
    st.subheader("Emoji Analysis")

    emoji_freq = fetch_emoji_stats(user_df)
    if len(emoji_freq)==0:
        st.info("No emoji found in this chat.")
    else:
        col1, col2 = st.columns([2, 1])

        with col1:
            fig = plot_emoji_stats(emoji_freq)
            st.pyplot(fig)
            plt.close(fig)

        with col2:
            emoji_df = plot_emoji_stats_df(emoji_freq)
            st.dataframe(emoji_df, use_container_width=True)



# def participant_comparison(df):
#     st.header("Participant Comparison")

#     selected_participants=st.multiselect("choose participants to compare",
#                                         df["sender"].dropna().unique().tolist())
#     if len(selected_participants)<2:
#         st.info("Select at least two participants to compare.")
#     else:
#         comparision_df=df[df["sender"].isin(selected_participants)].copy()

#         comparision_stats=comparision_df.groupby("sender").agg(
#             total_messages=("message","count"),
#             total_words=("word_count","sum"),
#             avg_message_length=("message_length","mean")
#         ).reset_index()

#         st.subheader("Message sent by Each Participant")

#         fig=plot_participant_comparision(
#             comparision_stats,
#             "total_messages",
#             "Total Messages Sent",
#             "Messages"
#         )
#         st.pyplot(fig)

#         st.subheader("Total Words by Participant")
#         fig=plot_participant_comparision(
#                     comparision_stats,
#                     "total_words",
#                     "Total Words Sent",
#                     "Words"
#                 )
#         st.pyplot(fig)

#         st.subheader("Average Message Length")
#         fig=plot_participant_comparision(comparision_stats,
#                                         "avg_message_length",
#                                         "Average Message Length by Participant",
#                                         "Characters"
#                                         )

#         st.pyplot(fig)


def participant_comparison(df):
    st.header("Participant Comparison")
    st.caption("Compare messaging habits and communication patterns between participants.")

    # 1. Participant Selection
    participants = df["sender"].dropna().unique().tolist()

    selected_participants = st.multiselect(
        "Choose participants to compare",
        participants,
        placeholder="Select at least two participants..."
    )

    if len(selected_participants) < 2:
        st.info("Select at least two participants to compare.")
        return

    # 2. Calculate Comparison Statistics
    comparison_df = df[df["sender"].isin(selected_participants)].copy()

    comparison_stats = comparison_df.groupby("sender").agg(
        total_messages=("message", "count"),
        total_words=("word_count", "sum"),
        avg_message_length=("message_length", "mean")
    ).reset_index()

    st.divider()

    # 3. Comparison Overview
    st.subheader("Comparison Overview")
    st.caption("A quick look at the selected participants.")

    st.dataframe(
        comparison_stats.rename(columns={
            "sender": "Participant",
            "total_messages": "Messages Sent",
            "total_words": "Total Words",
            "avg_message_length": "Avg Message Length"
        }).round(2),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # 4. Message Comparison
    st.subheader("Message Comparison")
    st.caption("Compare the total number of messages and words sent.")

    col1, col2 = st.columns(2)

    with col1:
        fig = plot_participant_comparision(
            comparison_stats,
            "total_messages",
            "Total Messages Sent",
            "Messages"
        )
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        fig = plot_participant_comparision(
            comparison_stats,
            "total_words",
            "Total Words Sent",
            "Words"
        )
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    # 5. Message Length Comparison
    st.subheader("Average Message Length")
    st.caption("Compare the average number of characters per message.")

    fig = plot_participant_comparision(
        comparison_stats,
        "avg_message_length",
        "Average Message Length by Participant",
        "Characters"
    )

    st.pyplot(fig)
    plt.close(fig)