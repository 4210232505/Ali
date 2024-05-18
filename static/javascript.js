const night= document.getElementById("night");
const body=document.querySelector("body");
const todo=document.querySelector(".todo");

function moon(){
        night.addEventListener ("click", ()=>{
        body.classList.toggle("dark");
    })
}

function moonTodo(){
    night.addEventListener ("click", ()=>{
    todo.classList.toggle("dark");
})
}

document.addEventListener("DOMContentLoaded", moon);
document.addEventListener("DOMContentLoaded", moonTodo);