
```markdown
Movie Query App

Overview

The Movie Query App is a Streamlit application that allows users to query movie data stored in a Neo4j database using natural language processing techniques. The app is powered by a pre-trained LLM (Llama-2) to convert natural language queries into Cypher queries, providing a seamless and intuitive way to interact with the movie database.

## Features

- Load movie data: Load movie data from a CSV file into the Neo4j database.
- Query movies: Use natural language to query the genre, actors, director, rating, or overview of a specific movie.
- Modern UI: User-friendly interface with a black theme for better aesthetics.

## Installation

### Prerequisites

- Python 3.7 or higher
- Neo4j database instance
- Streamlit
- Required Python packages (listed in requirements.txt)

### Clone the Repository

```bash
git clone https://github.com/yourusername/movie-query-app.git
cd movie-query-app
```

### Install the Dependencies

```bash
pip install -r requirements.txt
```

### Setup Neo4j

1. Start your Neo4j instance.
2. Update the Neo4j connection details in `neo4j_setup.py`:

```python
uri = "your_neo4j_uri"
username = "your_username"
password = "your_password"
```

### Download the Model

Ensure you have access to the pre-trained Llama-2 model and update the authentication token in `llm_setup.py`:

```python
auth_token = "your_huggingface_auth_token"
```

## Running the App

To run the Streamlit app, execute the following command in your terminal:

```bash
streamlit run app.py
```

## File Structure

The repository is divided into three main files for modularity and clarity:

1. `neo4j_setup.py`: Contains functions for setting up the Neo4j connection, loading data into the database, and querying the database.
2. `llm_setup.py`: Contains the setup for the LLM, including loading the tokenizer and model.
3. `app.py`: The main file that runs the Streamlit app, allowing users to load data and query the movie database.

## Example Usage

### User Query

```csharp
User query: What is the genre of Titanic?
```

Output: The genre of Titanic is Drama, Romance.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

This revised version organizes the content into clear sections, provides proper code formatting, and improves readability. Let me know if you need further adjustments!
