
console.log(googleKey)
const propNum = document.getElementById("title")
const propertyNum = propNum.getAttribute("prop_num")

fetch(`http://127.0.0.1:8000/api/property/${propertyNum}`)
  .then(response => response.json())
  .then(data => {
    // console.log(data.latitude, data.longitude)
    const latX= data.latitude
    const lngX= data.longitude
    initMap(latX, lngX)
  });

function initMap(latX, lngX) {
  const location = { lat: latX, lng: lngX };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: location,
  });
  const marker = new google.maps.Marker({
    position: location,
    map: map,
  });
}   
