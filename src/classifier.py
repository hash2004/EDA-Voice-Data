from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict
from pydantic import BaseModel, Field
from langchain.output_parsers.json import SimpleJsonOutputParser
from constants import fluency_classifier_context
from src.config import GROQ_API_KEY
import os

os.environ['GROQ_API_KEY'] = GROQ_API_KEY   


# Load environment variables from a .env file
class Fluency(BaseModel):
    """
    Parameters:
        -BaseModel
    
    Class Description:
        -This class defines the structure of the output object for the fluency object. 
        -Using Pydantic, the class defines the fields of the output object.
    """
    fluent: str = Field(description="Whether or not the candidate is fluent in the language. 1 for yes, 0 for no.")

"""
-The SimpleJsonOutputParser class is used to parse the JSON output from the xAI model.
"""
parser = SimpleJsonOutputParser(pydantic_object=Fluency)


def initialize_api_connections_context_fluency()->ChatGroq:
    """
    Parameters:
        -None
    
    Returns:
        -llm: ChatGroq
        
    Function Description:
        -This function initializes the API connections for the xAI model.
    """
    try:
        llm = ChatGroq(model_name="llama3-70b-8192")
        print("API connections initialized.")
        return llm
    except Exception as e:
        print(f"Error initializing API connections: {str(e)}")
        return None
    
    
def fleuncy_classifier(llm,query_text):
    """
    Parameters:
        -llm: ChatGroq
        -query_text: str
        
    Returns:
        -answer: str
        
    Function Description:
        -This function summarizes the resume of a candidate.
        - Finds the pros of the candidate in relation to the job description.
    """
    
    # Creating a prompt template
    prompt_template = ChatPromptTemplate.from_template(
        """
        <context>
        {context}
        Candidate's Resume and Job Description:
        {input}

        """
    )

    try:
        # Forming the prompt and invoking the model
        prompt = prompt_template.format(context=fluency_classifier_context, input=query_text)
        response = llm.invoke(prompt)
        
        # Parsing the JSON response
        answer = parser.parse(response.content)
        return answer
    except Exception as e:
        return f"Failed to process your input due to an error: {str(e)}"