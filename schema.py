import graphene
import json
from datetime import datetime
import uuid

class Post(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()

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

class CreateUser(graphene.Mutation):
    user= graphene.Field(User)
    class Arguments:
        username = graphene.String()
        
    def mutate(self, info, username):
        user = User(id=str(uuid.uuid4()), username=username, created_at=datetime.now())
        return CreateUser(user=user)


class CreatePost(graphene.Mutation):
    post = graphene.Field(Post)
    class Arguments:
        title = graphene.String()
        content = graphene.String()
    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        return CreatePost(post=post)



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
result = schema.execute(
    '''
    mutation{
        createPost(title:"hello", content: "world" )
        {
            post{
                title
                content
            }
        }
    }
    ''',
    variable_values={'limit': 3}
)
dictresult =dict(result.data.items())
print(json.dumps(dictresult, indent=2))

