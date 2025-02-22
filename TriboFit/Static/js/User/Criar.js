const conteudo = document.getElementById('conteudo')
const params = new URLSearchParams(location.search)
const url = params.get('url')
const tipo = params.get('type')
const button = document.getElementById('button')
let extensao
let post

fetch(url)
    .then(response => response.blob())
    .then(data => {
        post = data
        executarRestante(data)
    })
    .catch(error => console.error(error))

function executarRestante(post_blob) {
    if (tipo === 'Image') {
        extensao = 'png'
        const imageField = document.createElement('img')
        imageField.id = 'post'
        imageField.src = URL.createObjectURL(post_blob)

        conteudo.appendChild(imageField)
    } else if (tipo === 'Video') {
        extensao = 'webm'
        const videoField = document.createElement('video')
        videoField.id = 'post'
        videoField.src = URL.createObjectURL(post_blob)
        videoField.setAttribute("controls", "")

        conteudo.appendChild(videoField)
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form')

    if (form) {
        button.addEventListener('click', async (event) => {
            event.preventDefault()

            const title = document.getElementById('title').value
            const description = document.getElementById('description').value
            const tags = document.getElementById('tags').value

            let formData = new FormData()
            /* const file = new File([post], `post.${extensao}`, {type: post.type}) */

            formData.append('post', post, `post.${extensao}`)
            formData.append('title', title)
            formData.append('description', description)
            /* formData.append('tags', tags) */
            console.log(formData)

            try {
                response = await fetch('/Post/CreatePost/', {
                    method: 'POST',
                    body: formData,
                })
                
                if (response.ok) {
                    const responseData = await response.json()
                    console.log(responseData)
                    location.href = '/User/Perfil/'
                } else {
                    const errorData = await response.json()
                    console.error('Erro:', errorData)
                    alert('Erro ao criar postagem, tente novamente.')
                }
            } catch (error) {
                console.error('Erro na requisição:', error)
            }
                
        })
        
    } else {
        console.error("Formulário não encontrado!")
    }
})