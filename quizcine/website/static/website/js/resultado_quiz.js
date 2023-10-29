document.querySelectorAll('.frente').forEach(function(frente) {
  frente.addEventListener('click', function(event) {
      var cartao = frente.parentElement.parentElement;
      cartao.classList.toggle('virado');
  });
});
