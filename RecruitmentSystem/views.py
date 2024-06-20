from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import UpdateApplicationStatusForm, StudentApplicationForm, OCDataForm, OCBureauLeaderDataForm, LoginForm, OCPresidentDataForm, OCEventData2Form, SelectedOCForm
from .models import ApplicationStatus, StudentApplication, OCData, OCBureauLeaderData, OCPresidentData, OCEventData2, SelectedOC

# Create your views here.

def index(request):
    application_status = ApplicationStatus.objects.all()
    return render(request, 'index.html', {'application_status': application_status})

def studentapplication(request):
    if request.method == "POST":
        form = StudentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentApplicationForm()
    return render(request, 'studentapplication.html', {'form': form})

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def create_oc(request):
    register = StudentApplication.objects.all()
    if request.method == 'POST':
        form = OCDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_oc')
    else:
        form = OCDataForm()
    return render(request, 'create_oc.html', {'form': form,'register':register})

def create_ocbureauleader(request):
    if request.method == 'POST':
        form = OCBureauLeaderDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_ocbureauleader')  # Redirect to a success page
    else:
        form = OCBureauLeaderDataForm()
    return render(request, 'create_ocbureauleader.html', {'form': form})

def create_ocpresident(request):
    if request.method == 'POST':
        form = OCPresidentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_ocpresident')  # Redirect to a success page
    else:
        form = OCPresidentDataForm()
    return render(request, 'create_ocpresident.html', {'form': form})

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_type = form.cleaned_data['login_type']

            try:
                if login_type == 'OC':
                    user = OCData.objects.get(ocusername=username, ocpassword=password)
                    if user.ocbureau in ['Tugasan Khas', 'MakanMinum', 'Media', 'Kesihatan', 'Aktiviti']:
                        request.session['oc_name'] = user.ocname
                        return redirect('oc_page')  # Adjust to actual view name for OC page
                    
                elif login_type == 'OC Bureau Leader':
                    user = OCBureauLeaderData.objects.get(ocbureauleaderusername=username, ocbureauleaderpassword=password)
                    if user.ocbureauleaderbureau in ["['Tugasan Khas']", "['MakanMinum']", "['Media']", "['Kesihatan']", "['Aktiviti']"]:
                        request.session['ocbureauleader_name'] = user.ocbureauleadername
                        return redirect('oc_bureau_leader_page')  # Adjust to actual view name for OC Bureau Leader page
                    
                elif login_type == 'OC President':
                    user = OCPresidentData.objects.get(ocpresidentusername=username, ocpresidentpassword=password)
                    return redirect('oc_president_page')  # Adjust to actual view name for OC President page
                
                else:
                    form.add_error(None, "Invalid login type for the given user")
            except (OCData.DoesNotExist, OCBureauLeaderData.DoesNotExist):
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def oc_page(request):
    oc_name = request.session.get('oc_name', 'OC')
    events = OCEventData2.objects.all()
    selected_oc = SelectedOC.objects.all().order_by('-id')
    return render(request, "OC_Page.html", {'oc_name': oc_name, 'events': events, 'selected_oc':selected_oc})

def oc_bureau_leader_page(request):
    ocbureauleader_name = request.session.get('ocbureauleader_name', 'OC Bureau Leader')
    events = OCEventData2.objects.all()
    selected_oc = SelectedOC.objects.all()
    return render(request, "OC_Bureau_Leader_Page.html", {'ocbureauleader_name': ocbureauleader_name, 'events': events, 'selected_oc':selected_oc})

def oc_president_page(request):
    oc_count = OCData.objects.count()
    ocbureauleader_count = OCBureauLeaderData.objects.count()
    events = OCEventData2.objects.all()

    context = {
        'oc_count': oc_count,
        'ocbureauleader_count': ocbureauleader_count,
        'events': events
    }

    return render(request,"OC_President_Page.html", context)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def add_event(request):
    if request.method == "POST":
        form = OCEventData2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oc_president_page')  # Redirect to a list of events or another appropriate page
    else:
        form = OCEventData2Form()
    
    return render(request, 'add_event.html', {'form': form})

def select_oc_for_event(request):
    if request.method == "POST":
        form = SelectedOCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oc_bureau_leader_page')  # Adjust to the actual view name
    else:
        form = SelectedOCForm()
    return render(request, 'select_oc_for_event.html', {'form': form})

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def update_page(request):
    return render(request, 'update_page.html')

def update_oc_list(request):
    oc_list = OCData.objects.all()
    return render(request, 'update_oc_list.html', {'oc_list': oc_list})

def update_oc(request, pk):
    oc = get_object_or_404(OCData, pk=pk)
    if request.method == "POST":
        form = OCDataForm(request.POST, instance=oc)
        if form.is_valid():
            form.save()
            return redirect('update_oc_list')
    else:
        form = OCDataForm(instance=oc)
    return render(request, 'update_oc_form.html', {'form': form})

def update_ocbureauleader_list(request):
    ocbureauleader_list = OCBureauLeaderData.objects.all()
    return render(request, 'update_ocbureauleader_list.html', {'ocbureauleader_list': ocbureauleader_list})

def update_ocbureauleader(request, pk):
    ocbureauleader = get_object_or_404(OCBureauLeaderData, pk=pk)
    if request.method == "POST":
        form = OCBureauLeaderDataForm(request.POST, instance=ocbureauleader)
        if form.is_valid():
            form.save()
            return redirect('update_ocbureauleader_list')
    else:
        form = OCBureauLeaderDataForm(instance=ocbureauleader)
    return render(request, 'update_ocbureauleader_form.html', {'form': form})

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def delete_oc_list(request):
    oc_list = OCData.objects.all()
    return render(request, 'delete_oc_list.html', {'oc_list': oc_list})

def delete_oc(request, pk):
    oc = get_object_or_404(OCData, pk=pk)
    if request.method == "POST":
        oc.delete()
        return redirect('delete_oc_list')
    return render(request, 'delete_oc_confirm.html', {'oc': oc})

def delete_ocbureauleader_list(request):
    ocbureauleader_list = OCBureauLeaderData.objects.all()
    return render(request, 'delete_ocbureauleader_list.html', {'ocbureauleader_list': ocbureauleader_list})

def delete_ocbureauleader(request, pk):
    ocbureauleader = get_object_or_404(OCBureauLeaderData, pk=pk)
    if request.method == "POST":
        ocbureauleader.delete()
        return redirect('delete_ocbureauleader_list')
    return render(request, 'delete_ocbureauleader_confirm.html', {'ocbureauleader': ocbureauleader})

#==========================================================================
#==========================================================================
#==========================================================================

def application_list(request):
    applications = StudentApplication.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

def update_application_status(request, pk):
    application = get_object_or_404(StudentApplication, pk=pk)
    try:
        status = ApplicationStatus.objects.get(student_application=application)
    except ApplicationStatus.DoesNotExist:
        status = ApplicationStatus(student_application=application)

    if request.method == 'POST':
        form = UpdateApplicationStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = UpdateApplicationStatusForm(instance=status)

    return render(request, 'update_application_status.html', {'form': form, 'application': application})