import base64

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'logindex.html')
def login_post(request):
    name=request.POST['textfield']
    password=request.POST['textfield2']
    log=Login.objects.filter(username=name,password=password)
    if log.exists():
        log1 = Login.objects.get(username=name, password=password)
        request.session['lid']=log1.id
        if log1.type=='admin':
            return HttpResponse("<script>alert('welcome');window.location='/myapp/homeadmin/'</script>")
        if log1.type=='shopkeeper':
            return HttpResponse("<script>alert('welcome');window.location='/myapp/shomeindex1/'</script>")
        else:
            return HttpResponse("<script>alert('incorrect username and password');window.location='/myapp/login/'</script>")

    else:
        return HttpResponse("<script>alert('incorrect username and password');window.location='/myapp/login/'</script>")

def changepassword_adm(request):
    return render(request, 'admin/changepassword.html')

def changepassword_adm_post(request):
    currentpassword=request.POST['current']
    newpassword=request.POST['new']
    confirmpassword=request.POST['confirm']
    log = Login.objects.filter(id=request.session['lid'], password=currentpassword)
    if log.exists():
        log1 = Login.objects.get(id=request.session['lid'], password=currentpassword)
        if newpassword==confirmpassword:
            res2=Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse("<script>alert('success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('password doesn't match');window.location='/myapp/changepassword_adm/'</script>")

    else:
        return HttpResponse("<script>alert('password doesn't match');window.location='/myapp/changepassword_adm/'</script>")


def logout(request):
    request.session['lid']=''
    return HttpResponse("<script>alert('you are logged out');window.location='/myapp/login/'</script>")



def viewshopkeeper(request):
    shop=Shopkeeper.objects.filter(status='pending')
    return render(request, 'admin/viewshopkeeper_adm.html', {'data':shop})

def viewshopkeeper_post(request):
    search=request.POST['textfield']
    shop = Shopkeeper.objects.filter(status='pending',rationshop_no__icontains=search)
    return render(request, 'admin/viewshopkeeper_adm.html', {'data': shop})

def viewapprovedshopkeeper(request):
    shop=Shopkeeper.objects.filter(status='accepted')
    return render(request, 'admin/viewapprovedshopkeeper_adm.html', {'data':shop})

def viewapprovedshopkeeper_post(request):
    search=request.POST['textfield']
    shop = Shopkeeper.objects.filter(status='accepted',rationshop_no__icontains=search)
    return render(request, 'admin/viewapprovedshopkeeper_adm.html', {'data': shop})

def viewrejectedshopkeeper(request):
    shop=Shopkeeper.objects.filter(status='rejected')
    return render(request, 'admin/viewrejectedshopkeeper_adm.html', {'data':shop})

def viewrejectedshopkeeper_post(request):
    search=request.POST['textfield']
    shop = Shopkeeper.objects.filter(status='rejected',rationshop_no__icontains=search)
    return render(request, 'admin/viewrejectedshopkeeper_adm.html', {'data': shop})


def approvesk(request,id):
    res=Shopkeeper.objects.filter(LOGIN=id).update(status='accepted')
    os=Login.objects.filter(id=id).update(type='shopkeeper')
    return HttpResponse("<script>alert('verified');window.location='/myapp/viewshopkeeper/'</script>")

def rejectsk(request,id):
    res=Shopkeeper.objects.filter(LOGIN=id).update(status='rejected')
    os=Login.objects.filter(id=id).update(type='rejected')
    return HttpResponse("<script>alert('rejected');window.location='/myapp/viewshopkeeper/'</script>")


def viewcardholder(request):
    costom=Cardholder.objects.filter(status='pending')
    return render(request, 'admin/viewcardholder_adm.html', {'data':costom, 'app':''})
def viewcardholder_post(request):
    search=request.POST['textfield']
    costom = Cardholder.objects.filter(rationcard_no__icontains=search,status='pending')
    return render(request, 'admin/viewcardholder_adm.html', {'data': costom, 'app':''})

def viewcardholder_accepted(request):
    costom=Cardholder.objects.filter(status='approved')
    return render(request, 'admin/viewapprovedcardholder_adm.html', {'data':costom})

def viewcardholder_accepted_post(request):
    search=request.POST['textfield']
    costom = Cardholder.objects.filter(rationcard_no__icontains=search,status='approved')
    return render(request, 'admin/viewapprovedcardholder_adm.html', {'data': costom})

def viewcardholder_rejected(request):
    costom=Cardholder.objects.filter(status='rejected')
    return render(request, 'admin/viewrejectedcardholder_adm.html', {'data':costom})
def viewcardholder_rejected_post(request):
    search=request.POST['textfield']
    costom = Cardholder.objects.filter(rationcard_no__icontains=search,status='rejected')
    return render(request, 'admin/viewrejectedcardholder_adm.html', {'data': costom})


def approvech(request,id):
    res=Cardholder.objects.filter(LOGIN_id=id).update(status='approved')
    res=Login.objects.filter(id=id).update(type='cardholder')
    return HttpResponse("<script>alert('verified');window.location='/myapp/viewcardholder/'</script>")

def rejectch(request,id):
    res=Cardholder.objects.filter(LOGIN_id=id).update(status='rejected')

    os=Login.objects.filter(id=id).update(type='rejected')
    return HttpResponse("<script>alert('rejected');window.location='/myapp/viewcardholder/'</script>")




