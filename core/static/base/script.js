// if backdrop clicked then hide all modal and backdrop
$('.backdrop').click(function(){
	$(".modal-login").hide()
	$(".modal-signup").hide()
	$('.backdrop').hide()
})

// if login button clicked then show modal for login and backdrop
$(".login-trigger").click(function(){
	event.preventDefault() // prevent the button to function normally
	$(".modal-login").toggle()
	$('.backdrop').toggle()
})

// if signup button clicked then show modal for signup and backdrop
$(".signup-trigger").click(function(){
	event.preventDefault() // prevent the button to function normally
	$(".modal-signup").toggle()
	$('.backdrop').toggle()
})
