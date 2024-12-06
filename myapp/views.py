from django.shortcuts import render
from django.shortcuts import redirect
from myapp.models import FAQ
from myapp.models import laws
from myapp.models import university
from myapp.models import current_issue
from myapp.models import news
from myapp.models import energy
from myapp.models import health
from myapp.models import technology
from myapp.models import userRegister
from django.conf import settings
from django.core.mail import send_mail


def about(request):
	return render(request,'about.html')
def contactus (request):
	return render(request,'contactus.html')
def footer (request):
	return render(request,'footer.html')
def gallery (request):
    return render(request,'gallery.html')
def header (request):
    return render(request,'header.html')
def index (request):
    return render(request,'index.html')
def base(request):
	return render(request,'base.html')
def all_current_issue(request):
	x=current_issue.objects.all()
	return render(request,'all current issue.html',{'data':x})
def details_current_issue(request,id):
	x=current_issue.objects.get(id=id)
	return render(request,'details current issue.html',{'i':x})
def all_news(request):
	x=news.objects.all()
	return render(request,'all news.html',{'data':x})
def details_news(request,id):
	x=news.objects.get(id=id)
	return render(request,'details news.html',{'i':x})
def all_faq(request):
	x=FAQ.objects.all()
	return render(request,'all faq.html',{'data':x})
def all_laws(request):
	x=laws.objects.all()
	return render(request,'all laws.html',{'data':x})
def all_university(request):
	x=university.objects.all()
	return render(request,'all university.html',{'data':x})
def details_university(request,id):
	x=university.objects.get(id=id)
	return render(request,'details university.html',{'i':x})	
def register(request):
	if request.method=="POST":
		x=userRegister()
		x.first_name=request.POST.get('fn')
		x.last_name=request.POST.get('ln')
		x.phone=request.POST.get('ph')
		x.Email=request.POST.get('em')
		x.Password=request.POST.get('pw')

		x.save()
		print("data succ")
		return render(request,'Register.html',{'msg':"User successfully Register"})
	else:
		return render(request,'Register.html')
def login(request):
	if request.method=='POST':
		formpost=True
		us=request.POST.get('em')
		pw=request.POST.get('pw')
		errormessage=""
		expert = userRegister.objects.filter(Email = us , Password = pw)
		k=len(expert)
		if k>0:
			print(" valid credentials ")
			request.session['email'] = us

			return redirect('/myprofile')

		else:

			print("invalid credentials ")
			errormessage="invalid credentials"
			return render(request,'login.html',{'msg':"Invalid candidate"})
	else:
		print("else")
		return render(request,'login.html',)

def allenergy(request):
	x=energy.objects.all()
	return render(request,'all energy.html',{'data':x})
def allhealth(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	x=health.objects.all()
	return render(request,'all health.html',{'data':x})
def detailhealth(request,id):
	x=health.objects.get(id=id)
	return render(request,'detailhealth.html',{'i':x})
def alltechnology(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	x=technology.objects.all()
	return render(request,'all technology.html',{'data':x})	
def detailtechnology(request,id):
	x=technology.objects.get(id=id)
	return render(request,'detailtech.html',{'i':x})	

def myprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	Userdetail=userRegister.objects.get(Email=request.session['email'])
	return render(request,'myprofile.html',{'user':Userdetail})

def Edit_profile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	Userdetail=userRegister.objects.get(Email=request.session['email'])
	if request.method=='POST':
		detail=userRegister.objects.get(Email=request.session['email'])
		detail.first_name = request.POST.get('fn')
		detail.last_name = request.POST.get('ln')
		detail.phone = request.POST.get('ph')
		detail.Address = request.POST.get('add')
		detail.DOB = request.POST.get('dob')

		detail.save()
		data=userRegister.objects.get(Email=request.session['email'])
		return redirect('/myprofile',{'i':data})
	else:
		return render(request,'Edit profile.html',{'i':Userdetail})


	

def change_password(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		re=userRegister.objects.get(Email=request.session['email'])
		Opassword=request.POST.get('O')
		Npassword=request.POST.get('N')
		Rpassword=request.POST.get('R')
		print(Opassword,Npassword,Rpassword)
		if(Npassword==Rpassword):
			pa=re.Password
			print(pa)
			if(Opassword==pa):

				re.Password=Npassword
				re.Confirm_password=Npassword
				re.save()
				rest="Password Changed"
				return render(request,'change password.html',{'rest':rest})
			else:
				res="Invalid Current Password"
				return render(request,'change password.html',{'res':res})
		else:
			res="Confirm password and new password don't match"
			return render(request,'change password.html',{'res':res})
	else:
		return render(request,'change password.html')
def help_support(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
	  x=myhelp()
	  x.name=request.POST.get('tl')
	  x.name=request.POST.get('mg')
	  x.save()
	  print("data succ")
	  return render(request,'help&support.html')
	else:
		return render(request,'help&support.html')
def review(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=myrev()
		x.name=request.POST.get('tl')
		x.name=request.POST.get('mg')
		x.save()
		print("data succ")
		return render(request,'review.html')
	else:
		return render(request,'review.html')
def side(request):
	return render(request,'side.html')

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	del request.session['Email']
	return redirect('/login')

def forgotpassword(request):
	if (request.method=='POST'):
		em=request.POST.get('em')
		user=userRegister.objects.filter(Email=em)
		if(len(user)>0):
			pw=user[0].Password
			subject="Password"
			message="Welcome!Your Passwpord is "+pw
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[em]
			send_mail(subject,message,email_from,recipient_list)
			rest='Your Password sent to your respective Email Account.Please Check'
			return render(request,'forgotpassword.html',{'rest':rest})
		else:
			res='This Email Id Is Not Registered'
			return render(request,'forgotpassword.html',{'res':res})
	else:

			return render(request,'forgotpassword.html')


		


