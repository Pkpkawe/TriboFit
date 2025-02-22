let video = document.getElementById('video')
let canvas = document.getElementById('canvas')
let criarButton = document.getElementById('criar')
let mediaRecorder
let chunks = []

navigator.mediaDevices.getUserMedia({video: true})
    .then(stream => {
        video.srcObject = stream
    })
    .catch(err => {
        console.log('Não foi possível acessar a câmera: ' + err)
    })
    
criarButton.addEventListener('mousedown', (event) => {
    event.preventDefault()

    navigator.mediaDevices.getUserMedia({video: true, audio: true})
    .then(stream => {
        mediaRecorder = new MediaRecorder(stream, {mimeType: 'video/webm'})

        mediaRecorder.ondataavailable = event => chunks.push(event.data)

        mediaRecorder.onstop = () => {
            const blob = new Blob(chunks, {type: 'video/webm'})
            let formData = new FormData()

            formData.append('video', blob, 'video.webm')

            fetch('/User/Create/PreviewCreate/', {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log("Imagem enviado com sucesso")
                    location.href = `/User/Create/Edit/?url=${data.url}&type=Video`
                })
                .catch(error => console.error(error))
            
        }

        mediaRecorder.start()
    })
})
    
criarButton.addEventListener('mouseup', () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop()
    } else {
        canvas.width = video.videoWidth
        canvas.height = video.videoHeight
        
        const ctx = canvas.getContext('2d')
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
        
        
        canvas.toBlob(blob => {
            let formData = new FormData()
            formData.append('image', blob, "imagem.png")
            
            fetch('/User/Create/PreviewCreate/', {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log("Imagem enviado com sucesso")
                location.href = `/User/Create/Edit/?url=${data.url}&type=Image`
            })
            .catch(error => console.error(error))
        })
    }
})

criarButton.addEventListener('click', (event) => {
    event.preventDefault()
})

