from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UserUpdateForm,AddProfilePicForm

# Create your views here.

# View for SignUp

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data= request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registered':registered}
    return render(request,'login/signup.html',context = dict)

# View for login


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))


    return render(request,'login/login.html',context={'form':form})

# View for logout

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# View for profile veiw


@login_required
def profile(request):
    return render(request,'login/profile.html',context={})

# View for profile_updation


@login_required
def user_info_update(request):
    current_user = request.user
    form = UserUpdateForm(instance =current_user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))



    return render(request,'login/user_update.html',context={'form':form})

# View for password PasswordChangeForm


@login_required
def password_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data = request.POST)
        if form.is_valid():
            form.save()
            changed =True

    return render(request,'login/password_change.html',context={'form':form,'changed':changed})

@login_required
def add_profile_pic(request):
    current_user = request.user
    form = AddProfilePicForm()
    if request.method == 'POST':
        form =  AddProfilePicForm( request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit = False)
            user_obj.user = current_user
            user_obj.save()
            return HttpResponseRedirect(reverse('login:profile'))

    return render(request,'login/pro_pic_add.html',context={'form':form})



@login_required
def change_profile_pic(request):
    form = AddProfilePicForm(instance = request.user.user_profile)
    if request.method == 'POST':
        form =  AddProfilePicForm( request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:profile'))

    return render(request,'login/pro_pic_change.html',context={'form':form})
