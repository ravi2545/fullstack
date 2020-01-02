from django.shortcuts import render
from django import views
from django.http import HttpResponse, JsonResponse
from .models import expenditure, withdraw, loan, chain, income, returns
# Create your views here.


class all(views.View):
    def get(self, request):
        if request.GET['method']=='all':
            k = []
            j = expenditure.objects.all()
            for each in j:
                a = {"loan": each.loan_link_id, "chain":each.chain_link_id, "income":each.income_link_id, "returns":each.returns_link_id, "withdraw":each.withdraw_link_id, "id": each.id, "expensive": each.expense_link, "money_spent": each.money_spent,
                     "money_source": each.money_source, "expense_category": each.expense_category,
                     "description": each.description, "purchase_date": each.purchase_date}
                k.append(a)
            return JsonResponse({"data": k})

    def post(self, request):
        if request.method == "POST":

            return HttpResponse("yes")
