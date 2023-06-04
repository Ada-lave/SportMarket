

let Slider = document.querySelectorAll('.SliderImg');
let line = document.querySelectorAll('.Line');

line[0].classList.remove('hidden');


for (let i = 0; i < Slider.length; i++) {
    Slider[i].addEventListener('click', () => {

  
    for (let j = 0; j < line.length; j++) {
        line[j].classList.add('hidden');
    }

   
    line[i].classList.remove('hidden');

    if (i > 0) {
        line[i-1].classList.add('hidden');
    }


    if (i < line.length - 1) {
        line[i+1].classList.add('hidden');
    }
  });
}



