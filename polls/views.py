from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
from django.views import generic

from .forms import ContactForm



from django.template import loader


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


#def index(request):
 #   latest_question_list = Question.objects.order_by("-pub_date")[:5]
 #   context = {"latest_question_list": latest_question_list, "text": "Mon text"}
  #  return render(request, "polls/index.html", context)


# ------ AUtre technique ------------
#def index(request):
 #   latest_question_list = Question.objects.order_by("-pub_date")[:5]
  #  template = loader.get_template("polls/index.html")
   # context = {
    #    "latest_question_list": latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))


#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, "polls/detail.html", {"question": question})






#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))





def building(request, building_id):
    return HttpResponse("You're looking at building %s." % PricingDBBuilding.objects[building_id].name)    



















import openai
import time
import logging
from datetime import datetime



# gets API Key from environment variable OPENAI_API_KEY
client = openai.OpenAI()

assistant_id = "asst_Nb0en4wEzKNTTpzF9cyioeZN"
thread_id = "thread_fMwcWOBRQPYum3UUyOOYtrcM"
vs_id = "vs_YUuSw6fikktYVFeoDjTcIVOc"










def contact(request):
    form = ContactForm()
    txt = []
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form. is_valid():
            querr =  form.cleaned_data['message']
            message = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=querr,
            )
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread_id, assistant_id=assistant_id
            )
            messages = list(client.beta.threads.messages.list(thread_id=thread_id, run_id=run.id))
            message_content = messages[0].content[0].text

            newtext =f"\n{message_content.value}\n\n"


            
            txt.append(newtext)
    
    context = {'form':form, 'text':txt}
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #context = {"latest_question_list": latest_question_list}
    return render(request,"polls/form.html", context)
    #return render(request, "polls/index.html", context)




