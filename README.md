# Live Project
 
## Introduction:

For the last two weeks with the Tech Academy I worked on a Live Project in Python which simulated a real world work environment in which I worked with my peers and staff to do work on a website, in this project we each worked on our own personal section of our choosing. We used Django with an MVC pattern in the create the website, sqlite3 was used as a database, and Beautiful Soup 4 was used for web scraping. My section is dedicated to modern tanks of the world, which is a successor to previous websites I made while learning HTML, CSS, and Javascript. Below are some code snippets of the stories I worked on, full code files are also available in this repository.

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

### Details
The details pages, one for each entry, contains all the releveant data from the database in a table format. 

### API
The API functionality was done over two stories, this was the hardest of the stories I did on this project. It searches DBpedia (a project aiming to extract structured content from the information created in the Wikipedia project) for an abstract of the selected tank in english. This was much more complex than I originally expected since the DBpedia response returned way more information than I was expecting (many different types of information with most in multiple languages) with no easy way to limit it so I had to get creative to get the information that I wanted. I even needed to find a script to help extract specified values from a very complex JSON response into a list.

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




### BlogPost Create/Edit Pages
Two seperate stories included these pages, first was creating and scafolding the CRUD pages, second was styling and implementing the basic functionality of the create and edit pages. Both of these pages are very similar so they were part of the same stories.

~~~
<div class="blog-post-div">
    <h2 class="blog-post-header">Edit Blog Post</h2>
</div>

@using (Html.BeginForm("Edit", "BlogPost", FormMethod.Post, new { @class = "blog-post-form" }))
{
    @Html.AntiForgeryToken()

    <div class="form-horizontal">
        @Html.ValidationSummary(true, "", new { @class = "text-danger" })
        @Html.HiddenFor(model => model.BlogPostId)

        <div class="blog-post-form-group">
            @Html.LabelFor(model => model.Title, htmlAttributes: new { @class = "control-label" })
            <div class="blog-post-div">
                @Html.EditorFor(model => model.Title, new { htmlAttributes = new { @class = "form-control blog-post-input" } })
                @Html.ValidationMessageFor(model => model.Title, "", new { @class = "text-danger" })
            </div>
        </div>

        <div class="blog-post-form-group">
            @Html.LabelFor(model => model.Content, htmlAttributes: new { @class = "control-label" })
            <div class="blog-post-div">
                <!-- this should probably be a text field instead so it's easier to write/edit the text of the blog post -->
                @Html.EditorFor(model => model.Content, new { htmlAttributes = new { @class = "form-control blog-post-input" } })
                @Html.ValidationMessageFor(model => model.Content, "", new { @class = "text-danger" })
            </div>
        </div>

        <div class="blog-post-form-group">
            @Html.LabelFor(model => model.Posted, htmlAttributes: new { @class = "control-label" })
            <div class="blog-post-div">
                @Html.EditorFor(model => model.Posted, new { htmlAttributes = new { @class = "form-control blog-post-input" } })
                @Html.ValidationMessageFor(model => model.Posted, "", new { @class = "text-danger" })
            </div>
        </div>

        <div class="blog-post-form-group">
            @Html.LabelFor(model => model.Author, htmlAttributes: new { @class = "control-label" })
            <div class="blog-post-div">
                @Html.EditorFor(model => model.Author, new { htmlAttributes = new { @class = "form-control blog-post-input" } })
                @Html.ValidationMessageFor(model => model.Author, "", new { @class = "text-danger" })
            </div>
        </div>

        <div class="col-md-10 blog-post-div">
            <input type="submit" value="Save" class="btn btn-default blog-post-button blog-post-spacer" />
        </div>

        <div class="blog-post-div col-md-10">
            @Html.ActionLink("Back", "Index", null, new { @class = "btn btn-default blog-post-button2" })
        </div>
    </div>
}
~~~

### BlogPost Index Page
Three seperate stories included this page, first was creating and scafolding the CRUD pages, second was styling and implementing the basic functionality of the index page (showing the blog posts, getting buttons to work), third was styling and implementing a confirm delete modal and an alert with javascript/jQuery for extra funcationality.

~~~
<!-- Alert -->
<div class="blog-post-div blog-post-alert">
    <div class="alert alert-success blog-post-alert-text blog-post-spacer2 blog-post-alert-fade" id="alert">
        The blog post was deleted successfully <i class="fas fa-check"></i>
    </div>
</div>

<div class="blog-post-div">
    <h2 class="blog-post-header">Blog Post Index</h2>
</div>

<p>
    @Html.ActionLink("Create New", "Create")
</p>

<!-- Blog Posts -->
@foreach (var item in Model)
{
    <div class="blog-post-card-container" id="@item.BlogPostId">
        <div class="card blog-post-card">
            <div class="row no-gutters">
                <div class="blog-post-card-thumbnail">
                    <img src="https://picsum.photos/500" class="img-fluid " alt="">
                </div>
                <div class="col px-2 blog-post-flexbox flex-column">
                    <div class="blog-post-card-text-container">
                        <h4 class="blog-post-card-title">@Html.DisplayFor(modelItem => item.Title)</h4>
                        <p class="text-muted">@Html.DisplayFor(modelItem => item.Posted) by @Html.DisplayFor(modelItem => item.Author)</p>
                        <p class="card-text blog-post-spacer2">@Html.DisplayFor(modelItem => item.Content)</p>
                    </div>
                    <div class="blog-post-card-button-container">
                        <a href="@Url.Action("Edit", new { id = item.BlogPostId })" class="btn blog-post-button"><i class="fas fa-edit"></i> Edit</a>
                        <a href="@Url.Action("Details", new { id = item.BlogPostId })" class="btn blog-post-button"><i class="fas fa-info"></i> Details</a>
                        <button type="button" class="btn blog-post-button2" data-toggle="modal" data-target="#confirmDelete" data-item-id="@item.BlogPostId" data-item-title="@item.Title"><i class="fas fa-trash"></i> Delete</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
}

