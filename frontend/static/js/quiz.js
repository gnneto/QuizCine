$(document).ready(function() {
    $('form').on('submit', function(e) {
        var hasEmpty = false;
        $('input:radio').each(function() {
            var name = $(this).attr("name");
            if($("input:radio[name="+name+"]:checked").length == 0) {
                hasEmpty = true;
            }
        });
        if(hasEmpty) {
            e.preventDefault();
            $('#mensagemErro').text('Por favor, responda a todas as perguntas.').show();
        }
    });
});