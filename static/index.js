console.log("start")
let temperatureElement = document.getElementById("temperature");
let humidityElement = document.getElementById("humidity");

const xhr = new XMLHttpRequest();

xhr.responseType = "json";
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 200) {
    const data = xhr.response;
    console.log(data);
    if(data) {
      temperatureElement.innerHTML=data.temperature;
      humidityElement.innerHTML = data.humidity;
    }
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};

setInterval(()=> {
  xhr.open("GET", "/dht");
  xhr.send();
}, 5000)
