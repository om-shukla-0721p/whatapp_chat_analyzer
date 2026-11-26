import streamlit as st
from parser import parse_chat,create_df # read_chat
from preprocessing import preprocess_messages
from analysis import create_useful_columns
from dashboards import (overall_analysis,
                        individual_analysis,
                        participant_comparison)


@st.cache_data(show_spinner="Processing chat...")
def load_chat_data(raw_data):
    parsed_chat, unparsed_chat = parse_chat(raw_data)
    # print(">>> CHAT PROCESSING EXECUTED<<<")

    if len(parsed_chat) == 0:
        return None, len(unparsed_chat)

    processed_chat = preprocess_messages(parsed_chat)

    df = create_df(processed_chat)
    df = create_useful_columns(df)

    return df, len(unparsed_chat)


def main():
    st.set_page_config(
        page_title="Whatsapp Chat Analyzer",
        page_icon="💬",
        layout="wide"
    )

    st.markdown("""
            <style>
            /* Main background */
            .stApp {
                background-color: #101820;
                color: #E8EEF2;
            }

            /* Sidebar */
            [data-testid="stSidebar"] {
                background-color: #182631;
            }

            /* Main headings */
            h1, h2, h3 {
                color: #E8EEF2 !important;
            }

            /* Metric cards */
            [data-testid="stMetric"] {
                background-color: #1D2A35;
                border: 1px solid #304452;
                padding: 18px;
                border-radius: 12px;
            }

            /* Metric labels */
            [data-testid="stMetricLabel"] {
                color: #AAB8C5;
            }

            /* Metric values */
            [data-testid="stMetricValue"] {
                color: #45C4B0;
            }

            /* Navigation buttons */
            .stButton > button[kind="primary"] {
                background-color: #45C4B0;
                color: #101820;
                border: 1px solid #45C4B0;
                border-radius: 8px;
                font-weight: 600;
            }

            .stButton > button[kind="secondary"] {
                background-color: transparent;
                color: #AAB8C5;
                border: 1px solid #304452;
                border-radius: 8px;
            }

            /* Hover effect */
            .stButton > button:hover {
                border-color: #45C4B0;
                color: #45C4B0;
            }

            /* Dividers */
            hr {
                border-color: #304452;
            }

            /* Dataframes */
            [data-testid="stDataFrame"] {
                border: 1px solid #304452;
                border-radius: 10px;
            }
            </style>
            """, unsafe_allow_html=True)

    st.title("Whatsapp Chat Analyzer")
    st.write("Analyze your Whatsapp conversation and discover interesting patterns")

    uploaded_file=st.file_uploader(
        "upload your whatsapp chat",
        type=["txt"]
    )

    if uploaded_file is not None:
        try:
            raw_data = uploaded_file.getvalue().decode("utf-8-sig")
        except UnicodeDecodeError:
            st.error("Unable to read this file ." \
            "Please upload a valid UTF-8 Whatsapp export ")
            return 
        
        st.success("Chat uploaded successfully!")
        df, unparsed_count = load_chat_data(raw_data)

        if df is None or df.empty:
            st.error("Could not parse this chat. Please upload a valid Whatsapp export")
            return
        else:
            if unparsed_count > 0:
                st.warning(f"{unparsed_count} messages could not be parsed.")

            with st.sidebar:
                st.title("💬 Chat Analyzer")
                st.caption("Explore your conversations")

                st.divider()
                st.subheader("Navigation")

                if "section" not in st.session_state:
                    st.session_state.section = "Overall Analysis"

                if st.button("📊 Overall Analysis", use_container_width=True,
                             type="primary" if st.session_state.section=="Overall Analysis" else "secondary"):
                    st.session_state.section = "Overall Analysis"

                if st.button("👤 Individual Analysis", use_container_width=True,
                             type="primary" if st.session_state.section=="Individual Analysis" else "secondary"):
                    st.session_state.section = "Individual Analysis"

                if st.button("⚖️ Participant Comparison", use_container_width=True,
                             type="primary" if st.session_state.section=="Participant Comparison" else "secondary"):
                    st.session_state.section = "Participant Comparison"

                section = st.session_state.section

                st.divider()
                st.caption("CHAT INFORMATION")
                st.metric("Participants", df["sender"].nunique())
                st.metric("Total Messages", len(df))

            if section == "Overall Analysis":
                overall_analysis(df)

            elif section == "Individual Analysis":
                individual_analysis(df)

            elif section == "Participant Comparison":
                participant_comparison(df)


if __name__=="__main__":
    main()