def addstockdetails(request):
    return render(request, 'admin/addstockdetails_adm.html', )
def addstockdetails_post(request):
    item_name=request.POST['textfield2']
    quantity=request.POST['textfield3']
    price=request.POST['textfield4']
    ad=Stockdetails()
    from datetime import datetime
    date=datetime.now()
    ad.date=date
    ad.item_name=item_name
    ad.quantity=quantity
    ad.price=price
    ad.save()

    return HttpResponse('''<script>alert('stock added successfully');window.location='/myapp/homeadmin/'</script>''')

def editstockdetails(request,id):
    request.session['stid']=id
    ad=Stockdetails.objects.get(id=id)
    return render(request, 'admin/editstockdetails_adm.html', {'data':ad})
def editstockdetails_post(request):
    item_name=request.POST['textfield2']
    quantity=request.POST['textfield3']
    price=request.POST['textfield4']
    id=request.session['stid']
    ad=Stockdetails.objects.get(id=id)
    from datetime import datetime
    date=datetime.now()
    ad.date=date
    ad.item_name=item_name
    ad.quantity=quantity
    ad.price=price
    ad.save()

    return HttpResponse('''<script>alert('stock updated successfully');window.location='/myapp/viewstock/'</script>''')

def viewstock(request):
    stk=Stockdetails.objects.all()
    return render(request, 'admin/viewstockdetails_adm.html', {'data':stk})
def viewstock_post(request):
    search=request.POST['textfield']
    stk = Stockdetails.objects.filter(item_name__icontains=search)
    return render(request, 'admin/viewstockdetails_adm.html', {'data': stk})


def viewcomplaint(request):
    comp=complaint.objects.all()
    return render(request, 'admin/viewcomplaint_adm.html', {'data':comp})

def viewcomplaint_post(request):
    fromd =request.POST['textfield']
    tod=request.POST['textfield1']
    comp = complaint.objects.filter(date__range=[fromd,tod])
    return render(request, 'admin/viewcomplaint_adm.html', {'data': comp})

def addreply(request,id):
    return render(request, 'admin/addreply_adm.html',{'id':id})

def addreply_post(request):
    reply=request.POST['textarea']
    cid=request.POST['cid']
    obj=complaint.objects.filter(id=cid).update(status='Replied',reply=reply)
    return HttpResponse('''<script>alert('sending successfully');window.location='/myapp/viewcomplaint/'</script>''')

def addsubsidy(request):
    var=Stockdetails.objects.all()
    return render(request, 'admin/addsubsidy_adm.html',{'data':var})

def addsubsidy_post(request):
    # card_color=request.POST['textfield']
    beneficiaries=request.POST['textfield2']
    commodities=request.POST['textfield3']
    quantity=request.POST['quantity']
    price=request.POST['textfield4']
    quantitytype=request.POST['qtytype']
    su = Subsidydetails()
    if Subsidydetails.objects.filter(commodities_id=commodities,beneficiaries=beneficiaries, ).exists():
        su=Subsidydetails.objects.filter(commodities_id=commodities,beneficiaries=beneficiaries,)[0]
    from datetime import datetime
    date = datetime.now()
    su.date = date
    # su.card_color=beneficiaries
    su.beneficiaries=beneficiaries
    su.commodities_id =commodities
    su.quantity=quantity
    su.quantitytype=quantitytype


    su.price = price
    su.save()

    return HttpResponse('''<script>alert('subsidy added successfully');window.location='/myapp/homeadmin/'</script>''')


def viewsubsidy_adm(request):
    sub=Subsidydetails.objects.all()
    return render(request, 'admin/viewsubsidy_adm.html', {'data':sub})
def viewsubsidy_adm_post(request):
    search=request.POST['textfield']
    sub = Subsidydetails.objects.filter(beneficiaries__icontains=search)
    return render(request, 'admin/viewsubsidy_adm.html', {'data': sub})

def admin_viewbooking(request):
    bo=Booking.objects.all()
    return render(request, 'admin/viewallbooking_admin.html', {'data':bo})

def admin_viewbooking_post(request):
    fdate=request.POST['textfield2']
    tdate=request.POST['textfield3']
    bo = Booking.objects.filter(date__range=[fdate,tdate])
    return render(request, 'admin/viewallbooking_admin.html', {'data': bo})


def adm_viewbooking_sub(request,id):
    bo=Bookingsub.objects.filter(BOOKING=id)
    return render(request, 'admin/booking sub_adm.html',{'data':bo})

#################################################################
def register_shop(request):
    return render(request, 'regindex.html')
