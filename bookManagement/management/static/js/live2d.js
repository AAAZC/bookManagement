<!-- 左下角live2d效果 -->
setTimeout(() => {
L2Dwidget.init({
    "model": {
        "scale": 1
    },
    "display": {
        "position": "left",
        "width": 200,
        "height": 280,
        "hOffset": 0,
        "vOffset": -20
    },
    "mobile": {
        "show": true,
        "scale": 0.5
    },
    "react": {
        "opacityDefault": 0.7,
        "opacityOnHover": 0.2
    }
});
}, 1000
)