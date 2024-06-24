from django.shortcuts import render,redirect
from django.views.generic import DetailView
from library.models import Book,Borrow
from library.forms import CommentForm

# Create your views here.
class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'
    context_object_name = 'book'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        book = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.save()
            return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        comments = book.comments.all()
        comment_form = CommentForm()
        is_= Borrow.objects.filter(bookId=book.id, userId=self.request.user.id)
        print(is_)

        context['comments'] = comments
        context['comment_form'] = comment_form
        # context['is_borrowed'] = flag
        return context



    
def BookBorrowView(request, id):
    # print('hello')
    borrow = Borrow.objects.create(bookId=id, userId=request.user.id)
    borrow.save() 

    return redirect('book_details', id)
        
