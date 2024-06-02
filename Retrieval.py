import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_astradb import AstraDBVectorStore

# Load environment variables
load_dotenv()

# Set environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize embeddings
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Initialize AstraDB vector store
vstore = AstraDBVectorStore(
    collection_name="test",
    embedding=embedding,
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
)

# Create a retriever
retriever = vstore.as_retriever(search_kwargs={"k": 3})

# Define the prompt template
prompt_template = """
Based on the teachings of the Bhagavad Gita and the specific context provided, answer the following question. If the answer is not directly available from the text, provide an interpretation that aligns with its teachings.
Context: {context}
Question: {question}
Your answer:
"""

# Create the prompt and model
prompt = ChatPromptTemplate.from_template(prompt_template)
model = ChatGoogleGenerativeAI(model="gemini-pro")

# Create the chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

def get_response(question: str) -> str:
    """
    Get a response based on the provided context and question.

    :param context: The context to provide to the model.
    :param question: The question to ask the model.
    :return: The model's response.
    """
    return chain.invoke(question)

# print(get_response("what is Yoga of Knowledge?"))


