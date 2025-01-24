window.onload = function() {
    let Entrar = document.getElementById("Entrar")
    let Cadastrar = document.getElementById("Cadastrar")
    let FormCadastro = document.getElementById('Form_Cadastro')
    let FormLogin = document.getElementById('Form_Login')
    var event_login_click = false
    var event_cadastro_click = true

    Entrar.addEventListener('mouseenter', () => {
        Cadastrar.style.backgroundColor = 'white' // Cadastrar Desativado
        Cadastrar.style.color = 'black'

        Entrar.style.backgroundColor = '#29C31B' // Entrar Ativado
        Entrar.style.color = 'white'

    })
    
    Entrar.addEventListener('click', () => {
        FormCadastro.style.display = 'none'
        FormLogin.style.display = 'flex'
        event_login_click = true
    })
    
    Entrar.addEventListener('mouseout', () => {
        if (!event_login_click) {
            Entrar.style.backgroundColor = 'white' // Entrar Desativado
            Entrar.style.color = 'black'

            Cadastrar.style.backgroundColor = '#29C31B' // Cadastrar Ativado
            Cadastrar.style.color = 'white'

            event_cadastro_click = true
        } else {
            event_cadastro_click = false
        }
    })

    Cadastrar.addEventListener('mouseenter', () => {
        Cadastrar.style.backgroundColor = '#29C31B' // Cadastrar Ativado
        Cadastrar.style.color = 'white'

        Entrar.style.backgroundColor = 'white' // Entrar Desativado
        Entrar.style.color = 'black'
    })
    
    Cadastrar.addEventListener('click', () => {
        FormCadastro.style.display = 'flex'
        FormLogin.style.display = 'none'
        event_cadastro_click = true
    })
    
    Cadastrar.addEventListener('mouseout', () => {
        if (!event_cadastro_click) {
            Cadastrar.style.backgroundColor = 'white' // Cadastrar Desativado
            Cadastrar.style.color = 'black'

            Entrar.style.backgroundColor = '#29C31B' // Entrar Ativado
            Entrar.style.color = 'white'

            event_login_click = true
        } else {
            event_login_click = false
        }
    })
}
/*
Cadastrar.style.backgroundColor = '#29C31B' // Cadastrar Ativado
Cadastrar.style.color = 'white'

Entrar.style.backgroundColor = 'white' // Entrar Desativado
Entrar.style.color = 'black'

Cadastrar.style.backgroundColor = 'white' // Cadastrar Desativado
Cadastrar.style.color = 'black'

Entrar.style.backgroundColor = '#29C31B' // Entrar Ativado
Entrar.style.color = 'white'

*/