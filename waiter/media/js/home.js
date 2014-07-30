$(document).ready(function() {
	apendPanel();
	nav_tabs_open();	
	option_conexion_change();
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
		console.log(activeTab);
		$(activeTab).fadeIn();
	});
}

function option_conexion_change () {
	// body...	
		// $("select").change(function(event) {
		// 	 Act on the event 
		// 	console.log($(this).text());
		// });
	$("select").change(function () {		
		$( "select option:selected" ).each(function() {			
			var valor = $(this).val();
			$(".formulario").hide();
			if (valor == '0') {
				$("#localdb").show();
			};
			if (valor == '1') {
				$("#conexiondb").show();
			};
			if (valor == '2') {
				$("#webservicesdb").show();
			};			
		});		
	}).change();


}