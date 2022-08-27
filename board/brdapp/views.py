from django.shortcuts import HttpResponseRedirect, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, UserResponse, OneTimeCode
from .forms import AdForm, UserForm, OneTimeForm, ResponseForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.core.mail import send_mail

from .filters import PostFilter

from django.contrib.auth.models import User


def register_view(request):
    form = BaseRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        a = OneTimeCode.objects.create(code=''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10)), user=user)
        send_mail(
            subject="Registration Code",
            message=f"Greetings, {username}\n"
                    f"Your registration code: {a.code}\n",
            from_email='',
            recipient_list=[email])
        return redirect('/accounts/register/otc/')
    else:
        form = BaseRegisterForm
    return render(request, 'registration/register.html', {'form': form})


class BoardList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'board.html'
    context_object_name = 'board'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

# @login_required
# def add_response(request, pk):
#     responser = request.user
#     responser.save()
#     response_to = Post.objects.get(id=pk)
#     response_to.responsers.add(responser)
#
#     return redirect('board/')


class AdCreate(PermissionRequiredMixin, CreateView):
    form_class = AdForm
    model = Post
    template_name = 'ad_create.html'
    permission_required = ('brdapp.add_post')
    sucess_url = 'board/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class AdUpdate(PermissionRequiredMixin, UpdateView):
    form_class = AdForm
    model = Post
    template_name = 'ad_edit.html'
    permission_required = ('brdapp.change_post')
    sucess_url = 'board/'
    queryset = Post.objects.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404('Permission denied')
        return obj

class AdDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('board')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404('Permission denied')
        return obj

class AdDetail(DetailView):
    model = Post
    template_name = 'ad_detail.html'
    context_object_name = 'ad_detail'

class MyResponse(LoginRequiredMixin, CreateView):
    model = UserResponse
    form = ResponseForm
    fields = ['text',]
    template_name = 'responses.html'
    success_url = 'board/'
    context_object_name = 'responses'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.article = self.kwargs.get('pk')
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

        def get_success_url(self, **kwargs):
            return reverse('ad_detail', kwargs={'pk': self.kwargs.get('pk')})









