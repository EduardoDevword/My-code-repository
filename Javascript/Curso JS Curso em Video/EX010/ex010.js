var now = new Date()
var time = now.getHours()
console.log(`A hora atual é ${time}`)

if(time < 12){
    console.log("Bom dia")
} else if(time <= 18){
    console.log("Boa tarde")
} else{
    console.log("Boa noite")
}