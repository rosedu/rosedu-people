'use strict';

var alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',	'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

var pplSearch = document.querySelector('.people-search');
var docfrag = document.createDocumentFragment();

var highlightName = function () {
	var letter = this.innerHTML.toUpperCase();
	// var lis = document.querySelectorAll('.name-container cufontext');

	for (var i = 0; i < lis.length; i+=2) {
		var name = lis[i].innerHTML + lis[i+1].innerHTML;

		if(lis[i].innerHTML[0] === letter || lis[i+1].innerHTML[0] === letter) {
			// console.log(lis[i].parentNode.parentNode.parentNode.parentNode);
		}
	}
};
 
alphabet.forEach(function(e) {
	var li = document.createElement('li');
	li.addEventListener('click', highlightName, false);
	li.textContent = e;
	docfrag.appendChild(li);
});
 
pplSearch.appendChild(docfrag);