<!-- Modal -->
<div class="modal fade" id="confirmDelete" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content blog-post-modal-content">
            <div class="modal-header blog-post-modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Delete this Blog Post?</h5>
                <button type="button" class="close blog-post-close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                Are you sure you want to delete: <span class="title"></span>
            </div>
            <div class="modal-footer blog-post-modal-footer">
                <button type="button" class="btn blog-post-button" data-dismiss="modal">Close</button>
                <button type="submit" class="btn blog-post-button2" id="deleteButton">Delete</button>
            </div>
        </div>
    </div>
</div>

<script type="text/javascript">
    function gettoken() {
        var token = '@Html.AntiForgeryToken()';
        token = $(token).val();
        return token;
    }
    function showAlert() {
        $('#alert').addClass('in');
    }
    function hideAlert() {
        $('#alert').removeClass('in');
    }
    $('#confirmDelete').on('click', '#deleteButton', function (e) {
        var $modalDiv = $(e.delegateTarget);
        var id = $(this).data('itemId');
        var $postDiv = $('#' + id);
        $.ajax({ url: '/Blog/BlogPost/Delete/' + id, type: 'POST', data: {__RequestVerificationToken: gettoken()}})
        $postDiv.addClass('blog-post-hide');
        $modalDiv.modal('hide');
        showAlert();
        setTimeout(function () {
            hideAlert();
        }, 3000)
    });
    $('#confirmDelete').on('show.bs.modal', function (e) {
        var data = $(e.relatedTarget).data();
        $('.title', this).text(data.itemTitle);
        $('#deleteButton', this).data('itemId', data.itemId);
    });
</script>
~~~

### BlogPost Details/Delete Pages
Two seperate stories included these pages, first was creating and scafolding the CRUD pages, second was styling and implementing the basic functionality of the details and delete pages. Both of these pages are very similar so they were part of the same stories.

~~~
<div class="blog-post-div">
    <h2 class="blog-post-header">Delete this Blog Post?</h2>
</div>

<div class="blog-post-card-container">
    <div class="card blog-post-card">
        <div class="no-gutters">
            <div class="blog-post-div">
                <h4 class="blog-post-spacer">@Html.DisplayFor(model => model.Title)</h4>
                <div class="blog-post-card-image">
                    <img src="https://picsum.photos/500" class="img-fluid " alt="">
                </div>
            </div>
            <div class="blog-post-spacer2">
                <div class="blog-post-card-text-container2">
                    <p class="text-muted">by @Html.DisplayFor(model => model.Author)</p>
                    <p class="text-muted">@Html.DisplayFor(model => model.Posted)</p>
                    <p class="card-text blog-post-spacer2">@Html.DisplayFor(model => model.Content)</p>
                </div>
                <div class="row blog-post-card-button-container2">
                    <div class="col-8 blog-post-card-button-container-left blog-post-no-padding">
                        <!-- need to find way to make this look good on mobile too -->
                        <a href="@Url.Action("Index", new {  })" class="btn blog-post-button3 col-4"><i class="fas fa-chevron-left"></i> Back</a>
                        <a href="@Url.Action("Edit", new { id = Model.BlogPostId })" class="btn blog-post-button3 col-4"><i class="fas fa-edit"></i> Edit</a>
                    </div>
                    <div class="col-4 blog-post-card-button-container-right blog-post-no-padding">
                        <!-- need to find way to make this look good on mobile too -->
                        @using (Html.BeginForm())
                        {
                            @Html.AntiForgeryToken()
                            <button type="submit" class="btn blog-post-button4 col-8"><i class="fas fa-trash"></i> Delete</button>
                        }
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
~~~

### Blog.css
The CSS used for all these files is stored in the Blog.css file, this in combination with Bootstrap 4 styled the BlogPost pages to the required specifications.

~~~
.blog-post-modal-content {
    background-color: #333333;
    border: 0;
    box-shadow: 0px 0px 0.5rem var(--dark-color);
}

.blog-post-modal-header {
    border-bottom: 0;
}

.blog-post-close {
    color: var(--light-color);
    text-shadow: 0px 0px 0.5rem var(--dark-color);
}

.blog-post-modal-footer {
    border-top: 0;
}

.blog-post-hide {
    display: none;
}

.blog-post-alert {
    position: fixed;
    z-index: 999;
    width: 50%;
    left: 50%;
    transform: translate(-50%);
}

.blog-post-alert-text {
    font-weight: bold;
    text-align: center;
}

.blog-post-alert-fade {
    opacity: 0;
    -webkit-transition: opacity 0.25s linear;
    transition: opacity 0.25s linear;
}

.blog-post-alert-fade.in {
    opacity: 1;
}
~~~

### Other Stories
I also worked on a few other stories, including creating and scafolding the model and CRUD pages for BlogPost, making the rental area dropdown for the navbar, and working on creating and seeding the PostMaster for BlogPost.
