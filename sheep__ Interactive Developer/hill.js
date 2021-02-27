export class Hill {
    constructor(color, speed, total) {
        this.color = color;
        this.speed = speed;
        this.total = total;
    }

    resize(stageWidth, stageHeight) {
        this.stageWidth = stageWidth;
        this.stageHeight = stageHeight;

        this.points = [];
        this.gap = Math.ceil(this.stageWidth / (this.total - 2)); //(양이밖에서부터 자연스럽게 걸어들어옴)stage보다 크게만들려고 -2작게 나눔

        for (let i = 0; i < this.total; i++) {
            this.points[i] = {
                x: i * this.gap,
                y: this.getY() //랜덤
            };
        }

    }
    daw(ctx){
        ctx.fillStyle = this.color;
        ctx.beginPath();

        let cur = this.points[0];
        let prev = cur;

        let dots = [];
        cur.x += this.speed; //언덕을 움직이게 하려면

        if (cur.x > -this.gap) {  //(언덕이 끊어지지않도록)일정영역에서 사라지면 배열을 관리합니다.
            this.points.unshift({
                x: -(this.gap * 2),
                y: this.getY()
            });
        } else if (cur.x > this.stageWidth + this.gap) {
            this.points.splice(-1);
        }

        ctx.moveTo(cur.x, cur.y);

        let prevCx = cur.x;
        let prevCy = cur.y;

        for (let i = 1; i < this.points.length; i++) {
            cur = this.points[i];
            cur.x += this.speed; //언덕을 움직이게 하려면
            const cx = (prev.x + cur.x) / 2;
            const cy = (prev.y + cur.y) / 2;
            ctx.quadraticCurveTo(prev.x, prev.y, cx, cy);

            dots.push({
                x1: prevCx,
                y1: prevCy,
                x2: prev.x,
                y2: prev.y,
                x3: cx,
                y3: cy,
            });

            prev = cur;
            prevCx = cx;
            prevCy = cy;
        }

        ctx.lineTo(prev.x, prev.y);
        ctx.lineTo(this.stageWidth, this.stageHeight);
        ctx.lineTo(this.points[0].x, this.stageHeight);
        ctx.fill();

        return dots;

    }

    getY() {
        const min = this.stageHeight / 8;
        const max = this.stageHeight - min;
        return min + Math.random() * max;

    }
}