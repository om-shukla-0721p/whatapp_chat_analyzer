# WhatsApp Chat Analyzer

A Python-based web application built with Streamlit that analyzes exported WhatsApp conversations and provides insights into messaging patterns, participant activity, frequently used words, emojis, and more.


## Features

- **Overall Analysis:** View total messages, words, participants, and average message length.
- **Activity Timeline:** Analyze daily and monthly messaging trends.
- **Activity Patterns:** Explore messaging activity by weekday, hour, and through an activity heatmap.
- **Participant Activity:** Compare messaging patterns across participants.
- **Message Composition:** Explore message types and media distributions.
- **Word Frequency:** Discover the most frequently used words.
- **Word Cloud:** Visualize commonly used words.
- **Emoji Analysis:** Explore frequently used emojis.
- **Individual Analysis:** Examine the messaging habits and activity of individual participants.
- **Participant Comparison:** Compare message counts, word counts, and average message lengths.
- **Interactive Dashboard:** Navigate between different analysis sections.



## Tech Stack

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **Matplotlib & Seaborn** – Data visualization
- **Streamlit** – Interactive web application
- **WordCloud** – Word cloud generation
- **Emoji** – Emoji extraction and analysis
- **Collections (Counter)** – Word and emoji frequency counting




## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/om-shukla-0721p/whatapp_chat_analyzer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Whatsapp_chat_analyzer
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment (Windows Git Bash):

   ```bash
   source venv/Scripts/activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   python -m streamlit run app.py
   ```



## Usage

1. Run the application using Streamlit.
2. Upload an exported WhatsApp chat (`.txt` file).
3. Wait for the chat to be processed.
4. Use the sidebar navigation to explore:
   - Overall Analysis
   - Individual Analysis
   - Participant Comparison
5. Select participants where required to explore individual statistics and comparisons.
6. Explore the visualizations, activity patterns, word frequencies, and emoji statistics.



## Project Structure

```text
Whatsapp_chat_analyzer/
│
├── app.py                 # Main Streamlit application
├── parser.py              # Parses WhatsApp chat exports
├── preprocessing.py       # Cleans and preprocesses chat data
├── analysis.py            # Performs data analysis
├── visualization.py       # Creates visualizations
├── dashboards.py          # Organizes dashboard layouts
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```


## Development Tools & Resources

- **VS Code** – Code editor and development environment.
- **Git & GitHub** – Version control and project hosting.
- **ChatGPT** – Assistance with CSS styling, UI improvements, debugging, and understanding implementation approaches.



## Limitations

- Supports exported WhatsApp chat files in `.txt` format.
- Currently designed for text-based chat analysis.
- Media files themselves are not analyzed; only their corresponding export placeholders and metadata are categorized.
- Analysis is limited to the information available in the exported chat.


## Future Improvements

- Support for additional WhatsApp export formats.
- Sentiment analysis of chat messages.
- Improved multilingual text processing for Hindi and Hinglish.
- More interactive and customizable visualizations.
- Additional insights into conversation patterns.


## Privacy

- Upload only chat exports that you have permission to analyze.
- Avoid sharing sensitive or private conversations.
- If running locally, chat processing happens on your local machine.
- Be mindful when sharing screenshots or analysis results, as they may reveal personal information.


## Acknowledgements

This project was built as a hands-on learning experience to explore Python, data analysis, data visualization, and Streamlit application development.

Thanks to the open-source Python community and the developers of the libraries used in this project.