from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType,snake_case_fallback_resolvers, SubscriptionType
import books.resolvers
from ariadne.asgi import GraphQL


type_defs = [
    load_schema_from_path("jongo/schema.graphql"),
]

query = QueryType()
query.set_field("books", books.resolvers.list_books)

mutation = MutationType()
mutation.set_field("createBook", books.resolvers.create_book)
mutation.set_field("updateBook", books.resolvers.update_book)
mutation.set_field("deleteBook", books.resolvers.delete_book)

subscription = SubscriptionType()
subscription.set_source("books", books.resolvers.subscribe_to_books)

schema = make_executable_schema(type_defs, query, mutation,snake_case_fallback_resolvers)
app = GraphQL(schema, debug=True)