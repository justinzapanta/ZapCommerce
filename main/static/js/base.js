// Mobile menu toggle
const mobileMenuButton = document.getElementById('mobileMenuButton');
const mobileMenu = document.getElementById('mobileMenu');

mobileMenuButton.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Mobile categories dropdown toggle

const mobile_categories = document.querySelector('#mobile-nav')
function show_categories(){
    if (mobile_categories.classList.contains('hidden')){
        mobile_categories.classList.replace('hidden', 'block');
    }else{
        mobile_categories.classList.replace('block', 'hidden');
    }
}





// Desktop categories dropdown
const categoriesDropdown = document.getElementById('categoriesDropdown');
const dropdownContent = document.getElementById('dropdownContent');
let timeoutId;

function showDropdown() {
    clearTimeout(timeoutId);
    dropdownContent.classList.remove('opacity-0', 'invisible');
    dropdownContent.classList.add('opacity-100', 'visible');
}

function hideDropdown() {
    timeoutId = setTimeout(() => {
        dropdownContent.classList.remove('opacity-100', 'visible');
        dropdownContent.classList.add('opacity-0', 'invisible');
    }, 300); // 300ms delay before hiding
}

categoriesDropdown.addEventListener('mouseenter', showDropdown);
categoriesDropdown.addEventListener('mouseleave', hideDropdown);
dropdownContent.addEventListener('mouseenter', showDropdown);
dropdownContent.addEventListener('mouseleave', hideDropdown);

const search_input = document.querySelector('#search')
function search_product(event){
    event.preventDefault()

    window.location.href = `/products/${search_input.value}`    
}


const userMenuButton = document.getElementById('userMenuButton');
const userMenu = document.getElementById('userMenu');   
const userEmail = document.getElementById('userEmail');

// Toggle dropdown
userMenuButton.addEventListener('click', () => {
    userMenu.classList.toggle('hidden');
});

// Close dropdown when clicking outside
document.addEventListener('click', (event) => {
    if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
        userMenu.classList.add('hidden');
    }
});