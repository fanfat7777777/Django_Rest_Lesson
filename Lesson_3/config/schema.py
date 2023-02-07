import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from app_authors.models import AuthorModel, BookModel

#1
#class Query(ObjectType):
#    hello = graphene.String(default_value="Здравствуй!")

#schema = graphene.Schema(query=Query)



#2
#class AuthorType(DjangoObjectType):
#    class Meta:
#        model = AuthorModel
#        fields = '__all__'

#class Query(ObjectType):
#    all_authors = graphene.List(AuthorType)

#    def resolve_all_authors(root, info):
#        return AuthorModel.objects.all()

#schema = graphene.Schema(query=Query)



#3
#class AuthorType(DjangoObjectType):
#    class Meta:
#        model = AuthorModel
#        fields = '__all__'

#class BookType(DjangoObjectType):
#    class Meta:
#        model = BookModel
#        fields = '__all__'

#class Query(ObjectType):
#    all_authors = graphene.List(AuthorType)
#    all_book = graphene.List(BookType)

#    def resolve_all_authors(root, info):
#        return AuthorModel.objects.all()

#    def resolve_all_book(root, info):
#        return BookModel.objects.all()

#schema = graphene.Schema(query=Query)



#4
#class AuthorType(DjangoObjectType):
#    class Meta:
#        model = AuthorModel
#        fields = '__all__'

#class BookType(DjangoObjectType):
#    class Meta:
#        model = BookModel
#        fields = '__all__'

#class Query(ObjectType):
#    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=False))


#    def resolve_author_by_id(root, info, id=None):
#        if id:
#            return AuthorModel.objects.get(id=id)
#        return None

#    book_by_author = graphene.List(BookType, first_name=graphene.String(required=False))


#    def resolve_book_by_author(root, info, first_name=None):
#        books = BookModel.objects.all()
#        if first_name:
#            return books.filter(author__first_name=first_name)
#        return books

   

#schema = graphene.Schema(query=Query)

#5
class AuthorType(DjangoObjectType):
    class Meta:
        model = AuthorModel
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = BookModel
        fields = '__all__'

class Query(ObjectType):
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=False))


    def resolve_author_by_id(root, info, id=None):
        if id:
            return AuthorModel.objects.get(id=id)
        return None

    book_by_author = graphene.List(BookType, first_name=graphene.String(required=False))


    def resolve_book_by_author(root, info, first_name=None):
        books = BookModel.objects.all()
        if first_name:
            return books.filter(author__first_name=first_name)
        return books


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        first_name = graphene.String(required=True)
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(root, info, birthday_year, first_name, id):
        author = AuthorModel.objects.get(id=id)
        author.birthday_year = birthday_year
        author.first_name = first_name
        author.save()
        return AuthorUpdateMutation(author=author)


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(root, info, birthday_year, first_name, last_name):
        author = AuthorModel.objects.create(
            birthday_year=birthday_year, 
            first_name=first_name, 
            last_name=last_name
        )
        return AuthorCreateMutation(author=author)


class AuthorDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    author = graphene.List(AuthorType)

    @classmethod
    def mutate(root, info, id):
        AuthorModel.objects.get(id=id).delete()
        author = AuthorModel.objects.all()
        return AuthorDeleteMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorUpdateMutation.Field()
    create_author = AuthorCreateMutation.Field()
    delete_author = AuthorDeleteMutation.Field()

    

schema = graphene.Schema(query=Query, mutation=Mutation)