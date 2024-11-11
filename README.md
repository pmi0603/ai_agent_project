# AI Agent Project
This project is an AI-powered agent that performs web searches, extracts specific information based on user-defined prompts, and displays or downloads the results in a user-friendly interface.

###  Features
File Upload: Upload a CSV file to analyze data for multiple entities.
Custom Query Input: Enter custom queries with placeholders for dynamic information extraction.
Automated Web Search: Uses ScraperAPI to gather relevant data from the web.
Data Extraction with OpenAI: Extracts specific information from search results using OpenAI's LLM.
Data Display and Export: View extracted data in a table with an option to download it as a CSV.
Prerequisites
Python 3.x: Make sure Python is installed on your system.
OpenAI API Key: **You need an OpenAI API key to use the language model for data extraction.**
ScraperAPI Key: **You need a ScraperAPI key for automated web search functionality.**

PS:**You need to add API's in .env file in root folder, other wise will encounter error401.** 

**Setup and Installation**


## Step 1: Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/yourusername/ai_agent_project.git
cd ai_agent_project
## Step 2: Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
## Step 3: Install Dependencies
Use requirements.txt to install the necessary libraries:

pip install -r src/requirements.txt
## Step 4: Set Up Environment Variables
Create a .env File: In the root directory of the project, create a file named .env.

Add Your API Keys: Open .env and add your ScraperAPI and OpenAI API keys as follows:

SCRAPER_API_KEY=your_scraperapi_key_here
OPENAI_API_KEY=your_openai_api_key_here
Add .env to .gitignore: Make sure .env is listed in .gitignore to prevent accidental sharing of API keys.

## Step 5: Running the Application
To start the application, use Streamlit:

streamlit run src/main.py
This command will open the application in your web browser.

**Usage**
Upload CSV File: Upload a CSV file containing a list of entities (e.g., company names) in one column.
Define a Query: Enter a query prompt with placeholders, e.g., Find the email of {company}.
Run Extraction: Click "Run Extraction" to perform searches and extract information for each entity.
View and Download Results: The extracted data will appear in a table format. Click "Download CSV" to save the results.

## Project Demonstration

Watch a walkthrough of the project on Loom: [Project Demo](https://drive.google.com/file/d/1r-ClkT4OMgpntpFjAsLo2uDGZm7Xl4_1/view?usp=sharing)

