from django.contrib import admin
from accounts.models import Account,Transaction
# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)