def register_shop_post(request):
    shop_no=request.POST['textfield']
    shopkeeper_name=request.POST['sn']
    district=request.POST['textfield2']
    place=request.POST['textfield3']
    post=request.POST['textfield4']
    pincode=request.POST['textfield5']
    thaluk=request.POST['textfield6']
    ward_no=request.POST['textfield7']
    phone=request.POST['textfield8']
    email=request.POST['textfield11']
    photo=request.FILES['PHOTO']

    password=request.POST['textfield9']
    confirm_password=request.POST['textfield9']

    if Login.objects.filter(username=email).exists():
        return HttpResponse(
            '''<script>alert('email already exists');history.back()</script>''')

    if password!=confirm_password:
        return HttpResponse(
            '''<script>alert('passwords donot match');history.back()</script>''')

    from datetime import datetime
    date = 'shopkeeper/'+datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
    fs = FileSystemStorage()
    fn = fs.save(date, photo)
    path = fs.url(date)

    a=Login()
    a.username=email
    a.password=password
    a.type='pending'
    a.save()
    re=Shopkeeper()
    re.shopkeeper_name = shopkeeper_name
    re.rationshop_no = shop_no
    re.district = district
    re.email = email
    re.place = place
    re.post = post
    re.pincode = pincode
    re.thaluk=thaluk
    re.ward_no=ward_no
    re.phone=phone
    re.status='pending'
    re.LOGIN=a
    re.photo=path
    re.save()

    return HttpResponse('''<script>alert('registered successfully');window.location='/myapp/login/'</script>''')

def changepassword_shop(request):
    return render(request, 'shop/changepassword_shop.html')

def changepassword_shop_post(request):
    currentpassword=request.POST['current']
    newpassword=request.POST['new']
    confirmpassword=request.POST['confirm']
    log = Login.objects.filter(id=request.session['lid'], password=currentpassword)
    if log.exists():
        log1 = Login.objects.get(id=request.session['lid'], password=currentpassword)
        if newpassword==confirmpassword:
            res2=Login.objects.filter(id=request.session['lid']).update(password=currentpassword)
            return HttpResponse("<script>alert('success');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('password doesn't match');window.location='/myapp/changepassword_shop/'</script>")

    else:
        return HttpResponse("<script>alert('password doesn't match');window.location='/myapp/changepassword_shop/'</script>")



def viewstockavailability(request):
    stk=Stockdetails.objects.all()
    return render(request,'shop/viewstockavailable.html',{'data':stk})



def skviewstockavailability(request):
    res=Stockdetails.objects.all()
    return render(request,'shop/viewstockavailable.html',{'data':res})

def sksendrqst(request,id):
    return render(request, 'shop/addstockquantity.html',{'id':id} )

def adminviewstkrequest(request):
    so=requeststock.objects.filter(status='pending')
    return render(request,'admin/viewstockrequest.html',{'data':so})

def adminviewstkrequest_search(request):
    fdate = request.POST['textfield']
    tdate = request.POST['textfield2']
    so=requeststock.objects.filter(status='pending',date__range=[fdate,tdate])
    return render(request, 'admin/viewstockrequest.html', {'data': so})

def adminviewapprovedstkrequest(request):
    so=requeststock.objects.filter(status='approved')
    return render(request,'admin/approvedviewstockrequest.html',{'data':so})

def adminviewapprovedstkrequest_search(request):
    fdate=request.POST['textfield']
    tdate=request.POST['textfield2']
    so=requeststock.objects.filter(status='approved',date__range=[fdate,tdate])
    return render(request,'admin/approvedviewstockrequest.html',{'data':so})

def approverequest(request,id):
    res=requeststock.objects.filter(id=id).update(status='approved')
    return HttpResponse('''<script>alert('approved successfully');window.location='/myapp/adminviewstkrequest/'</script>''')


def skviewapprovedstkrequest(request):
    so=requeststock.objects.filter(status='approved',SHOPKEEPER__LOGIN_id=request.session['lid'])
    return render(request,'shop/approvedviewstockrequest.html',{'data':so})

def skviewapprovedstkrequest_search(request):
    sname=request.POST['textfield']
    so=requeststock.objects.filter(status='approved',SHOPKEEPER__LOGIN_id=request.session['lid'],STOCKDETAILS__item_name__icontains=sname)
    return render(request,'shop/approvedviewstockrequest.html',{'data':so})


def sksendrqst_post(request):
    quantity=request.POST['textfield2']
    sid=request.POST['sid']
    var=requeststock()
    var.SHOPKEEPER=Shopkeeper.objects.get(LOGIN=request.session['lid'])
    var.STOCKDETAILS_id=sid
    var.quantity=quantity
    var.status='pending'
    from datetime import datetime
    var.date=datetime.now().strftime('%Y-%m-%d')
    var.save()
    return HttpResponse('''<script>alert('Added successfully');window.location='/myapp/viewstockavailable/'</script>''')

    # return render(request, 'shop/addstockquantity.html',{'data':var})






def update_stock(request):
    res=Stockdetails.objects.all()
    return render(request, 'shop/updatestock_avail_shop.html',{'data':res})
