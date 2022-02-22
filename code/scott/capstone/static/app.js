console.log('hello')
const propNum = document.getElementById("title")
const propertyNum = propNum.getAttribute("prop_num")

fetch(`http://127.0.0.1:8000/api/property/${propertyNum}`)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    const { latX, lngX } = data
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
