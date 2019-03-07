from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from assets.utils import create_hash
from users.models import UserProfile
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSetRegister(viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def sign_up(self, request):
        data = request.data

        seller = data['seller']
        usercpf = data['cpf']
        username = data['name']
        useremail = data['email']
        userpass = data['password']

        if not UserProfile.objects.filter(email=useremail).exists():
            if not UserProfile.objects.filter(name=username).exists():
                user = UserProfile.objects.create_user(
                    username=create_hash(),
                    is_seller=seller,
                    name=username,
                    email=useremail,
                    cpf=usercpf,
                    password=userpass,
                )
                return JsonResponse({
                    'success': True,
                    'message': 'Cadastro Efetuado Com Sucesso',
                    'status': 200,
                })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Usuário Já Cadastrado',
                'status': 200,
            })

    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def sign_in(self, request):
        data = request.data

        useremail = data['email']
        userpass = data['password']

        exists_user = UserProfile.objects.prefetch_related().filter(email=useremail).count()

        if exists_user != 0:

            related_user = UserProfile.objects.prefetch_related().get(email=useremail)

            user = authenticate(
                password=userpass,
                username=related_user.username
            )

            if user:
                return JsonResponse({
                    'success': True,
                    'message': 'login efetuado com sucesso',
                    'status': 200,
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Senha Incorreta',
                })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Usuário não encontrado',
            })





