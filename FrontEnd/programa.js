//FrondEnd mínimo

//La dirección 127.0.0.1 es la local del pc, es decir, 
//la url queda alojada en la pc en el puerto 8000 en una función sumar

let url = "http://127.0.0.1:8000/";

//url + parámetros
let myAPI = url + "?a=5&b=45";

//Para conectarse de manera remota se usa fetch y que espere la respuesta de la API await
//await es un comportamiento asíncrono

async function crearPeticion(){
    let response = await fetch(myAPI);
    let datos = response.json();
}