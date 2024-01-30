from django.shortcuts import render, redirect
from .models import Bank
from .forms import BankForm
import requests
from django.shortcuts import render, get_object_or_404, redirect
def bank_list(request):
    banks = Bank.objects.all()
    return render(request, 'banks/bank_list.html', {'banks': banks})


def add_banks(request):
    if request.method == 'POST':
        num_banks = int(request.POST.get('num_banks', 0))

        api_url = 'https://random-data-api.com/api/v2/banks'
        response = requests.get(api_url, params={'size': num_banks})

        try:
            banks_data_list = response.json()
        except ValueError:
            banks_data_list = []

        for bank_data in banks_data_list:
            bank_form = BankForm(bank_data)
            if bank_form.is_valid():
                bank_form.save()

        return redirect('bank_list')

    return render(request, 'banks/add.html')

def bank_edit(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)

    if request.method == 'POST':
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect('bank_list')
    else:
        form = BankForm(instance=bank)

    return render(request, 'banks/bank_edit.html', {'form': form, 'bank': bank})


def bank_delete(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)

    if request.method == 'POST':
        bank.delete()
        return redirect('bank_list')

    return render(request, 'banks/bank_delete.html', {'bank': bank})


