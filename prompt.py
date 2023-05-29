# Adapted from https://github.com/hwchase17/langchain/blob/master/langchain/chains/sql_database/prompt.py

from langchain.prompts.prompt import PromptTemplate

PROMPT_SUFFIX = """Only use the following tables:
{table_info}

Question: {input}"""

_postgres_prompt = """You are a PostgreSQL expert. Given an input question, first create a syntactically correct PostgreSQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today".
Pay attention to add table name in front of column name in the SELECT statement with the format "table_name.column_name".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

"""

POSTGRES_PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "top_k"],
    template=_postgres_prompt + PROMPT_SUFFIX,
)