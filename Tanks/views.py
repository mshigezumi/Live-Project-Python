from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TankForm, NamesForm, IDForm
from .models import Tank
import requests
import json
from bs4 import BeautifulSoup
from .extract import json_extract

def tanksHome(request):
    return render(request, 'tanks/home.html')

def tanksGallery(request):
    return render(request, 'tanks/gallery.html')

def tanksVideos(request):
    return render(request, 'tanks/videos.html')

def tanksContact(request):
    return render(request, 'tanks/contact.html')

def tanksAdmin(request):
    tanks = Tank.objects.all()
    return render(request, 'tanks/admin.html', {'tanks': tanks})

def tanksCreate(request):
    form = TankForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tanksAdmin')
    else:
        print(form.errors)
        form = TankForm()
    return render(request, 'tanks/createRecord.html', {'form': form})

def tanksList(request):
    tanks = Tank.objects.all()
    namesForm = NamesForm(request.POST or None) # need to save? print errors?
    idForm = IDForm(request.POST or None) # need to save? print errors?
    return render(request, 'tanks/list.html', {'tanks': tanks, 'namesForm': namesForm, 'idForm': idForm})
    # tanksList = []
    # for tank in tanks:
    #     tanksList.append(tank.name)
    #     tanksList.append(['Country: ' + tank.country, 'Generation: ' + tank.generation, 'Year: ' + str(tank.year)])
    # return render(request, 'tanks/tanksList.html', {'tanksList': tanksList})

def tanksDetails(request, pk):
    pk = int(pk)
    tank = get_object_or_404(Tank, pk=pk)
    return render(request, 'tanks/details.html', {"tank": tank})

def tanksEdit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Tank, pk=pk)
    form = TankForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('tanksAdmin')
        else:
            print(form.errors)
    else:
        return render(request, 'tanks/edit.html', {'form': form})

def tanksDelete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Tank, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('tanksAdmin')
    return render(request, 'tanks/confirmDelete.html', {"item": item})

def tanksConfirm(request): # this confirms deletion
    if request.method == 'POST':
        form = TankForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('tanksAdmin')
    else:
        return redirect('tanksAdmin')

def tanksAPI(request):
    if request.method == "POST":
        name = request.POST['name'] # gets the name attribute from the namesForm that is passed through list
        response = requests.get('http://vmdbpedia.informatik.uni-leipzig.de:8080/api/1.0.0/values?entities='+ name +'&property=dbo%3Aabstract&format=JSON&pretty=NONE&limit=100&offset=0&key=1234&oldVersion=false')
        inputJson = response.json()
        with open('Tanks/data.txt', 'w') as outfile:
            json.dump(inputJson, outfile) # writes json response into data.txt, looking to get the values labeled under 'value' with the 'xml:lang' of 'en'
        values = json_extract(inputJson, 'value') # extracts values labeled with 'value' into a list
        abstract = values[1::2] # get even index values to filter the correct 'value' fields (the ones with the abstract in it)
        lang = json_extract(inputJson, 'xml:lang') # extracts values labeled with 'xml:lang' into a list
        zipDict = dict(zip(lang, abstract)) # combines two lists into a dictionary
        print(zipDict)
        if response:
            return render(request, 'tanks/API.html', {"data": zipDict['en']}) # returns the value with the key 'en' (english)
        else:
            return render(request, 'tanks/API.html', {"data": response.status_code}) # 400 if it doesn't work
    else:
        return redirect('tanksList')

def tanksSoup(request):
    if request.method == "POST":
        id = request.POST['id'] # gets the id attribute from the idForm that is passed through list
        response = requests.get('https://www.militaryfactory.com/armor/detail.asp?armor_id=' + id)
        soup = BeautifulSoup(response.content, 'html.parser') # passes response through beautifulsoup
        content = soup.find_all('span', class_='textLarge') # finds all the span tags with the class textLarge, puts them into a list
        # would need for loop here if I wanted multiple content items printed
        text = content[0].get_text() # content[0] is the span I want to get the text from
        # print(list(content[0].stripped_strings))
        print(text)
        if response:
            return render(request, 'tanks/soup.html', {"soup": text}) # returns the extracted text
        else:
            return render(request, 'tanks/soup.html', {"soup": response.status_code})  # 400 if it doesn't work
    else:
        return redirect('tanksList')