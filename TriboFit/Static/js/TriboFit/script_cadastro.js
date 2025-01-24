document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('Form_Cadastro')

    if (form) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault()

            const name = document.getElementById('name_cadastro').value
            const email = document.getElementById('email_cadastro').value
            const password = document.getElementById('password_cadastro').value
            const confirm_password = document.getElementById('confirm_password_cadastro').value
            const telephone = null
            const date_birth = null

            const data = {name, email, password, telephone, date_birth}

            if (password === confirm_password) {
                try {
                    const response = await fetch('/User/', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(data),

                    })

                    if (response.ok) {
                        window.location.href = '/User/Home/'
                    } else {
                        const errorData = await response.json()
                        console.error('Erro:' + errorData)
                        alert("Erro ao cadastrar usuário, tente novamente.")

                    }
                } catch (error) {
                    console.error('Erro na requisição:', error)

                }
            } else {
                alert('Senha e Confirmar Senha diferentes!')
            }
            

        })
    } else {
        console.error("Formulário não encontrado!")
    }
})