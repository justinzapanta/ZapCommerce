//Banner
const carousel = document.getElementById('carousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const totalImage = 2
let currentIndex = 0;

function showSlide(index, carousel) {
    currentIndex = index;
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + totalImage) % totalImage;
    showSlide(currentIndex, carousel);
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % totalImage;
    showSlide(currentIndex, carousel);
});

// Auto-play functionality
setInterval(() => {
    currentIndex = (currentIndex + 1) % totalImage;
    showSlide(currentIndex, carousel);
}, 5000);



//new product
const carousel1 = document.getElementById('carousel1');
const prevBtn1 = document.getElementById('prevBtn1');
const nextBtn1 = document.getElementById('nextBtn1');
let newProductIndex = 0;

prevBtn1.addEventListener('click', () => {
    newProductIndex = (currentIndex - 1 + 3) % 3;
    showSlide(newProductIndex, carousel1);
});

nextBtn1.addEventListener('click', () => {
    newProductIndex = (newProductIndex + 1) % 3;
    showSlide(newProductIndex, carousel1);
});


//sales paroducts
const carousel2 = document.getElementById('carousel2');
const prevBtn2 = document.getElementById('prevBtn2');
const nextBtn2 = document.getElementById('nextBtn2');
let salesProductIndex = 0;

prevBtn2.addEventListener('click', () => {
    salesProductIndex = (salesProductIndex - 1 + 3) % 3;
    showSlide(salesProductIndex, carousel2);
});

nextBtn2.addEventListener('click', () => {
    salesProductIndex = (salesProductIndex + 1) % 3;
    showSlide(salesProductIndex, carousel2);
});

//timer
function updateTimer() {
    const deadline = new Date("2024-12-25T00:00:00").getTime();
    const now = new Date().getTime();
    const timeLeft = deadline - now;

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    document.getElementById("days").innerHTML = days.toString().padStart(2, '0');
    document.getElementById("hours").innerHTML = hours.toString().padStart(2, '0');
    document.getElementById("minutes").innerHTML = minutes.toString().padStart(2, '0');
    document.getElementById("seconds").innerHTML = seconds.toString().padStart(2, '0');

    if (timeLeft < 0) {
        clearInterval(timerInterval);
        document.getElementById("timer").innerHTML = "EXPIRED";
    }
}

const timerInterval = setInterval(updateTimer, 1000);
updateTimer(); // Initial call to avoid delay


const loading_ = document.querySelector('#loading_')
const all_products_container = document.querySelector('#all-products-container')
const for_you_container = document.querySelector('#for-you-products')
const pagination = 1
let already_load = ''

async function show_more(_this, device="desktop"){
    let count = 1
    let show_products = document.querySelector(`#${_this.id}`)
    
    if (device == 'desktop'){
        show_products.classList.replace('md:block','md:hidden')
    }else if (device == 'mobile'){
        show_products.classList.replace('block','hidden')
    }
    loading_.classList.replace('hidden', 'flex')
 
    try{
        const new_product_container = document.createElement('div')
        new_product_container.classList.add('grid', 'grid-cols-1', 'sm:grid-cols-2', 'md:grid-cols-3', 'lg:grid-cols-5', 'gap-4', 'mt-4', 'font-lato')

        const response = await fetch(`/api/product/get-all/${pagination}/${device}`)
        let data = await response.json()
        let products = data.products
        let stop = false 

        products.forEach(product => {
            if (already_load == product.product_id){
                stop = true
            }

            if (count == 1){
                already_load = product.product_id
                count += 1
            }

            console.log(count)

            if (!stop){
                // product card 
                let new_product_card = document.createElement('div')
                new_product_card.innerHTML = `
    
                    <a href="/view/${product.product_id}">
                        <div class="bg-white rounded-lg shadow-lg overflow-hidden flex flex-col h-full border">
                            <div class="relative pt-[100%]">
                                <img src="${product.product_image}" alt="Air Max" class="absolute top-0 left-0 w-full h-full object-cover">
                                <div class="absolute top-0 left-0 bg-red-500 text-white px-2 py-1 m-2 rounded-md text-xs font-bold">
                                    ${product.product_discount}% OFF
                                </div>
                            </div>
                            <div class="p-4 flex-grow flex flex-col justify-between">
                                <h2 class="text-md font-semibold text-gray-800 mb-2 line-clamp-2">${product.product_name}</h2>
                                <div class="flex justify-between items-center">
                                    <div class="text-sm font-bold text-gray-900">$${product.product_price}</div>
                                    <div class="text-sm text-red-500 line-through">$99.99</div>
                                </div>
                            </div>
                        </div>
                    </a>
                `
    
                if (device == 'desktop'){
                    new_product_container.appendChild(new_product_card)
                }else{
                    for_you_container.appendChild(new_product_card)
                }
            }

        })
        all_products_container.appendChild(new_product_container)

        if (products.length == 10 && device == 'mobile' && !stop){
            show_products.classList.replace('hidden', 'block')
        }else if(products.length == 10 && device == 'desktop' && !stop){
            show_products.classList.replace('md:hidden', 'md:block')
        }

        loading_.classList.replace('flex', 'hidden')
    }catch(error){
        console.log(error)
    }
}