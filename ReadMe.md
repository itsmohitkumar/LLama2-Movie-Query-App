# Movie Query App |LLama 2

## Overview

The Movie Query App is a Streamlit application that enables users to query movie data stored in a Neo4j database using natural language processing techniques. The app harnesses the power of a pre-trained LLM (Llama-2) to seamlessly translate natural language queries into Cypher queries, facilitating an intuitive interaction with the movie database.

### Manually Downloading and Cleaning Data

Users can manually download the data from Kaggle and clean it before loading it into the app. The dataset can be found in the `Dataset` folder, and the exploratory data analysis (EDA) and cleaning process are documented in the `Notebook` folder. To clean the data:

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows). 
2. Read the dataset into a Pandas DataFrame.
3. Drop unnecessary columns, such as 'Poster_Link' and 'Series_Title'.
4. Fill null values in columns as necessary.
5. Convert data types, such as converting strings to integers for numerical columns like 'Runtime' and 'Released_Year'.
6. Explore and visualize the data using libraries like Matplotlib and Seaborn to gain insights and ensure data integrity.
7. Once cleaned, the data can be imported into the Neo4j database for use within the app.

   
## Features

- **Load movie data:** Import movie data from a CSV file into the Neo4j database.
- **Query movies:** Utilize natural language to inquire about the genre, actors, director, rating, or overview of a specific movie.
- **Modern UI:** Enjoy a user-friendly interface with a sleek black theme for enhanced aesthetics.

## Installation

### Prerequisites

- Python 3.7 or higher
- Neo4j database instance
- Streamlit
- Required Python packages (listed in requirements.txt)

### Clone the Repository

```bash
git clone https://github.com/itsmohitkumar/movie-query-app.git
cd movie-query-app
```

### Install the Dependencies

```bash
pip install -r requirements.txt
```

## Additional Installation Steps (If Needed)

If you encounter any issues with installing the requirements, try running the following commands:

```bash
%pip install llama-index-llms-huggingface
%pip install llama-index-embeddings-huggingface

%pip install llama-index-embeddings-langchain

!pip install -U langchain-community

!pip install accelerate
!pip install -i https://pypi.org/simple/ bitsandbytes
```

### Setup Neo4j

1. Start your Neo4j instance. you can set up a free instance on the [Neo4j website](https://neo4j.com/).
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

## Note:
If you encounter issues running the app on your local machine because of no GPU, you can try using Google Colab with [this link]([https://colab.research.google.com/drive/1O20KcAx6uCDpw7SGlPj_i16oB4aKaLzx?usp=sharing]).

## File Structure

The repository is divided into three main files for modularity and clarity:

1. `neo4j_setup.py`: Contains functions for setting up the Neo4j connection, loading data into the database, and querying the database.
2. `llm.py`: Contains the setup for the LLM, including loading the tokenizer and model.
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
