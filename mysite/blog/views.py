from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# class RegisterUser(CreateView):
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items()) + list(c_def.items()))
