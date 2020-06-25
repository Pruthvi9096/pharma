from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from django.forms.models import model_to_dict,modelformset_factory
from .models import Pharmacy,DrugRequest
from .forms import RequestForm,PharmacyForm
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def index(request):
    pharmacy = False
    try:
        pharmacy = request.user.pharmacy
    except:
        pass
    requests = False
    # form = PharmacyForm()
    form = False
    if pharmacy:
        requests = pharmacy.pharmacy.all().order_by('-id')
        page = request.GET.get('page', 1)
        edit = request.GET.get('edit',False)
        paginator = Paginator(requests, 10)
        try:
            requests = paginator.page(page)
        except PageNotAnInteger:
            requests = paginator.page(1)
        except EmptyPage:
            requests = paginator.page(paginator.num_pages)
        if edit and request.method == 'GET':
            form = PharmacyForm(instance=pharmacy)
        if request.method == 'POST':
            form = PharmacyForm(request.POST,instance=pharmacy)
            if form.is_valid():
                pharma = form.save(commit=False)
                pharma.user = request.user
                pharma.save()
                return render(request,'home.html',{'pharmacy':pharmacy,'requests':requests,'form':False})
    else:
        create = request.GET.get('create',False)
        if create and request.method == 'GET':
            form = PharmacyForm()
        if request.method == 'POST':
            form = PharmacyForm(request.POST)
            if form.is_valid:
                pharmacy = form.save(commit=False)
                pharmacy.user = request.user
                pharmacy.save()
                return redirect('index')

    return render(request,'home.html',{'pharmacy':pharmacy,'requests':requests,'form':form})

def requestForm(request):
    pharmacies = Pharmacy.objects.all()
    if request.method == 'POST':
        form = RequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request Created Succesfully.')
        else:
            print(form.errors)
            return render(request,'form.html',{'pharmacies':pharmacies,'form':form})
        return redirect(reverse('request'))
    else:
        form = RequestForm()
    return render(request,'form.html',{'pharmacies':pharmacies,'form':form})

def requestDetails(request,pk):
    req = DrugRequest.objects.get(id=pk)
    return render(request,'request_detail.html',{'request':req})

def doneRequest(request,pk):
    req = DrugRequest.objects.get(id=pk)
    req.status = 'done'
    req.save()
    return render(request,'request_detail.html',{'request':req})

def search(request):
    q = request.GET.get('q').strip()
    select = request.GET.get('select')
    pharmacy = False
    if q != '':
        if select:
            try:
                result = Pharmacy.objects.get(name=q)
                return JsonResponse(model_to_dict(result),safe=False)
            except:
                pass
        results = Pharmacy.objects.filter(
            Q(name__icontains=q) |
            Q(address__icontains=q) |
            Q(city__icontains=q) |
            Q(state__icontains=q) |
            Q(zipcode__icontains=q) |
            Q(contact__icontains=q)
            
        )
    else:
        results = {}
    if results:
        pharmacy = [{'label':line.name+'\n'+line.show_address,'value':line.name} for line in results]
    
    return JsonResponse(pharmacy,safe=False)

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('index'))
        else:
            messages.error(request,'username or password not correct')
            return redirect(reverse('login'))
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=raw_password)
			login(request,user)
			return redirect(reverse('index'))
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'logout.html')