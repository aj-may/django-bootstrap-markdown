$(document).ready(function() {
	$('.md-edit textarea').tabby({tabString:'    '});

	function updateMarkdown() {
		$('.md-edit').each(function() {
			$(this).find('.preview').html( marked( $(this).find('textarea').val() ) );
		})
	}
	updateMarkdown();

	$('.md-edit textarea').keyup(function() {
		updateMarkdown();
	})

	$('.md-edit textarea').change(function() {
		updateMarkdown();
	})

	$('.md-edit').each(function() {
		$(this).find('textarea').scroll(function(e) {
			var percent = $(this).scrollTop() / ( $(this)[0].scrollHeight-$(this).height() );
			var preview = $(this).parent().parent().find('.preview');
			preview.scrollTop( (preview[0].scrollHeight - preview.height()) * percent );
		});
	});
})