from django.db import models
from role.models import Role
from user.models import User


class UserRoleMapping(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    role_id = models.ForeignKey(Role, on_delete=models.PROTECT)
    # Other fields for the UserEntityMapping model

