import io

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect, render_to_response
import json

from reportlab.pdfgen import canvas

from pos.forms import LoginForm
from .models import Product, Order, OrderItem, StoreDetails


def userlogin(request):
    store = StoreDetails.objects.all()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(username=username, password=password)

        if form.is_valid():
            try:
                userdetails = User.objects.get(username=username)
            except User.DoesNotExist:
                # raise Http404("Message does not exist!")
                # return render(request, 'user/user_does_not_exist.html', {'user': username})
                return render(request, 'pos/login.html',
                              {
                                  'store': store,
                                  'form': LoginForm(),
                                  'fixusername': 'ERR: 122... Make sure the username and password are correct.'
                              })

            if userdetails.is_active is False:
                # pass
                # Return a 'disabled account' error message
                # return render(request, 'subscription/account_deactivated.html', {'user': username})
                return HttpResponse("Error... " + username + "'s account is Deactivated!")

            # if userdetails.is_superuser is True:
            #     # pass
            #     # return redirect("not_company")
            #     return HttpResponse('Managers Not Allowed!')

        else:
            return render(request, 'pos/login.html',
                          {
                              'store': store,
                              'form': LoginForm(),
                              'fixform': 'ERR: 121... Make sure the username and password are correct.'
                          })

        if user is not None and form.is_valid():
            login(request, user)
            # Redirect to users dashboard.
            return redirect('dashboard')

        else:
            # Return an 'invalid login' error message.
            # messages.error(request, "Username: " + username + " & password: " + password + " Dont match!")
            return render_to_response('pos/login.html',
                                      {
                                          'fixform': 'ERROR: 122... User Does Not Exist!',
                                          'store': store,
                                      })

    else:
        form = LoginForm()
        # links = CitiJobsPagesAndOtherAccount.objects.all()
        # jobs = Jobs.objects.all()[:6]
        return render(request, 'pos/login.html',
                      {
                          'store': store,
                          'form': LoginForm(),
                      })


@login_required
def dashboard(request):
    store = StoreDetails.objects.all()
    return render(request, 'pos/dashboard.html',
                  {
                      'store': store,
                  })


@login_required
def getProduct(request):
    global product_response
    product_response = {}
    print('INSIDE getProduct')
    product_barcode = request.GET['product_barcode']
    print("BARCODE::: " + product_barcode)

    try:
        returned_product = Product.objects.get(barcode=product_barcode)
        product_response = {
            'product_id': returned_product.product_id,
            'quantity': returned_product.quantity,
            'productname': returned_product.productname,
            'price': returned_product.price
        }
        print('PRODUCT_NAME: ', returned_product.productname)
    except Product.DoesNotExist:
        print('Product Does Not Exist!')
    return JsonResponse(product_response)


@login_required
def billing(request):
    products = list(Product.objects.filter(active=True))
    return render(request, 'pos/billing_details.html', {'products': products})


@login_required
def billing_success(request):
    products = list(Product.objects.filter(active=True))
    return render(request, 'pos/billing_details.html',
                  {
                      'products': products,
                      'success': 'success',
                  })


@login_required
def order(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        product_names = []
        product_prices = []
        if data is None:
            raise AttributeError
        print(data)
        # customer = Customer.objects.get(pk=data['customer_id'])
        order = Order.objects.create(total_price=data['total_price'],
                                     success=False)
        for product_id in data['product_ids']:
            getOrderItems = OrderItem(product=Product.objects.get(pk=product_id), order=order).save()

            #deducing from stock
            deduceFromQuantity(product_id)

            #testing receipt
            product = Product.objects.get(pk=product_id)
            product_names.append(product.productname)
            product_prices.append(product.price)

            print("ORDER ITEM: ", product.productname + " PRICE: " + str(product.price))
            #printReceipt(product.productname, str(product.price), data['total_price'])
            order.success = True
        order.save()

        print('TOTAL PRICE: ', data['total_price'])


        #
        # # create a file like buffer to receive the pdf
        # buffer = io.BytesIO()
        #
        # # create the pdf obj, using the buffer as its file
        # p = canvas.Canvas(buffer)
        #
        # # draw things on the pdf. here is where the pdf generation happens
        # # see the reportlab documentation for the full list of functionality
        # p.drawString(200, 810, "STORE NAME")
        # p.drawString(280, 790, product_names)
        # p.drawString(300, 780, "K" + str(list(product_prices)))
        # p.drawString(200, 770, "MONTH ENDING : AUGUST, 2019")
        # p.drawString(100, 100, "K" + str(data['total_price']))
        #
        # # close the pdf obj cleanly and we are done.
        # p.showPage()
        # p.save()
        #
        # # fileResponse sets the content-disposition header so that browsers present the option to save the file
        # buffer.seek(0)
        # return FileResponse(buffer, as_attachment=False,
        #                     filename='receipt.pdf')






        products = list(Product.objects.all())
        # return render(request, 'pos/billing_details.html',
        #               {
        #                   'success': order.success,
        #                   'products': products,
        #               })
        return redirect(billing)


def printReceipt(productname, price, totalprice):
    #create a file like buffer to receive the pdf
    buffer = io.BytesIO()

    #create the pdf obj, using the buffer as its file
    p = canvas.Canvas(buffer)

    #draw things on the pdf. here is where the pdf generation happens
    #see the reportlab documentation for the full list of functionality
    p.drawString(200, 810, "STORE NAME")
    p.drawString(280, 790, productname)
    p.drawString(300, 780, "K" + str(price))
    p.drawString(200, 770, "MONTH ENDING : AUGUST, 2019")
    p.drawString(100, 100, "K"+str(totalprice))

    #close the pdf obj cleanly and we are done.
    p.showPage()
    p.save()

    #fileResponse sets the content-disposition header so that browsers present the option to save the file
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='receipt.pdf')


def deduceFromQuantity(product_id):
    product = Product.objects.get(pk=product_id)
    product.quantity -= 1
    product.save()

#
# def orders(request):
#
#     return render(request, 'pos/orders.html',
#                   {
#                       'orders':
#                   })