def updatestock_post(request):
    item_name=request.POST['select']
    quantity=request.POST['textfield3']

    print(request.session['lid'],"lid")

    a=updatestock()
    shopkeeper = Shopkeeper.objects.get(LOGIN=request.session['lid'])
    if updatestock.objects.filter(STOCK_id=item_name,SHOPKEEPER=shopkeeper).exists():
        a = updatestock.objects.filter(STOCK_id=item_name,SHOPKEEPER=shopkeeper)[0]
    a.STOCK_id=item_name
    a.stock=quantity
    a.quantity=quantity
    a.status='updated'
    from datetime import datetime
    a.date=datetime.now().today()
    a.SHOPKEEPER=Shopkeeper.objects.get(LOGIN=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('stock updated successfully');window.location='/myapp/homeshop/'</script>''')

def viewupdatedstock(request):
    re=updatestock.objects.filter(SHOPKEEPER__LOGIN_id=request.session['lid'])
    return render(request,'shop/viewupdatedstock.html',{'data':re})


def addtoken(request):
    return render(request, 'shop/addtoken_shop.html')
def addtoken_post(request):
    token_no=request.POST['textfield2']
    date=request.POST['textfield']
    from_time=request.POST['textfield11']
    to_time=request.POST['textfield22']
    ad=Token()
    ad.token_no=token_no
    ad.from_time=from_time
    ad.to_time=to_time
    ad.date=date
    ad.SHOPKEEPER=Shopkeeper.objects.get(LOGIN=request.session['lid'])
    ad.save()
    return HttpResponse('''<script>alert('Token added succeessfully');window.location='/myapp/addtoken/'</script>''')

def viewtoken(request):
    ro=Token.objects.filter(SHOPKEEPER__LOGIN_id=request.session['lid'])

    l = []
    for i in ro:
        req = '0'
        if Token_request.objects.filter(TOKEN=i).count()>0:
            req = str(Token_request.objects.filter(TOKEN=i).count())+ ' '
        l.append({
            'id':i.id,
            'token_no':i.token_no,
            'date':i.date,
            'from_time':i.from_time,
            'to_time':i.to_time,
            'SHOPKEEPER':i.SHOPKEEPER,
            'req': req
        })

    return render(request,'shop/viewtoken.html',{'data':l})

def viewtoken_post(request):
    fromd=request.POST['textfield']
    tod=request.POST['textfield1']
    tk= Token.objects.filter(SHOPKEEPER__LOGIN_id=request.session['lid'],date__range=[fromd,tod])
    return render(request,'shop/viewtoken.html',{'data':tk})


def viewtokenrequest(request,id):
    req=Token_request.objects.filter(TOKEN_id=id)
    return render(request, 'shop/viewtokenrqst_shop.html',{'data':req})

def viewtokenrequest_post(request):
    search=request.POST['textfield']
    return HttpResponse('ok')

def viewbooking(request):
    bo=Booking.objects.filter(SOPKEEPER__LOGIN_id=request.session['lid'])
    return render(request, 'shop/viewbooking_shop.html',{'data':bo})

def viewbooking_post(request):
    fdate=request.POST['textfield2']
    tdate=request.POST['textfield3']
    bo = Booking.objects.filter(date__range=[fdate,tdate],SOPKEEPER__LOGIN_id=request.session['lid'])
    return render(request, 'shop/viewbooking_shop.html', {'data': bo})


def viewbooking_sub(request,id):
    bo=Bookingsub.objects.filter(BOOKING=id)
    return render(request, 'shop/booking sub.html',{'data':bo})


def viewpayment(request):
    pay=Booking.objects.filter(status='paid',SOPKEEPER__LOGIN_id=request.session['lid'])
    return render(request, 'shop/viewpayment_shop.html',{'data':pay})
def viewpayment_post(request):
    search=request.POST['textfield']
    return HttpResponse('ok')

def viewsubsidy_shop(request):
    sub=Subsidydetails.objects.all()
    return render(request, 'shop/viewsubsidy_shop.html',{'data':sub})
def viewsubsidy_shop_post(request):
    search=request.POST['textfield']
    sub=Subsidydetails.objects.filter(beneficiaries__icontains=search)
    return render(request, 'shop/viewsubsidy_shop.html',{'data':sub})

def homeadmin(request):
    return render(request, 'admin/adminhomeindex2.html')

def homeshop(request):
    return render(request, 'shop/shophomeindex2.html')


def shomeindex1(request):
    return render(request,"shop/shomeindex.html")

def other_viewbooking(request):
    bo=Booking.objects.all()
    return render(request, 'shop/viewotherbooking_shop.html',{'data':bo})

def other_viewbooking_post(request):
    search=request.POST['textfield2']
    bo = Booking.objects.filter(CARDHOLDER__rationcard_no__icontains=search)
    return render(request, 'shop/viewotherbooking_shop.html', {'data': bo})


def other_viewbooking_sub(request,id):
    bo=Bookingsub.objects.filter(BOOKING=id)
    return render(request, 'shop/other_booking sub_adm.html',{'data':bo})


def shopviewprofile(request):
    vi=Shopkeeper.objects.get(LOGIN=request.session['lid'])
    return render(request,'shop/viewprofileshop.html',{'data':vi})

def editprofileshop(request):
    var=Shopkeeper.objects.get(LOGIN=request.session['lid'])
    return render(request,'shop/editshop.html',{'data':var})

def editprofileshop_post(request):
    shop_no = request.POST['textfield']
    shopkeeper_name = request.POST['sn']
    district = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pincode = request.POST['textfield5']
    thaluk = request.POST['textfield6']
    ward_no = request.POST['textfield7']
    phone = request.POST['textfield8']
    email = request.POST['textfield11']
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fn = fs.save(date, photo)
        path = fs.url(date)
        var = Shopkeeper.objects.get(LOGIN_id=request.session['lid'])
        var.photo=path
        var.LOGIN_id=request.session['lid']
        var.save()
        return HttpResponse(
            '''<script>alert('edit succeessfully');window.location='/myapp/shopviewprofile/'</script>''')
    var = Shopkeeper.objects.get(LOGIN_id=request.session['lid'])
    var.shopkeeper_name = shopkeeper_name
    var.rationshop_no = shop_no
    var.district = district
    var.place = place
    var.post = post
    var.pincode = pincode
    var.thaluk=thaluk
    var.ward_no=ward_no
    var.phone=phone
    var.email=email
    var.LOGIN_id=request.session['lid']
    var.save()
    return HttpResponse(
        '''<script>alert('edit succeessfully');window.location='/myapp/shopviewprofile/'</script>''')











#############################user



def userlogin(request):
    username=request.POST['username']
    password=request.POST['password']
    log=Login.objects.filter(username=username,password=password)
    if log.exists():
        log1 = Login.objects.get(username=username, password=password)
        lid=log1.id
        if log1.type == 'cardholder':
            ch=Cardholder.objects.get(LOGIN__id=lid)
            return JsonResponse({'status':'ok','lid': str(lid),'type':log1.type})
        else :
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})


def userreg(request):
    cardholder_name=request.POST['cardholdername']
    rationcard_no=request.POST['cardno']
    # card_color=request.POST['cardcolor']
    card_type=request.POST['cardtype']
    place=request.POST['place']
    post=request.POST['post']
    pincode=request.POST['pincode']
    district=request.POST['district']
    members_no=request.POST['membersno']
    members_name=request.POST['membersname']
    house_no=request.POST['houseno']
    ward_no=request.POST['wardno']
    occupation=request.POST['occup']
    spouse_name=request.POST['spouse']
    phone=request.POST['phn']
    email_id=request.POST['email']
    photo=request.POST['photo']
    gender=request.POST['gender']
    password=request.POST['password']
    confirm_password=request.POST['confirmpass']
    if Login.objects.filter(username=email_id).exists():
        return JsonResponse({'status':'no'})
    if password==confirm_password:

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
        fs = base64.b64decode(photo)
        open(r'C:\\Users\\haripriya\\PycharmProjects\\rationmanagementsystem\\media\\user\\'+date,'wb').write(fs)
        path ="/media/user/"+date

        si=Login()
        si.username=email_id
        si.password=password
        si.type='pending'
        si.save()

        ob=Cardholder()
        ob.cardholder_name=cardholder_name
        ob.rationcard_no=rationcard_no
        # ob.card_color=card_color
        ob.card_type=card_type
        ob.place=place
        ob.post=post
        ob.pincode=pincode
        ob.district=district
        ob.members_no=members_no
        ob.members_name=members_name
        ob.house_no=house_no
        ob.ward_no=ward_no
        ob.occupation=occupation
        ob.spouse_name=spouse_name
        ob.phone=phone
        ob.gender=gender
        ob.email_id=email_id
        ob.photo=path
        ob.LOGIN=si
        ob.save()
    return JsonResponse({'status':'ok'})

def viewprofile(request):
    lid=request.POST['lid']
    ob=Cardholder.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok',
                         'cardholdername':ob.cardholder_name,
                         'cardno':ob.rationcard_no,
                         # 'cardcolor':ob.card_color,
                         'cardtype':ob.card_type,
                         'place':ob.place,
                         'post':ob.post,
                         'pincode':ob.pincode,
                         'district':ob.district,
                         'membersno':ob.members_no,
                         'membersname':ob.members_name,
                         'houseno':ob.house_no,
                         'wardno':ob.ward_no,
                         'occupation':ob.occupation,
                         'spousename':ob.spouse_name,
                         'phn':ob.phone,'mail':ob.email_id,
                         'gender':ob.gender,'photo':ob.photo})

def editpro(request):
    lid=request.POST['lid']
    name=request.POST['cardholdername']
    cardno=request.POST['cardno']
    # cardcolor=request.POST['cardcolor']
    card_type= request.POST['cardtype']
    place=request.POST['place']
    post=request.POST['post']
    pincode=request.POST['pincode']
    district=request.POST['district']
    mem_no=request.POST['membersno']
    mem_name=request.POST['membersname']
    house_no=request.POST['houseno']
    wardno=request.POST['wardno']
    occup=request.POST['occupation']
    spousename=request.POST['spousename']
    phone=request.POST['phone']
    gender=request.POST['gender']
    photo=request.POST['photo']

    obj=Cardholder.objects.get(LOGIN_id=lid)
    obj.cardholder_name=name
    obj.rationcard_no=cardno
    # obj.card_color=cardcolor
    obj.card_type=card_type
    obj.place=place
    obj.post=post
    obj.pincode=pincode
    obj.district=district
    obj.members_no=mem_no
    obj.members_name=mem_name
    obj.house_no=house_no
    obj.ward_no=wardno
    obj.occupation=occup
    obj.spouse_name=spousename
    obj.phone=phone
    obj.gender=gender
    if len(photo)>4:
        import os
        from rationmanagementsystem import settings
        if os.path.exists(settings.MEDIA_ROOT+obj.photo.replace('media/user/', '\\user\\').replace('/', '\\')):
            os.remove(settings.MEDIA_ROOT + obj.photo.replace('media/user/', '\\user\\').replace('/', '\\'))
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = base64.b64decode(photo)
        open(r'C:\\Users\\haripriya\\PycharmProjects\\rationmanagementsystem\\media\\user\\' + date, 'wb').write(fs)
        path = "/media/user/" + date

        obj.photo=path
    obj.save()
    return JsonResponse({'status':'ok'})










def userviewstock(request):
    obj=Stockdetails.objects.all()
    l=[]
    for i in obj :
        l.append({'id':i.id,'date':i.date,'item_name':i.item_name,'quantity':i.quantity,'price':i.price})
    return JsonResponse({'status':'ok','data':l})





def userviewupdatedstock(request):
    sid=request.POST['sid']
    lid=request.POST['lid']

    card_color=request.POST['card_color']

    l = []
    cnd = Cardholder.objects.get(LOGIN_id=lid)
    aa=Subsidydetails.objects.filter(beneficiaries=Cardholder.objects.get(LOGIN_id=lid).card_type)
    for j in aa:
        if aa.exists():
            # ab = Subsidydetails.objects.get(card_color=card_color)
            obj=updatestock.objects.filter(SHOPKEEPER_id=sid,STOCK__item_name=j.commodities.item_name)
            print(obj)
            # obj=updatestock.objects.filter(SHOPKEEPER__id=sid)
            for i in obj :

                qty = float(i.stock)
                if cnd.card_type == 'APL(White)' and j.quantitytype=='percard':
                    qty = '5'
                elif cnd.card_type == 'APL(Blue)' and j.quantitytype=='perperson':
                    qty = 2*float(cnd.members_no)
                elif cnd.card_type == 'BPL(Pink)' and i.STOCK.item_name.lower()=='rice' and j.quantitytype=='perperson':
                   qty = 4*float(cnd.members_no)
                elif cnd.card_type == 'BPL(Pink)' and i.STOCK.item_name.lower() == 'wheat' and j.quantitytype == 'perperson':
                   qty = 1 * float(cnd.members_no)
                elif cnd.card_type == 'AAY(Yellow)' and i.STOCK.item_name.lower()=='rice' and j.quantitytype=='percard':
                   qty = '30'
                elif cnd.card_type == 'AAY(Yellow)' and i.STOCK.item_name.lower()=='wheat' and j.quantitytype=='percard':
                   qty = '5'
                elif cnd.card_type == 'AAY(Yellow)' and i.STOCK.item_name.lower()=='kerosene' and j.quantitytype=='percard':
                   qty = '0.5'
                print(qty)
                l.append({'id':i.id,'date':i.date,'item_name':i.STOCK.item_name,'quantity':qty,'price':j.price ,})
    return JsonResponse({'status':'ok','data':l})




def addtocart(request):
    id=request.POST['upsid']
    lid=request.POST['lid']

    quantity=request.POST['quantity']
    u=Cardholder.objects.get(LOGIN_id=lid).card_color
    c=cart()
    import datetime
    c.date=datetime.datetime.now().today()
    c.CARDHOLDER=Cardholder.objects.get(LOGIN_id=lid)
    c.STOCK=Stockdetails.objects.get(id=id)
    c.quantity=quantity
    c.UPDATESTOCK_id=id
    c.save()
    return JsonResponse({'status': 'ok'})

def viewcart(request):
    lid=request.POST['lid']
    re=cart.objects.filter(CARDHOLDER__LOGIN_id=lid)
    l=[]
    total=0
    for i in re:
        total+=(float(i.UPDATESTOCK.STOCK.price)*int(i.quantity))
        l.append({'id':i.id,'date':i.date,'itemname':i.UPDATESTOCK.STOCK.item_name,'quantity':i.quantity,'price':i.UPDATESTOCK.STOCK.price,})
    print(l)
    return JsonResponse({'status': 'ok','data':l,'amount':str(total) })


def dltfromcart(request):
    cid=request.POST['cid']
    var=cart.objects.filter(id=cid).delete()
    return JsonResponse({'status': 'ok' })



def viewsubsidy(request):
    card_color = request.POST['card_color']

    # abj=Subsidydetails.objects.filter(card_color=card_color)
    abj=Subsidydetails.objects.all()
    n=[]
    for i in abj:
        n.append({'id':i.id,'date':i.date,
                  'cardcolor':i.card_color,
                  'beneficiaries':i.beneficiaries,
                  'commodities':i.commodities.item_name,
                  'quantity':i.quantity,
                  'price':i.price})
    return JsonResponse({'status':'ok','data':n})

def bookitem(request):

    return JsonResponse({'status':'ok'})

def makepayment(request):
    return JsonResponse({'status':'ok'})

#def viewbill(request):
  #  lid=request.POST['lid']
  #  ab=
  #  return JsonResponse({'status':'ok'})

def selecttoken(request):
    return JsonResponse({'status':'ok'})

def viewstatus(request):
    lid=request.POST['lid']
    an=Token_request.objects.filter(CARDHOLDER__LOGIN_id=lid)
    l=[]
    for i in an:
        l.append({'id':i.id,'date':i.date,'time':i.time,'token':i.TOKEN.token_no})
    return JsonResponse({'status':'ok','data':l})

def addcomplaint(request):
    lid=request.POST['lid']
    c=request.POST['complaint']
    ab=complaint()
    from datetime import datetime
    ab.date=datetime.now().date().today()
    ab.status='pending'
    ab.reply='pending'
    ab.complaint=c
    ab.CARDHOLDER=Cardholder.objects.get(LOGIN_id=lid)

    ab.save()
    return JsonResponse({'status':'ok'})

def viewreply(request):
    lid = request.POST['lid']
    w=complaint.objects.filter(CARDHOLDER__LOGIN_id=lid)
    l=[]
    for i in w:
        l.append({'id':i.id,'date':i.date,'status':i.status,'reply':i.reply,'complaint':i.complaint})
    return JsonResponse({'status':'ok','data':l})


def viewshop(request):
    lid=request.POST['lid']
    # a=Shopkeeper.objects.filter(place=Cardholder.objects.get(LOGIN_id=lid).place)
    a=Shopkeeper.objects.filter(status='accepted')
    l = []
    for i in a:
        l.append({'id': i.id, 'shopno':i.rationshop_no,'photo':i.photo,
                  'place': i.place,
                  'post': i.post,'pincode':i.pincode,
                  'district': i.district,
                  'phone':i.phone,'email':i.email})
    return JsonResponse({'status': 'ok', 'data': l})


def viewshop_search(request):
    search=request.POST['search']
    a=Shopkeeper.objects.filter(status='accepted',place__icontains=search)
    l = []
    for i in a:
        l.append({'id': i.id, 'shopno':i.rationshop_no,'photo':i.photo,
                  'place': i.place,
                  'post': i.post,'pincode':i.pincode,
                  'district': i.district,
                  'phone':i.phone,'email':i.email})
    return JsonResponse({'status': 'ok', 'data': l})


def cardholderviewpayment(request):
    lid=request.POST['lid']
    v=Payment.objects.filter(CARDHOLDER__LOGIN_id=lid)
    l=[]
    for i in v:
        l.append({'id':i.id,'date':i.date,
                  'totalprice':i.total_price,
                  'status':i.status,'booking':i.BOOKING,'cardholder':i.CARDHOLDER})
        return JsonResponse({'status': 'ok','data':l})





def user_payment_(request):
    lid = request.POST['lid']
    mytotal = 0
    res2 = cart.objects.filter(CARDHOLDER__LOGIN_id=lid)
    for i in res2:
        print(res2,"jj")
        boj = Booking()
        boj.status = 'paid'
        boj.CARDHOLDER = Cardholder.objects.get(LOGIN_id=lid)
        boj.SOPKEEPER_id = i.UPDATESTOCK.SHOPKEEPER.id
        boj.total_price = 0
        import datetime
        boj.date = datetime.datetime.now().date().today()
        boj.save()
        for j in res2:
            quantity = int(j.quantity)
            st = updatestock.objects.filter(STOCK__id=j.UPDATESTOCK.STOCK.id, STOCK__quantity__gte=quantity)
            if st.exists():
                bs = Bookingsub()
                bs.BOOKING_id = boj.id
                bs.UPDATESTOCK_id = j.UPDATESTOCK.id
                bs.quantity = j.quantity
                bs.status = 'paid'
                bs.save()
                # mytotal += (float(j.UPDATESTOCK.STOCK.price) * int(j.quantity))

        cart.objects.filter(CARDHOLDER__LOGIN_id=lid).delete()
        boj = Booking.objects.get(id=boj.id)
        boj.total_amount = mytotal
        boj.save()
    return JsonResponse({'k': '0', 'status': "ok"})

def user_payment_(request):
    lid = request.POST['lid']
    mytotal = 0
    res2 = cart.objects.filter(CARDHOLDER__LOGIN_id=lid)
    for i in res2:
        print(res2,"jj")
        boj = Booking()
        boj.status = 'paid'
        boj.CARDHOLDER = Cardholder.objects.get(LOGIN_id=lid)
        boj.SOPKEEPER_id = i.UPDATESTOCK.SHOPKEEPER.id
        boj.total_price = 0
        import datetime
        boj.date = datetime.datetime.now().date().today()
        boj.save()
        for j in res2:
            quantity = int(j.quantity)
            st = updatestock.objects.filter(STOCK__id=j.UPDATESTOCK.STOCK.id, STOCK__quantity__gte=quantity)
            if st.exists():
                bs = Bookingsub()
                bs.BOOKING_id = boj.id
                bs.UPDATESTOCK_id = j.UPDATESTOCK.id
                bs.quantity = j.quantity
                bs.status = 'paid'
                bs.save()
                # mytotal += (float(j.UPDATESTOCK.STOCK.price) * int(j.quantity))

        cart.objects.filter(CARDHOLDER__LOGIN_id=lid).delete()
        boj = Booking.objects.get(id=boj.id)
        boj.total_amount = mytotal
        boj.save()
    return JsonResponse({'k': '0', 'status': "ok"})

def user_payment_single(request):
    lid = request.POST['lid']
    sid = request.POST['sid']
    import json
    pids = json.loads(request.POST['pids'])
    cnd = Cardholder.objects.get(LOGIN_id=lid)
    aa=Subsidydetails.objects.filter(beneficiaries=Cardholder.objects.get(LOGIN_id=lid).card_type)
    boj = Booking()
    boj.status = 'paid'
    boj.CARDHOLDER = Cardholder.objects.get(LOGIN_id=lid)
    boj.SOPKEEPER_id = sid
    boj.total_price = 0
    import datetime
    boj.date = datetime.datetime.now().date().today()
    boj.save()
    amt = 0
    for j in aa:
        if aa.exists():

            # obj=updatestock.objects.filter(id__in=pids,SHOPKEEPER_id=sid,STOCK__item_name=j.commodities.item_name)
            obj = updatestock.objects.filter(SHOPKEEPER_id=sid, STOCK__item_name=j.commodities.item_name)
            print(obj)
            # obj=updatestock.objects.filter(SHOPKEEPER__id=sid)
            for i in obj:

                qty = float(i.stock)
                if cnd.card_type == 'APL(White)' and j.quantitytype == 'percard':
                    qty = '5'
                elif cnd.card_type == 'APL(Blue)' and j.quantitytype == 'perperson':
                    qty = 2* float(cnd.members_no)
                elif cnd.card_type == 'BPL(Pink)' and i.STOCK.item_name.lower() == 'rice' and j.quantitytype == 'perperson':
                    qty = 4 * float(cnd.members_no)
                elif cnd.card_type == 'BPL(Pink)' and i.STOCK.item_name.lower() == 'wheat' and j.quantitytype == 'perperson':
                    qty = 1 * float(cnd.members_no)
                elif cnd.card_type == 'AAY(Yellow)' and i.STOCK.item_name.lower() == 'rice' and j.quantitytype == 'percard':
                    qty = '30'
                elif cnd.card_type == 'AAY(Yellow)' and i.STOCK.item_name.lower() == 'wheat' and j.quantitytype == 'percard':
                    qty = '5'
                elif cnd.card_type == 'AAY(Yellow)' and i.STOCK.item_name.lower() == 'kerosene' and j.quantitytype == 'percard':
                    qty = '0.5'

                bojs = Bookingsub()
                bojs.BOOKING=boj
                bojs.UPDATESTOCK=i
                bojs.quantity=qty
                bojs.save()
                amt+=float(j.quantity)*float(j.price)
                print(j.quantity,"fhjhj")
                print(j.price,"price")

                # l.append({'id':i.id,'date':i.date,'item_name':i.STOCK.item_name,'quantity':j.quantity,'price':j.price ,})
    boj.total_price = amt
    print(amt,"amount")
    boj.save()
    pay=Payment()
    pay.date=datetime.datetime.now()
    pay.total_price=amt
    pay.status="paid"
    pay.CARDHOLDER=Cardholder.objects.get(LOGIN_id=lid)
    pay.BOOKING=boj
    pay.save()
    return JsonResponse({'k': '0', 'status': "ok"})

def userviewtoken(request):
    sid=request.POST['sid']
    res=Token.objects.filter(SHOPKEEPER_id=sid)
    l=[]
    for i in res :
        if Token_request.objects.filter(TOKEN_id=i.id).exists():
            continue
            # return JsonResponse({'status': "no"})

        l.append({'id':i.id,'tokenno':i.token_no,'date':i.date,'fromtime':i.from_time,'totime':i.to_time,})
    print(l)
    return JsonResponse({'status':"ok",'data':l})


def userchoosetoken(request):
    lid=request.POST['lid']
    tid=request.POST['tid']
    res=Token_request.objects.filter(TOKEN_id=tid,CARDHOLDER_id=lid)
    if res.exists():
        return JsonResponse({'status':"no"})
    tr=Token_request()
    from datetime import datetime
    tr.date=datetime.now().today()
    tr.time=datetime.now().time()
    tr.CARDHOLDER=Cardholder.objects.get(LOGIN_id=lid)
    tr.TOKEN=Token.objects.get(id=tid)
    tr.save()
    return JsonResponse({'status':"ok"})

def user_viewbooking(request):
    lid=request.POST['lid']
    bu=Booking.objects.filter(CARDHOLDER__LOGIN__id=lid)
    l=[]
    for  i in bu:
        l.append({"id":i.id,
                  "date":i.date,
                  "total_price":i.total_price,
                  "rationshop_no":i.SOPKEEPER.rationshop_no,
                  "place":i.SOPKEEPER.place})
    print(l,'ab')
    return JsonResponse({'status': "ok","data":l})

def user_viewbooking_sub(request):
    bid=request.POST['bid']
    bu=Bookingsub.objects.filter(BOOKING_id=bid)
    l=[]
    for  i in bu:
        l.append({"id":i.id,"quantity":i.quantity,"item":i.UPDATESTOCK.STOCK.item_name,"price":i.UPDATESTOCK.STOCK.price})
    return JsonResponse({'status': "ok","data":l})

def user_viewpayment(request):
    lid=request.POST['lid']
    pu=Payment.objects.filter(CARDHOLDER__LOGIN_id=lid)
    l=[]
    for i in pu:
        l.append({"id":i.id,"date":i.date,'total_price':i.total_price,'status':i.status})
        print(l)
    return JsonResponse({'status': "ok","data":l})


def user_token(request):
    lid=request.POST['lid']
    pu=Token_request.objects.filter(CARDHOLDER__LOGIN_id=lid)
    l=[]
    for i in pu:
        l.append({"id":i.id,"date":i.date,'fromtime':i.TOKEN.from_time,'totime':i.TOKEN.to_time,'tokenno':i.TOKEN.token_no})
        print(l)
    return JsonResponse({'status': "ok","data":l})



def canceltoken(request):
    id=request.POST['id']
    res=Token_request.objects.get(id=id).delete()
    return JsonResponse({'status': "ok"})
