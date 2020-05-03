const app = document.getElementById('COVID');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'https://corona-api.com/countries/us', true);
request.onload = function () {

//"confirmed":1119176,"recovered":158287,"critical":15151

  // Begin accessing JSON data here
  var data1 = JSON.parse(this.response);
	  const card = document.createElement('div');
      card.setAttribute('class', 'card');

      const h1 = document.createElement('h1');
      h1.textContent = "Latest Covid Imformation in USA";
//death_rate":5.809750639076097,"recovery_rate":14.255519333650192,
      const p = document.createElement('p');
	  p.textContent = "Deaths: "+ data1.data.latest_data.deaths;
	  
	  card.appendChild(h1);
      card.appendChild(p);
	  
	  const q = document.createElement('p');
	  q.textContent = "confirmed: "+ data1.data.latest_data.confirmed;
	  
      card.appendChild(q);
	  
	  const e = document.createElement('p');
	  e.textContent = "recovered: "+ data1.data.latest_data.recovered;
	  
      card.appendChild(e);
	  
	  const b = document.createElement('p');
	  b.textContent = "critical: "+ data1.data.latest_data.critical;
	  
      card.appendChild(b);
	  
	  const f = document.createElement('p');
	  f.textContent = "death rate: "+ data1.data.latest_data.death_rate;
	  
      card.appendChild(f);
	  
	  const i = document.createElement('p');
	  i.textContent = "recovery rate: "+ data1.data.latest_data.recovery_rate;
	  
      card.appendChild(i);
	  
      container.appendChild(card);
      
}

request.send();