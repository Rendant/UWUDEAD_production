let buttonCountPlus = document.getElementById("btn-plus");
let buttonCountMinus = document.getElementById("btn-minus");
let count = document.getElementById("Quantity");
let number = 1;

buttonCountPlus.onclick = function() {
        number++;
        count.value = number; 
};

buttonCountMinus.onclick = function() {
   if (number >= 2) {
       number--;
       count.value = number;
    }
}