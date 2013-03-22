
var removableInputs = document.getElementsByClassName('removable-field');
var nextLink = document.getElementsByClassName('link-field').length;
var noLinks = nextLink;

document.querySelector('#add-link').addEventListener('click',
        function() {
            var linkDiv = document.createElement('div');
            linkDiv.classList.add('removable-field');
            linkDiv.classList.add('link-field');

            var input = document.createElement('input');
            input.id = 'id_link' + (++nextLink);
            input.type = 'text';
            input.name = 'link' + nextLink;
            input.defaultValue = "";
            input.maxLength = 100;
            linkDiv.appendChild(input);
            addDeleteButton(linkDiv);
            document.querySelector('#link-form').appendChild(linkDiv);
        },
        false);

var removeContainer = function(element) {
    element.parentNode.parentNode.removeChild(element.parentNode)
}

var addDeleteButton = function(field) {
    var delButton = document.createElement('a');
    delButton.classList.add('icon-delete');
    delButton.addEventListener('click', function() { removeContainer(delButton) }, false);
    field.appendChild(delButton)
};

[].forEach.call(removableInputs, addDeleteButton);
