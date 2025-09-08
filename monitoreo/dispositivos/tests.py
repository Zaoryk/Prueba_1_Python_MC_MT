from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Device, Measurement, Alert, Category, Zone

def dashboard_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "Necesitas iniciar sesion.")
        return redirect("login")
    
    devices_by_category = (
        Category.objects.filter(organization_id=org_id)
        .annotate(count=Count("device"))
    )

    devices_by_zone = (
        Zone.objects.filter(organization_id=org_id)
        .annotate(count=Count("device"))
    )

    week_ago = timezone.now() - timedelta(days=7)
    alerts_week = (
        Alert.objects.filter(organization_id=org_id, triggered_at__gte=week_ago)
        .values("severity")
        .annotate(count=Count("id"))
    )
    alerts_count = {"Critical": 0, "High": 0, "Medium": 0}
    for a in alerts_week:
        alerts_count[a["severity"]] = a["count"]

    last_measurements = Measurement.objects.filter(
        organization_id=org_id
    ).order_by("-measured_at")[:10]

    recent_alerts = Alert.objects.filter(
        organization_id=org_id
    ).order_by("-triggered_at")[:5]

    return render(request, "dispositivos/dashboard.html", {
        "devices_by_category": devices_by_category,
        "devices_by_zone": devices_by_zone,
        "alerts_count": alerts_count,
        "last_measurements": last_measurements,
        "recent_alerts": recent_alerts,
    })