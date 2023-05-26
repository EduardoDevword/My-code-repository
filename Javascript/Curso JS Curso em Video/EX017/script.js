function gerar(){
    var num = document.getElementById("num")
    var tab = document.getElementById("tab")
    var cont = Number(num.value)

    for( var i = num.value; i < 11; i ++){
        // o createElement cria um elemento HTML pelo JavaScript e introduz onde desejado
        var opt = document.createElement("option")
        opt.text = `${cont} X ${i} = ${cont * i}`
        tab.appendChild(opt)

    }
}