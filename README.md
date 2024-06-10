# 🌟 Geeta AI 🌟

Geeta AI is an AI-powered question-answering system that leverages the teachings of the Bhagavad Gita to provide insights and solutions to your queries. The application utilizes Google's Generative AI for embeddings and AstraDB for vector storage to retrieve relevant information and generate responses. 🙏🧘‍♂️

## Project Structure 📂

- **retrival.py**: This script initializes the embeddings, vector store, retriever, and creates the chain for generating responses.
- **streamlit.py**: This script sets up a Streamlit application to interact with the user, handle queries, and display conversation history.
- **model.py**: This script handles the PDF processing, text splitting, and inserting the processed texts into the AstraDB vector store.

## Setup Instructions ⚙️

### Prerequisites 📝

- Python 3.8 or later 🐍
- An AstraDB account with a created collection 🌐
- Google API Key for accessing Google's Generative AI 🔑

### Installation 🚀

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Adityaraj142857/GeetaAI.git
    cd GeetaAI
    ```

2. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    Create a `.env` file in the project root directory and add the following:
    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ASTRA_DB_APPLICATION_TOKEN=your_astra_db_application_token
    ASTRA_DB_API_ENDPOINT=your_astra_db_api_endpoint
    ```

4. **Add your PDF file:**
    Place your Bhagavad Gita PDF file in the `data` directory and ensure it is named `Gitapress_Gita_Roman.pdf`.

### Running the Application 🏃‍♂️

1. **Prepare the vector store:**
    Run the `model.py` script to process the PDF and insert texts into the AstraDB vector store.
    ```bash
    python model.py
    ```

2. **Start the Streamlit application:**
    Run the `streamlit.py` script to start the web interface.
    ```bash
    streamlit run streamlit.py
    ```

### Usage 💡

1. Open the Streamlit app in your web browser. 🌐
2. Enter your query related to the teachings of the Bhagavad Gita in the text input field. 📝
3. Click the "Ask Radhey" button to get a response. 🔍
4. The conversation history will be displayed below the input field, showing the problems and solutions provided. 💬

## Hosting 🌐
This app is currently hosted using Streamlit Community Cloud. Please pay a visit: [Geeta AI on Streamlit](https://geetaai.streamlit.app/) 🚀

## Customization 🎨

- **Background Image and Styling:** Customize the background image and styles by modifying the `add_bg_from_url` function in `streamlit.py`.
- **Prompt Template:** Adjust the prompt template in `retrival.py` to change how the AI formulates responses based on the context and question.

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request with your changes. 🌟

## License 📜

This project is licensed under the MIT License. See the LICENSE file for more details. 📄

---

Feel free to get in touch if you have any questions or suggestions! 🙌

