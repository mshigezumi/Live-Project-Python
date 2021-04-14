var slideIndex = 1;
showSlides(slideIndex);

function openModal() {
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

function changeSlide(number) {
    showSlides(slideIndex += number);
}

function currentSlide(number) {
    showSlides(slideIndex = number);
}

function showSlides(number) {
    var slides = document.getElementsByClassName("slides");
    var dots = document.getElementsByClassName("thumbnail");
    var captionText = document.getElementById("caption");
    if (number > slides.length) {
        slideIndex = 1;
    } else if (number < 1) {
        slideIndex = slides.length;
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (let i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt;
}