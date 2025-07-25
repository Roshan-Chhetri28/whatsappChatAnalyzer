# WhatsApp Chat Analyzer 💬📊

A powerful web application to analyze and visualize your WhatsApp chat data. Get insights about your conversations with interactive charts and statistics.

![WhatsApp Chat Analyzer](https://via.placeholder.com/800x400?text=WhatsApp+Chat+Analyzer)

## ✨ Features

- **User Statistics**: View total messages, words, media messages, and links shared
- **Active User Analysis**: Identify the most active participants in group chats
- **Timeline Visualization**: See message activity over time with monthly and daily charts
- **Activity Patterns**: Discover which days and months have the highest chat activity
- **Weekly Heatmap**: Visualize peak conversation times throughout the week
- **Word Cloud**: Generate word clouds to see the most frequently used terms
- **Emoji Analysis**: Track and analyze emoji usage patterns

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/whatsappChatAnalyzer.git
   cd whatsappChatAnalyzer
   ```

2. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Launch the Streamlit app
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

## 📱 How to Use

1. **Export your WhatsApp chat**:
   - Open WhatsApp
   - Go to the chat you want to analyze
   - Tap ⋮ (three dots) > More > Export chat
   - Choose "Without Media"
   - Save the .txt file

2. **Analyze your chat**:
   - Upload the .txt file in the sidebar
   - Select a user (or "Overall" for group analysis)
   - Click "Show User Stats"
   - Explore the various visualizations and insights

## 📊 Sample Visualizations

- User Statistics Dashboard
- Monthly and Daily Message Timelines
- Weekly and Monthly Activity Patterns
- Word Cloud of Common Terms
- Emoji Usage Analysis

## 🛠️ Technologies Used

- **Streamlit**: For the interactive web interface
- **Pandas**: For data manipulation and analysis
- **Matplotlib & Seaborn**: For data visualization
- **WordCloud**: For generating word clouds
- **Regex**: For pattern matching and extraction

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/whatsappChatAnalyzer/issues).

## 👨‍💻 Author

- Your Name - [@yourusername](https://github.com/yourusername)

---

*Made with ❤️ for WhatsApp chat enthusiasts*
