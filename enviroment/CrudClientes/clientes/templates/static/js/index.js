var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

function eliminarCliente(clienteID) {
  var request = $.ajax({
      type: "POST",
      url: "{% url 'eliminar_cliente' %}",
      data: {
          "csrfmiddlewaretoken": "{{ csrf_token }}",
          "cliennte_id": clienteID                    
      },
  });
  request.done(function(response) {
      alert("Cliente eliminado");
      // Cierra el modal, oculta el identificador eliminado, etc.
  });
}