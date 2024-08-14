from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the OpenAI API key from environment variables
my_key_openai = os.getenv("openai_apikey")

# Initialize the OpenAI LLM model
llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

# Create a prompt template that instructs the model to list the favorite colors of the people mentioned
prompt = ChatPromptTemplate.from_messages(
    [("system", "Write the favorite color of each person mentioned here:\n\n{context}")]
)

# Create example documents where each document mentions a person's favorite color
docs = [
    Document(page_content="Gamze likes red but doesn't like yellow"),
    Document(page_content="Murat likes green but not as much as he likes blue"),
    Document(page_content="If you ask Burak, he will say he doesn't have a favorite color, but it's clear he likes orange")
]

# Create a chain that processes and combines the documents using the prompt and LLM
chain_1 = create_stuff_documents_chain(llm, prompt)

# Invoke the chain with the documents and print the results
print(chain_1.invoke({"context": docs}))


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional
from langchain.chains.openai_functions import create_openai_fn_runnable

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the OpenAI API key from environment variables
my_key_openai = os.getenv("openai_apikey")

# Define a Pydantic model to describe a person
class Person(BaseModel):
    """A class to define information about a person"""

    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person")
    occupation: Optional[str] = Field(None, description="The occupation of the person")

# Define a Pydantic model to describe a city
class City(BaseModel):
    """A class to define information about a city"""

    name: str = Field(..., description="The name of the city")
    license_plate_code: str = Field(..., description="The license plate code of the city")
    climate: Optional[str] = Field(None, description="The climate of the city")

# Initialize the OpenAI LLM model
llm = ChatOpenAI(model="gpt-4-0125-preview", api_key=my_key_openai)

# Create a prompt template that instructs the model to save entities correctly
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are the world's most successful algorithm at saving entities"),
        ("human", "Call the necessary functions to save the entities mentioned in this input: {input}"),
        ("human", "Hint: Make sure you respond in the correct format")
    ]
)

# Create a chain that processes inputs and extracts entity information based on the defined models
chain_2 = create_openai_fn_runnable([Person, City], llm, prompt)

# Invoke the chain with different inputs and print the results
print(chain_2.invoke({"input": "Aydın is 34 years old, a successful computer engineer"}))
print(chain_2.invoke({"input": "The weather is always hot in Aydın, so air conditioning is always on in cars with license plate code 09"}))
