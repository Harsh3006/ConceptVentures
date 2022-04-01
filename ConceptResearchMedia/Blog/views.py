from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import BlogPost, BlogCategory
from meta.views import Meta

class BlogListView(ListView):
    model = BlogPost
    template_name = 'ConceptResearchMedia/blog/blog-home.html'
    ordering = ['-created_on', '-modified_on']
    paginate_by = 18
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meta"] = Meta(
                use_og=True,
                use_facebook=True,
                og_title='Blog',
                description='Read our latest articles and reports, with expert perspectives, proprietary data, and thought-provoking insights.',
                url='', 
                image='',
                object_type='website')
        context["categories"] = BlogCategory.objects.all()
        return context

class BlogDetailView(DetailView):
    login_required = True
    model = BlogPost
    context_object_name = 'post'
    template_name = 'ConceptResearchMedia/blog/blog-post.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_blog_post"] = BlogPost.get_related_blog_post(self.object)
        return context      
    
def CategoryView(request, category):
    if (BlogCategory.objects.filter(name=category).exists()):
        category_id =  BlogCategory.objects.only('id').get(name=category).id
        category_posts = BlogPost.objects.filter(category=category_id)
        return render(request, 'ConceptResearchMedia/blog/category.html', {'category_posts': category_posts})
    else:
        # retrun http404 here to show not found page
        return redirect('blog')


    