let counts1 = setInterval(updated1, 90);
let counts2 = setInterval(updated2, 90);
let counts3 = setInterval(updated3, 90);
let upto1 = 0;
let upto2 = 0;
let upto3 = 0;

function updated1() {
    var firstcount = document.querySelector("#counter1");
    var number1 = parseInt(firstcount.dataset.count);
    firstcount.innerHTML = ++upto1;
    if (upto1 === number1) {
        clearInterval(counts1);
    }
}

function updated2() {
    const secondcount = document.querySelector("#counter2");
    try {
      var number2 = parseInt(secondcount.dataset.count);
    } catch (error) {
      console.log(error)
      var number2 = 0;
    }
    secondcount.innerHTML = ++upto2;
    if (upto2 === number2) {
        clearInterval(counts2);
    }
}

function updated3() {
    var thirdcount = document.querySelector("#counter3");
    var number3 = parseInt(thirdcount.dataset.count);
    thirdcount.innerHTML = ++upto3;
    if (upto3 === number3) {
        clearInterval(counts3);
    }
}

// contact form Logic

var contactform = document.getElementById('contact_form');

contactform.addEventListener('submit', function (e) {
  e.preventDefault();
  submitcontactformdata()
})

function submitcontactformdata() {
  var userformdata = {
    'name': contactform.Name.value,
    'email': contactform.email.value,
    'message': contactform.message.value,
  }

  var url = '/submit_contact_form/'
  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ 'userformdata': userformdata })
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      contactform.Name.value = ''
      contactform.email.value = ''
      contactform.message.value = ''
      document.getElementById('contact_form_alert').style.display = "block"
      document.getElementById('contact_form_alert').style.opacity = "1"
      console.log('Data :', data)
    })
}

// Get all elements with class="closebtn"
var close = document.getElementsByClassName("closebtn");
      var i;
      for (i = 0; i < close.length; i++) {
        close[i].onclick = function () {
          var div = this.parentElement;
          div.style.opacity = "0";
          setTimeout(function () { div.style.display = "none"; }, 600);
        }
      }



