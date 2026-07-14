from django.shortcuts import render
from .models import Contact
# Create your views here.
def contact(request):
    subjects=["html","css","js","react","mysql"]
    name=""
    age=""
    if request.method=="POST":
        name=request.POST.get("S_name")
        age=request.POST.get("age")
        if name:
            name=name.upper()
            #Save data into the database
        if name and age:
            Contact.objects.create(
                name=name,
                age=age
            )
            #Fetch all records from the database
            contacts=Contact.objects.all()
            print(contacts)
    data= {
        "name":name,
        "age":age,
        "course":"Python",
        "subject":subjects,
        "contacts":contacts
    }
    return render(request , "contact.html",data)