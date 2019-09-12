from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from contestant.models import Contestant



"""
CREATING THE HOMEPAGE: The department_name and session fields are variables that
can be changed to meet custom needs.
context is a dictionary that is parsed into the template.
"""
def home_page(request, *args, **kwargs):
    department_name = "NAQSS"
    session = "2019/2020"
    context = {"department_name": department_name, "session": session }
    return render(request, "home.html", context)


def example_page(request, *args, **kwargs):
    return render(request, "example.html")
 


# DON'T MESS WITH THIS CODE!!!!!
# This part validates users login taking from the login form 
# and checking if they match the data already stored in the txt files
def login_view(request):
    # a = input("enter username: ")
    # b = input("enter password: ")
    a = str(request.POST.get('username'))
    b = str(request.POST.get('password'))
    ouser = open('usernames.txt', 'r')
    okey = open('passwords.txt', 'r')
    user = ouser.read()
    key = okey.read()
    if a in user:
    # if a in user:
        x = 1
    else:
        x = 0
    if b in key:
    # if b in key:
        y = 1
    else:
        y = 0
    if x == 1 and y == 1:
        print("success")
        redirect_url = "/vote/president"
        # print(redirect_url)
    else:
        print("failed")
        redirect_url = "#"
        print(redirect_url)
    form = "a"
    page_heading = "Login to vote here!"
    template_name = 'login.html'
    context = {"form": form, "page_heading": page_heading, "redirect_url": redirect_url}
    return render(request, template_name, context)

# login_view()