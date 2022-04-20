from ariadne.asgi import GraphQL
from jongo.graphql_config import schema

app = GraphQL(schema, debug=True)