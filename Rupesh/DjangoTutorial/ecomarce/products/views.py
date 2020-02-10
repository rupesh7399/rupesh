from django.http import *
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from carts.models import Cart

# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product/list.html"


class ProductFeaturedListView(ListView):
    template_name = "list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        queryset = Product.objects.all().featured()
        return queryset


class ProductSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active = True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm")
        return instance
    

class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = "product/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn'exist")

        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "featured.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()
