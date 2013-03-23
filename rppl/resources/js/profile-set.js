
var removableInputs = document.getElementsByClassName('removable-field');
var addRoleLinks = document.getElementsByClassName('add-role');
var nextLink = document.getElementsByClassName('link-field').length;

var nextRole = Object.keys(projectId).reduce(
        function(obj, i) {
            obj[i] = 100;
            return obj;
        }, {});
var noLinks = nextLink;

document.querySelector('.add-link').addEventListener('click',
        function() {
            var linkDiv = document.createElement('div');
            linkDiv.classList.add('removable-field');
            linkDiv.classList.add('link-field');

            var input = document.createElement('input');
            input.id = 'id_link' + (++nextLink);
            input.type = 'text';
            input.name = 'link' + nextLink;
            input.maxLength = 100;
            linkDiv.appendChild(input);
            addDeleteButton(linkDiv);
            document.querySelector('.link-form').appendChild(linkDiv);
        },
        false);

[].forEach.call(addRoleLinks,
        function(link) {
            link.addEventListener('click',
                function() {
                    roleNo = nextRole[link.dataset.name]++;
                    var roleDiv = document.createElement('div');
                    roleDiv.classList.add('removable-field');

                    var id = projectId[link.dataset.name];
                    var name = id + '_role' + roleNo;

                    editionSelect = document.createElement('select');
                    editionSelect.name = name + '_0';
                    editionSelect.id = 'id_' + name + '_0';

                    roleSelect = document.createElement('select');
                    roleSelect.name = name + '_1';
                    roleSelect.id = 'id_' + name + '_1';

                    roleDiv.appendChild(editionSelect);
                    roleDiv.appendChild(roleSelect);

                    for (var i in roles) {
                        option = document.createElement('option');
                        option.text = roles[i];
                        roleSelect.add(option, null);
                    }

                    var editions = projectEditions[link.dataset.name];
                    for (var i in editions) {
                        option = document.createElement('option');
                        option.text = editions[i];
                        editionSelect.add(option, null);
                    }

                    addDeleteButton(roleDiv);
                    link.parentNode.appendChild(roleDiv);
                }, false);
        });

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
