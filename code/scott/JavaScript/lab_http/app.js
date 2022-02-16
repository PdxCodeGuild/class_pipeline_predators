console.log('working')
const btn = document.querySelector("button");
const body = document.querySelector("body");
function getKitty() {
    fetch("https://api.thecatapi.com/v1/images/search")
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        let image = document.createElement("img");
        image.src = data[0].url;
        body.appendChild(image);
    });
}
btn.addEventListener("click", getKitty);
