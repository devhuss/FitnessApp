function didYou(){
    if (document.querySelector('h3').innerHTML === 'Click the Button if You Did!') {
    document.querySelector('h3').innerHTML = 'Awesome!';
    } else if(document.querySelector('h3').innerHTML === 'Awesome!') {
    document.querySelector('h3').innerHTML = 'Double Awesmeness!';
    }else if(document.querySelector('h3').innerHTML === 'Double Awesmeness!') {
    document.querySelector('h3').innerHTML = 'Triple Awesomeness!';
    } else if(document.querySelector('h3').innerHTML === 'Triple Awesomeness!') {
        document.querySelector('h3').innerHTML = 'What are you waiting for? Fill in your log!';
    }
    else {
        document.querySelector('h3').innerHTML = 'Click the Button if You Did!';
    }
}