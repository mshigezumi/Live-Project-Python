# Live Project
 
## Introduction:

For the last two weeks with the Tech Academy, I worked on a Live Project in Python which simulated a real-world work environment in which I worked with my peers and staff to do work on a website, in this project we each worked on our own personal section of our choosing. We used Django with an MVC pattern in the create the website, sqlite3 was used as a database, and Beautiful Soup 4 was used for web scraping. My section is dedicated to modern tanks of the world, which is a successor to previous websites I made while learning HTML, CSS, and Javascript. Below are some code snippets of the stories I worked on, full code files are also available in this repository.

## Pages and Stories:

### Django .py files
These files contain all the python used in this project with views.py, models.py, forms.py, and url.py being the most used files. These were worked on throughout the live project and edited as needed for each story.

### Homepage
The homepage was worked on over time and is still not in a state competely to my liking, however this page wasn't the focus of the project so it's mainly there for the functionality.

### Admin
The admin page was made with the ability to select an entry to edit or create a new one. This was done over a couple of stories.

### Edit
The edit page contains a form as a table to edit an existing details page of a tank. This page also has the button to delete an entry.

### Delete
The delete page is a confirmation that the user wants to delete the selected entry. If accepeted a POST request is sent to delete the entry.

### List
The list page was created and improved over a few stories, it contains the majority of the functionality created during the live project. It shows a list of the tanks which are in the database with some basic information and sorting functionality provided by sorttable.js. Each entry has a link to the individual details page of the tank. This page also has the selection menu to use the API and web scraping functions, these can be easily moved to a more intuitive or convenient location.

~~~
{% extends "tanks/base.html" %}

{% block title %}Modern Tanks of the World List{% endblock %}

{% block header %}List{% endblock %}

{% block content %}

<table class="sortable">
    <tr class="sticky-row">
        <th>Name:</th>
        <th>Country:</th>
        <th>Generation:</th>
        <th>Entered Service In:</th>
    </tr>
    {% for tank in tanks %}
    <tr>
        <td rowspan="1"><a href="../{{ tank.pk }}/details">{{ tank.name }}</a></td>
        <td rowspan="1">{{ tank.country|title }}</td>
        <td rowspan="1">{{ tank.generation }}</td>
        <td rowspan="1">{{ tank.year }}</td>
    </tr>
    {% endfor %}
</table>

<div class="search-abstract">
    <h3>Search DBpedia for abstract on Tank</h3>
    <form method="POST" action="{% url 'tanksAPI' %}">
        <div class="form-object-container">
            {% csrf_token %}
            {{ namesForm.non_field_errors }}
            {{ namesForm.as_p }}
        </div>
        <div class="form-button-container">
            <input type="submit" class="button" value="Search">
        </div>
    </form>
</div>
<br>
<div class="search-article">
    <h3>Search www.militaryfactory.com for article on Tank</h3>
    <form method="POST" action="{% url 'tanksSoup' %}">
        <div class="form-object-container">
            {% csrf_token %}
            {{ idForm.non_field_errors }}
            {{ idForm.as_p }}
        </div>
        <div class="form-button-container">
            <input type="submit" class="button" value="Search">
        </div>
    </form>
</div>

{% endblock %}
~~~

### Details
The details pages, one for each entry, contains all the releveant data from the database in a table format. 

### API
The API functionality was done over two stories, this was the hardest of the stories I did on this project. It searches DBpedia (a project aiming to extract structured content from the information created in the Wikipedia project) for an abstract of the selected tank in english. This was much more complex than I originally expected since the DBpedia response returned way more information than I was expecting (many different types of information with most in multiple languages) with no easy way to limit it so I had to get creative to get the information that I wanted. I even needed to find a script to help extract specified values from a very complex JSON response into a list. I had to extract two seperate lists due to how the infomration was stored, one for the values themselves and one for the xml:lang tag which indicated which language the value was in. From there some excess information was sorted out and the two lists were combined into a dictonary so the correct key value pair could be selected and returned to the API page.

~~~
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
~~~

### Web Scraping
The web scraping functionality was done over two stories, it uses Beautiful Soup 4. For this example of web scraping I took articles off of www.militaryfactory.com and displayed their main content onto the soup page. Finding the correct combination of methods to remove all the formating and tags besides the newline characters from the repsonse was tedious. In the end it was finding all the spans with a specific class, putting those results into a list, and using the get_text() method on the span I wanted extractred the text I wanted from the response.

~~~
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
~~~
