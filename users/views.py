from rest_framework.views import APIView
from rest_framework.response import Response

# class TestApiView(APIView):
#     def get(self, *args, **kwargs):
#         params_dict = self.request.query_params.dict()
#         print(params_dict)
#         print(self.request.META.get('HTTP_ASD'))
#         return Response('hello from get')
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         print(data)
#         return Response('hello from post')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
#
#
# class Test2View(APIView):
#     def get(self,*args,**kwargs):
#         print(kwargs)
#         return Response('ok')

users = [
    {'name': 'Max', "age": 15},
    {'name': 'Kira', "age": 20},
    {'name': 'Karina', "age": 30},
    {'name': 'Olha', "age": 12},
    {'name': 'Nataly', "age": 25}
]


class UserListCreateView(APIView):

    def get(self, *args, **kwargs):
        return Response(users)

    def post(self, *args, **kwargs):
        data = self.request.data
        users.append(data)
        return Response(data)


class UserRetrieveUpdateDestroy(APIView):
    def get(self,*args,**kwargs):
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('Not found')
        return Response(user)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('Not found')

        name = data['name']
        age = data['age']
        user['name'] = name
        user['age'] = age
        return Response(user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            users[pk]
        except IndexError:
            return Response('Not found')
        del users[pk]
        return Response('deleted')


