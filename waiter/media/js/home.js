$(document).ready(function() {
	apendPanel();
	nav_tabs_open();	
	option_conexion_change();
	test_conexion($("#form_conexion"));
	validate_formulario();	
});

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
				console.log("holi");
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
			'id_database': {
				required: true,					
			},
	});
	console.log("valido: " + form.valid());

// http://jqueryvalidation.org/valid
	
	// jQuery.validator.setDefaults({
	// 	debug: true,
	// 	success: "valid"
	// });

	form.bind('change keyup', function() {			
		jQuery('#form_conexion').validate();
		console.log("valido: " + form.valid());		
		if (jQuery('#form_conexion').valid()) {
			$('#btn_test').removeAttr("disabled");
		}else{
			$('#btn_test').attr('disabled', 'disabled'); 
		};
	});




	// $('#form_conexion').bind('change keyup', function() {		
		// console.log($(this));
		// $('#form_conexion').validate({
		// 	rules: {
		// 		'id_database': {
		// 			required: true,					
		// 		},
		// 	// inputEmailConfirm: {
  //               // required: true,  // <-- redundant
  //               // email: true,     // <-- redundant
  //               // equalTo: '#inputEmail'
  //           // }  // <-- removed trailing comma
  //       }});

  //       if ($('#form_conexion').validate().checkForm()) {
		// 	$('#btn_test').attr('disabled', 'disabled'); 
		// 	console.log("entra desabilitar");       
		// } else {
		// 	$('#btn_test').removeAttr("disabled");
		// 	console.log("entra5");
		// } });	
    // http://www.pedroventura.com/javascript/jquery-activar-desactivar-boton-submit-de-formulario/
    // http://stackoverflow.com/questions/1594952/jquery-disable-enable-submit-button
    // http://www.enmanosdenadie.com.ar/2012/03/validando-formularios-con-jquery-desactivar-boton-validate/
    // http://stackoverflow.com/questions/18754020/bootstrap-3-with-jquery-validation-plugin
    // http://stackoverflow.com/questions/15341747/form-validation-using-jquery-validate-js
}

	