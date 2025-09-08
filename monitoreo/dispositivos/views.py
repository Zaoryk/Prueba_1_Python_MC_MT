from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from datetime import timedelta
from .models import Organization, Device, Category, Zone, Alert, Measurement
from .forms import RegisterForm, LoginForm, PasswordResetForm

def device_list_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "You must login first.")
        return redirect("login")

    # Filtros
    category_id = request.GET.get("category")
    zone_id = request.GET.get("zone")

    devices = Device.objects.filter(organization_id=org_id)

    if category_id and category_id != "all":
        devices = devices.filter(category_id=category_id)

    if zone_id and zone_id != "all":
        devices = devices.filter(zone_id=zone_id)

    categories = Category.objects.filter(organization_id=org_id)
    zones = Zone.objects.filter(organization_id=org_id)

    return render(request, "dispositivos/device_list.html", {
        "devices": devices,
        "categories": categories,
        "zones": zones,
        "selected_category": category_id,
        "selected_zone": zone_id,
    })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Organizacion registrada de manera exitosa. Ahora puedes logearte.")
            return redirect("login")
    else:
            form = RegisterForm()
    return render(request, "dispositivos/register.html", {"form": form})
    
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                org = Organization.objects.get(email=email, deleted_at__isnull=True)
                if org.check_password(password):
                    request.session["org_id"] = org.id
                    messages.success(request, f"Bienvenido {org.name}!")
                    return redirect("dashboard")
                else:
                    messages.error(request, "Clave invalida.")
            except Organization.DoesNotExist:
                messages.error(request, "Organizacion no encontrada.")
    else:
        form = LoginForm()
    return render(request, "dispositivos/login.html", {"form": form})

def logout_view(request):
    request.session.flush()
    messages.info(request, "You have been logged out.")
    return redirect("login")

def password_reset_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                org = Organization.objects.get(email=email)
                messages.success(request, "Las instruciones para reiniciar tu clave se ha enviado al correo (simulado :3).")
                return redirect("login")
            except Organization.DoesNotExist:
                messages.error(request, "Correo no registrado.")
    else:
        form = PasswordResetForm()
    return render(request, "dispositivos/password_reset.html", {"form": form})
    
def dashboard_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "Necesitas iniciar sesion.")
        return redirect("login")
    org = Organization.objects.get(id=org_id)
    return render(request, "dispositivos/dashboard.html", {"org": org})