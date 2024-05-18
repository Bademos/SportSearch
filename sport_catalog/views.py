from django.shortcuts import render
from .models import SportUser, SportType,  ProcessingStatus, Event, Review, Complaint,Application, UsersSportTypes

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import login_required


from .forms import  UserRegistrationForm, ProfileEditForm, UserEditForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def index(request):

# Create your views here.
    return render(request, 'index.html')

class EventDetailedView(generic.DetailView):
    model = Event

class SportuserDetailedView(generic.DetailView):
    model = SportUser

class ReviewDetailedView(generic.DetailView):
    model = Review

class ComplaintsDetailedView(generic.DetailView):
    model = Complaint


class AllEventsListView(generic.ListView):
    model = Event

class AllReviewsListView(generic.ListView):
    model = Review
class AllSportUsers(generic.ListView):
    model = SportUser
    template_name ='sport_catalog/sportsmen_list.html' 
    def get_queryset(self):
        return SportUser.objects.filter(isSportsMen=True)
    
class AllManagerUsers(generic.ListView):
    model = SportUser
    template_name ='sport_catalog/manager_list.html' 
    def get_queryset(self):
        return SportUser.objects.filter(isManager=True)

class EventsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing events to current user.
    """
    model = Event
    template_name ='sport_catalog/event_list_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(manager=self.request.user).order_by('date')
    
class ComplaintsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing events to current user.
    """
    model = Complaint
    template_name ='sport_catalog/complaint_list_by_user.html'
    paginate_by = 10

   
    def get_queryset(self):
        print("+++++++++++++++++++++++++++++++++++++")

        su = SportUser.objects.filter(user= self.request.user)[0]

        print(su)
        print("+++++++++++++++++++++++++++++++++++++")


        hu = Review.objects.filter(sender = su)
        print(hu)

        print("+++++++++++++++++++++++++++++++++++++")
        #print(Complaint.objects.filter(review in hu))
        return Complaint.objects.filter(review = hu[0])
    
class ReviewsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing events to current user.
    """
    model = Review
    template_name ='sport_catalog/review_list_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        su = SportUser.objects.filter(user= self.request.user)
        return Review.objects.filter(sender= su[0])

def test(request):
    #projects = Project.objects.all()
  
    context = {}
    return render(request, 'index.html', context)
    



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])


            # Save the User object
            new_user.save()
            profile = SportUser.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.SportUser, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.sportuser)
        return render(request,
                      'registration/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
    

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    #initial={'date_of_death':'12/10/2016',}

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(DeleteView):
    model = Event
    #success_url = reverse_lazy('authors')


class ReviewCreate(CreateView):
    model = Review
    fields = '__all__'
    #initial={'date_of_death':'12/10/2016',}

class ReviewUpdate(UpdateView):
    model = Review
    fields = '__all__'

class ReviewDelete(DeleteView):
    model = Review
    #success_url = reverse_lazy('authors')