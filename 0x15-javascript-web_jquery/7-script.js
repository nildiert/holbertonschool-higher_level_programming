$(function () {
    let $character = $("#character")
    $.ajax({
	type: 'GET',
	url: "https://swapi.co/api/people/5/?format=json",
	success: function(data) {
	    $character.text(data.name);
	}
    });
});
