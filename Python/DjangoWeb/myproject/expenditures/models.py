from django.db import models
from django.conf import settings
# Create your models here.

class loan(models.Model):
    loan_amount = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"Loan amount is {self.loan_amount}"



class chain(models.Model):
    chainview = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"chain is {self.chainview}"



class income(models.Model):
    incomes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"Income is {self.incomes}"



class returns(models.Model):
    returnslist = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"returns is {self.returnslist}"


class withdraw(models.Model):
    withdraws = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"withdraw amount is {self.withdraws}"


class expenditure(models.Model):
    loan_link = models.ForeignKey('loan', default=0, on_delete=models.CASCADE, blank=True)
    chain_link = models.ForeignKey('chain', default=0, on_delete=models.CASCADE, blank=True)
    income_link = models.ForeignKey('income', default=0, on_delete=models.CASCADE, blank=True)
    returns_link = models.ForeignKey('returns', default=0, on_delete=models.CASCADE, blank=True)
    withdraw_link = models.ForeignKey('withdraw', default=0, on_delete=models.CASCADE, blank=True)
    expense_link = models.CharField(max_length=10, choices=settings.SOURCE, default=settings.SOURCE[0][0], null=True,
                                    blank=True)
    money_spent = models.PositiveIntegerField()
    money_source = models.CharField(max_length=10, choices=settings.BANKS, default=settings.BANKS[1][0], null=True,
                                    blank=True)
    expense_category = models.CharField(max_length=20, choices=settings.CATEGORY, default=settings.CATEGORY[3][0])
    description = models.CharField(max_length=200, default=None, null=True)
    purchase_date = models.DateField()

