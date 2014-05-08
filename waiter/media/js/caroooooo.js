
$(document).ready(function() {
	
	var velocidad = 5000;
	var run = setInterval('rotate()',speed);

	var item_whidth = $(".carousel-indicators li").outerWidth();
	var left_value  = item_whidth * (-1);

	$(".carousel-indicators li:first").before($(".carousel-indicators li:last"));
	$("ol").css({'left': 'left_value'});

	$("#prev").click(function() {
		var left_indent = parseInt($("ol").css('left'))+item_whidth;
		$("ol").animate({"left": left_indent},200, function() {
			$(".carousel-indicators li:first").before($(".carousel-indicators li:last"));
			$("ol").css({'left': 'left_value'});
		});
		return false;
	});

	$("#next").click(function() {
		var left_indent = parseInt($("ol").css('left'))-item_whidth;
		$("ol").animate({"left": left_indent},200, function() {
			$(".carousel-indicators li:last").before($(".carousel-indicators li:first"));
			$("ol").css({'left': 'left_value'});
		});
		return false;	
	});

	$(".carousel-inner").hover(function() {
		clearInterval(run);
	}, function() {
		run = setInterval('rotate()',speed);
	});
});

function rotate () {
	$("#next").click();
}