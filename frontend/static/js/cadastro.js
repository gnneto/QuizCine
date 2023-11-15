var script = document.createElement('script');
document.head.appendChild(script);

document.querySelector('form').addEventListener('submit', function(event) {
    var senha = document.querySelector('#senha').value;
    var confsenha = document.querySelector('#confsenha').value;
    var email = $('#email').val().toLowerCase();
    var cell = document.querySelector('#cell').value.replace(/\D/g,'');

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
    } else if (email == senha){
      alert('Sua senha não pode ser seu email');
      event.preventDefault();
    } else if (cell.length < 11){
      alert('Informe um celular valido.');
      event.preventDefault();
    }

});
const formatoCell = (event) => {
  let input = event.target
  input.value = mascaraCell(input.value)
}

const mascaraCell = (value) => {
  if (!value) return ""
  value = value.replace(/\D/g,'')
  value = value.replace(/(\d{2})(\d)/,"($1) $2")
  value = value.replace(/(\d)(\d{4})$/,"$1-$2")
  return value
}
