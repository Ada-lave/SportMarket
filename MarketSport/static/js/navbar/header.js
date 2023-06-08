


//search

let input = document.querySelector('.SearchInput');
let icon = document.querySelector('.search');

icon.addEventListener('click',()=>{

    input.classList.toggle('SearchInput--active');

      
  
})

//stickyheader

let lastTop = 0;
let header = document.querySelector('header');
let menu = document.querySelector('.menu');


window.addEventListener('scroll',function(){

  let CurrentTop = window.pageYOffset;




  if(window.pageYOffset == 0){

    header.style.backgroundColor = "#D2E740"
    header.style.height = "80px";
    header.style.position = ""
    menu.style.visibility = ""

  }else if(CurrentTop > lastTop){
    MainBlock.classList.remove('ProfileMenuHidden');
    input.classList.remove('SearchInput--active')
    header.style.backgroundColor = "#fff"
    header.style.height = "50px";
    header.style.position = "fixed"
    menu.style.visibility = "hidden"
    

  
  } else{
    header.style.backgroundColor = "#fff"
    header.style.height = "80px";
    header.style.position = "fixed"
    menu.style.visibility = ""
   
  }


  lastTop = CurrentTop;

})




//profile


const UserIcon = document.querySelector('.ProfileImg');
const MainBlock = document.querySelector('.ProfileMenu')

UserIcon.addEventListener('click', ()=>{

      MainBlock.classList.toggle('ProfileMenuHidden');
})


