function show(e) {
    var debt = e.currentTarget.childNodes[2];
    debt.style.display = "block";
}

function hide(e) {
    var debt = e.currentTarget.childNodes[2];
    debt.style.display = "none";
}

var knights = document.getElementsByClassName("knight");
console.log(knights);
for (i in knights) {
    var knight = knights[i];
    var debts = knight.childNodes[2];
    knight.addEventListener("mouseover", show, false);
    knight.addEventListener("mouseout", hide, false);
    debts.style.display = "none";
}
