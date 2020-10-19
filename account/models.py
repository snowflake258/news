from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password):
        user = self.__init_new_user(email, date_of_birth, password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.__init_new_user(email, date_of_birth, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def __init_new_user(self, email, date_of_birth, password):
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    is_active = models.BooleanField(
        verbose_name='Активный?',
        default=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('date_of_birth',)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
