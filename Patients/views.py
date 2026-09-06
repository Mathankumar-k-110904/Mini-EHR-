from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    total_patients = Patient.objects.count()

    return render(
        request,
        'Patients/home.html',
        {
            'total_patients': total_patients
        }
    )

@login_required
def add_patient(request):

    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:
        form = PatientForm()

    return render(request, 'Patients/add_patient.html', {'form': form})

@login_required
def patient_list(request):
    search = request.GET.get('search', '')

    patients = Patient.objects.all().order_by('-created_at')

    if search:
        patients = patients.filter(
            Q(name__icontains=search) |
            Q(phone__icontains=search)
        )

    return render(
        request,
        'Patients/patient_list.html',
        {
            'patients': patients,
            'search': search
        }
    )

@login_required
def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)

    return render(
        request,
        'Patients/patient_detail.html',
        {'patient': patient}
    )

@login_required
def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect("patient_detail", id=patient.id)

    else:
        form = PatientForm(instance=patient)

    return render(
        request,
        "Patients/edit_patient.html",
        {
            "form": form,
            "patient": patient
        }
    )

@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        patient.delete()
        return redirect("patient_list")

    return render(
        request,
        "Patients/delete_patient.html",
        {"patient": patient}
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:
            messages.error(
                request,
                "Incorrect username or password."
            )

    return render(request, "Patients/login.html")


def logout_view(request):

    logout(request)

    return redirect("login")