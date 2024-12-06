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

        let rate_button = ''
        if (item.status === 'Delivered'){
            rate_button = `<button onclick="open_rate_modal(this, '${item.product_name}')" id="${item.product_id}" class='ml-6 px-5 py-1 rounded-md hover:bg-slate-800 bg-slate-950 text-white'>Rate & Review</button>`
        }
        new_div.innerHTML = `
                <div class="h-full my-auto ml-2 flex-1">
                    <div class='flex'>
                            <img src='${item.product_image}' class='w-14 mr-4 h-16 rounded-xl'>
                        <a href='/view/${item.product_id}' class="font-bold font-lato">
                            ${item.product_name} (${item.product_qt})
                            <p class="font-bold font-lato text-sm">Price: ₱${item.product_original_price}</p>
                            <p class="font-bold font-lato text-sm">Size: ${item.product_size}</p>
                        </a>
                    </div>
                </div>
                <div class="h-full my-auto font-lato flex space-x-2">
                    <h1>₱${item.product_price}</h1>
                    <div>
                        ${ rate_button }
                    </div>
                </div>

        `

        const new_hr = document.createElement('hr')
        new_hr.classList.add('w-full', 'mt-4')
        item_container.appendChild(new_div)
        item_container.appendChild(new_hr)
    })

    try{
        if (items_json.items[0].status !== 'In Progress'){
            modal_cancelOrder_button.classList.add('hidden')
        }else{
            modal_cancelOrder_button.classList.remove('hidden')
        }
    }catch {
        
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

const starRating = document.querySelector('#starRating')
let color = 'text-yellow-400'

function selected_star(rate){
    const fullStars = Math.floor(rate)
    const hasHalfStar = rate % 1 !== 0

    for (let i = 0; i < 5; i++) {
        if (i < fullStars) {
            starRating.innerHTML += `<i onclick="star(${i+1})" class="${color} fas fa-star hover:cursor-pointer mt-2"></i>`
        } else if (i === fullStars && hasHalfStar) {
            starRating.innerHTML += `<i onclick="star(${i+1})" class="${color} fas fa-star hover:cursor-pointer-half-alt mt-2"></i>`
        } else {
            starRating.innerHTML += `<i onclick="star(${i+1})" class="${color} far fa-star hover:cursor-pointer mt-2"></i>`
        }
    }
}


const review_modal = document.querySelector('#review_modal')
const product_name = document.querySelector('#product_name_modal')
const review = document.querySelector('#review')
const submit_button = document.querySelector('#submit_button')
let total_rating = 0
let product_id

async function open_rate_modal(this_, prod_name){
    product_id = this_.id
    starRating.innerHTML = ''
    product_name.textContent = prod_name

    const response = await fetch('/api/product/check/review', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({ product_id : this_.id })
    }) 

    const response_json = await response.json()
    
    try {
        
        if (response_json.review.rating){
            starRating.setAttribute('rate', response_json.review.rating)
            review.textContent = response_json.review.comment
            submit_button.textContent = 'Update'
            total_rating = response_json.review.rating
            color = 'text-yellow-400'
        }else{
            starRating.setAttribute('rate', 0)
            review.textContent = ''
            submit_button.textContent = 'Submit'
            color = 'text-yellow-400'
        }
    }catch{
        starRating.setAttribute('rate', 0)
        submit_button.textContent = 'Submit'
    }
    
    const rate = parseFloat(starRating.getAttribute('rate'))
    selected_star(rate)
    review_modal.classList.replace('hidden', 'flex')
}


function star(total_selected_star){
    color = 'text-yellow-400'
    starRating.innerHTML = ''
    starRating.setAttribute('rate', total_selected_star)
    total_rating = parseInt(total_selected_star)
    const rate = parseFloat(starRating.getAttribute('rate'))

    selected_star(rate)
}

function close_reviewModal(){
    total_rating = 0
    product_id = ''
    review_modal.classList.replace('flex', 'hidden')
}


async function submit_review(this_){
    if (total_rating !== 0){
        document.querySelector(`#${this_.id}`).disabled = true
        
        const response = await fetch('/api/product/submit/review', {
            method : 'POST',
            headers : {'Content-Type' : 'application/json'},
            body : JSON.stringify({
                product_id : product_id,
                product_rating : parseInt(total_rating),
                user_comment : String(review.value)
            })
        })

        location.reload()
    }else{
        starRating.innerHTML = ''
        color = 'text-red-500'
        rate = 0
        selected_star(rate)
    }
}