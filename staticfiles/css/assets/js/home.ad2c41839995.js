var slider_img = $('.slider-img');
var images = ['vanilla.png', 'avocado.png', 'chocolate.png'];
var container = $('.best-flavors-wrapper');
var flavors = ["Vanilla", "Avocado", "Chocolate"];
var i = 0;

function prev(){
        if(i <=0) {
        i = images.length;
        }
        i--;
        return setImg();
}

function next(){
        if (i >= images.length - 1) {
        i = -1;
        }
        i++;
        return setImg();
}

function setImg(){
        container.find('.spec-flavor').text(flavors[i]);
        return slider_img.attr('src', './../static/img/' + images[i]);
}

