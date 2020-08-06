var idade = 25
var trabalhoAtivo = true

if (idade >= 21 || trabalhoAtivo) {
    console.log("OK")
}


//Contador
for (var contador =1; contador < 11; contador++){
    console.log(contador)
}
//Sequência de dias
for (var index = 1; index < 10; index++) {
    console.log("Dia " + index)
}

//Função Tabuada com qualquer número
function tabuada(n, i, final){
    for (var i = i; i <= final; i++){
        if (n*i < 10){
            console.log(n+" x " + "0"+i + " = " + "0"+n*i)
        }
        else if (i < 10){
            console.log(n+" x " + "0"+i + " = " + n*i)
        }
        else{
            console.log(n+" x " + i + " = " + n*i)
        }
    }
}

numero = 9
inicioMulti = 1
finalMulti = 10
console.log("Veja abaixo a Tabuada de " + numero + ", começando em " + inicioMulti + " e terminando em " + finalMulti + ":\n")
tabuada(numero, inicioMulti, finalMulti)



//for com Listas
var listaDeCarros = [ "Fox", "Uno", "Gol", "Astra", "Fiesta"]

for (var i = 0; i < listaDeCarros.length; i++) {
    console.log("Nome do Carro: " + listaDeCarros[i])
}

//for com Listas
var listaDeLucro = [100, 30, 300, -10, 600, 10]
var lucroTotal = 0;

for (var i = 0; i < listaDeLucro.length; i++) {
    lucroTotal += listaDeLucro[i]
}
console.log(lucroTotal)

//for com Listas
var listaDeGanhos = [10, 30, -10, -5, -1, 40]
var totalNegativos = 0

for (var i = 0; i < listaDeGanhos.length; i++) {
    if (listaDeGanhos[i] < 0) {
        totalNegativos += 1
    }
}
console.log(totalNegativos)

//for com Listas
var listaDeFrutas = [ "Uva", "Banana",  "Manga", "Cajá", "Pinha"]
var busca = "Cajá"

for (var i = 0; i < listaDeFrutas.length; i++) {
    if (busca == listaDeFrutas[i]) {
        console.log("Sim, temos a fruta " + busca + " disponível")
    }
}



//Break e Continue
var cartela = [8, 13, 18, 22, 42, 49]
var numeroSorteado = 42

for (var i = 0; i < cartela.length; i++) {
    if (numeroSorteado == cartela[i]) {
        console.log("Encontrei o número!")
        break
    }
    console.log(cartela[i]) // Imprime números até encontar o número sorteado.
}

//Pares
for (var i = 0; i <= 20; i++) {
    if (i % 2 == 1) {
        continue //quando for ímpar, ele passa para o próximo loop, ignorando o "console.log(i)" abaixo
    }
    console.log(i)
}

//Imprime todos menos "cesar".
var listaDeNomes = ["cesar", "pamela", "camila", "pedro"]
for (var i = 0; i < listaDeNomes.length; i++) {
    if (listaDeNomes[i] == "cesar") {
        continue
        //quando o nome for cesar, ele simplesmente passa para o próximo loop
    }
    console.log(listaDeNomes[i])
}

//imprimir nome junto com o sobrenome “Macedo” para cada integrante da família. Menos para Pedro, que é "Sousa"
var familia = ["Joana", "Felipe", "Gabriela", "Carlos", "Pedro", "Bruno"]
for(var i = 0; i < familia.length; i++){
    if(familia[i] == "Pedro"){
        console.log(familia[i] + " Sousa")
        continue
    }
    console.log(familia[i] + " Macedo")
}

//Encontrar o “Rei” e parar o loop utilizando break
var baralho = ["Ás", "Dama", "Rei", "Valete"]

for (var i=0; i < baralho.length; i++){
    if (baralho[i] == "Rei") {
        console.log("Encontrei o Rei!")
        break
    }
}


// Verifica se a palavra dentro da lista começa com maiúscula ou não utilizando função e for !!!
function comecaComMaiuscula(palavra){
    return /^[A-Z]/.test(palavra)
}
  
var palavras = ["Amor", "copo", "Bolacha", "biscoito"];
  
// Seu código vem aqui embaixo.
for (var i = 0; i < palavras.length; i++){
    if (comecaComMaiuscula(palavras[i])){
       console.log(palavras[i] + " Começa com maiúscula")
    }
    else{
       console.log(palavras[i] + " Não começa com maiúscula")
    }
}
/^[A-Z]/.test //Verifica se tem letra Maiúscula na palavra pesquisada




