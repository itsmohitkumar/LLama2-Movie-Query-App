import re
import streamlit as st
from neo4j_setup import load_data_into_neo4j, query_neo4j
from llm import get_tokenizer_model

# Streamlit page configuration
st.set_page_config(page_title="Movie Query App", page_icon="🎬", layout="wide", initial_sidebar_state="expanded")

# Streamlit style configuration for black theme
st.markdown(
    """
    <style>
    .css-18e3th9 {
        background-color: #1e1e1e;
        color: white;
    }
    .css-1d391kg {
        background-color: #1e1e1e;
    }
    .css-qri22k {
        background-color: #333333;
    }
    .css-12ttj6m {
        background-color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def parse_query(natural_language_query):
    patterns = {
        r'genre of (.+)\?': "MATCH (m:Movie {title: $title}) RETURN m.genre AS result",
        r'actors in (.+)\?': "MATCH (m:Movie {title: $title})<-[:ACTED_IN]-(a:Actor) RETURN a.name AS result",
        r'director of (.+)\?': "MATCH (m:Movie {title: $title})<-[:DIRECTED]-(d:Director) RETURN d.name AS result",
        r'rating of (.+)\?': "MATCH (m:Movie {title: $title}) RETURN m.rating AS result",
        r'overview of (.+)\?': "MATCH (m:Movie {title: $title}) RETURN m.overview AS result",
        # Add more patterns as needed
    }

    for pattern, cypher_template in patterns.items():
        match = re.search(pattern, natural_language_query, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            return cypher_template, {'title': title}

    return None, None

def handle_query(natural_language_query):
    cypher_query, params = parse_query(natural_language_query)
    if cypher_query:
        result = query_neo4j(cypher_query, **params)
        if result and isinstance(result, list) and result[0] and not result[0].startswith("Error"):
            if "genre of" in natural_language_query.lower():
                return f"The genre of {params['title']} is {', '.join(result)}."
            elif "actors in" in natural_language_query.lower():
                return f"The actors in {params['title']} are {', '.join(result)}."
            elif "director of" in natural_language_query.lower():
                return f"The director of {params['title']} is {', '.join(result)}."
            elif "rating of" in natural_language_query.lower():
                return f"The rating of {params['title']} is {result[0]}." if result[0] else f"No rating found for {params['title']}."
            elif "overview of" in natural_language_query.lower():
                return f"Overview of {params['title']}: {result[0]}." if result[0] else f"No overview found for {params['title']}."
        else:
            return f"Sorry, I couldn't find any information about {params['title']}. {result[0] if result else ''}"
    else:
        return "I'm not sure how to answer that. Please ask about the genre, actors, director, rating, or overview of a specific movie."

# Load tokenizer and model
tokenizer, model = get_tokenizer_model()
if not tokenizer or not model:
    st.error("Failed to initialize LLM. Check model setup.")
    st.stop()

st.title("Movie Query App")

'''
# Load CSV data
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    load_message = load_data_into_neo4j(uploaded_file)
    st.success(load_message)
'''

# Load CSV data into Neo4j
csv_file = './Dataset/Cleaned/cleaned_imdb_data.csv'
if st.button('Load Data into Neo4j'):
    load_data_into_neo4j(csv_file)


# Example usage with user input
natural_language_query = st.text_input("Ask about a movie", "What is the genre of Titanic?")

if st.button('Submit'):
    db_response = handle_query(natural_language_query)
    if db_response:
        st.write(db_response)
    else:
        st.write("No response from handle_query.")
