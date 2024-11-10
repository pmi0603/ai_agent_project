
# **README.md for AI Agent Project**

**Project Description**
This project aims to develop an AI agent that can read data from a CSV file or Google Sheets, perform web searches based on user-defined queries, and extract relevant information using a large language model (LLM). The agent will provide a user-friendly dashboard where users can upload their data, define search queries, and view or download the extracted results.

**Features**
File Upload & Google Sheets Integration: Users can upload CSV files or connect to Google Sheets to input data.
Dynamic Query Input: Users can specify custom prompts for information retrieval, utilizing placeholders for dynamic entity replacement.
Automated Web Search: The agent conducts web searches for each entity and gathers relevant results.
LLM Integration: Extracts specific information from web search results using an LLM.
User-Friendly Dashboard: Displays extracted data in a structured format with options to download results as CSV or update Google Sheets.

**Technical Stack**
Dashboard/UI: Streamlit or Flask
Data Handling: Pandas for CSV management; Google Sheets API for integration
Search API: SerpAPI, ScraperAPI, or similar
LLM API: Groq or OpenAI’s GPT API
Backend: Python
Agents: Langchain

**Setup Instructions**

Clone the repository:
```bash
git clone https://github.com/yourusername/ai-agent-project.git
cd ai-agent-project

**Install dependencies:**
```bash
pip install -r requirements.txt

**Set up environment variables:**

Create a .env file in the root directory and add your API keys:
text
GOOGLE_SHEET_API_KEY=your_google_sheet_api_key
SERPAPI_KEY=your_serpapi_key
LLM_API_KEY=your_llm_api_key

**Usage Guide**
Run the application:
```bash
streamlit run app.py  # If using Streamlit
# OR 
python app.py          # If using Flask

Access the dashboard in your web browser at http://localhost:8501 (Streamlit) or http://localhost:5000 (Flask).
Upload your CSV file or connect to a Google Sheet.
Define your search query using placeholders (e.g., "Get me the email address of {company}").
View and download the extracted results.
