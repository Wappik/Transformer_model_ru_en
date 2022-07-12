let checkLang

displayLang()

function displayLang() {

	if(!window.checkLang) {
		document.getElementById('firstLanguage').innerHTML = 'Русский'
		document.getElementById('secondLanguage').innerHTML = 'English'
	}
	else {
		document.getElementById('firstLanguage').innerHTML = 'English'
		document.getElementById('secondLanguage').innerHTML = 'Русский'
	}
}



$('#postTranslate').bind('input keyup', function(){
    var $this = $(this);
    var delay = 500; // 1 seconds delay after last input

    clearTimeout($this.data('timer'));
    $this.data('timer', setTimeout(function(){
        $this.removeData('timer');
        display()
    }, delay));
});


async function display() {
	let place = document.getElementById('postTranslate').value
	let res
	if (place == '') {
		res = ''
	}
	else {
		res = await eel.get_word(place)()
	}
	document.getElementById('info').innerHTML = res
}


$('#show').click(function() {
	window.checkLang = !window.checkLang
	console.log(window.checkLang)
	displayLang()
});