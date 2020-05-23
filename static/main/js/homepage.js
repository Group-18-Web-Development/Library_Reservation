$("#demo-navbar .dropdown-menu a").click(function () {
    var href = $(this).attr('href');
    $("#tab-list a[href = '" + href + "']").tab('show');
})
// 设置涟漪效果使用方法非常简单 只需要引入jq库 然后在使用选择器选择要渲染的标签获得jQuery对象后使用ripples方法，下面三个参数自己试验就可以实现涟漪的效果了.例如
$('section').ripples({
    //imageUrl: null,   //要用作背景的图像的URL。如果没有，插件将尝试使用计算的background-imageCSS属性的值。也接受数据URI。
    dropRadius: 10, //通过在画布上单击或移动鼠标而产生的拖放的大小（以像素为单位）。
    perturbance: 0.4, //基本上由波纹引起的折射量。0表示没有折射。
    resolution: 512, //要呈现的WebGL纹理的宽度和高度。此值越大，渲染越平滑，涟漪传播越慢。
    //interactive: true,//鼠标点击和鼠标移动是否会触发效果。
    //crossOrigin: "",  //用于受影响图像的crossOrigin属性。
});
// 设置页脚特效
jQuery('#bobo').raindrops({
    color: '#a5d2da',
    canvasHeight: 80,
    waveHeight: 300,
});