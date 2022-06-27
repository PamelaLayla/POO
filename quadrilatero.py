import { Ponto } from "./Ponto";

export class Quadrilatero {
    private x1: Number;
    private x2: Number;
    private y1: Number;
    private y2: Number;

    constructor(x1:Number, x2:Number, y1:Number, y2:Number) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }

    public getX1(): Number {
        return this.x1;
    }

    public setX1(x1:Number) {
        this.x1 = x1;
    }

    public getY1(): Number {
        return this.y1;
    }

    public setY1(y1:Number) {
        this.y1 = y1;
    }

    public getX2(): Number {
        return this.x2;
    }

    public setX2(x2:Number) {
        this.x2 = x2;
    }

    public getY2(): Number {
        return this.y2;
    }

    public setY2(y2:Number) {
        this.y2 = y2;
    }

    public pertenceArea(p:Ponto): Boolean {
        if (
            p.getX() >= this.getX1() && p.getX() <= this.getX2()
            &&
            p.getY() >= this.getY1() && p.getY() <= this.getY2()
        ) {
            return true;
        } else {
            return false;
        }
    }
}