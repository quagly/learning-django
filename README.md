# Django tutorial

using Django version 1 because I need to learn how to migrate to version 2

This tutorial is complete for Django 1.  It is follows the tutorial with the addtion of comments

* using Django 1.11
* using Python 3.7.0

Useful links for Django 1.11
* [tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
* [django-admin](https://docs.djangoproject.com/en/1.11/ref/django-admin/)
* [settings](https://docs.djangoproject.com/en/1.11/topics/settings/)
* [url dispatcher](https://docs.djangoproject.com/en/1.11/topics/http/urls/)
* [deployment checklist](https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/)





# Django notes


[TOC]



# Django notes looking but not running John's code

To quick start this project we will start with the Django demo code John Appert created.  This code may be found in John's [private repository on github](https://github.com/jjapp/standvastHMS/)

From the [requirements.txt](https://github.com/jjapp/standvastHMS/blob/master/requirements.txt) this code using Django 1.11.3.  According to the [Django project download page ](https://www.djangoproject.com/download/)and the [FAQ ](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django)



*   Django 1.11 ended 'mainstream support' on December 2, 2017
*   Django 1.11 'extended support' ends April 2020 - no security patches after that
*   1.11.20 is the current version of Django 1
*   Django [does not using connection](https://docs.djangoproject.com/en/2.1/ref/databases/#persistent-database-connections) pooling by default
*   Django recommends python 3 for performance
*   Python 2 is [end-of-life](https://pythonclock.org/) Jan 1, 2020
*   Django 2 is [not backward compatible](https://docs.djangoproject.com/en/2.1/releases/2.0/#backwards-incompatible-2-0)
*   Many [python modules and projects are committed](https://python3statement.org/) to dropping support for python 2 in 2020

Actions to consider for John's code



*   Run John's demo app
*   Review functionality and workflow
*   Upgrade to most recent Django 1.11 to include security patches
*   Use python 3
*   Create tests
*   Create source code repository for app
*   Evaluate level of effort to upgrade to Django 2
*   Run ``manage.py check` `on project
*   Add [test coverage](https://docs.djangoproject.com/en/1.11/topics/testing/advanced/#topics-testing-code-coverage) report
*   Evaluate code for [race conditions](https://docs.djangoproject.com/en/1.11/ref/models/expressions/#avoiding-race-conditions-using-f)?
*   Evaluate code for [Cross Site Request Forgeries protection](https://docs.djangoproject.com/en/1.11/ref/csrf/)
*   Use postgresql database
    *   Django need create database permissions to run tests
*   Evaluate and select platform to run on
*   Identity management integration
*   For more complex views consider [class based views ](https://docs.djangoproject.com/en/1.11/topics/class-based-views/intro/)


# Django tutorial

[Tutorial for Django 1.1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) since John's code is 1.1

Completed tutorial is in [mike's public github](https://github.com/quagly/learning-django)

Tutorial creates a "polls" application


## Steps to run

Install[ Django](https://docs.djangoproject.com/en/1.11/intro/install/)

In mysite directory run

	`./manage.py runserver`

Go to [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/).  This presents a list of questions.  Just one question in the tutorial.

Click on a question to vote

Display vote totals


## Anatomy of an Django request

What happens when a browser goes to [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/)?



1. [mysite/urls.py](https://github.com/quagly/learning-django/blob/master/mysite/mysite/urls.py) to resolve urls

    Says to look at polls.urls for urls matching regex ^polls/


    ```
    url(r'^polls/', include('polls.urls'))

    ```


2.  [polls/urls.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/urls.py) to resolve polls application urls

use  views.IndexView when matching ^$


```
url(r'^$', views.IndexView.as_view(), name='index')
```


3. [polls/views.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/views.py)

IndexView is a generic list


```
class IndexView(generic.ListView)
```


View uses the polls/index.html template


```
template_name = 'polls/index.html'
```


Template context calls this data latest_question_list


```
context_object_name = 'latest_question_list'
```


Model is last 5 published queries


<table>
  <tr>
   <td><code>return Question.objects.filter(</code>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><code>pub_date__lte=timezone.now()</code>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><code>).order_by('-pub_date')[:5]</code>
   </td>
  </tr>
</table>



## Two tracks, model and view


### Model

[polls/model.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/models.py)

Question is a model


```
class Question(models.Model)
```


Defines two fields


```
question_text
pub_date
```


Comes from database table


```
sqlite3 db.sqlite3 "select * from polls_question"

1|What's up?|2019-03-07 18:59:15
```



### View


```
template_name = 'polls/index.html'
```


Resolve view

[mysite/settings.py ](https://github.com/quagly/learning-django/blob/master/mysite/mysite/settings.py)

Look for templates in ${APP}/templates


```
'DIRS': [os.path.join(BASE_DIR, 'templates')]
```


Which resolves to best practice location

[polls/templates/polls/index.html](https://github.com/quagly/learning-django/blob/master/mysite/polls/templates/polls/index.html)



**Static Section**


<table>
  <tr>
   <td><code>{% load static %}</code>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><code><link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" /></code>
   </td>
  </tr>
</table>


Located at


```
static 'polls/style.css'
```


Using Django defaults resolves to

[polls/static/polls/style.css](https://github.com/quagly/learning-django/blob/master/mysite/polls/static/polls/style.css)



References image


```
"images/background.gif"
```


Using Django defaults resolves to

[polls/static/polls/images/background.gif](https://github.com/quagly/learning-django/blob/master/mysite/polls/static/polls/images/background.gif)

**Dynamic Section**

Get the question list from latest_question_list context.  Loop through the latest_question_list.  Get the question text from the 'detail' view.


<table>
  <tr>
   <td><strong><code>{% if latest_question_list %}</code></strong>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>   <ul></code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>   {% for question in latest_question_list %}</code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>       <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li></code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>   {% endfor %}</code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>   </ul></code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>{% else %}</code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>   <p>No polls are available.</p></code></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><strong><code>{% endif %}</code></strong>
   </td>
  </tr>
</table>


What gets displayed is from


```
url 'polls:detail' question.id
```


Where is this?  Resolve


```
url 'polls:detail'
```


This says to resolve the detail url of the polls application.

[polls/urls.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/urls.py)


```
url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
```


 The detail view is just /polls/{question PK}.  We can look at question 1 at this url

[http://127.0.0.1:8000/polls/1/](http://127.0.0.1:8000/polls/1/)

The DetailView is defined in [polls/views.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/views.py) as a generic.DetailView


```
class DetailView(generic.DetailView):
```


A DetailView takes a primary key and returns detail from foreign key relationships

The Index page does not display detail choices for a question, just the question text.  By referencing polls:detail we ensure that question text are only display if they have choices.

Looking again at [polls/models.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/models.py)

We find choices with a foreign key to questions


<table>
  <tr>
   <td><code>class Choice(models.Model):</code>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><code>   question = models.ForeignKey(Question, on_delete=models.CASCADE)</code>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><code>   choice_text = models.CharField(max_length=200)</code>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td><code>   votes = models.IntegerField(default=0)</code>
   </td>
  </tr>
</table>



```
sqlite3 db.sqlite3 "select * from polls_choice"
```


1|Not much|2|1

2|The sky|5|1


```
sqlite3 db.sqlite3 ".schema polls_choice"
CREATE TABLE IF NOT EXISTS "polls_choice"
("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
, "choice_text" varchar(200) NOT NULL
, "votes" integer NOT NULL
, "question_id" integer NOT NULL REFERENCES "polls_question" ("id"));
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
```


Return last five published question text for questions with choices published in the past and render with the view formatting and background image.

http://127.0.0.1:8000/polls/


## Test

Django has its own test framework that is based on the standard unittest module  It creates, populates, and destroys a test database. This works well for testing application logic, but does not test browser/user interaction.

[polls/tests.py](https://github.com/quagly/learning-django/blob/master/mysite/polls/tests.py)

[Django Testing doc](https://docs.djangoproject.com/en/1.11/topics/testing/overview/)


```
./manage.py test polls

