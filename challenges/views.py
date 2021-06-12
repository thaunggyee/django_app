from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}
def index(request):
    month_click = ""
    month_list = list(monthly_challenges.keys()) ##["jan","feb","march", ---]
    for month in month_list: #jan
        cap_month = month.upper() + " "  #JAN
        click_link = reverse("month-challenge", args=[month])  ##ip/challenges/january
        month_click += f"<li><a href=\"{click_link}\">{cap_month}</a></li>" ## . JANUARY
    style = f"<ul>{month_click}</ul>"
    return HttpResponse(style)

def redirect(request, month): ##ip/challenges/redirrect/1
    mc = list(monthly_challenges.keys()) #list

    if month > len(mc): ##passwed 1< 12
       return HttpResponseNotFound("Invalid month")

    redirect_month = mc[month - 1] ## mc[0] = january
    redirect_path = reverse("month-challenge", args=[redirect_month]) #ip/challenges/jaunary
    #return HttpResponseRedirect("/challenges/" + redirect_month )
    return HttpResponseRedirect(redirect_path)
def month(request, month): #ip/challenges/january
    try:
      month_output = monthly_challenges[month] ##value of january key from dictionary
      html_responese = render_to_string("challenges/challenges.html", {
          "text": month_output ### text = value 
      })
      return HttpResponse(html_responese)
    except:
      return HttpResponseNotFound("Invalid Month")