# 🎥 YouTube Sentiment Analysis MLOps Pipeline

An end-to-end MLOps project that fetches YouTube comments and analyzes audience sentiment using Natural Language Processing.

The application allows users to enter a YouTube Video URL or Video ID and automatically performs:

- Comment collection using the YouTube Data API
- Data cleaning
- Sentiment analysis
- Data visualization
- Interactive dashboard display

---

## 🚀 Features

- Fetches YouTube comments using the YouTube Data API
- Accepts both YouTube Video URLs and Video IDs
- Cleans duplicate and empty comments
- Performs sentiment analysis using VADER
- Classifies comments as:
  - 😊 Positive
  - 😐 Neutral
  - 😞 Negative
- Displays sentiment metrics and charts
- Interactive Streamlit dashboard
- Error handling for invalid videos and API errors
- Retry mechanism for failed requests
- Unit testing using Pytest
- Continuous Integration using GitHub Actions
- Docker containerization
- Docker Compose support

---

## 🏗️ Project Architecture

```text
User
  ↓
Streamlit Dashboard
  ↓
YouTube Data API
  ↓
Fetch Comments
  ↓
Data Cleaning
  ↓
Sentiment Analysis
  ↓
Visualization
  ↓
Dashboard Results

🛠️ Technologies Used
Python
Pandas
YouTube Data API v3
Google API Python Client
VADER Sentiment Analysis
Streamlit
Matplotlib
Pytest
Docker
Docker Compose
GitHub Actions
📂 Project Structure
youtube-sentiment-mlops/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env
│
├── src/
│   ├── get_comments.py
│   ├── data_cleaning.py
│   ├── sentiment_analysis.py
│   ├── visualization.py
│   └── main.py
│
├── tests/
│   └── test_data_cleaning.py
│
├── data/
│   ├── youtube_comments.csv
│   ├── cleaned_comments.csv
│   ├── cleaned_sentiment_results.csv
│   └── sentiment_chart.png
│
└── .github/
    └── workflows/
        └── ci.yml
⚙️ Installation
1. Clone the repository
git clone <your-repository-url>
2. Navigate to the project folder
cd youtube-sentiment-mlops
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows
venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
🔑 YouTube API Setup

Create a .env file in the project root:

YOUTUBE_API_KEY=your_api_key_here

The YouTube Data API key is required to fetch comments.

▶️ Run the Application
Run the Streamlit Dashboard
streamlit run app.py

Then open:

http://localhost:8501

Enter a YouTube Video URL or Video ID and click Analyze Comments.

🐳 Run with Docker

Build the Docker image:

docker build -t youtube-sentiment-dashboard .

Run the container:

docker run -p 8501:8501 --env-file .env youtube-sentiment-dashboard

Open:

http://localhost:8501
🐳 Run with Docker Compose

Start the application:

docker compose up --build

Open:

http://localhost:8501

Stop the application:

Ctrl + C
🧪 Run Tests

Run all tests:

python -m pytest

The project includes unit tests for the data cleaning module.

🔄 Continuous Integration

GitHub Actions automatically checks the project when code is pushed to the main branch.

The CI workflow:

Sets up Python
Installs dependencies
Checks Python files for syntax errors
📊 Sentiment Categories
Sentiment	Description
😊 Positive	Positive audience reactions
😐 Neutral	Neutral comments
😞 Negative	Negative audience reactions
🔮 Future Improvements
Add sentiment percentages
Add word cloud visualization
Support larger numbers of comments
Deploy the Streamlit application to the cloud
Add advanced machine learning models
Store analysis history in a database
👩‍💻 Author

Dhanyashree C

