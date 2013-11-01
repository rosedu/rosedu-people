'use strict';

var alphabet = [];

var pplSearch = document.querySelector('.people-search');
var docfrag = document.createDocumentFragment();

var highlightName = function () {
	var toggle = document.querySelector('.btn-active');
	var letter = this.innerHTML.toUpperCase();
	var persons = document.querySelectorAll('.person');

	this.classList.toggle('btn-active');

	if(toggle && toggle !== this)
		toggle.classList.remove('btn-active');
	if(toggle === this) {
		var hidden = document.querySelectorAll('.search-hidden');
		
		[].forEach.call(hidden, function(el) {
			el.classList.remove('search-hidden');
		});
	} else {
        [].forEach.call(persons, function(p){
			p.classList.remove('search-highlight');
			p.classList.remove('search-hidden');

			if(p.dataset.name) {
				var name = p.dataset.name.split(' ');
				if(name[0][0] === letter || name[1][0] === letter) {
					p.classList.add('search-highlight');
				} else {
					p.classList.add('search-hidden');
				}
			}
		});

        [].forEach.call(document.querySelectorAll('.person.blank'), function(b) {
            b.classList.add('search-hidden');
        });
    }
};

[].forEach.call( document.querySelectorAll('.person'),
        function  fn(p){
            if (p.dataset.name) {
                var name = p.dataset.name.split(' ');
                if (jQuery.inArray(name[0][0], alphabet) === -1) {
                    alphabet.push(name[0][0]);
                }
                if (jQuery.inArray(name[1][0], alphabet) === -1) {
                    alphabet.push(name[1][0]);
                }
            }
        });

alphabet.sort();

alphabet.forEach(function(e) {
	var li = document.createElement('li');
	li.addEventListener('click', highlightName, false);
	li.textContent = e;
	docfrag.appendChild(li);
});
 
pplSearch.appendChild(docfrag);
