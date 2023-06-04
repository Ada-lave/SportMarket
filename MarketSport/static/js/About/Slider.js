
let MainImg = document.querySelector('.MainImg');

let Imgs = document.querySelectorAll('.SliderImg');

console.log(MainImg)

MainImg.src = Slider[0].src;

for(let i = 0 ; i < Slider.length; i++){

    Slider[i].addEventListener('click', ()=>{
        MainImg.src = Slider[i].src;

    })

}

console.log(Slider)




