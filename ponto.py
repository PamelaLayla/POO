export class Ponto {
    private nome: String;
    private x: Number;
    private y: Number;

    constructor(nome:String, x:Number, y:Number) {
        this.nome = nome;
        this.x = x;
        this.y = y;
    }

    public getNome(): String {
        return this.nome;
    }

    public setNome(nome:String) {
        this.nome = nome;
    }

    public getX(): Number {
        return this.x;
    }

    public setX(x:Number) {
        this.x = x;
    }

    public getY(): Number {
        return this.y;
    }

    public setY(y:Number) {
        this.y = y;
    }
}