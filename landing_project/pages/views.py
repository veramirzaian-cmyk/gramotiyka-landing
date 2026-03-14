from django.shortcuts import render
from .models import Landing, Feature, Testimonial, Section
from .forms import LeadForm
from .utils import send_telegram_message

def landing_view(request):
    landing = Landing.objects.first()
    features = Feature.objects.all()
    testimonials = Testimonial.objects.all()
    sections = Section.objects.filter(is_active=True).order_by('order')

    success = False

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()

            message = f"""
Нова заявка 🚀

Ім'я: {lead.name}
Email: {lead.email}
Повідомлення: {lead.message}
            """

            send_telegram_message(message)

            success = True
            form = LeadForm()
    else:
        form = LeadForm()

    return render(request, 'pages/landing.html', {
        'landing': landing,
        'features': features,
        'testimonials': testimonials,
        'sections': sections,
        'form': form,
        'success': success,
    })