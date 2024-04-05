from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from app1.forms import InputForm
from datetime import datetime


# Create your views here.
def view1(request):
    return HttpResponse("hello world")
    
def transactions(request):
    
    if request.method=="POST":
        form = InputForm(request.POST)
        if form.is_valid():
            transactionType = form.cleaned_data['transaction_type']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description']
            t = Transactions(date=datetime.now(), transaction_type=transactionType, amount=amount, description=description)
            t.save()
    
    allTransactions = Transactions.objects.order_by("date")
    allTransactions = list(allTransactions)
    
    total = 0
    
    result = []
    for transaction in allTransactions:
        t1 = {}
        t1['date'] = transaction.date
        t1['transaction_type'] = transaction.transaction_type
        t1['amount'] = transaction.amount
        t1['description'] = transaction.description
        if transaction.transaction_type=="credit":
            total +=  transaction.amount
        else:
            total -= transaction.amount
        t1['running_balance'] = total            
            
        result.append(t1)
        
    result = sorted(result, key=lambda x: x['date'], reverse=True)
    form = InputForm()
    dict1 = {"transactions": result, "form": form}
    return render(request, "transactions.html", dict1)

