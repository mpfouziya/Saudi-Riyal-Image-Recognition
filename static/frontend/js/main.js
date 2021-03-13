const loader=document.querySelector('.loader');
const main=document.querySelector('.main');

function init(){
    setTimeout(() =>{
    setTimeout(()=> (loader.style.opacity =0 ), 50);

    main.style.display='block';
    setTimeout(()=> (main.style.opacity=1 ), 100);
    },4000);
}

init();

function showPreview(event){
if(event.target.files.length>0)
{
    var src= URL.createObjectURL(event.target.files[0]);
    var preview=document.getElementById("file-ip-1-preview");
    preview.src=src;
    preview.style.display="block";
}
}
