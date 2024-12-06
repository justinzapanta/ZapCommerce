const modal = document.querySelector('#modal')
const first_name = document.querySelector('#first_name')
const last_name = document.querySelector('#last_name')
const email = document.querySelector('#email')
const address = document.querySelector('#address')
const modal_td = document.querySelectorAll('.modal_td')
const table_body = document.querySelector('#table_body')
const select_status = document.querySelector('#status')
const confirmation_modal = document.querySelector('#confirmation_modal')

let invoice
async function openModal(this_){
    invoice = this_.id
    const response = await fetch('/api/seller/orders/info', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({ invoice : this_.id })
    })

    const response_json = await response.json()
    const user_info = response_json.user_info
    console.log(response_json.user_info.status)
    if (select_status.options[0].value === response_json.user_info.status){
        select_status.options[0].selected = true

    }else if (select_status.options[1].value === response_json.user_info.status){
        select_status.options[1].selected = true

    }else if (select_status.options[2].value === response_json.user_info.status){
        select_status.options[2].selected = true
    }

    first_name.value = user_info.first_name
    last_name.value = user_info.last_name
    email.value = user_info.email
    address.value = user_info.address

    table_body.innerHTML = ''

    response_json.order_list.forEach(order => {
        const new_tr = document.createElement('tr')
        new_tr.classList.add('hover:bg-gray-50', 'text-sm', 'transition-colors', 'duration-200')

        new_tr.innerHTML = `
            <td class="py-4 px-6 whitespace-nowrap modal-td flex">
                <img class='w-10 h-10 rounded-full' src='${order.product_image}' >
                <div class='h-full my-auto'>
                    ${order.product_name}
                </div>
            </td>
            <td class="py-4 px-6 whitespace-nowrap modal-td">${order.product_size}</td>
            <td class="py-4 px-6 whitespace-nowrap modal-td">${order.product_price}</td>
            <td class="py-4 px-6 whitespace-nowrap modal-td">${order.product_quantity}</td>
            <td class="py-4 px-6 whitespace-nowrap modal-td">${order.product_totalPrice}</td>
        `

        table_body.appendChild(new_tr)
    })

    modal.classList.replace('hidden', 'flex')
}

function close_modal(){
    modal.classList.replace('flex', 'hidden')
}


function close_confirm_modal(){
    confirmation_modal.classList.replace('flex', 'hidden')
}

function open_confirm_modal(){
    confirmation_modal.classList.replace('hidden', 'flex')
}


async function update_transaction_status(){
    const response = await fetch('/api/seller/update/status', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({
            invoice : invoice,
            new_status : select_status.value
        })
    })

    location.reload()
}