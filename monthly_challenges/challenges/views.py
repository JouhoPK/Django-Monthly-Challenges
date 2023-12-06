from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": "20 minutes of Straight A's content",
    "february": "30 minutes of Straight A's content",
    "march": "$20 in income for Straight A's from Printify",
    "april": "20 minutes of Straight A's content",
    "may": "30 minutes of Straight A's content",
    "june": "$20 in income for Straight A's from Printify",
    "july": "20 minutes of Straight A's content",
    "august": "30 minutes of Straight A's content",
    "september": "$20 in income for Straight A's from Printify",
    "october": "20 minutes of Straight A's content",
    "november": "30 minutes of Straight A's content",
    "december": None
}

def main(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def views_int(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def views(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        raise Http404()