//Precisamos agora que você escreva a função deixaEntrar(dataDeNascimento, censura).

//A função deve receber dois parâmetros:

//O primeiro deve representar a data de nascimento do cliente no formato dd/mm/aaaa 
//O segundo deve representar a censura da sessão, ou seja, a idade mínima do cliente para que ele possa acessar a sala.

//A função deve retornar true caso o cliente tenha idade maior ou igual a censura e false caso contrário.
//A função calcularIdade não precisa ser alterada

function calcularIdade(dataDeNascimento) {
    var [dia, mes, ano] = dataDeNascimento.split('/');
    var d = new Date();
    var anoAtual = d.getFullYear();
    var mesAtual = d.getMonth() + 1;
    var diaAtual = d.getDate();
    ano = +ano; mes = +mes; dia = +dia;
    var quantosAnos = anoAtual - ano;
    if (mesAtual < mes || mesAtual == mes && diaAtual < dia) {
        quantosAnos--;
    }
    return quantosAnos < 0 ? 0 : quantosAnos;
}
  
// Escreva aqui sua função
function deixaEntrar(dataDeNascimento, censura){
    return calcularIdade(dataDeNascimento) > censura ? true : false
}
console.log(deixaEntrar("03/02/1998", 21))



var d = new Date()
console.log(d.getDate())        //data, dia em numeral
console.log(d.getDay())         //dia da semana, comecando em 0 como domingo
console.log(d.getFullYear())    //ano atual
console.log(d.getHours())       //hora atual
console.log(d.getMilliseconds())//milisegundo
console.log(d.getMinutes())     //minuto da hora
console.log(d.getMonth())       //mes do ano, comecando em 0 como janeiro
console.log(d.getSeconds())     //segundo






// Filtragem com Filter() e ARROW FUNCTION
const people = [
    { name: 'Carlos', age: 28 },
    { name: 'Henrique', age: 22 },
    { name: 'João', age: 27 },
    { name: 'Paulo', age: 30}
]
const newArray = people.filter(person => person.age > 22)
console.table(newArray)





// Filtragem de Preços com, Filter()
function precoEntre(valorMenor, valorMaior, precos){
    
    function vmenor(value){
        return value <= valorMaior
    }
    
    function vmaior(value){
        return value >= valorMenor
    }

    preco = precos.filter(vmenor)      // ou .filter(v => v >= valorMenor) - ARROW FUNCTION
    precofilter = preco.filter(vmaior) // ou .filter(v => v <= valorMaior) - ARROW FUNCTION
    return precofilter
}

menorCusto = 7
maiorCusto = 9
tabelaDePrecos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

console.log(precoEntre(menorCusto, maiorCusto, tabelaDePrecos))






// Filtragem de Preços 
// Crie uma função precosEntre(valorMenor, valorMaior, precos) que deve utilizar as funções maisBaratosQue e maisCarosQue para retornar os preços que estão entre o valorMenor e o valorMaior. Sua função deve receber então dois parâmetros:
// - valorMenor para representar o valor mínimo dos preços a serem listados
// - valorMaior para representar o valor máximo dos preços a serem listados
// - precos para representar um array com os preços dos produtos
//Ela deve retornar um array com todos os preços entre valorMenor e valorMaior

function maisBaratosQue(valor, precos) {
    return precos.filter(p => p <= valor);
}

function maisCarosQue(valor, precos){
    return precos.filter(p => p >= valor);
}

function precosEntre(valorMenor, valorMaior, precos){
    var maisBaratos = maisBaratosQue(valorMaior, precos)
    return maisCarosQue(valorMenor, maisBaratos)
}

menorCusto = 4
maiorCusto = 9
tabelaDePrecos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

console.log(precosEntre(menorCusto, maiorCusto, tabelaDePrecos))






// IndexOf() com .map()  // Verifica se tem a palavra procurada na lista  // Transforma todas as palavras da lista para MAIÚSCULA
function estavaPresenteNaAula(nomeDoAluno, nomesDosPresentes){
    if (nomesDosPresentes.indexOf(nomeDoAluno) >= 0) {
        console.log("tem " + nomeDoAluno + " na lista")
    }
    else{
        console.log("Não tem " + nomeDoAluno + " na lista")
    }
}

nome = "luCaS"
lista = ["LUcAs", "Pedro", "Sarah", "Bianca", "João"].map((item) => item.toUpperCase())
estavaPresenteNaAula(nome.toUpperCase(), lista)





