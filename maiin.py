import { Quadrilatero } from "./classes/Quadrilatero";
import { Ponto } from "./classes/Ponto";

let quadrilatero = new Quadrilatero(0, 10, 0, 10);

let a = new Ponto('A', 0, 10);
let b = new Ponto('B', 10, -2);
let c = new Ponto('C', 3, 2);
let d = new Ponto('D', 10, 5);
let e = new Ponto('E', 12, 8);

let pontos = [a, b, c, d, e];

for (let i = 0; i < pontos.length; i++) {
    console.log('O ponto ' + pontos[i].getNome() + (quadrilatero.pertenceArea(pontos[i]) ? ' pertence ' : ' não pertence ') + 'ao quadrilátero');
}