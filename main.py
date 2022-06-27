import {Cliente} from "./cliente"
import {TipoCliente} from "./tipo_cliente"
import {Produto} from "./produto"
import {NotaFiscal} from "./nota_fiscal"
import {ItemNotaFiscal} from "./item_nota_fiscal"

//Criar um Cliente
let cliente = new Cliente(1, "Pamela Layla", 600, "800.400.000-33",TipoCliente.PESSOA_FISICA);

let p1 = new Produto(1, 100, "Massa de tapioca", 9.00);
let p2 = new Produto(2, 200,"Farinha", 4.00);
let p3 = new Produto(3, 900, "Arroz ", 3.80);

let nf = new NotaFiscal(1, 201, cliente);

let itnf1 = new ItemNotaFiscal(1, 1, 10, p7);
let itnf2 = new ItemNotaFiscal(2, 2, 10, p8);
let itnf3 = new ItemNotaFiscal(3, 3, 10, p3);

itnf1.valorItemNotaFiscal();
itnf2.valorItemNotaFiscal();
itnf3.valorItemNotaFiscal();

nf.adicionarItem(itnf1);
nf.adicionarItem(itnf2);
nf.adicionarItem(itnf3);

nf.imprimirNotaFiscal();