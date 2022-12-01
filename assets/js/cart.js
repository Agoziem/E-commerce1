
// Cart logic for deleting Cart

// Cart logic for Updating Item

var updatebutton = document.getElementsByClassName('update-cart');
for (i = 0; i < updatebutton.length; i++) {
  updatebutton[i].addEventListener('click', function () {
    var productid = this.dataset.product;
    var action = this.dataset.action;
    console.log('User:', user)
    if (user === 'AnonymousUser') {
      addCookieItem(productid, action)
    } else {
      updateuserorder(productid, action)
    }
  })
}

// Adding Item and removing button for logged in User

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
      // document.getElementById('get_cart_items').innerHTML =`${data['num_of_cart']} items`
      // document.getElementById('get_cart_total').innerHTML = `Check out (#${data['Total_Amount']})`
      // document.getElementById(`bookamount${productid}`).innerHTML = data['item_Amount']
      // document.getElementById(`productamount${productid}`).innerHTML = data['item_quantity']
      // document.getElementById('get_main_cart_items').innerHTML = data['num_of_cart']
      location.reload()
  
    }
    )
}

// Adding Item and removing button for Anonymous User

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

// deleting Item 

var deletebutton = document.getElementsByClassName('delete_item');
for (i = 0; i < deletebutton.length; i++) {
  deletebutton[i].addEventListener('click', function (e) {
    var productid = this.dataset.product;
    var action = this.dataset.action;
    console.log('User:', user)
    // if (user === 'AnonymousUser') {
    //   addCookieItem(productid, action)
    // } else {
    //   updateuserorder(productid, action)
    // }
    deleteuserorder(e,productid, action)
  }) 
}

function deleteuserorder(e,productid, action) {

  var url = '/main/delete_item/'
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
      // var Card=document.getElementById("card");
      // var Cart_card = document.getElementById(`cart_card${productid}`)
      // Cart_card.innerHTML = ""
      // document.getElementById('get_cart_items').innerHTML =`${data['num_of_cart']} items`
      // document.getElementById('get_cart_total').innerHTML = `Check out (#${data['Total_Amount']})`
      // document.getElementById('get_main_cart_items').innerHTML = data['num_of_cart']
      // console.log('Data :', data)
      // console.log(e.target.parentElement)
      location.reload()
    }
    )
}