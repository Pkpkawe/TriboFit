document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('Form_Login')

    if (form) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault()

            const email = document.getElementById('email_login').value
            const password = document.getElementById('password_login').value

            const data = {email, password}

            try {
                const response = await fetch('/User/Entrar/', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data),

                })

                if (response.ok) {
                    window.location.href = '/User/Home/'
                } else {
                    const errorData = await response.json()
                    console.error('Erro:' + errorData)
                    alert("Erro ao authenticar usuário, tente novamente.")

                }
            } catch (error) {
                console.error('Erro na requisição:', error)

            }
        

        })
    } else {
        console.error("Formulário não encontrado!")
    }
})