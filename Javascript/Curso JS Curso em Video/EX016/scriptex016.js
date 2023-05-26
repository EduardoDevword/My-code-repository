function cont(){
    var inicio = document.getElementById("ni")
    var fim = document.getElementById("nf")
    var passos = document.getElementById("np")
    var res = document.getElementById("res")
    
    if (inicio.value == 0 || fim.value == 0 || passos.value == null){
        window.alert("[ERROR] Informe todos os valores!")
    } else{
        res.innerHTML = "Contando:"
        var ini = Number(inicio.value)
        var f  = Number(fim.value)
        var p = Number(passos.value)
        if(ini < f){
            if(p <= 0){
                p = 1
                window.alert("O valor zero para passos é incorreto corrigindo para 1!")
            }
            for ( var i = ini; i <= f; i += p){
                res.innerHTML += `${i} \u{1F449}`
            } res.innerHTML += `FIM \u{1F6A9}`
        }
           
    }
}