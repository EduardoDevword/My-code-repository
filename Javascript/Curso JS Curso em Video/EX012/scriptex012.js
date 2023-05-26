function load(){
    var time_now = new Date()
    var time  = time_now.getHours()
    var day_color = document.getElementById("fundo")
    var txt_time = document.getElementById("times")
    var time_image = document.getElementById("img_time")

    if(time >= 0 && time < 12){
        txt_time.innerHTML = `It's now ${time} o'clock, Good morning`
        time_image.src = "IMAGENS/morning_img.jpg"
        document.body.style.background = "#ff9c1d"

    } else if(time <= 18){
        txt_time.innerHTML = `It's now ${time} o'clock, Good afternoon`
        time_image.src = "IMAGENS/afternoon_img.jpg"
        document.body.style.background = "#f5c678"
    } else {
        txt_time.innerHTML = `It's now ${time} o'clock, Good evening ,
        It's time from coding`
        time_image.src = "IMAGENS/night_img.jpg"
        document.body.style.background = "black"
    }
}

    