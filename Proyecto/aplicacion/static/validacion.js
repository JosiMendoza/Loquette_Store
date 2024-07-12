function validar(){
    var correo = document.getElementById("correo").value;
    var contraseña = document.getElementById("contrasenia").value;
    var run = document.getElementById("run").value;

    if(correo === ""||contraseña=== ""){
        alert("Rellene los campos antes de continuar");
    }

    if(contraseña.value.length <= 12){
        alert("La contraseña debe tener un largo maximo 12");
    }

    

}