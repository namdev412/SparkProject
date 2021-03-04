from django.shortcuts import render
from Manager.models import *

# Create your views here.

class DashBoard:
    def index(self):
        return render(self,'manager/Login.html')
    def login(self):
        if self.method == 'POST':
            user_email = self.POST.get('email')
            user_password = self.POST.get('password')
            user = Manager.objects.get(email=user_email,password = user_password)
            self.session['user_id'] = user.id
            if user:
                trans = Transactions.object.all()
                return render(self, 'manager/home.html', {'result': trans})
            else:
                message = "Invalid Credentials"
                return render(self, 'manager/login.html', {'message': message})
        else:
            return render(self, 'magaer/Login.html')
    def home(self):
        trans = Transactions.objects.all()
        return render(self, 'manager/home.html',{'result': trans})
    def logout(self):
        del self.session['user_id']
        return render(self, 'manager/Login.html')

    def cust_details(self):
        cust = Customer.objects.all()
        return render(self,'manager/CustomerDetails.html',{'customer':cust})

    def date_range(self):
        if self.method == 'POST':
            start_date = self.POST.get('startdate')
            end_date = self.POST.get('enddate')
            trans = Transactions.objects.filter(Date__range=[start_date, end_date])
            print(trans)
            return render(self, 'manager/DateRangeTrans.html',{'trans':trans})
        else:
           return render(self,'manager/DateRange.html')

    def daterangetrans(self):
        return render(self,'manager/DateRangeTrans.html')

    def cust_trans(self):
        if self.method == 'POST':
            val = list(self.POST.get("total").split(","))
            trans =Transactions.objects.filter(member_id__in= val)
            return render(self,'manager/CustTrans.html',{'trans':trans})

