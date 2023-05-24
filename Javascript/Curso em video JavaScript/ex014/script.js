function tabuada(){
    var num = document.getElementById("num")
    var tab = document.getElementById("tab")
    var res = document.getElementById("res")
    var n = Number(num.value)
    for( var i  = num.value; i < 11; i++){
        opt = document.createElement("option")
        opt.text = `${n} X ${i} = ${i*n} `
        tab.appendChild(opt)
        
    }
}