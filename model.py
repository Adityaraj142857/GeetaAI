import os
from getpass import getpass
from langchain_astradb import AstraDBVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables from .env file
load_dotenv()

# Configure your embedding model and vector store
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vstore = AstraDBVectorStore(
    collection_name="test",
    embedding=embedding,
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
)
# print("Astra vector store configured")
pdfreader = PdfReader('data/Gitapress_Gita_Roman.pdf')
from typing_extensions import Concatenate
# read text from pdf
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# We need to split the text using Character Text Split such that it sshould not increse token size
seperator =[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        ""
    ]
text_splitter = RecursiveCharacterTextSplitter(
    separators = seperator,
    chunk_size = 600,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

# Create embeddings by inserting your documents into the vector store.
inserted_ids = vstore.add_texts(texts)
print(f"\nInserted {len(inserted_ids)} documents.")