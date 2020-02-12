from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
# CRUD create update retrieve delete
from .models import Address
from billing.models import BillingProfile
from .forms import AddressForm


def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(request.POST)
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
            request)

        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billingProfile = billing_profile
            instance.address_type = address_type
            instance.save()

            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")

        else:
            print("Error here")
            return redirect("carts:checkout")

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("carts:checkout")
    return redirect("carts:checkout")


def checkout_address_reuse_view(request):
    print("hi")
    if request.user.is_authenticated:
        context = {}
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        if request.method == "POST":
            print(request.POST)
            shipping_address = request.POST.get('shipping_address', None)
            address_type = request.POST.get('address_type', 'shipping')
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(
                request)
            if shipping_address is not None:
                qs = Address.objects.filter(
                    billingProfile=billing_profile, id=shipping_address)
                if qs.exists():
                    request.session[address_type +
                                    "_address_id"] = shipping_address
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
    return redirect("cart:checkout")
