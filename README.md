# Text-To-Retrieval-SQL
This project is a Streamlit web application that uses Google Gemini (via the google-generativeai API) to convert natural language questions into SQL queries. Users can type questions about student data. The app demonstrates prompt engineering, safe SQL extraction, and seamless integration of LLMs with database-backed applications.

# Text-to-SQL Streamlit App with Gemini

This project is a Streamlit web application that uses Google Gemini (via the `google-generativeai` API) to convert natural language questions into SQL queries, execute them on a local SQLite database, and display the results. It demonstrates prompt engineering, LLM integration, and safe SQL execution.

---

## Features

- **Natural Language to SQL**: Enter questions in plain English and get the corresponding SQL query.
- **Automatic Query Execution**: The generated SQL is run on a sample `STUDENT` database.
- **Instant Results**: Query results are displayed in the Streamlit interface.
- **Robust SQL Extraction**: The app extracts only the SQL statement from Gemini's response to avoid errors.

---

## Project Structure
text_to_sql/ │ ├── app.py # Main Streamlit app ├── sql.py # Script to create and populate the SQLite database ├── requirements.txt # Python dependencies └── student.db # SQLite database (created by sql.py)


---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/text_to_sql.git
cd text_to_sql

## Install Dependencies
## It's recommended to use a virtual environment:

python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

pip install -r [requirements.txt](http://_vscodecontentref_/4)

Set Up Your Google API Key
Get your Google Gemini API key.
Set it as an environment variable:

Create the Database
Run the following to create and populate student.db:
python [sql.py](http://_vscodecontentref_/5)

Run the Streamlit App
streamlit run [app.py](http://_vscodecontentref_/6)
