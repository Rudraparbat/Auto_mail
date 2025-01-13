import streamlit as st
from langchain_core.prompts import PromptTemplate
from scrap import *
from model import *
import re

class Chain :
    def __init__(self):
        self.llm = model()
        
    def is_valid_url(self, url):
        url_pattern = re.compile(
        r'^(https?://)?'  
        r'(\w+(:\w+)?@)?'  
        r'([A-Za-z0-9.-]+)'  
        r'(\.[A-Za-z]{2,})'  
        r'(:\d+)?'  
        r'(/[\w%.-]*)*'  
        r'(\?\S*)?'  
        r'(#\S*)?$'
        )
        return bool(url_pattern.match(url))

    def get_job_profile_data(self , scrap_data) :
        try :
            prompt_template = PromptTemplate.from_template(
            """
            You are a professional job data parser. Analyze the provided text and extract key details in JSON format:

                Text: {raw_text}

                Expected JSON structure:
                {{
                    "skills": ["skill1", "skill2", "skill3", ...],
                    "description": "Job description here.",
                    "experience_needed": "Details about experience needed here.",
                    "about_the_job" : "Details about the job in 3 key points" ,
                    "Responsibility" : "Details about the job respponsibility in 3 points "
                }}

                If any detail is missing in the text, use "N\A".
                ###  VALID JSON (NO PREAMBLE)

            
            """
            )
            res = prompt_template | self.llm
            data = res.invoke({
                "raw_text": str(scrap_data)
            })
            return data.content
        except :
            return False
    def get_mail(self,job_details) :
        try :
            prompt_template = PromptTemplate.from_template(
            """
            I have a JSON object containing details of a job post. The JSON includes fields like skills, 
            company_name, description, experience_needed, about_the_job, location 
            Use this data to craft a professional cold email, highlighting how
            my skills and experience align with the job requirements.

                Here is the JSON structure with the job details:

                {json_data}

            Ensure the email is written in professional and engaging language and in a structured way and not too long.
            ### (NO PREAMBLE)
            
            """
            )
            result = prompt_template | self.llm
            email = result.invoke({'json_data' : job_details })
            return email.content
        except :
            return False

def main():
    chain = Chain()
    st.title("Welcome to the Cold Email Generator App")
    job_url = st.text_input("Enter the job posting URL:")
    is_clicked = st.button("submit")
    if is_clicked :
        if chain.is_valid_url(job_url) :
            scrapped_data = scrape_page_text(job_url)
            job_details = chain.get_job_profile_data(scrapped_data)
            if job_details == False :
                st.write("## lama is sleeping too much request")
                return
            mail_data = chain.get_mail(job_details)
            st.code(mail_data , language="markdown")
        else :
            st.write("Sorry this is not a url")

if __name__ == "__main__":
    main()
