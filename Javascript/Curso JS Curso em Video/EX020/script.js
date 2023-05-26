let val = document.getElementById("num")
let list = document.getElementById("lis")
let listVal= []
let res = document.getElementById("res")
// indexof busca o index de um determinado elemento.
// length mostra quantos valores a dentro do array.
// Match max e min sao funcoes que pegam o menor e o maior valor de um array entre tanto pode se obter o mesmo resultado por meio do for.

// funcao que verifica se os valores estao de acordo com a pagina.
function checkVal(num){
    
    if(Number(num) >= 1 && Number(num) <= 100){
        return true
    }
    else {
        return false
    }
}
// funcao que verifica se os valores estao no array.
function checkList(num, pos){
    // -1 em array quer dizer que o elemento nao consta dentro da lista.
    if(pos.indexOf(Number(num)) != -1){
        return true
    }
    else {
        return false
    }
}

function add(){
    if (checkVal(val.value) && !checkList(val.value, listVal)){
        listVal.push(val.value)
        var element = document.createElement("option")
        element.text = `Nº ${val.value}`
        list.appendChild(element)
        res.innerHTML = " "
    }
    else {
        window.alert("Valor negados pela pagina.")
    }
    val.value = " "
    val.focus()
}

function finalizar(){
    if (listVal == ""){
        window.alert("Para rodar essa função primeiro adicione valores a caixa acima")
    }
    else{
        var maior = Math.max.apply(Math,listVal)
        var menor = Math.min.apply(Math,listVal)
        var total = 0
        for (let pos in listVal){
            total += Number(listVal[pos])
            // obtendo maior e menor valor por meio do for 
            // if (listVal[pos] > maior){maior = listVal[pos]}
            // if (listVal[pos] < menor){menor = listVal[pos])
        }
        var media = total / listVal.length

        res.innerHTML = `Ao todo se encontram ${listVal.length} elementos.<br>`+
        `O maior valor desta lista é ${maior} <br>` + 
        `O menor valor desta lista é ${menor} <br>` +
        `O e a soma entre todos eles é ${total}<br>` +
        `A media de todos esses valores é ${media}`
    }
}
    