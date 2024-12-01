const modal = document.querySelector('#modal')
const loading = document.querySelector('#loading')
const item_container = document.querySelector('#item-container')
const modal_totalPrice = document.querySelector('#motal-totalPrice')
const modal_cancelOrder_button = document.querySelector('#modal-cancel')
const modal_cancel = document.querySelector('#cancel-order-modal')

let invoice;
async function show_products(self){
    invoice = self.id
    loading.classList.replace('hidden', 'flex')

    const items = await fetch('/api/orders/show', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({invoice : self.id})
    })

    const items_json = await items.json()
    item_container.innerHTML = ``
    items_json.items.forEach(item => {
        const new_div = document.createElement('div')
        new_div.classList.add(
            'flex', 'mt-4', 'mr-4', 
            'rounded-xl', 'pr-4'
        )

        new_div.innerHTML = `
                <div class="h-full my-auto ml-2 flex-1">
                    <a href='/view/${item.product_id}' class="font-bold font-lato">
                        ${item.product_name} (${item.product_qt})
                    </a>
                    <h1 class="font-bold font-lato text-sm">Size: ${item.product_size}</h1>
                </div>
                <div class="h-full my-auto font-lato">
                    <h1>₱${item.product_price}</h1>
                </div>
        `
        item_container.appendChild(new_div)
    })

    if (items_json.items[0].status !== 'In Progress'){
        modal_cancelOrder_button.classList.add('hidden')
    }else{
        modal_cancelOrder_button.classList.remove('hidden')
    }
    
    modal_totalPrice.textContent = `Total Price: ₱${items_json.items[0].product_totalPrice}`
    loading.classList.replace('flex', 'hidden')
    modal.classList.replace('hidden', 'flex')
}

function close_modal(modal_name){
    if (modal_name == 'orders_modal'){
        modal.classList.replace('flex', 'hidden')
        if (modal_cancel.classList.contains('flex')){
            modal_cancel.classList.replace('flex', 'hidden')
        }
    }else{
        modal_cancel.classList.replace('flex', 'hidden')
    }
}


function cancel_order(){
    modal_cancel.classList.replace('hidden', 'flex')
}


async function cancel_orderNow(){
    const response = fetch('/api/orders/cancel', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({invoice : invoice})
    })

    
    location.reload(true)
}
