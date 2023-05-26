function verificar(){
    var now_year = new Date()
    var year = now_year.getFullYear() 
    var fyear = document.getElementById("num")
    var res = document.getElementById("res")
    
    if(fyear.value == 0 || fyear.value > year){
        window.alert("[ERROR] Verifique os dados informados e tente novamente!")
    } else { 
        var fsex = document.getElementsByName("radsex")
        var age = year - Number(fyear.value)
        var genre = " "
        var img = document.createElement("img")
        img.setAttribute("id", "foto")

        if (fsex[0].checked) {
            genre = "Homen"

            if ( age >= 0 && age <= 3){
                // Bebe
                img.setAttribute("src", "homen_bebe.png")
                res.innerHTML = `Detectamos um homen de ${age} anos logo voce é Bebe`
                document.body.style.background = "blue"

            } else if (age >= 4 && age < 12){
                // Crianca
                img.setAttribute("src", "homen_crianca.png")
                res.innerHTML = `Detectamos um homen de ${age} anos logo voce é Crianca`
                document.body.style.background = "blue"

            } else if (age >= 12 && age <= 18 ){
                // Adolecente
                img.setAttribute("src", "homen_adolecente.png")
                res.innerHTML = `Detectamos ${age} anos logo voce é Adolecente`
                document.body.style.background = "blue"

            } else if (age >= 19 && age < 30){
                // Jovem
                img.setAttribute("src", "homen_joven.png")
                res.innerHTML = `Detectamos um homen de  ${age} anos logo voce é Jovem`
                document.body.style.background = "blue"

            } else if (age < 50){
                // Adulto
                img.setAttribute("src", "homen_joven.png")
                res.innerHTML = `Detectamos um homen de ${age} anos logo voce é Adulto`
                document.body.style.background = "blue"


            } else {
                // Idoso
                img.setAttribute("src", "homen_velho.png")
                res.innerHTML = `Detectamos um homen de ${age} anos logo voce é Idoso`
                document.body.style.background = "blue"
            }

        } else if  (fsex[1].checked){
            genre = "Mulher"

            if ( age >= 0 && age <= 3){
                // Bebe
                img.setAttribute("src", "mulher_bebe.png")
                res.innerHTML = `Detectamos uma mulher de ${age} anos logo voce é Bebe`
                document.body.style.background = "pink"

            } else if (age >= 4 && age < 12){
                // Crianca
                img.setAttribute("src", "mulher_.crianca.png")
                res.innerHTML = `Detectamos uma mulher de ${age} anos logo voce é Crianca`
                document.body.style.background = "pink"

            } else if (age >= 12 && age <= 18 ){
                // Adolecente
                img.setAttribute("src", "mulher_adolecente.png")
                res.innerHTML = `Detectamos uma mulher de ${age} anos logo voce é Adolecente`
                document.body.style.background = "pink"

            } else if (age >= 19 && age < 30){
                // Jovem
                img.setAttribute("src", "mulher_jovem.png")
                res.innerHTML = `Detectamos uma mulher de ${age} anos logo voce é Jovem`
                document.body.style.background = "pink"

            } else if (age < 50){
                // Adulto
                img.setAttribute("src", "mulher_jovem.png")
                res.innerHTML = `Detectamos uma mulher de ${age} anos logo voce é Adulto`
                document.body.style.background = "pink"

            } else {
                // Idoso
                img.setAttribute("src", "mulher_velha")
                res.innerHTML = `Detectamos uma mulher de ${age} anos logo voce é Idoso`
                document.body.style.background = "pink"
            }
        }
        res.style.textAlign = "center"
        res.appendChild(img)
        
    }   
    
}