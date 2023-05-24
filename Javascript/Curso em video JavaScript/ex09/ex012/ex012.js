var now = new Date()
var time  = now.getDay()

switch(time){
    case 0:
        console.log("Domingo")
        break

    case 1:
        console.log("Segunda")
        break

    case 2:
        console.log("Terça")
        break

    case 3:
        console.log("Quarta")
        break

    case 4:
        console.log("Quinta")
        break

    case 5:
        console.log("Sexta")
        break

    default:
        console.log("Sabado")
}