// Transforma Primeira letra de cada palavra do texto em MAIÚSCULA
function primeiraLetraMaiuscula(text) {
    var listWords = text.toLowerCase().split(" ");
    for (var a = 0; a < listWords.length; a++) {
        var palavra = listWords[a];   // palavra = "hoje"

        var firstLetter = palavra[0]; // firstLetter = "h"
        palavra = firstLetter.toUpperCase() + palavra.slice(1); // "palavra.slice(1)" Pega todo o texto da variável "palavra" a partir da posição [1].

        listWords[a] = palavra;
    }
    return listWords.join(" ");
}

var frase = "Hoje eu acordei diferente"
console.log(primeiraLetraMaiuscula(frase))






// Objeto em JS e função nativa filter()
var pessoas = [
    {nome: "Lucas", idade: 22, Estado: "CE"},
    {nome: "Suelen", idade: 33, Estado: "RJ"},
    {nome: "Alguem", idade: 18, Estado: "SP"}
]
pessoas = pessoas.filter(item => item.Estado == "CE")
console.table(pessoas)






// Transforma todas as palavras do array para maiúscula usando push()
function transformaParaMaiusculo(palavras){
    var lista = Array()
    for (i=0; i < palavras.length; i++){
        console.log(lista)
        lista.push(palavras[i].toUpperCase())
    }
    return lista
}

console.log(transformaParaMaiusculo(["LUcAs", "Pedro", "Sarah", "Bianca", "João"]))






// Gerar dezenas aleatórias de 1 à 60
function gerarDezenas(){
    var num = Array()
    for (var i = 0; i < 6; i++){
        var dezenas = Math.random() * 60
        console.log(dezenas)
        if (dezenas < 0.5){
            dezenas += 0.5
        }
        num.push(Math.round(dezenas))
    }
    return num
}

console.log(gerarDezenas())






//Gerando um número inteiro aleatório entre dois valores, incluindo o MAIOR.
function getRandomIntInclusive(min, max) {
    min = Math.ceil(min); //.ceil() arredonda pra Mais
    max = Math.floor(max); //.floor() arredonda pra Menos
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandomIntInclusive(10, 15))






// Retorna o menor e o maior dentre cinco valores passados como parâmetro.
function maxmin(a, b, c, d, e){
    menor = Math.min(a,b,c,d,e)
    maior = Math.max(a, b, c, d, e)
    return [menor, maior]
}





//==================================================================================================//
// Calcula o total das passagens de Ônibus.
function numeroDeOnibus(ida, volta) {
    var partida = Array(ida)
    var chegada = Array(volta)

    for (var i = 0; i < partida.length; i++) {
        if (ida == 1){
            partida[i] = Number(prompt("Valor do Ônibus da ida ao trabalho?"))
        }
        else{
            partida[i] = 4//Number(prompt(`Valor do ${i+1}º Ônibus da ida ?`))
        }
    }

    for (var i = 0; i < chegada.length; i++) {
        if (volta == 1){
            chegada[i] = Number(prompt("Valor do Ônibus da volta do trabalho?"))
        }
        else{
            chegada[i] = 2//Number(prompt(`Valor do ${i+1}º Ônibus da volta ?`))
        }
    }
    var idaVolta = partida.concat(chegada)
    return partida, chegada, idaVolta
}

var quantOnibus1 = 3//Number(prompt("Quantos Ônibus você pega, somente na ida ao trabalho ?"))
var quantOnibus2 = 3//Number(prompt("Quantos Ônibus você pega, somente na volta do trabalho ?"))
console.log(numeroDeOnibus(quantOnibus1, quantOnibus2))



// Como usar uma variável ou um array de dentro de uma função no escopo global ?

for (var i = 0; i < idaVolta.length; i++){
    totIV += idaVolta[i]
}
for (var i = 0; i < chegada; i++){
    totC += chegada[i]
}
for (var i = 0; i < partida; i++){
    totP += partida[i]
}

alert(`O valor da ida é R$${totP}, o valor da volta é R$${totC} e o total é ${totIV}`)
//==================================================================================================//







// Retornar true se idade e altura forem respectivamente igual ou maior a 18 e 170.
var usuario1 = ['Et da Estônia', 17, 170]
var usuario2 = ['Pessoa do Pântano', 39, 198]
var usuario3 = ['Homem da Lua Virada', 21, 149]
var usuario4 = ['Pequena Paulistana', 18, 171]
var usuario5 = ['Menino da Porteira', 13, 142]

