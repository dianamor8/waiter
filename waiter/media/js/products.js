var id_modal;
$(document).ready(function() {
	//show_modal_categorie('.call');
	add_categoria($('#add_categorie_form'),'#categorieModal', '/add/new/categorie/');
	modalDatosEliminar('.delete');
	update_categoria($('.formulario'),'#editCategorieModal', '/update/categorie/');	
	deleteCategoria('#frmEliminar', '#tabla_categorias', '#deleteCategorieModal');
	modalAgregarOpen('#modalAgregar');
	modalActualizarOpen('.call');
	$('body').on('hidden.bs.modal', '.modal', function () {
		console.log('cada que cierra');
		$(this).removeData('bs.modal');

	});
});


function modalAgregarOpen (idModal) {
	$(idModal).click(function(event) {
		$('#id_mensaje_categoria small').remove();		

	});	
}



function modalActualizarOpen (idModal) {
	// $(idModal).click(function(event) {
	// 	var data_id = $(this).data('id');		
	// 	$('#id_mensaje_categoria'+data_id+' small').remove();

	// 	$('#editCategorieModal'+data_id).removeData();
	// });	

	$(document.body).on('click', idModal, function(){
		var data_id = $(this).data('id');		
		$('#id_mensaje_categoria'+data_id+' small').remove();
		$('#id_nombre').val($(this).data('nombre'));	
	});	
}


function show_modal_categorie (idForm) {
	$(document.body).on('click', '.delete', function(){
		console.log("cliquea delete");
	// $(idForm).click(function(event) {				
	// 	// console.log('invocando modal '+ $(this).attr('data-target'));
	// 	// id_modal = $(this).attr('data-id');
	// 	console.log("cliquea delete");
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
				$(idModal).modal('hide');
				location.reload();				
				// $('tbody tr').remove();
				// $.each(data.tabla, function(index, val) {
				// 	$('tbody').append(val.tabla);
				// });
			}else{
				var mensaje = '<small><div class="alert alert-danger mensaje">' +
				'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
				'</div></small>';
				$('#id_mensaje_categoria').html(mensaje);				
				$.each(data.errores, function(index, element){					
					var mensajes_error = '<span>' + element+ '</span>';										
					// index... da los atributos
					$(".mensaje").append(mensajes_error);					
				});
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
				console.log("NO ESTA HACIENDO BIEN UPDATE");
				var mensaje = '<small><div class="alert alert-danger mensaje">' +
				'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
				'</div></small>';
				$('#id_mensaje_categoria'+data_id).html(mensaje);				
				$.each(data.errores, function(index, element){					
					var mensajes_error = '<span>' + element+ '</span>';										
					// index... da los atributos
					$(".mensaje").append(mensajes_error);					
				});
			}
		});		
	});
}

function limpiar_campos(campos){
	$(campos).val('');
}

function modalDatosEliminar (modalDeleteCategoria) {
	$(document.body).on('click', modalDeleteCategoria, function(){
	//$(modalDeleteCategoria).click(function(event) {				
		// console.log('invocando modal '+ $(this).attr('data-target'));	
		// event.preventDefault();
		var idCategoria = $(this).data('id');
		var nombreCategoria = $(this).data('nombre');		
		$('#modal_idCategoria').val(idCategoria);
		$('#modal_name').text(nombreCategoria);
	});	 
}

function deleteCategoria (idForm, idTabla, idModal) {
	var options ={
		url : '/delete/categorie/',
		success: function(response){
			if (response.status=="True") {
				var idCategoria = response.categoria_id;
				var elementos = $(idTabla + ' >tbody >tr').length;
				if (elementos==1) {
					location.reload();
				}else{
					$('#tr'+idCategoria).remove();					
				}
			}else{
				alert("Hubo un error al eliminar");
			}
			$(idModal).modal('hide');
		}
	};	
	$(idForm).ajaxForm(options);		
}


