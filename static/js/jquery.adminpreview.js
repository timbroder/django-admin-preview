$(document).ready(function(){
	$(".previewslide").click(function(){
		$.ajax({
			url:$(this).attr('id'),
			context: $(this).parent().parent(),
			success:function(data){
				var $html = $(data);
				$('.previewed').each(function(){
					$(this).remove();
				});
				
				if(!$html.hasClass('previewed')){
					$html.addClass('previewed');
				}
				
				$html.addClass($(this.context).attr('class'));		
				$(this.context).after($html);
			}
		});
	});
});
