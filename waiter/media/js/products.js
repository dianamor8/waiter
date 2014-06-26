$(document).ready(function() {
	show_modal_categorie('call');
	add_categoria($('#add_categorie_form'),'#categorieModal', '/add/new/categorie/')
});

// CATEGORIE
function show_modal_categorie (idForm) {
	$(".call").click(function(event) {		
		// console.log($(this).attr('data-id'));
		// $("#div-form-group").before('{%add_categoria '+ $(this).attr('data-id')+ '%}');
		console.log('{%add_categoria '+ $(this).attr('data-id')+'%}');
	});
}

function add_categoria (idForm, idModal, url_rest) {
	
	idForm.on('submit', function(event) {
		console.log("entra1")
		event.preventDefault();
		var json = $(this).serialize();
		$.post('/add/new/categorie/', json, function(data) {
			/*optional stuff to do after success */
			if (data.respuesta) {
				$(idModal).modal('hide');
				$('tbody tr').remove();
				$.each(data.tabla, function(index, val) {
					$('tbody').append(val.tabla);
				});
			}else{
				console.log("NO ESTA HACIENDO BIEN");
			}			
		});
		
	});
}

function limpiar_campos(campos){
	$(campos).val('');
}