$(document).ready(function() {
	
	// MÉTODOS DEPURADOS
	limpiarModales();

	//  >> ABRE EL MODAL CON LOS DATOS DE LA FILA SELECCIONADA
	modalActualizarOpen('.call');	
	modalOpenDataArea('.editArea');
	// >> ABRE EL MODAL CON LOS DATOS DE LA FILA SELECCIONADA
	modalDatosEliminar('.delete', 'Categoria');
	modalDatosEliminar('.delete', 'Area');

	// >>BORRA LOS MENSAJES DE ERROR CADA QUE SE ABRE UN MODAL 
	eliminarHtml('.call', '#id_mensaje_categoria small');
	eliminarHtml('.editArea', '#id_mensaje_area small');

	// >> FUNCIONES DE CRUD CON AJAX 
	
	// CATEGORIA
	add_categoria($('#add_categorie_form'),'#categorieModal', '/add/new/categorie/');	
	update_categoria($('.formulario'),'#editCategorieModal', '/update/categorie/');	
	deleteCategoria('#frmEliminar', '#tabla_categorias', '#deleteCategorieModal');	
	
	// AREA DE PRODUCCION
	add_area($('#add_production_area_form'),'#areaModal', '/new/area/');	
	update_area($('.formularioArea'),'#editAreaModal', '/update/area/');	
	deleteArea('#frmEliminarArea', '#tabla_areas', '#deleteAreaModal');	


});

// LIMPIA LOS CAMPOS DE LOS MODALES CADA QUE UNA VENTANA MODAL SE CIERRA
function limpiarModales () {	
	$('body').on('hidden.bs.modal', '.modal', function () {		
		$(this).removeData('bs.modal');		
		
	});		
}

// idAccionador=Quien dispara el evento
// idParteEliminar=Id de la parte a eliminar en el HTML
function eliminarHtml (idAccionador, idParteEliminar) {
	$(idAccionador).click(function(event) {
		$(idParteEliminar).remove();
	});
}

// CARGA AL MODAL LOS DATOS DE LA FILA SELECCIONADA
function modalActualizarOpen (idModal) {
	
	$(document.body).on('click', idModal, function(){
		console.log($(this));
		var data_id = $(this).data('id');	
		$('#id_mensaje_categoria'+data_id+' small').remove();		
		$('#editCategorieModal'+data_id+' #id_nombre').val($(this).data('nombre'));		
	});	
}


// CARGA AL MODAL DE AREA LOS DATOS DE LA FILA SELECCIONADA
function modalOpenDataArea (idModal) {
	$(document.body).on('click', idModal, function(){	
		var data_id = $(this).data('id');	
		var data_nombre = $(this).data('nombre');
		$('#id_mensaje_area'+data_id+' small').remove();		
		$('#editAreaModal'+data_id+' #id_nombre').val(data_nombre);		
	});	
}

function show_modal_categorie (idForm) {
	$(document.body).on('click', '.delete', function(){
		console.log("cliquea delete");
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

function modalDatosEliminar (modalDelete, clave) {
	$(document.body).on('click', modalDelete, function(){
		var id = $(this).data('id');
		var nombre = $(this).data('nombre');		
		$('#modal_id'+clave).val(id);
		$('#modal_name').text(nombre);
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
				if (response.mensaje) {
					alert(response.mensaje);
				}else{
					alert("Lo sentimos, hubo un error al eliminar.");
				};				
			}
			$(idModal).modal('hide');
		}
	};	
	$(idForm).ajaxForm(options);		
}



function add_area (idForm, idModal, url_rest) {				
	idForm.on('submit', function(event) {		
		event.preventDefault();
		var json = $(this).serialize();
		console.log(json)
		$.post(url_rest, json, function(data) {
			/*optional stuff to do after success */
			if (data.respuesta) {	
				$(idModal).modal('hide');
				location.reload();				
			}else{
				var mensaje = '<small><div class="alert alert-danger mensaje">' +
				'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
				'</div></small>';
				$('#id_mensaje_area').html(mensaje);				
				$.each(data.errores, function(index, element){					
					var mensajes_error = '<span>' + element+ '</span>';										
					// index... da los atributos
					$(".mensaje").append(mensajes_error);					
				});
			}			
		});
	});
}

function update_area (idForm, idModal, url_rest) {
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
				var mensaje = '<small><div class="alert alert-danger mensaje">' +
				'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
				'</div></small>';
				$('#id_mensaje_area'+data_id).html(mensaje);				
				$.each(data.errores, function(index, element){					
					var mensajes_error = '<span>' + element+ '</span>';										
					// index... da los atributos
					$(".mensaje").append(mensajes_error);					
				});
			}
		});		
	});
}

function deleteArea (idForm, idTabla, idModal) {
	var options ={
		url : '/delete/area/',
		success: function(response){
			if (response.status=="True") {
				var idArea = response.area_id;
				var elementos = $(idTabla + ' >tbody >tr').length;
				if (elementos==1) {
					location.reload();
				}else{
					$('#tr'+idArea).remove();					
				}
			}else{				
				if (response.mensaje) {
					alert(response.mensaje);
				}else{
					alert("Lo sentimos, hubo un error al eliminar.");
				};				
			}
			$(idModal).modal('hide');
		}
	};	
	$(idForm).ajaxForm(options);		
}


