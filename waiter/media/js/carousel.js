$(document).ready(function() {
	var velocidad = 5000;
	var run = setInterval('activarCarrusel()', velocidad);

	$("#next").click(function() {
		var indiceActivo = parseInt($(".item.active").data("slideto"));
		var nuevoIndice = indiceActivo+1;
		if (calcularImagenes()==indiceActivo+1) {
			var nuevoIndice = 0;			
		};		
		$("#img"+indiceActivo).removeClass('active');		
		$("#img"+nuevoIndice).addClass('active');
		$("#li"+indiceActivo).removeClass('active');
		$("#li"+nuevoIndice).addClass('active');
	});
	anterior();
});

function calcularImagenes () {
	var nroImagenes = $(".carousel-indicators li").size();	
	return nroImagenes;
}

function siguiente() {	
	$("#next").click(function() {
		var indiceActivo = parseInt($(".item.active").data("slideto"));
		var nuevoIndice = indiceActivo+1;
		if (calcularImagenes()==indiceActivo+1) {
			var nuevoIndice = 0;			
		};

		$("#img"+indiceActivo).removeClass('active');		
		$("#img"+nuevoIndice).addClass('active');
		$("#li"+indiceActivo).removeClass('active');
		$("#li"+nuevoIndice).addClass('active');
	});
}

function anterior() {	
	$("#prev").click(function() {
		var indiceActivo = parseInt($(".item.active").data("slideto"));
		var nuevoIndice = indiceActivo-1;
		if (indiceActivo==0) {
			var nuevoIndice = calcularImagenes()-1;			
		};		
		
    	$("#img"+nuevoIndice).addClass('active');	    		
		$("#li"+indiceActivo).removeClass('active');
		$("#li"+nuevoIndice).addClass('active');		

	});
}

function activarCarrusel () {	
	$("#next").click();
}		


function changeImage(idName){
	var nroImagen = parseInt(idName);
	var indiceActivo = parseInt($(".item.active").data("slideto"));
	$("#img"+indiceActivo).removeClass('active');		
	$("#img"+nroImagen).addClass('active');
	$("#li"+indiceActivo).removeClass('active');
	$("#li"+nroImagen).addClass('active');		
}
