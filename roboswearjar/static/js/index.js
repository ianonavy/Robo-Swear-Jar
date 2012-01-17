function show(e) {
    var debt = e.currentTarget.childNodes[3];
    debt.style.display = "block";
}
 
function hide(e) {
    var debt = e.currentTarget.childNodes[3];
    debt.style.display = "none";
}
 
var knights = document.getElementsByClassName("knight");
for (i in knights) {
    var knight = knights[i];
    var debts = knight.childNodes[3];
    console.log(knight.childNodes);
    knight.addEventListener("mouseover", show, false);
    knight.addEventListener("mouseout", hide, false);
    debts.style.display = "none";
}
