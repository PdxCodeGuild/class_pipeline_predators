const img = document.querySelector("img")
console.log('start')
fetch ('https://api.thecatapi.com/v1/images/search').then(function(response){
    return response.json()
})
.then (function(data){
    img.src = data[0].url
    console.log(img)
    document.body.appendChild(img)
})
console.log('end')