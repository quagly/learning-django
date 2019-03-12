from django.shortcuts import  get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question

# last 5 questions
# using render does not require loader import
# since it knows how to work with templates

class IndexView(generic.ListView):
    # generic.ListView will display list of objects
    # uses default template <app name>/<model name>_list.html
    # unless specified here
    template_name = 'polls/index.html'
    # default context_object_name is question_list
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# because this code is so common Django offers generic
# to simplify this common case
# def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})
class DetailView(generic.DetailView):
    # generic.DetailView will display detail for an object
    model = Question
    # generic.DetailView default template name is <app name>/<model name>_detail.html.
    # we want a different appearance for our DetailView and ResultsView so we give them
    # different templates
    # if not using that, then set here
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# no generic for custom code like this
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