function maiorAlto(usuario){
    if (usuario[1] >= 18 && usuario[2] >= 170){
        return true
    }
    else{return false}
}
console.log(maiorAlto(usuario2))






// classificar altura dos alunos em grupos:
// grupoA - Alunos com altura entre 150 a 159
// grupoB - Alunos com altura entre 160 a 169
// grupoC - Alunos com altura de 1.70 ou mais
var alunos = [170, 159, 151, 187, 156, 191, 165, 154, 167, 169, 171, 170, 160]

var grupoA = []
var grupoB = []
var grupoC = []

for (var i = 0; i < alunos.length; i++){
    if (alunos[i] <= 159){
        grupoA.push(alunos[i])
    }
    else if (alunos[i] <= 169){
        grupoB.push(alunos[i])
    }
    else {
        grupoC.push(alunos[i])
    }
}
console.log(grupoA, grupoB, grupoC)







// Calcular valor da mensalidade de um estacionamento através do número da placa.
// - Se o motorista realizou até 20 entradas, ele deve pagar R$ 10,00 por entrada realizada.
// - Da vigésima primeira entrada em diante, cada entrada custa R$ 5,00 ao cliente.

// A primeira função se chama calcularNumeroDeEntradas(placa). A função deve retornar o número de entradas que esse carro realizou no estacionamento.

// A segunda função se chama calcularValorDevido(placa). A função deve calcular o valor que o proprietário do carro tem que pagar segundo a política de preços estabelecida. Naturalmente, será necessário utilizar a primeira função dentro da segunda.
var placas = [
    'RXB-2525', 'AKX-3333', 'ORO-7142','RXB-2525', 'AKX-3333', 'ORO-7142',
    'AKX-3333', 'RXB-2525', 'AKX-3333','AKX-3333', 'RXB-2525', 'AKX-3333',
    'RXB-2525', 'AKX-3333', 'ORO-7142','AKX-3333', 'AKX-3333', 'RXB-2525',
    'AKX-3333', 'ORO-7142', 'ORO-7142','AKX-3333', 'AKX-3333', 'RXB-2525',
    'AKX-3333', 'AKX-3333', 'RXB-2525','AKX-3333', 'AKX-3333', 'RXB-2525',
    'AKX-3333', 'ORO-7142', 'ORO-7142','AKX-3333', 'ORO-7142', 'ORO-7142',
    'ORO-7142', 'RXB-2525', 'AKX-3333','AKX-3333', 'ORO-7142', 'ORO-7142',
    'AKX-3333', 'RXB-2525', 'AKX-3333','AKX-3333', 'RXB-2525', 'AKX-3333',
    'RXB-2525', 'AKX-3333', 'ORO-7142','AKX-3333', 'AKX-3333', 'RXB-2525',
    'AKX-3333', 'ORO-7142', 'ORO-7142','AKX-3333', 'AKX-3333', 'RXB-2525',
    'AKX-3333', 'AKX-3333', 'RXB-2525','AKX-3333', 'AKX-3333', 'RXB-2525'
]
 
function calcularNumeroDeEntradas(placa){

    var totalEntrada = 0

    for (var i = 0; i < placas.length; i++){
        if (placa == placas[i]){
          totalEntrada += 1
        }
    }
    return totalEntrada
    // n = placas.filter(p => p == placa)
    // return n.length
}
  
function calcularValorDevido(placa){

    var valorDevido = calcularNumeroDeEntradas(placa)

    if (valorDevido <= 20){
       valorDevido *= 10
    }
    else{
       valorDevido = (valorDevido - 20) * 5 + (20 * 10)
    }
    return valorDevido
}

console.log(calcularValorDevido('AKX-3333'))






// Escreva uma função calculaGostos(notas)
//deve receber somente 1 parâmetro: um array de notas. Ela deve retornar também um array com três elementos:

// - O primeiro, com a quantidade de notas iguais a 0 ou 1. Seriam os que não gostaram do filme
// - O segundo, com a quantidade de notas iguais a 2 ou 3. Seriam os que acharam o filme mediano
// - O terceiro, com a quantidade de notas iguais a 4 ou 5. Seriam os que gostaram do filme.

function calculaGostos(notas){
    var ate1 = 0
    var ate2 = 0
    var ate3 = 0

    for (var i = 0; i < notas.length; i++){
        if (notas[i] <= 1){
            ate1++
        }
        else if(notas[i] <= 3){
            ate2++
        }
        else{
            ate3++
        }
    }
    return [ate1, ate2, ate3]
}

console.log(calculaGostos([2,4,2,5,1,4,3,4,5,0,5]))







