$(document).ready(function() {
	apendPanel();
	nav_tabs_open();	
	option_conexion_change();
	test_conexion($("#form_conexion"));
	validate_formulario();		
	mensajes_espaniol();
	test_conexion ($('#btn_test'), '/test_conexion/');	
});

function mensajes_espaniol (argument) {
	// body...
	$.extend(jQuery.validator.messages, {
		required: "Este campo es requerido.",
		// remote: "Please fix this field.",
		// email: "Please enter a valid email address.",
		// url: "Please enter a valid URL.",
		// date: "Please enter a valid date.",
		// dateISO: "Please enter a valid date (ISO).",
		// number: "Please enter a valid number.",
		// digits: "Please enter only digits.",
		// creditcard: "Please enter a valid credit card number.",
		// equalTo: "Ingresa el mismo valor.",
		// accept: "Please enter a value with a valid extension.",
		// maxlength: $.validator.format("Please enter no more than {0} characters."),
		// minlength: $.validator.format("Please enter at least {0} characters."),
		// rangelength: $.validator.format("Please enter a value between {0} and {1} characters long."),
		// range: $.validator.format("Please enter a value between {0} and {1}."),
		// max: $.validator.format("Please enter a value less than or equal to {0}."),
		// min: $.validator.format("Please enter a value greater than or equal to {0}.")
	});
}
   


// apertura de tabs de panel 
function apendPanel () {
	$(".contenido").hide();
	$("ul.nav-tabs li:first").addClass('active').show();
	$(".contenido:first").show();
}

// clic en cada tabs de panel
function nav_tabs_open () {
	$("ul.nav-tabs li").click(function(event) {
		$("ul.nav-tabs li").removeClass('active');
		$(this).addClass('active');
		$(".contenido").hide();
		var activeTab= $(this).find('a').attr('href');		
		$(activeTab).fadeIn();
	});
}

function option_conexion_change () {
	$("#id_fuente").change(function () {
		// $( "select option:selected" ).each(function() {			
		$(this).find("option:selected").each(function () {
    		$(".formulario").hide();
			var valor = $(this).val();			
			if (valor == '') {
				console.log("sin valor");
			};
			if (valor == '0') {
				$("#localdb").show();
			};
			if (valor == '1') {
				$("#conexiondb").show();
				var form = $('#form_conexion');				
			};
			if (valor == '2') {
				$("#webservicesdb").show();
			};			
		});		
	}).change();

}

function test_conexion (idForm) {
	// form_conexion
	console.log("entrando");
	idForm.on('submit', function(event) {
		event.preventDefault();
		var json = $(this).serialize();
		console.log(json);
	});

}

function validate_formulario () {
	var form = $('#form_conexion');
	form.validate({
		rules: {
			'database': {
				required: true,					
			},
			'userdb': {
				required: true,					
			},
			'host': {
				required: true,					
			},
			'port': {
				required: true,					
			},
		}
	});
	form.bind('change keyup', function() {
		jQuery('#form_conexion').validate();
		console.log("valido: " + form.valid());		
		if (jQuery('#form_conexion').valid()) {
			$('#btn_test').removeAttr("disabled");
		}else{
			$('#btn_test').attr('disabled', 'disabled'); 
		};
	});    
}

function test_conexion (idButton, url_rest) {
	$('#btn_test').click(function(event) {	
		var json = $('#form_conexion').serialize();		
		// $.post(url_rest, json, function(data) {
		// 	/*optional stuff to do after success */
		// 	if (data.respuesta) {
		// 		var mensaje = '<small><div class="alert alert-danger mensaje">' +
		// 		'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
		// 		'</div></small>';
		// 		$('#id_mensaje_test').html(mensaje);
		// 		$('.mensaje').append(data.respuesta);			
		// 		alert('esta correcto');
		// 	}else{
		// 		alert('no esta correcto');			
		// 	};
		// });

		$.ajax({			
			url: /test_conexion/,
			type: 'POST',
			dataType: 'json',
			data: json, 'csrfmiddlewaretoken': '{{ csrf_token }}',
			success: function(data){
				console.log('Success jijij!');
				var mensaje = '<small><div class="alert alert-danger mensaje">' +
				'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
				'</div></small>';
				$('#id_mensaje_test').html(mensaje);
				$('.mensaje').append(data.respuesta);
			}            
		});		
		return false;
		// .done(function(data) {			
		// 	var mensaje = '<small><div class="alert alert-danger mensaje">' +
		// 		'<button type="button" class="close" data-dismiss="alert">&times;</button>'+
		// 		'</div></small>';
		// 	$('#id_mensaje_test').html(mensaje);
		// 	$('.mensaje').append(data.respuesta);			
		// })
		// .fail(function() {
		// 	console.log("error");
		// })
		// .always(function() {
		// 	console.log("complete");
		// });
		
	});
}

	