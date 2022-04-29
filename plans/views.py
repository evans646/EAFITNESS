from django.shortcuts import render, get_object_or_404, redirect
from stripe.api_resources import customer, subscription
from .forms import CustomSignupForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Beauty, FitnessPlan,Customer,Food,Health,Culture,Love,FitnessBlog
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

import stripe
stripe.api_key= 'sk_test_51Ju6PeE9EMUzkjDtSScXBBRUBSOGkY7CobWtxDxUapVGMCWibuH53rjWyuIV9maaKp4Qn9VpO7RE5A8wX2QCcEJo006qsqVE3X'


#only super users can access this account
@user_passes_test(lambda u: u.is_superuser)
def updateaccounts(request):
    customers = Customer.objects.all()
    for customer in customers:
        subscription = stripe.Subscription.retrieve(customer.stripe_subscription_id)
        if subscription.status != 'active':
            customer.membership = False
        else:
            customer.membership = True
        customer.cancel_at_period_end = subscription.cancel_at_period_end
        customer.save()
    return HttpResponse('completed') 
    
def home(request):
    plans = FitnessPlan.objects
    return render(request, 'plans/home.html', {'plans':plans})

def about(request):
    return render(request, 'interface/about.html')

def fitnessBlogs(request):
    fitnessBlogs = FitnessBlog.objects
    return render(request,'interface/fitnessBlogs.html', {'fitnessBlogs':fitnessBlogs})

def fitness(request,pk):
    fitness = get_object_or_404(FitnessBlog,pk=pk)
    if fitness.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'interface/fitnessPage.html', {'fitness':fitness})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
       return render(request, 'interface/fitnessPage.html', {'fitness':fitness})

#to show all foods
def foodsPage(request):
    foodBlogs = Food.objects
    return render(request,'interface/foodsPage.html', {'foodBlogs':foodBlogs})
#this is the food object,so if a user !has sub to premium they will be redirected to join 
def food(request,pk):
    food = get_object_or_404(Food,pk=pk)
    if food.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'interface/food.html', {'food':food})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
       return render(request, 'interface/food.html', {'food':food})


def healthBlogs(request):
    healthBlogs = Health.objects
    return render(request,'interface/healthBlogs.html',{'healthBlogs':healthBlogs})

def health(request,pk):
    health = get_object_or_404(Health,pk=pk)
    if health.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'interface/health.html', {'health':health})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
       return render(request, 'interface/health.html', {'health':health})


def beautyBlogs(request):
    beautyBlogs = Beauty.objects
    return render(request,'interface/beautyBlogs.html',{'beautyBlogs':beautyBlogs})

def beauty(request,pk):
    beauty = get_object_or_404(Beauty,pk=pk)
    if beauty.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'interface/beautyPage.html', {'beauty':beauty})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
       return render(request, 'interface/beautyPage.html', {'beauty':beauty})


def loveBlogs(request):
    loveBlogs = Love.objects
    return render(request,'interface/loveBlogs.html',{'loveBlogs':loveBlogs})

def love(request,pk):
    love = get_object_or_404(Love,pk=pk)
    if love.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'interface/lovePage.html', {'love':love})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
       return render(request, 'interface/lovePage.html', {'love':love})

def cultureBlogs(request):
    cultureBlogs = Culture.objects
    return render(request,'interface/cultureBlogs.html',{'cultureBlogs':cultureBlogs})



def culture(request,pk):
    culture = get_object_or_404(Culture,pk=pk)
    if culture.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'interface/culture.html', {'culture':culture})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
       return render(request, 'interface/culture.html', {'culture':culture})


def plan(request,pk):
    plan = get_object_or_404(FitnessPlan, pk=pk)
    if plan.premium :
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'plans/plan.html', {'plan':plan})
            except Customer.DoesNotExist:
                    return redirect('join')
        return redirect('join')
    else:
        return render(request, 'plans/plan.html', {'plan':plan})

def join(request):
    return render(request, 'plans/join.html')

@login_required
def checkout(request):

    try:
        if request.user.customer.membership:
            return redirect('settings')
    except Customer.DoesNotExist:
        pass
    #coupons
    coupons = {'halloween':15, 'welcome':10,'evansreferral':20}
    
    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(email=request.user.email, source=request.POST['stripeToken'])
        plan = 'price_1Ju6f2E9EMUzkjDtpVYOaDJj'
        if request.POST['plan'] == 'yearly':
            plan = 'price_1Ju6gHE9EMUzkjDtgWkkEkAo'
        if request.POST['coupon'] in coupons:
            percentage = coupons[request.POST['coupon'].lower()]
            try:
                coupon = stripe.Coupon.create(duration='once', id=request.POST['coupon'].lower(),
                percent_off=percentage)
            except:
                pass
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}], coupon=request.POST['coupon'].lower())
        else:
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}])

        customer = Customer()
        customer.user = request.user
        customer.stripeid = stripe_customer.id
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = subscription.id
        customer.save()
        
        return redirect('home')
    else:
        coupon = 'none'
        plan = 'monthly'
        price = 1000
        og_dollar = 10
        coupon_dollar = 0
        final_dollar = 10
        if request.method == 'GET' and 'plan' in request.GET:
            if request.GET['plan'] == 'yearly':
                plan = 'yearly'
                price = 10000
                og_dollar = 100
                final_dollar = 100
        if request.method == 'GET' and 'coupon' in request.GET:
            if request.GET['coupon'].lower() in coupons:
                coupon = request.GET['coupon'].lower()
                percentage = coupons[request.GET['coupon'].lower()]
                coupon_price = int((percentage / 100) * price)
                price = price - coupon_price
                coupon_dollar = str(coupon_price)[:-2] + '.' + str(coupon_price)[-2:]
                final_dollar = str(price)[:-2] + '.' + str(price)[-2:]

        return render(request, 'plans/checkout.html',
        {'plan':plan,'coupon':coupon,'price':price,'og_dollar':og_dollar,
        'coupon_dollar':coupon_dollar,'final_dollar':final_dollar})

def settings(request):
    membership = False
    cancel_at_period_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)
        subscription.cancel_at_period_end = True
        request.user.customer.cancel_at_period_end = True
        cancel_at_period_end = True
        subscription.save()
        request.user.customer.save()
    else:
        try:
            if request.user.customer.membership:
                membership = True
            if request.user.customer.cancel_at_period_end:
                cancel_at_period_end = True
        except Customer.DoesNotExist:
            membership = False
    return render(request, 'registration/settings.html', {'membership':membership,
    'cancel_at_period_end':cancel_at_period_end})

@user_passes_test(lambda u: u.is_superuser)
def updateaccounts(request):
    customers = Customer.objects.all()
    for customer in customers:
        subscription = stripe.Subscription.retrieve(customer.stripe_subscription_id)
        if subscription.status != 'active':
            customer.membership = False
        else:
            customer.membership = True
        customer.cancel_at_period_end = subscription.cancel_at_period_end
        customer.save()
    return HttpResponse('completed')



class SignUp(generic.CreateView):
    form_class = CustomSignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'  
  
    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class ResetPassword(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/resetpassword.html'
    email_template_name = 'registration/passwordreset_email.html'
    subject_template_name = 'registration/passwordreset_sub.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')