function validarRegistro(){
    var correo = document.getElementById("correo").value;
    var contraseña = document.getElementById("exampleInputPassword1").value;
    var run = document.getElementById("rut").value;

    if(correo === ""||contraseña=== ""||run ==""){
        alert("Rellene los campos antes de continuar");
    }

    if(contraseña.value.length <= 12){
        alert("La contraseña debe tener un largo maximo 12");
    }

  

}