from django.shortcuts import render
from .forms import QuestionForm

# Create your views here.
def questions_list(request):
    if request.method == "POST":
        print(request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionForm()
    
    return render(request, 'questions/questions.html',{'form': form})
