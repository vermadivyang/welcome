//fact file about me
const app = document.getElementById('fact');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'infromation.json', true);
request.onload = function () {
document.getElementById("Border").style.border = "thick solid green";

  // Begin accessing JSON data here
  var myObj, a;
  var myObj, b;
  var myObj, c;
  var myObj, d;
  var myObj, e;
  var myObj, f;
  var myObj, g;
	myObj = {
		"full_name":"Divyang Verma",
		"Age":"10",
		"hobbies":"Science, Math, Piano, playing with Deetya, ...",
		"sibilings":"Deetya, age:2",
		"school":"brown elementey",
		"grade":"4th",
		"games":"None",
	};
	a = myObj.full_name;
	b = myObj.Age;
	c = myObj.hobbies;
	d = myObj.sibilings;
	e = myObj.school;
	f = myObj.grade;
	g = myObj.games;
	
	document.getElementById("about1").innerHTML = "Full name:  "+a;
	document.getElementById("about2").innerHTML = "Age:  "+b;
	document.getElementById("about3").innerHTML = "Hobbies:  "+c;
	document.getElementById("about4").innerHTML = "Sibling:  "+d;
	document.getElementById("about5").innerHTML = "School:  "+e;
	document.getElementById("about6").innerHTML = "Grade:  "+f;
	document.getElementById("about7").innerHTML = "Games:  "+g;
	
	  // <!-- var aLink = document.createElement('a');   -->
      // <!-- var link = document.createTextNode("Corona-API");  -->
	  // <!-- aLink.appendChild(link);     -->
	   // <!-- aLink.href = "https://corona-api.com/countries/us";  	   -->
	   // <!-- card.appendChild(aLink); -->
	  
      container.appendChild(card);
}
request.send();
		