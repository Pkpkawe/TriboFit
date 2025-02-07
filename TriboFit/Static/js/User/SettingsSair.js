window.onload = function() {
    Sair = document.getElementById("Sair_SideBar")
    Confirmar_Sair = document.getElementById("Sair")
    Botão_Sair = document.getElementById("botao_sair")
    Botão_Cancelar = document.getElementById("botao_cancelar")

    Sair.addEventListener('click', () => {
        Confirmar_Sair.style.display = 'flex'
    })

    Botão_Cancelar.addEventListener('click', () => {
        Confirmar_Sair.style.display = 'none'
    })

    Botão_Sair.addEventListener('click', async () => {
        try {
            const response = await fetch('/User/Sair/')

            if (response.ok) {
                window.location.href = '/User/'
            } else {
                const errorData = await response.json()
                console.error('Erro:' + errorData)
                alert("Erro ao tentar sair, tente novamente.")
            }  
        } catch (error) {
            console.error('Erro na requisição:', error)
        }
    })
}