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
      h1.textContent = "Latest Covid Information in USA";
//death_rate":5.809750639076097,"recovery_rate":14.255519333650192;

      const p = document.createElement('p');
	  p.textContent = "Casualties: "+ data1.data.latest_data.deaths;
	  
	  card.appendChild(h1);
      card.appendChild(p);
	  
	  const q = document.createElement('p');
	  q.textContent = "Confirmed cases: "+ data1.data.latest_data.confirmed;
	  
      card.appendChild(q);
	  
	  const e = document.createElement('p');
	  e.textContent = "Recovered: "+ data1.data.latest_data.recovered;
	  
      card.appendChild(e);
	  
	  const b = document.createElement('p');
	  b.textContent = "Critical: "+ data1.data.latest_data.critical;
	  
      card.appendChild(b);
	  
	  const f = document.createElement('p');
	  f.textContent = "Death rate: "+ data1.data.latest_data.calculated.death_rate;
	  
      card.appendChild(f);
	  
	  const i = document.createElement('p');
	  i.textContent = "Recovery rate: "+ data1.data.latest_data.calculated.recovery_rate;
	  
      card.appendChild(i);
	  
	  const j = document.createElement('p');
	  j.textContent = "Above information is real time information based on WHO api call."
	  j.textContent += "You can come back to this page at any point in time to learn more about the latest count. ";
	  j.textContent += "Information is sourced from corona-apis and here is the link if you want to learn more about it."
	 
      card.appendChild(j);
	  
	  var aLink = document.createElement('a');  
      var link = document.createTextNode("Corona-API"); 
	  aLink.appendChild(link);    
	   aLink.href = "https://corona-api.com/countries/us";  	  
	   card.appendChild(aLink);
	  
	  
	  // const k = document.createElement('p');
	  // k.textContent = ""
	  
      // card.appendChild(k);
	  
	  // const m = document.createElement('p');
	  // m.textContent = "0.0479377763158% of the world in 4 march 2020 has COVID-19 ";
	  // 
	  
      // card.appendChild(m);
	  
      container.appendChild(card);
      
}

request.send();