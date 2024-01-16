function createCounterUpdater(counterId) {
  let upto = 0;
  const counter = document.querySelector(counterId);
  const number = parseInt(counter.dataset.count);

  return function() {
      counter.innerHTML = ++upto;
      if (upto === number) {
          clearInterval(counts);
      }
  };
}

let counts1 = setInterval(createCounterUpdater("#counter1"), 90);
let counts2 = setInterval(createCounterUpdater("#counter2"), 90);
let counts3 = setInterval(createCounterUpdater("#counter3"), 90);

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



