var id_modal;
$(document).ready(function() {
	
	show_modal_categorie('call');
	add_categoria($('#add_categorie_form'),'#categorieModal', '/add/new/categorie/')
	update_categoria($('.formulario'),'#editCategorieModal', '/update/categorie/')
});

function show_modal_categorie (idForm) {
	$(".call").click(function(event) {				
		// console.log('invocando modal '+ $(this).attr('data-target'));
		id_modal = $(this).attr('data-id');
	});
}

function add_categoria (idForm, idModal, url_rest) {			
	idForm.on('submit', function(event) {		
		event.preventDefault();
		var json = $(this).serialize();
		console.log(json)
		$.post(url_rest, json, function(data) {
			/*optional stuff to do after success */

			if (data.respuesta) {
				console.log("ENTRA DATA");
				$(idModal).modal('hide');
				location.reload();
				console.log("ENTRA DATA2");
				// $('tbody tr').remove();
				// $.each(data.tabla, function(index, val) {
				// 	$('tbody').append(val.tabla);
				// });
			}else{
				console.log("NO ESTA HACIENDO BIEN");
			}			
		});
		
	});
}

function update_categoria (idForm, idModal, url_rest) {
	idForm.on('submit', function(event) {							
		event.preventDefault();				
		var data_id = $(this).attr('data-id')				
		var json = $(this).serialize()+"&id="+data_id+"";				
		$.post(url_rest, json, function(data, textStatus, xhr) {			
			/*optional stuff to do after success */			
			if (data.respuesta) {				
				$(idModal+data_id).modal('hide');
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