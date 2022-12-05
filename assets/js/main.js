const hambuger = document.querySelector('.hambuger');
const navMenu = document.querySelector('.nav-bar-sm');

hambuger.addEventListener('click', () => {
  hambuger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll("#nav-item-m-sm").forEach(n =>
  n.addEventListener("click", () => {
    hambuger.classList.remove("active");
    navMenu.classList.remove("active");
  }));


const dropdownbtn = document.querySelector('.dropdownbtn');
const dropdowntrigger = document.querySelector('.dropdowntrigger');
const dropdownlist = document.querySelector('.dropdownlist');

if (user !== 'AnonymousUser') {
  dropdowntrigger.addEventListener('click', () => {
    dropdownlist.classList.toggle("active");
    dropdownbtn.classList.toggle("active");
  })
}



let mybutton = document.getElementById("myBtn");
let navigationbar = document.getElementById("navigation");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
    // navigationbar.classList.add('shadow-sm');
  } else {
    mybutton.style.display = "none";
    // navigationbar.classList.remove('shadow-sm');
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Swipper .js 

var swiper = new Swiper(".slider_content", {

  spaceBetween: 25,
  slidesPerGroup: 3,
  loop: true,
  loopFillGroupWithBlank: true,
  centerSlide: 'true',
  fade: "true",
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
  },
});

AOS.init({
  anchorPlacement: 'top-left',
  duration: 1000
});


// Subscription form logic

var subform = document.getElementById('sub_form');



subform.addEventListener('submit', function (e) {
  e.preventDefault()
  submitsubformdata()
})

function submitsubformdata() {
  var userdata = {
    'email': subform.email.value,
  }

  var url = '/submit_sub_form/'
  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ 'userdata': userdata })
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      subform.email.value = ''
      document.getElementById('sub_form_alert1').style.display = "block"
      document.getElementById('sub_form_alert1').style.opacity = "1"
      console.log('Data :', data)
    })
}

// Subscription button logic for Small Screen

var subformsmall = document.getElementById('sub_form2');
subformsmall.addEventListener('submit', function (e) {
  e.preventDefault()
  submitsubformdata2()
})

function submitsubformdata2() {
  var userdata = {
    'email': subform.email.value,
  }

  var url = '/submit_sub_form/'
  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ 'userdata': userdata })
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      subformsmall.email.value = ''
      document.getElementById('sub_form_alert2').style.display = "block"
      document.getElementById('sub_form_alert2').style.opacity = "1"
      console.log('Data :', data)
    })
}

var close = document.getElementsByClassName("closebtn");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function () {
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function () { div.style.display = "none"; }, 600);
  }
}

// Product Rating 

var ratings = document.getElementsByClassName('number-rating');
console.log(ratings)
const starsTotal = 5;
for (i = 0; i < ratings.length; i++) {
  var rating = ratings[i].dataset.rating;
  var ratingid = ratings[i].dataset.id;
  document.addEventListener('DOMContentLoaded', getRatings(rating, ratingid));
}


function getRatings(rating, ratingid) {
  const starPercentage = (rating / starsTotal) * 100;
  const starPercentageRounded = `${Math.round(starPercentage / 10) * 10}%`;
  console.log(starPercentageRounded)
  document.querySelector(`.rating${ratingid}z .stars-inner`).style.width = starPercentageRounded;
}