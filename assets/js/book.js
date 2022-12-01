let search = document.querySelector(".search");
let clear = document.querySelector(".clear");

search.onclick=function(){
    document.querySelector('.search_container').classList.toggle("active");
    document.querySelector('.icon').classList.toggle("active")
}
clear.onclick=function(){
    document.getElementById('search').value ='';
}


// Sort by Category
// when dealing with anything that has to deal with display make sure that bootstrap class was not used
filterSelection('All')
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("filterDiv");
 
  if (c == "All") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

// Show filtered elements
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

function myFunction() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    catalog = document.getElementById("bookcatalog");
    cardwrapper = catalog.getElementsByClassName('filterDiv');
  
  
    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < cardwrapper.length; i++) {
      title = cardwrapper[i].getElementsByTagName("h6")[0];
      txtValue = title.textContent || title.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        cardwrapper[i].style.display = '';
  
      } else {
        cardwrapper[i].style.display = 'none';
      }
    }
  }

// Update Cart Item
  var updatebutton = document.getElementsByClassName('update-cart');
  for (i = 0; i < updatebutton.length; i++) {
    updatebutton[i].addEventListener('click', function () {
      var productid = this.dataset.product;
      var action = this.dataset.action;
      console.log('User:', user)
      if (user === 'AnonymousUser') {
        addCookieItem(productid, action)
        console.log('not logged in')
      } else {
        updateuserorder(productid, action)
      }
    })
  }
  
function updateuserorder(productid, action) {
    console.log('user is Authenticated, sending Data')
    var url = '/main/update_item/'
    fetch(url, {
      method: "POST",
      headers: {
        'content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify({ 'productId': productid, 'action': action })
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        document.getElementById('get_main_cart_items').innerHTML = data['num_of_cart']
        console.log('Data :', data)
      }
      )
  }
 
  
  function addCookieItem(productid, action){
    console.log('User is not authenticated')
  
    if (action == 'add'){
      if (cart[productid] == undefined){
      cart[productid] = {'quantity':1}
  
      }else{
        cart[productid]['quantity'] += 1
      }
    }
  
    if (action == 'remove'){
      cart[productid]['quantity'] -= 1
  
      if (cart[productid]['quantity'] <= 0){
        console.log('Item should be deleted')
        delete cart[productid];
      }
    }
    console.log('CART:', cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    
    location.reload()
  }
