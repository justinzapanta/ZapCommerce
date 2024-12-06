const openModalBtn = document.querySelector('#openModal')
const modal = document.querySelector('#productModal')
const modalContent = document.querySelector('#modalContent')
const productForm = document.querySelector('#productForm')
const productPrice = document.querySelector('#productPrice')
const productDiscount = document.querySelector('#productDiscount')
const discountedPrice = document.querySelector('#discountedPrice')
const cancelButton = document.querySelector('#cancelButton')
const productRate = document.querySelector('#productRate')
const starRating = document.querySelector('#starRating')

const productName = document.querySelector('#productName')
const productDescription = document.querySelector('#productDescription')
const searchKey = document.querySelector('#searchKey')
const productImage = document.querySelector('#productImage')
const saveButton = document.querySelector('#saveButton')
const productSize = document.querySelector('#productSize')
const productType = document.querySelector('#productType')

let product_id
async function openModal(this_) {
    starRating.innerHTML = ''
    productImage.value = ''
    if (this_ !== 'add-product'){
        product_id = this_.id
        const response = await fetch('/api/product/seller-product', {
            method : 'POST',
            headers : {'Content-Type' : 'application/json'},
            body : JSON.stringify({id : this_.id})
        })
        
        saveButton.textContent = 'Save Changes'
        const response_json = await response.json()
        productName.value = response_json.product[0].product_name
        productPrice.value = response_json.product[0].product_price
        productDiscount.value = response_json.product[0].product_discount
        discountedPrice.value = response_json.product[0].product_price_w_disc
        productDescription.value = response_json.product[0].product_details
        productRate.value = response_json.product[0].product_rate
        searchKey.value = response_json.product[0].product_search_key
        productSize.value = response_json.product[0].product_size
        
        if (productType.options[0].value === response_json.product[0].product_type){
            productType.options[0].selected = true
        }else if (productType.options[1].value === response_json.product[0].product_type){
            productType.options[1].selected = true
        }else if (productType.options[2].value === response_json.product[0].product_type){
            productType.options[2].selected = true
        }else{
            productType.options[3].selected = true
        }

        const rate = parseFloat(productRate.value)
        const fullStars = Math.floor(rate)
        const hasHalfStar = rate % 1 !== 0
        
        for (let i = 0; i < 5; i++) {
            if (i < fullStars) {
                starRating.innerHTML += '<i class="fas fa-star"></i>'
            } else if (i === fullStars && hasHalfStar) {
                starRating.innerHTML += '<i class="fas fa-star-half-alt"></i>'
            } else {
                starRating.innerHTML += '<i class="far fa-star"></i>'
            }
        }
    }else{
        product_id = 'none'
        productName.value = ''
        productPrice.value = ''
        productDiscount.value = ''
        discountedPrice.value = ''
        productDescription.value = ''
        productRate.value = '0'
        searchKey.value = ''    
        productSize.value = ''
        saveButton.textContent = 'Save'
    }

    modal.classList.remove('hidden')
    setTimeout(() => {
        modal.classList.add('opacity-100')
        modalContent.classList.remove('scale-95', 'opacity-0')
        modalContent.classList.add('scale-100', 'opacity-100')
    }, 50)
}

function closeModal() {
    modal.classList.remove('opacity-100')
    modalContent.classList.remove('scale-100', 'opacity-100')
    modalContent.classList.add('scale-95', 'opacity-0')
    setTimeout(() => {
        modal.classList.add('hidden')
    }, 300)
}

modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal()
    }
})

function calculateDiscountedPrice() {
    const price = parseFloat(productPrice.value) || 0
    const discount = parseFloat(productDiscount.value) || 0
    const discounted = price - (price * discount / 100)
    discountedPrice.value = discounted.toFixed(2)
}

productPrice.addEventListener('input', calculateDiscountedPrice)
productDiscount.addEventListener('input', calculateDiscountedPrice)

const inputs = document.querySelectorAll('.input')

function not_empty(){
    let not_empt = true

    inputs.forEach(input => {
        if (input.value == ''){
            not_empt = false
            input.classList.replace('border-gray-300', 'border-red-500')
        }else{
            input.classList.replace('border-red-500', 'border-gray-300')
        }
    })

    return not_empt
}



async function update_product(){
    if (not_empty()){
        const form_data = new FormData()

        form_data.append('product_id', product_id,)
        form_data.append('product_name', productName.value,)
        form_data.append('product_price', productPrice.value,)
        form_data.append('product_discount', productDiscount.value,)
        form_data.append('product_details', productDescription.value,)
        form_data.append('product_search_key', searchKey.value,)
        form_data.append('product_size', productSize.value,)
        form_data.append('product_type', productType.value,)
        
        if (productImage.files[0]){
            form_data.append('product_image' , productImage.files[0])
        }
    

        if (product_id !== 'none'){
            const response = await fetch('/api/seller/product/update', {
                method : 'POST',
                body : form_data
            })
            location.reload()
        }else{
            if (productImage.files[0]){
                const response = await fetch('/api/seller/product/new-product', {
                    method : 'POST',
                    body : form_data
                })
                location.reload()
            }else{
                productImage.classList.replace('text-gray-500', 'text-red-500')
            }
        }
    }
}

const deleteModal = document.querySelector('#deleteModal')
function show_delete_modal(){
    deleteModal.classList.replace('hidden', 'flex')
}

function close_delete_modal(){
    deleteModal.classList.replace('flex', 'hidden')
}

async function delete_product(){
    const response = await fetch('/api/seller/product/delete', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({'product_id' : product_id})
    })

    location.reload()
}

