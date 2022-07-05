from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse
from django.views import generic

from questions.models import Test, Questions, Answer


class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'list_tests'

    def get_queryset(self):
        return Test.objects.order_by('-date_test')


def QuestionView(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Questions.objects.filter(test_num=test.id)
    try:
        answer = get_object_or_404(Answer, pk=request.POST['answer'])
        answer.votes += 1
        answer.save()
        print(answer.votes)
    except:
        print(request.POST)
    return render(request, 'questions/questions.html', {'questions': questions, 'test': test})


class AnswerView(generic.DetailView):
    model = Answer
    template_name = 'questions/answers.html'
    context_object_name = 'answers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Questions.objects.filter(id=self.kwargs['pk'])[0]
        return context


def TestsResults(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions_set.all()
    return render(request, 'questions/results.html', {'questions': questions, 'test': test})
