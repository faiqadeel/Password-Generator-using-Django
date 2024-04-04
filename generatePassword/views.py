from random import choice, randint, shuffle

from django.http import HttpResponse
from django.shortcuts import render

from generatePassword.templates.pages.form import PasswordGeneratorForm

from .models import GeneratedPassword


# Create your views here.
# This is a request handler
def hello(request):
    # form = PasswordGeneratorForm(request.POST or None)
    if request.method == "POST":
        if "GeneratePassword" in request.POST:
            email = request.POST.get("email")
            appName = request.POST.get("WebsiteName")
            pasword = pswd()
            generated_password = GeneratedPassword(
                email=email, websiteName=appName, password=pasword
            )
            generated_password.save()
            return render(
                request,
                "pages/index.html",
                {
                    "emailId": email,
                    "websiteName": appName,
                    "genPassword": pasword,
                    "PasswordGenerated": True,
                },
            )

        elif "SearchforPassword" in request.POST:
            search = request.POST.get("searchText")
            result = GeneratedPassword.objects.get(websiteName=search)

            return render(
                request,
                "pages/index.html",
                {
                    "show_search_results": True,
                    "emailId": result.email,
                    "websiteName": result.websiteName,
                    "genPassword": result.password,
                },
            )
    return render(
        request,
        "pages/index.html",
    )


def pswd():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    upper_letters = [i.upper() for i in letters]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    password_letters = [choice(letters) for i in range(randint(4, 6))]
    password_upper_letters = [choice(upper_letters) for i in range(randint(4, 6))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password = (
        password_letters + password_symbols + password_numbers + password_upper_letters
    )
    shuffle(password)
    hard_password = "".join(password)
    return hard_password
