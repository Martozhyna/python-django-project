from rest_framework.views import APIView
from rest_framework.response import Response

from .services import UserService


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

# users = [
#     {'name': 'Max', "age": 15},
#     {'name': 'Kira', "age": 20},
#     {'name': 'Karina', "age": 30},
#     {'name': 'Olha', "age": 12},
#     {'name': 'Nataly', "age": 25}
# ]
#
#
# class UserListCreateView(APIView):
#
#     def get(self, *args, **kwargs):
#         return Response(users)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         users.append(data)
#         return Response(data)
#
#
# class UserRetrieveUpdateDestroy(APIView):
#     def get(self,*args,**kwargs):
#         pk = kwargs.get('pk')
#         try:
#             user = users[pk]
#         except IndexError:
#             return Response('Not found')
#         return Response(user)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         pk = kwargs.get('pk')
#         try:
#             user = users[pk]
#         except IndexError:
#             return Response('Not found')
#
#         name = data['name']
#         age = data['age']
#         user['name'] = name
#         user['age'] = age
#         return Response(user)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         try:
#             users[pk]
#         except IndexError:
#             return Response('Not found')
#         del users[pk]
#         return Response('deleted')

class UserApiView(APIView, UserService):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._read()


def smth_went_wrong(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            return Response(str(err))

    return inner


class UserListCreateView(UserApiView):
    def get(self, *args, **kwargs):
        return Response(self.get_all())

    @smth_went_wrong
    def post(self, *args, **kwargs):
        data = self.request.data
        user = self.add(data)
        return Response(user)


class UserRetrieveUpdateDestroyView(UserApiView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = self.get_by_id(pk)
        return Response(user)

    @smth_went_wrong
    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        user = self.update_by_id(pk, data)
        return Response(user)

    @smth_went_wrong
    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        res = self.deleted_by_id(pk)
        return Response(res)
