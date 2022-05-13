from django.contrib import admin
from .models import Todo
#adminにTodoを登録
admin.site.register(Todo)