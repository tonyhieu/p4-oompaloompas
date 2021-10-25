var quotes = [
    'Optimism is the one quality more associated with success and happiness than any other. - Brian Tracy',
    'Happiness is not something ready-made. It comes from your own actions.- Dalai Lama',
    'All our dreams can come true if we have the courage to pursue them. - Walt Disney',
    'Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill',
    'I can’t change the direction of the wind, but I can adjust my sails to always reach my destination. – Jimmy Dean',
    'Move out of your comfort zone. You can only grow if you are willing to feel awkward and uncomfortable when you try something new. - Brian Tracy' ,
    'We must be willing to let go of the life we planned so as to have the life that is waiting for us. – Joseph Campbell',
    'People who are crazy enough to think they can change the world, are the ones who do. - Rob Siltanen',
    'Happiness is not by chance, but by choice. – Jim Rohn',
    'We may encounter many defeats but we must not be defeated. – Maya Angelou'
]

function newQuote() {
    var randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
}