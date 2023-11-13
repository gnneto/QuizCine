$(document).ready(function(){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}")
            }
        }
    });

    $.get("http://127.0.0.1:8000/apifilme/", function(data, status){
        data.forEach(function(filme, index){
            var filmeDiv = $("<div class='card my-2'></div>");
            filmeDiv.append("<h5 class='card-header' data-toggle='modal' data-target='#filmeModal' data-index='"+index+"'>"+filme.titulo+"</h5>");
            $("#filmes").append(filmeDiv);
        });

        $('#filmeModal').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget);
            var index = button.data('index');
            var filme = data[index];
            var modal = $(this);
            modal.find('.modal-title').text(filme.titulo);
            var bodyHtml = "<p><strong>Gêneros:</strong> " + filme.generos + "</p>" +
                           "<p><strong>Avaliação:</strong> " + filme.avaliacao + "</p>" +
                           "<p><strong>Diretor:</strong> " + filme.diretor + "</p>" +
                           "<p><strong>Data de lançamento:</strong> " + filme.data_lancamento + "</p>" +
                           "<p><strong>Descrição:</strong> " + filme.descricao + "</p>";
            for (var plataforma in filme.links) {
                if (filme.links[plataforma]) {
                    bodyHtml += "<button onclick=\"window.location.href='" + filme.links[plataforma] + "'\">" + plataforma + "</button>";
                }
            }
            modal.find('.modal-body').html(bodyHtml);
            $("#editarFilme").data('id', filme.id);
            $("#deletarFilme").data('id', filme.id);
        });

        $.get('/is_authenticated/', function(data) {
            if (data.is_authenticated) {
                // usuario autenticado
                $("#editarFilme").show();
                $("#deletarFilme").show();
            } else {
                // usuario nao autenticado
                $("#editarFilme").hide();
                $("#deletarFilme").hide();
            }
        });

        $("#deletarFilme").click(function(){
            var id = $(this).data('id');
            $.ajax({
                url: 'http://127.0.0.1:8000/apifilme/' + id + '/',
                type: 'DELETE',
                success: function(result) {
                    location.reload();
                }
            });
        });

        $("#editarFilme").click(function(){
            var id = $(this).data('id');
            var novoTitulo = prompt("Digite o novo título do filme:");
            if (novoTitulo != null) {
                $.ajax({
                    url: 'http://127.0.0.1:8000/apifilme/' + id + '/',
                    type: 'PUT',
                    data: JSON.stringify({titulo: novoTitulo}),
                    contentType: 'application/json; charset=utf-8',
                    dataType: 'json',
                    success: function(result) {
                        location.reload();
                    }
                });
            }
        });
    });
});