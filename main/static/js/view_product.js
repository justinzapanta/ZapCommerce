const carousel = document.getElementById('carousel');

//get product size
let product_sizee = 0

function product_size(_this){
    product_sizee = _this.value
}

//add to cart
const notif = document.querySelector('#notif')
const text = document.querySelector('#notif-text')
const size_notif = document.querySelector('#size-notif')

function add_to_cart(_this){
    if(_this.id){
        if (product_sizee != 0){
            const request = new XMLHttpRequest()
            request.open('POST', '/api/cart/add-product/')
            request.setRequestHeader('Content-Type', 'application/json')
            request.send(JSON.stringify({
                id : _this.id,
                product_size : product_sizee,
                }))

            request.onloadend = () => {
                const response = JSON.parse(request.responseText)
                if (response.message == 'Added Successfully'){
                    get_cart_totalItem()
                    text.textContent = response.message
                }else{
                    text.textContent = 'Already Added'
                }

                notif.classList.replace('hidden', 'flex')

                setInterval(() => {
                    notif.classList.replace('flex', 'hidden')
                }, 2000);
            }
        }else{
            size_notif.classList.replace('hidden', 'flex')
        }
    }
}


const starRating = document.querySelector('#starRating')

async function rate(){
    const rate = parseFloat(starRating.getAttribute('rate'))
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


    console.log(total_rate)
}

rate()

