// JavaScript code to switch images every 5 seconds and loop back to the beginning
let currentImageIndex = 0;
const carouselImages = document.querySelectorAll('.carousel-image');
const numImages = carouselImages.length;
setInterval(() => {
    carouselImages[currentImageIndex].classList.remove('active');
    currentImageIndex = (currentImageIndex + 1) % numImages;
    carouselImages[currentImageIndex].classList.add('active');
    const transformValue = `translateX(-${currentImageIndex * 100}%)`;
    document.querySelector('.carousel-image-wrapper').style.transform = transformValue;
    // Check if we have reached the end and loop back to the beginning
    if (currentImageIndex === 0) {
        for (let i = 0; i < numImages; i++) {
            carouselImages[i].classList.remove('active');
        }
        carouselImages[0].classList.add('active');
        document.querySelector('.carousel-image-wrapper').style.transform = 'translateX(0)';
        currentImageIndex = 0;
    }
}, 4000);



// --------------Color switching----------

function toggleMode() {
    const body = document.body;
    const sections = document.getElementsByClassName("section");
    const slider = document.querySelector('.light');
    const slider1 = document.querySelector('.dark');
    const mul = document.querySelectorAll(".main-container, .main1, .navbar, .our-services, .footer, .card_div, .profile_dropdown");

    if (body.classList.contains("light-mode")) {
        body.classList.remove("light-mode");
        body.classList.add("dark-mode");
        slider.style.display = "none";
        slider1.style.display = "block";

        for (let i = 0; i < sections.length; i++) {
            sections[i].classList.remove("light-mode");
            sections[i].classList.add("dark-mode");
        }
        mul.forEach(element => {
            element.classList.remove("light-mode");
            element.classList.add("dark-mode");
        });


    } else {
        body.classList.remove("dark-mode");
        body.classList.add("light-mode");
        slider1.style.display = "none";
        slider.style.display = "block";


        for (let i = 0; i < sections.length; i++) {
            sections[i].classList.remove("dark-mode");
            sections[i].classList.add("light-mode");
        }

        mul.forEach(element => {
            element.classList.remove("dark-mode");
            element.classList.add("light-mode");
        });
    }
}

// -------------------------------------------------------

// ----------------------Larging the image------------------------------

function large(n) {
    var img = document.getElementById(n);
    img.style.display = "flex";
}


// --------------------profile drop-------------------

function profile_drop(){
    var drop = document.getElementById("profile_dropdown");

    if(drop.style.display === "none"){
        drop.style.display = "block";
    }
    else{
        drop.style.display = "none";
    }
}