var time_now = new Date()
var time  = time_now.getHours()
console.log(`A hora atual é de ${time} h`)
if(time < 12){
    console.log("Bom dia senhor")
} else if(time <= 18){
    console.log("Boa tarde senhor")
} else{
    console.log("Boa noite senhor")
}