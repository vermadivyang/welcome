function sendEmail() {
	Email.send({
	Host: "smtp.gmail.com",
	Password : "^|0m(^rpet|)V",
	Username : "DivyangVerma.26@gmail.com",
	To : 'DivyangVerma.26@gmail.com',
	From : "DivyangVerma.26@gmail.com",
	Subject : "Test123",
	Body : "hello",
	}).then(
		message => alert("mail sent successfully")
	);
}