from django.shortcuts import render
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html' 
    def user_contact(request):
    # Запрашиваем объект модели Contact
        contact = Contact.objects.get(pk=3)

        # Создаём объект формы и передаём в него объект модели с pk=3
        form = ContactForm(instance=contact)

    # Передаём эту форму в HTML-шаблон
        return render(request, 'users/contact.html', {'form': form}) 

# Create your views here.
