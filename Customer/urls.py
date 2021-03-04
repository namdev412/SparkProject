from django.urls import path
from Customer.views import CustomerView

urlpatterns = [
    path('', CustomerView.index),
    path('login', CustomerView.login, name='login'),
    path('register', CustomerView.register, name='register'),
    path('transaction', CustomerView.transaction, name='transaction'),
    path('debit', CustomerView.debit, name='debit'),
    path('credit', CustomerView.credit, name='credit'),
    path('logout', CustomerView.logout, name='logout')
 ]
