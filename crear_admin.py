import os
from django.contrib.auth import get_user_model

User = get_user_model()
campo = User.USERNAME_FIELD
valor = os.environ[f"DJANGO_SUPERUSER_{campo.upper()}"]

user = User.objects.filter(**{campo: valor}).first() or User(**{campo: valor})
user.email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
user.set_password(os.environ["DJANGO_SUPERUSER_PASSWORD"])
user.is_staff = True
user.is_superuser = True
user.is_active = True
user.save()
print("Superusuario listo:", valor)