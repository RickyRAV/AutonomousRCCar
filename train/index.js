if('addEventListener' in document){
    document.addEventListener('DOMContentLoad', ()=>{
       FastClick.attach(document.body); // 300ms delay between physical tap and the firing of a click event
    }, false);
}

//send a request to switch on the GPIOs
const switchOn = (direction)=>{
    fetch('http://localhost:5000/' + direction)
    .then(res => res.text())
    .then(res => console.log(res))
    .catch(err => console.log(err));
}

const switchOff = (direction)=>{
    fetch('http://localhost:5000/' + direction + '-off')
        .then(res => res.text())
        .then(res => console.log(res))
        .catch(error => console.log(error));
}

//bindin the buttons on the UI
const buttons = ['forward', 'backward', 'left', 'right'];
buttons.forEach(btn =>{
 const htmlTags = document.querySelector(`#${btn}`);

 // switches on on mousedown
 htmlTags.addEventListener('mousedown', ()=>{
    switchOn(btn);
 });

 //switches off on mouseup
 htmlTags.addEventListener("mouseup", ()=>{
    switchOff(btn);
 })
});

// keeping track which keys are down
const keysDown = {
    up:false,
    down:false,
    left: false,
    right: false,
}

//map the keys to the directions+
const keyDirections = {
    up: 'forward',
    down: 'backward',
    left: 'left',
    right: 'right'
}

//bind the keyboard keys
const directions = ['up', 'down', 'left', 'right'];

directions.map((key)=>{
    Mousetrap.bind(key, ()=>{
        if(!keysDown[key]){
            keysDown[key] = true;
            switchOn(keyDirections[key]);
        }
    }, 'keydown');

    Mousetrap.bind(key, ()=>{
            keysDown[key] = false;
            switchOff(keyDirections[key]);
    }, 'keyup')
});
