const carousel = document.getElementById('carousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const imageIndex = document.getElementById('image-index')
let currentIndex = 0;

function showSlide(index, carousel) {
    currentIndex = index;
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + 4) % 4;
    imageIndex.textContent = parseInt(currentIndex) + 1
    showSlide(currentIndex, carousel);
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % 4;
    imageIndex.textContent = parseInt(currentIndex) + 1
    showSlide(currentIndex, carousel);
});


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