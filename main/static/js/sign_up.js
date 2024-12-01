const email = document.querySelector('#email')
const password = document.querySelector('#password')
const confirm_password = document.querySelector('#confirm-password')
const notif = document.querySelector('#notif')
const register_form = document.querySelector('#register_form')

function sign_up(){
    if (password.value.length >=8){
        if (password.value != confirm_password.value){
            notif.textContent = "Passwords don't match"
        }else{
            if (String(email.value).includes('@gmail.com')){
                register_form.submit()
            }else{
                notif.textContent = "Your username must be a valid Gmail address ending with @gmail.com"
            }
        }
    }else{
        notif.textContent = 'Password must be at least 8 characters'
    }

}