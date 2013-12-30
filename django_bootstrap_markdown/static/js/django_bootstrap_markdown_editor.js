$(document).ready(function() {
	$('.md-edit textarea').tabby({tabString:'       '});

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

	$('.markdown-image-btn').click(function() {
		window.markdown_textarea = $(this).parent().parent().find('textarea');
		window.markdown_cursor_pos = $(window.markdown_textarea).prop('selectionStart');
		window.open('/markdown/image/');
	});

	window.markdown_image_callback = function(sized, original, alt) {
        var v = $(window.markdown_textarea).val();
        var textBefore = v.substring(0, window.markdown_cursor_pos);
        var textAfter  = v.substring(window.markdown_cursor_pos, v.length);
        $(window.markdown_textarea).val( textBefore+ "[!["+alt+"]("+sized+")]("+original+")" +textAfter );
        $(window.markdown_textarea).keyup();
	}
})