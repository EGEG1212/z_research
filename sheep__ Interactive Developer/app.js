import {
    Hill
} from './hill.js';

import {
    SheepController
} from './sheep-controller.js';

class App {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext("2d");
        document.body.appendChild(this.canvas);  // 캔버스생성.바디에추가
        
        this.hills = [
            new Hill('#ff4674', 0.2, 12),
            new Hill('#ff59c2', 0.5, 8),
            new Hill('#ff4674', 1.4, 6)
        ];

        window.addEventListener('resize', this.resize.bind(this), false);// 스크린사이즈를 가져오기위한
        this.resize();

        requestAnimationFrame(this.animate.bind(this));  
    }

    resize() {
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;

        this.canvas.width = this.stageWidth * 2;
        this.canvas.height = this.stageHeight * 2;
        this.ctx.scale(2,2);

        for (let i = 0; i < this.hills.length; i++) {
            this.hills[i].resize(this.stageWidth, this.stageHeight);
        }

        this.SheepController.resize(this.stageWidth, this.stageHeight);
    }

    animate(t) {
        requestAnimationFrame(this.animate.bind(this));

        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

        let dots;
        for (let i = 0; i<this.hills.length; i++){
            dots = this.hills[i].draw(this.ctx);
        }
        this.SheepController.draw(this.ctx, t, dots);
    }
}


window.onload = () => {
    new App();
};