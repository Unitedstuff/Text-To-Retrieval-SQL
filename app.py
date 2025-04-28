import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    # model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_conent(prompt[0], question)
    # return response.text
    # Combine prompt and question into a single string
    full_prompt = prompt[0] + "\n" + question
    # Use the correct method to generate content
    model = genai.GenerativeModel('gemini-2.0-flash-001')
    response = model.generate_content(full_prompt)
    return response.text


def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        # Execute the SQL query
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        rows = []
    finally:
        conn.close()
    return rows

prompt = [

    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]


st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)
#     # response_sql = response.strip().split('\n')[0]
#     response=read_sql_query(response,"student.db")
#     st.subheader("The Response is")
#     for row in response:
#         print(row)
#         st.header(row)
# ...existing code...

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    # Try to extract the first line that looks like a SQL statement
    for line in response.split('\n'):
        line = line.strip()
        if line.lower().startswith("select") or line.lower().startswith("insert") or line.lower().startswith("update") or line.lower().startswith("delete"):
            response_sql = line
            break
    else:
        response_sql = response.strip()  # fallback if nothing found

    response = read_sql_query(response_sql, "student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
        