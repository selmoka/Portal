from django.shortcuts import get_object_or_404, redirect, render
# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from django.db.models import Q
from .models import Event, Person, PersonStatus

def index(request):
	return render(request, 'portal/index.html')


def add_person_data(request):
    # if request.method == 'POST':
        # ...
        # return redirect('portal:index')
            #     <p>First Name <input type="text" name="first_name" id="first_name"></p>
            # <p>Last Name <input type="text" name="last_name" id="last_name"></p>
            # <p>Other Name <input type="text" name="other_name" id="other_name"></p>
            # status
            # <p>ID Number <input type="text" name="id_number" id="id_number"></p>
            # <p>Mobile <input type="text" name="mobile" id="mobile"></p>
            # <p>Email <input type="text" name="email" id="email"></p>
            # <p>Description <input type="text" name="description" id="description"></p>
            # <input type="submit" value="Add">
    
    try:
        print('here')
        print(request.POST['first_name'])
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        other_name = request.POST['other_name']
        id_number = request.POST['id_number']
        mobile = request.POST['mobile']
        email = request.POST['email']
        description = request.POST['description']
        events = Event.objects.all()
        # print(events[0].id)
        # print(events[0].name)
        # print(events)
        e = Event.objects.get(name='fire_sale')
        statusall = PersonStatus.objects.all()
        print(statusall[0].id)
        print(statusall[0].name)
        print(statusall)
        s = PersonStatus.objects.get(pk=request.POST['status'])
        p = Person(first_name=first_name, last_name=last_name, other_name=other_name, 
        id_number=id_number, mobile=mobile, email=email, description=description,
        event=e, status=s)
        print(p)
        p.save()
        return render(request, 'portal/add_person.html', 
            {'message': "You have saved the rental!", 'type_message':'success'})
    except:
        return render(request, 'portal/add_person.html', 
            {'message': "Please type a value!", 'type_message':'error'})
    

def add_person(request):
    # if request.method == 'POST':
        # ...
        # return redirect('portal:index')
    return render(request, 'portal/add_person.html')

def show_person(request, person_id):
    # 
    # try:
    #     # print(rental_id)
    #     person = Person.objects.get(pk=person_id)
    #     return render(request, 'person_details.html', {'person': person})
    # # print(rental_id)
    # except:
    #     rentals_withreturn = Rental.objects.all().exclude(return_date=None).order_by('-rental_date')
    #     rentals_noreturn = Rental.objects.all().filter(return_date=None).order_by('-rental_date')
    #     # print(rentals_withreturn)
    #     # print(rentals_noreturn)
    #     return render(request,'rentals.html', {'rentals_withreturn': rentals_withreturn, 
    #         'rentals_noreturn': rentals_noreturn})
    # try:
    print(person_id)
    person = Person.objects.get(pk=person_id)
    print(person)
    print(person_id)
    return render(request, 'portal/person_details.html', {'person': person})
    # except:
        # return render(request, 'portal/person_show_error.html')
    


def show_safe_persons(request):
    person_status = PersonStatus.objects.get(name='safe')
    persons = Person.objects.all().filter(status=person_status) 
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })


def search_results(request):
    context = None
    if request.method != 'POST':
        return redirect('portal:index')

    text = request.POST.get('search', '').strip()
    results = Person.objects.filter(
         Q(first_name__icontains=text) |
         Q(last_name__icontains=text) |
         Q(other_name__icontains=text) |
         Q(description__icontains=text))
    return render(request, 'portal/show_results_search.html', {
            'title': 'Search Results',
            'main_heading': 'Search Results',
            'results': results
        })
