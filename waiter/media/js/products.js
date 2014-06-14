$(document).ready(function() {
	show_modal_categorie('call');	
});

// CATEGORIE
function show_modal_categorie (idForm) {
	$(".call").click(function(event) {		
		// console.log($(this).attr('data-id'));
		// $("#div-form-group").before('{%add_categoria '+ $(this).attr('data-id')+ '%}');
		console.log('{%add_categoria '+ $(this).attr('data-id')+'%}');
	});
}