// Desktop categories dropdown
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