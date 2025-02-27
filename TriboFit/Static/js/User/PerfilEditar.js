const cancelarButton = document.getElementById('cancelar_editar')
const editarButton = document.getElementById('editar')
const salvarButton = document.getElementById('salvar')
const divInputFile = document.getElementById('input_file')
const inputDescription = document.getElementById('description')
const inputFile = document.getElementById('edit_image_perfil')
let file
let contagemChanges = 0

editarButton.addEventListener('click', () => {
    editarButton.style.display = 'none'
    cancelarButton.style.display = 'flex'
    salvarButton.style.display = 'flex'
    divInputFile.style.display = 'block'
    inputDescription.style.border = 'solid 1px #b5b5b5'
    inputDescription.style.background = '#f3f3f3'
    inputDescription.disabled = false
})

inputFile.addEventListener('change', () => {
    const image = document.getElementById('Imagem_PerfilInfo')
    const testFile = inputFile.files[0]

    if (!testFile) {
        return
    } else {
        if (testFile.type.startsWith("image/")) {
            if (contagemChanges == 0){
                file = testFile
                image.src = URL.createObjectURL(file)
                contagemChanges += 1
            } else {
                URL.revokeObjectURL(file)
                file = testFile
                image.src = URL.createObjectURL(file)
            }
        }
    }

    
})

cancelarButton.addEventListener('click', () => {
    location.reload()
})

salvarButton.addEventListener('click', () => {
    const description = document.getElementById('description').value
    console.log(file)
    let formData = new FormData()
    formData.append('description', description)
    
    if (file) {
        formData.append('image_perfil', file)
    }

    fetch('/User/Perfil/Update/', {
        method: "PATCH",
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            location.reload()
        })
        .catch(error => console.log(error))
    
})

