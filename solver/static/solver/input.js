const boxes = document.getElementsByClassName("box");
let focused;
const nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

function detect_focus(box, focused){
    
    if (focused != null){
        console.log(focused)
        focused.style.backgroundColor = "rgba(255, 255, 255, 0)"
    }
    
    box.style.backgroundColor = "rgb(255, 245, 158)";
    return box;

}

for (let i = 0; i < 81; i++){
    boxes[i].addEventListener('click', function() { 
        focused = detect_focus(this, focused);
    });
}
document.addEventListener('keydown', (event) => {userPressedKey(event)})
function userPressedKey(event){
    if (event.key in nums){
        focused.innerHTML = event.key;
    }
}