from django.db import models

# Create your models here.

class User(models.Model):
    emp_no = models.CharField(max_length=20, verbose_name='사원번호')
    username = models.CharField(max_length=20, verbose_name='이름')
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'