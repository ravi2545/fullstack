from django.shortcuts import render
from django import views
from django.http import HttpResponse, JsonResponse
from .models import expenditure

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

class al(views.View):
    def get(self, request):
        if request.GET['method']=='all':
            k = []
            j=[]
            idd=1
            # j = expenditure.objects.all()
            # q1 = expenditure.objects.all()
            for p in expenditure.objects.raw("SELECT * FROM expenditures_expenditure where id=1"):
                k.append(p)
            for each in k:
                a = {"loan": each.loan_link_id, "chain":each.chain_link_id, "income":each.income_link_id, "returns":each.returns_link_id, "withdraw":each.withdraw_link_id, "id": each.id, "expensive": each.expense_link, "money_spent": each.money_spent,
                     "money_source": each.money_source, "expense_category": each.expense_category,
                     "description": each.description, "purchase_date": each.purchase_date}
                j.append(a)
            return JsonResponse({"data": j})
            # for e in expenditure.objects.all():
            #     k.append(e.id)
            # for e in expenditure.objects.all():
            #     j.append(e.money_spent)
            # for i in k:
            #     if i==10:
            #         return HttpResponse("TRUE")
            #     else:
            #         return HttpResponse("Flase")
            # return JsonResponse({"data":j})

            # for each in j:
            #     a = {"loan": each.loan_link_id, "chain":each.chain_link_id, "income":each.income_link_id, "returns":each.returns_link_id, "withdraw":each.withdraw_link_id, "id": each.id, "expensive": each.expense_link, "money_spent": each.money_spent,
            #          "money_source": each.money_source, "expense_category": each.expense_category,
            #          "description": each.description, "purchase_date": each.purchase_date}
            #     k.append(a)


    def post(self, request):
        if request.method == "POST":

            return HttpResponse("yes")
