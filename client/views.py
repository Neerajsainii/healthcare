from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from .models import UserSignup, Admin, Doctor, MedicalPractitioner
import random,string
def signup(request):
    if request.method == 'POST':
        user_data = {
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'age': request.POST.get('age'),
            'gender': request.POST.get('gender'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'repassword': request.POST.get('repassword'),
            'user_type': request.POST.get('user_type'),  # Add a field to determine user type
        }
        if UserSignup.objects.filter(email=user_data['email']).exists():
            return HttpResponse('User with this email already exists. Please choose a different one.')

        if user_data['password'] != user_data['repassword']:
            return HttpResponse('Passwords do not match. Please try again.')

        hashed_password = make_password(user_data['password'])

        # Create user based on user type
        if user_data['user_type'] == 'admin':
            user = Admin(
                firstname=user_data['firstname'],
                lastname=user_data['lastname'],
                age=user_data['age'],
                gender=user_data['gender'],
                email=user_data['email'],
                password=hashed_password,
                AdminId=generate_random_password(user_data['firstname'])
                 
            )
        elif user_data['user_type'] == 'doctor':
            user = Doctor(
                firstname=user_data['firstname'],
                lastname=user_data['lastname'],
                age=user_data['age'],
                gender=user_data['gender'],
                email=user_data['email'],
                password=hashed_password,
                DocId=generate_random_password(user_data['firstname'])
            )
        elif user_data['user_type'] == 'medical_practitioner':
            user = MedicalPractitioner(
                firstname=user_data['firstname'],
                lastname=user_data['lastname'],
                age=user_data['age'],
                gender=user_data['gender'],
                email=user_data['email'],
                password=hashed_password,
                MedId=generate_random_password(user_data['firstname'])
            )
        else:
            return HttpResponse('Invalid user type.')

        user.save()
        print('User signed up successfully!')

        return redirect('whome') 

    return render(request, 'signup.html')

def generate_random_password(username):
    # Generate the user's name part
    if len(username)>=5:
        user_part = username[:5]
        random_part = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=3))
    else:
        user_part = username[:len(username)]
        random_part = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=(8-len(username))))

   
    password = user_part + random_part
    return password
class AdminLoginView(View):
    def get(self, request):
        return render(request, 'admin_login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user and user.is_admin:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

class DoctorLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user and user.is_doctor:
            login(request, user)
            return redirect('doctor_dashboard')  # Redirect to doctor dashboard
        else:
            return render(request, 'doctor_login.html', {'error': 'Invalid credentials'})

class MedicalPractitionerLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user and user.is_medical_practitioner:
            login(request, user)
            return redirect('medical_practitioner_dashboard')  # Redirect to medical practitioner dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact object
        contact = Contact.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )
        
        # Optionally, you can perform additional validations here
        
        # Save the Contact object
        contact.save()

        return redirect('whome')  # Redirect to the same page after form submission
    
    return render(request, 'contact.html')

def home(request):
    return render(request,'index.html')
