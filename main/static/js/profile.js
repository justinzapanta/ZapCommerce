const auth_form = document.querySelector('#auth-form')
const new_password = document.querySelector('#new_password')
const notif = document.querySelector('#notif')
const current_passowrd = document.querySelector('#current_passowrd')
const current_password_notif = document.querySelector('#current_password_notif')

async function submit_form() {
    if (String(new_password.value).length >= 8){
        notif.classList.add('hidden')

        const response = await fetch('/api/profile/verify/password', {
            method : 'POST',
            headers : {'Content-Type' : 'application/json'},
            body : JSON.stringify({current_password : current_passowrd.value})
        })
        
        const response_json = await response.json()

        if (response_json.message === 'Invalid Password'){
            current_password_notif.textContent = response_json.message
        }else{
            auth_form.submit()
        }
        console.log()
    }else{
        notif.classList.remove('hidden')
    }
}



async function profile_pic_uploaded(this_){
    const image = document.querySelector(`#${this_.id}`)
    
    if (image.files[0]){
        form_data = new FormData()
        form_data.append('profile_picture', image.files[0])

        const response = await fetch('/api/profile/update/profile-picture', {
            method : 'POST',
            body : form_data
        })

        location.reload()
    }
}