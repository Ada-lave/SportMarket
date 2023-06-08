


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



let BurgerWrapper = document.querySelector('.BurgerWrapper')
let OpenMenu = document.querySelector('.OpenMenu')
let Category = document.querySelector('.Category')
let CategoryList = document.querySelector('.CategoryList')
let text = document.querySelectorAll('.BurgerItem')
let TextCategory = document.querySelectorAll('.CategoryTextItem')



OpenMenu.addEventListener('click',()=>{
  BurgerWrapper.classList.toggle('BurgerWrapperActiv');
  CategoryList.classList.remove('CategoryListActive')
  for(let i = 0; i < text.length; i++){
    text[i].classList.toggle('BurgerItemActive');
  }

  for(let i = 0; i < TextCategory.length; i++){
    TextCategory[i].classList.remove('CategoryTextItemActiv');
  }

});
        

Category.addEventListener('click',()=>{


  CategoryList.classList.toggle('CategoryListActive')
  for( let i = 0; i < TextCategory.length; i++){

    TextCategory[i].classList.toggle('CategoryTextItemActiv')

  }
  


})




