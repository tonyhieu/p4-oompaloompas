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
    "lindaPic10.jpg"
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
