import chainlit as cl
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from prompt import POSTGRES_PROMPT
import os

llm = OpenAI(temperature=0.5)
db = SQLDatabase.from_uri(os.getenv("POSTGRES_URI"))
db_chain = SQLDatabaseChain.from_llm(
    llm=llm, 
    db=db, 
    prompt=POSTGRES_PROMPT, 
    use_query_checker=True, 
    return_intermediate_steps=True
    )

@cl.on_message  # this function will be called every time a user inputs a message in the UI
def main(message: str):
    result = db_chain(message)
    # send back the final answer
    cl.Message(content=result['result']).send()
