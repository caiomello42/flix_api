import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.prompt import SQL_PREFIX
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

DB_PATH = Path(__file__).resolve().parent / "db.sqlite3"

TABLES = [
    "genres_genre",
    "actors_actor",
    "movies_movie",
    "movies_movie_actors",
    "movies_movielog",
    "reviews_review",
]

# Não usar chaves aqui: o SQL_PREFIX passa por str.format().
PROJECT_CONTEXT = """
Contexto do projeto:
- movies_movielog guarda o histórico dos filmes; action é 'create' (criação), 'update' (edição) ou 'delete' (exclusão).
- Filmes excluídos não existem mais em movies_movie, consulte movies_movielog.
- As datas estão em UTC.
Responda sempre em português.
"""


def build_agent():
    db = SQLDatabase.from_uri(
        f"sqlite:///file:{DB_PATH.as_posix()}?mode=ro&uri=true",
        include_tables=TABLES,
    )
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return create_sql_agent(
        llm=llm,
        db=db,
        agent_type="tool-calling",
        prefix=SQL_PREFIX + PROJECT_CONTEXT,
        verbose=True,
    )


if __name__ == "__main__":
    load_dotenv()
    question = " ".join(sys.argv[1:]) or "Quais foram os filmes excluídos no mês de setembro de 2026?"
    print(build_agent().invoke({"input": question})["output"])
