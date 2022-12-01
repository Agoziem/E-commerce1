var updatebutton = document.getElementsByClassName('update-cart');
for (i = 0; i < updatebutton.length; i++) {
  updatebutton[i].addEventListener('click', function () {
    var productid = this.dataset.product;
    var action = this.dataset.action;
    console.log('User:', user)
    if (user === 'AnonymousUser') {
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

