const list1= document.querySelectorAll('.list1');
function activeLink(){
    list1.forEach((item) =>
    item.classList.remove('active'));
    this.classList.add('active');
}
list1.forEach((item)=>
item.addEventListener('click',activeLink));
