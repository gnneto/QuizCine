var script = document.createElement('script');
document.head.appendChild(script);

document.querySelector('form').addEventListener('submit', function(event) {
    var senha = document.querySelector('#senha').value;
    var confsenha = document.querySelector('#confsenha').value;
    var email = $('#email').val();

    var regexEmail = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;

    if (senha !== confsenha) {
      alert('As senhas não coincidem!');
      event.preventDefault();
    } else if (senha.length < 8 || senha.length > 32) {
      alert('A senha deve ter entre 8 e 32 caracteres!');
      event.preventDefault();
    } else if (!regexEmail.test(email)) {
      alert('Por favor, insira um email válido!');
      event.preventDefault();
    }
});
