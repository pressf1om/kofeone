from django.shortcuts import render, redirect
# from .forms import ContactForm

def main(request):
    return render(request, 'main/main.html')

"""def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return
        redirect('thanks')
    else:
        form = ContactForm() """