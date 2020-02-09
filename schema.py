import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

class Query(graphene.ObjectType):
    user = graphene.List(User, limit= graphene.Int())

    def resolve_user(self, info, limit=None):
        return [
            User(id="1", username="piash", created_at= datetime.now()),
            User(id="2", username="Tareque", created_at= datetime.now()),
            User(id="3", username="Masum", created_at= datetime.now()),
        ][:limit]

schema = graphene.Schema(query=Query)
result = schema.execute(
    '''
    {
        user(limit:2){
            id
            username
            createdAt
        }
    }
    '''
)
dictresult =dict(result.data.items())
print(json.dumps(dictresult, indent=2))

