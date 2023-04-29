// if backdrop clicked then hide all modal and backdrop
$('.backdrop').click(function(){
	$(".modal-login").hide()
	$(".modal-signup").hide()
	$('.backdrop').hide()
})

$(".login-trigger").click(function(){
	event.preventDefault()
	$(".modal-login").toggle()
	$('.backdrop').toggle()
})

$(".signup-trigger").click(function(){
	event.preventDefault()
	$(".modal-signup").toggle()
	$('.backdrop').toggle()
})
