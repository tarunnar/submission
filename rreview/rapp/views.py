import json
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import orders, MyUser
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Avg
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
User = get_user_model()

@login_required
def logout_view(request):
    try:
        logout(request)
    except:
        return HttpResponse(json.dumps({"status": "Fail"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status": "Done"}), content_type="application/json")
def login(request):
    if request.method == "POST":
        user = auth.authenticate(email=request.POST['email'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return HttpResponse(json.dumps({"status": "login_succ", "redirect_url":"search"}), content_type="application/json")
        else:
            pass
        return HttpResponse(json.dumps({"status": "Invalid credentials"}), content_type="application/json")
    return render(request, 'login.html')
@login_required
def get_review_data(request, restaurant_id):
    print(type(request.user))
    if request.method == "POST":
        rating_value = request.POST.get('rating_value')
        rating_text = request.POST.get('rating_text')
        order_id = "{}_{}_{}".format(int(timezone.now().timestamp()), request.user, restaurant_id)
        order = orders(order_id=order_id, restaurant_id=restaurant_id, user=request.user.email, rating=rating_value, rating_text=rating_text)
        try:
            order.save()
        except Exception as e:
            return HttpResponse(json.dumps({"status": "Failure"}), content_type="application/json")
        else:
            avg_rating = orders.objects.filter(restaurant_id=restaurant_id).aggregate(Avg('rating'))
            data_to_send = {
                "rating_value": rating_value,
                "rating_text": rating_text,
                "user_id": request.user.email,
                "order_id": order_id,
                "avg_rating": avg_rating.get("rating__avg"),
                "status": "Success"
            }
            return HttpResponse(json.dumps(data_to_send), content_type="application/json")
    elif request.method == "GET":
        orders_qs = orders.objects.filter(restaurant_id=restaurant_id)
        avg_rating = orders.objects.filter(restaurant_id=restaurant_id).aggregate(Avg('rating'))
        orders_list = []
        for order in orders_qs:
            order_data = {
                    "rating_value": order.rating,
                    "rating_text": order.rating_text,
                    "user_id": order.user,
                    "order_id": order.order_id
                }
            orders_list.append(order_data)
        reviews_json_string = json.dumps({"avg_rating": avg_rating.get("rating__avg"), "reviews": orders_list})
        return render(request, 'rating.html', {"reviews_json_string": reviews_json_string})
    return render(request, 'rating.html', {"hi": 1})

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')
        if password == confirm_password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User.objects.create_user(email=email, password=password)
                return HttpResponse(json.dumps({"status": "success"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"status": "already exists"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": "password and confirm password are different"}), content_type="application/json")
    return render(request, 'signup.html')
@login_required
def restaurants_search(request):
    print("restaurant_search")
    return render(request, "index.html")
