from django.urls import path
from django.conf.urls import include, url
from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView, RequestLoanView


app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("loan/", RequestLoanView.as_view(), name="request_loan"),
]
