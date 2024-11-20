let total_result = 0

function delete_product(id){
    const request = new XMLHttpRequest()
    request.open('POST', '/api/cart/delete-product')
    request.setRequestHeader('Content-Type', 'application/json')
    request.send(JSON.stringify({
        id : id
    }))

    request.onloadend = () => {
        const response = JSON.parse(request.responseText)
        if (response['message'] == 'success'){
            const product = document.getElementById(id)
            
            if (product){
                product.remove()
                total_price()
            }
        }
    }
}

function total_price(){
    total_result = 0
    const total_prices = document.querySelectorAll('.total-price')
    const display_total = document.querySelector('#display-total-price')
    
    total_prices.forEach(price => {
        if (String(price.textContent).includes(',')){
            let temp_price = String(price.textContent).replace(',', '')
            total_result += parseInt(temp_price)
        }else{
            total_result += parseInt(price.textContent)
        }
    });

    display_total.textContent = `Total Price: ${total_result.toLocaleString()}`

}

const dialog_holder = document.querySelector('#dialog-holder')
let cart_id;

function show_dialog(_this) {
    if (dialog_holder.classList.contains('hidden')){
        dialog_holder.classList.replace('hidden', 'flex')
        cart_id = _this.getAttribute('cart_id')
    }
}


function close_dialog(){
    if (dialog_holder.classList.contains('flex')){
        dialog_holder.classList.replace('flex', 'hidden')
    }
}


function remove_product(){
    if (dialog_holder.classList.contains('flex')){
        dialog_holder.classList.replace('flex', 'hidden')
    }
    
    delete_product(cart_id)
}

async function update_quantity(_this){
    if (parseInt(_this.value) >= 1){
        const quantity = _this.value
        const price = document.querySelector(`#price-${_this.id}`).textContent.split(',').join('')
        const total_price_h1 = document.querySelector(`#total-price-${_this.id}`)
        
        let total_pricee = parseInt(quantity) * parseInt(price)
        total_price_h1.textContent = total_pricee.toLocaleString()
        total_price()

        const response = await fetch('/api/cart/update-product', {
            headers : {'Content-Type' : 'application/json'},
            method : "POST",
            body : JSON.stringify({
                id : _this.getAttribute('cart_id'),
                quantity : quantity
            })
        })
    }else{
        show_dialog(_this)
    }
}


async function check_out(){
    const response = await fetch('/api/cart/checkout', {
        method : 'POST',
        headers : { "Content-Type" : "application/json" },
        body : JSON.stringify({check_out : true})
    })

    const url = await response.json()

    if (url){
        window.location.href = url.link
    }
}