import os
import csv
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError, DatabaseError
import warnings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ignore all warnings
warnings.filterwarnings("ignore")

# Neo4j connection setup
try:
    uri = os.getenv("NEO4J_URI")
    username = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")
    driver = GraphDatabase.driver(uri, auth=(username, password))
except (ServiceUnavailable, AuthError) as e:
    print(f"Error connecting to Neo4j: {e}")
    driver = None

def load_data_into_neo4j(csv_file):
    try:
        with driver.session() as session:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    session.write_transaction(create_movie_node, row)
        return "Data loaded successfully"
    except Exception as e:
        return f"Error loading data into Neo4j: {e}"

def create_movie_node(tx, row):
    query = """
    MERGE (m:Movie {title: $title})
    SET m.released_year = $released_year, m.certificate = $certificate, 
        m.runtime = $runtime, m.genre = $genre, m.rating = $rating, 
        m.overview = $overview, m.meta_score = $meta_score, 
        m.no_of_votes = $no_of_votes, m.gross = $gross
    MERGE (d:Director {name: $director})
    MERGE (d)-[:DIRECTED]->(m)
    FOREACH (actor IN $actors |
        MERGE (a:Actor {name: actor})
        MERGE (a)-[:ACTED_IN]->(m)
    )
    """
    tx.run(query, 
           title=row['Series_Title'], 
           released_year=row['Released_Year'],
           certificate=row['Certificate'],
           runtime=row['Runtime'],
           genre=row['Genre'],
           rating=row['IMDB_Rating'],
           overview=row['Overview'],
           meta_score=row['Meta_score'],
           no_of_votes=row['No_of_Votes'],
           gross=row['Gross'],
           director=row['Director'],
           actors=[row['Star1'], row['Star2'], row['Star3'], row['Star4']])

def query_neo4j(query, **kwargs):
    if not driver:
        return ["Error: Unable to connect to the database"]
    try:
        with driver.session() as session:
            result = session.run(query, **kwargs)
            return [record["result"] for record in result]
    except (ServiceUnavailable, DatabaseError) as e:
        return [f"Database query error: {e}"]
