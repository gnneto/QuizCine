document.querySelectorAll('.interno').forEach(function(interno) {
  interno.addEventListener('click', function(event) {
      var cartao = interno.parentElement;
      var botoes = cartao.querySelector('.botoes');

      if (!botoes.contains(event.target)) {
          cartao.classList.toggle('virado');
      }
  });
});
