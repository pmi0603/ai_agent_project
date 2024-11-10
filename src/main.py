import streamlit as st
import pandas as pd
import openai
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Set up API keys
SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Streamlit app title
st.title("AI Agent Project Dashboard")

# Step 1: Upload File
st.header("1. Upload a CSV File")
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

data = None
if uploaded_file:
    data = pd.read_csv(uploaded_file)

# Step 2: Show Data Preview
if data is not None:
    st.write("### Data Preview")
    st.write(data)
    column_name = st.selectbox("Select the main column for entities", data.columns)

# Step 3: Enter Query Prompt
st.header("2. Define Your Query")
query_template = st.text_input("Enter your query with placeholders (e.g., 'Find the email of {company}')")

# Step 4: Search and Extract Information
st.header("3. Run Web Search and Extract Information")
if st.button("Run Extraction") and data is not None and query_template:
    extracted_data = []

    for entity in data[column_name]:
        query = query_template.replace("{company}", entity)
        target_url = f"https://www.google.com/search?q={query}"
        api_url = f"http://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url={target_url}"
        
        # Scrape the search results
        response = requests.get(api_url)
        if response.status_code == 200:
            page_content = response.text
            
            # LLM Processing
            prompt = f"Extract the email address of {entity} from the following text: {page_content}"
            llm_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an assistant that extracts specific information."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            extracted_info = llm_response.choices[0].message['content'].strip()
            extracted_data.append({"Entity": entity, "Extracted Info": extracted_info})
        else:
            st.warning(f"Failed to retrieve data for {entity}. Status code: {response.status_code}")

    # Convert results to DataFrame and display
    extracted_df = pd.DataFrame(extracted_data)
    st.write("### Extracted Data")
    st.write(extracted_df)

    # Step 5: Download Option
    st.header("4. Download Extracted Data")
    csv = extracted_df.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name="extracted_data.csv", mime="text/csv")
