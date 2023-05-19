from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from polls.models import Question

from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


@swagger_auto_schema(
    methods=["post"],
    responses={
        status.HTTP_201_CREATED: 'OK',
        status.HTTP_400_BAD_REQUEST: "Bad request, incorrect fields.",
    },
    manual_parameters=[],
)
@api_view(["POST"])
@permission_classes([HasAPIKey])
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return Http404('Question not found')
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
