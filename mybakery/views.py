from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Product
from .models import MenuItem

# Create your views here.
def home(request):
    # For homepage, get only a few menu items to highlight
    menu_items = MenuItem.objects.filter(is_available=True).order_by('order')[:3]  # just 3 items for preview
    return render(request, 'home.html', {'menu_items': menu_items})

def about(request):
    return render(request, 'about.html')

def thank_you(request):
    return render(request, 'thank_you.html')

def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True).order_by('order')
    return render(request, 'menu.html', {'menu_items': menu_items})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # or reload page with success message
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})