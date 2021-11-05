var pictures = [
    "lindaPic.jpg",
    "lindaPic2.jpg",
    "lindaPic3.jpg",
    "lindaPic4.jpg",
    "lindaPic5.jpg",
    "lindaPic6.JPG",
    "lindaPic7.JPG",
    "lindaPic8.JPG",
    "lindaPic9.JPG",
    "Elvis.jpg"
]

function newPicture() {
    // get a random factor, e.g 0-1
    var randomFactor = Math.random();
    // get a random seed base on the length of given array, e.g it is pictures in this case
    var randomSeed = randomFactor * pictures.length;
    // round down the randomSeed to a random number int, e.g 0~9
    // The Math.floor() function returns the largest integer less than or equal to a given number
    var randomNumber = Math.floor(randomSeed);
    document.getElementById('pictureDisplay').src = "/static/assets/pictures/" + pictures[randomNumber];
}

function grayIt(){
    if($('#pictureDisplay').hasClass("blur")) $('#pictureDisplay').removeClass('blur');
    if($('#pictureDisplay').hasClass("grayscale")) $('#pictureDisplay').removeClass('grayscale');
    else $('#pictureDisplay').addClass('grayscale');
}

function blurIt(){
    if($('#pictureDisplay').hasClass("grayscale")) $('#pictureDisplay').removeClass('grayscale');
    if($('#pictureDisplay').hasClass("blur")) $('#pictureDisplay').removeClass('blur');
    else $('#pictureDisplay').addClass('blur');
}

// mouse over effects
$(document).on({
    mouseenter: function () {
        //stuff to do on mouse enter
        var name =  document.getElementById('pictureDisplay').src;
        if (name.toLowerCase().includes("linda")){
            document.getElementById('author').innerHTML = "Present by: Linda Liu"
        }
        else if (name.toLowerCase().includes("elvis")){
            document.getElementById('author').innerHTML = "Present by: Elvis Tang"
        }

    },
    mouseleave: function () {
        //stuff to do on mouse leave
        document.getElementById('author').innerHTML = ""
    }
}, "#pictureDisplay"); //pass the element as an argument to .on