/* Programar uma função filme que recebe três arrays com os nomes de personagens, filmes e ano de estréia no cinema. A função deve receber também um valor de id escolhido pelo usuário com intervalo de 1 até o tamanho máximo dos arrays fornecidos e retornar uma frase com o seguinte modelo: "personagem é um personagem do filme filme que estreou no cinema em lançamento." Se o valor de id for inválido, a função deve retornar a frase "Essa não é uma opção válida."   */
function filme(personagens, filmes, lancamentos, id){
    if (filmes.length != personagens.length || filmes.length != lancamentos.length){
        return "Inválido! Os Arrays devem ter o mesmo tamanho"
    }
    else if (id < 1 || id > personagens.length){
        return "Essa não é uma opção válida."
    }
    else{
        return personagens[id-1] + " é um personagem do filme " +filmes[id-1] + " que estreou no cinema em " + lancamentos[id-1] + "."
    }
}

personagens = ["Hermione", "Trinity", "Leia"]
filmes = ["Harry Potter", "Matrix", "Star wars"]
lancamentos = [2001, 1999, 1977]
id = 3
console.log(filme(personagens, filmes, lancamentos, id))







// Programe uma função series que recebe dois parâmetros, um prefixo com o nome da série e um array com a lista de todos os episódios da série. A função deve retornar um novo array com a lista de episódios iniciando com o nome da série.
function series(prefixo, array){
    resultado = []
    for (var i = 0; i < array.length; i++){
        resultado.push(prefixo + " " + array[i])
    }
    return resultado
}

harryPotterPrefixo = "Harry Potter";
harryPotterSeries = [
  "e a Pedra Filosofal",
  "e a Câmara Secreta",
  "e o Prisioneiro de Azkaban",
  "e o Cálice de Fogo",
  "e a Ordem da Fênix",
  "e o Enigma do Príncipe",
  "e as Relíquias da Morte"
]
console.log(series(harryPotterPrefixo, harryPotterSeries))
// Criar um site de sinopse de series, onde se possa escolher entre as séries, a temporada e o episodio. Através de selecão e arrays. Inicialmente começar com Blindspot e The 100. E colocar uma imagem de fundo referente à série.
/*!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!*/







// Programe uma função maiorQueNum que busca em um dado array apenas os números maiores do que o número fornecido no segundo parâmetro da função e retorna um novo array apenas com esses números.
function maiorQueNum(array, num){
    var resposta = []
    for (var i = 0; i < array.length; i++){
        if (array[i] > num){
            resposta.push(array[i])
        }
    }
    return resposta
}

var numeros = [10, 4, 7, 128, 42, -1, 0, 300, -5]
var num = 5
console.log(maiorQueNum(numeros, num))







//   Pergunta no Stack Overflow
function buscarDivisivelPor(array, num){
    var valido = []
    for (var i = 0; i < array.length; i++){
        if (array[i] % num == 0 && array[i] != 0){
            valido.push(array[i])
            break
        }
    }
    if (valido != []){
        return valido[0]
    }
    else{
        return "Nenhum número válido encontrado!"
    }
}

var array = [10, 4, 7, 128, 42, -1, 0, 300, -5]
var num = 400
console.log(buscarDivisivelPor(array, num))








// Programe uma função buscarDivisivelPor que recebe dois parâmetros, um array de números e um número de teste, retornando como resposta o primeiro número do array que seja divisível pelo número dado e diferente de zero. Caso nenhum número do array passe no teste, retorne o texto "Nenhum número válido encontrado!".
function buscarDivisivelPor(array, num){
    var valido = []
    for (var i = 0; i < array.length; i++){
        if (array[i] % num == 0 && array[i] != 0){
            valido.push(array[i])
            return valido[0]
        }
    }
    
    if (array.length == i){
        return "Nenhum número válido encontrado!"
    }
}
  
var array = [10, 4, 7, 128, 42, -1, 0, 300, -5]
var num = 2
console.log(buscarDivisivelPor(array, num))






function seArraysIguais(a, b){
    if (a.length == b.length){
        for (var i = 0; i < a.length; i++){
            if (a[i] == b[i]){
                continue
            }
            else{
                function dentro(c, d){
                    var c = a[i]
                    var d = b[i]
                    seArraysIguais(c,d)
                }
                return dentro(c,d)
                
            }
        }
        if (i == a.length){
            return true
        }
    }

    else{
        return false
    }

}

var a = [1,[3,2]]
var b = [1,[3,2]]
console.log(seArraysIguais(a, b))