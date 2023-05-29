# Example Text-to-SQL Chatbot 🚀🤖

The is an example chatbot built with Chainlit and LangChain to demostrate the capability of Text-to-SQL using OpenAI's LLM. The chatbot is connected to a postgres database with the Brazilian E-Commerce Public Dataset. You can try it here:
[sql-chatbot.fly.dev](https://sql-chatbot.fly.dev/)

- **Chainlit:** [Chainlit Documentation](https://docs.chainlit.io) 📚
- **LangChain:** [LangChain Documentation](https://python.langchain.com/en/latest/index.html) 📚
- **Data Source:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Development
To run the application locally, make sure you have set the environment variable `OPENAI_API_KEY` or set it in the `docker-compose` file, then simply run:
```
docker compose up --build
```
This starts the `postgres` container, loads the `Brazilian E-Commerce Public Dataset` into the database, and starts the Chatbot application container. You could visit the chatbot at 
```
http://localhost:8000
```