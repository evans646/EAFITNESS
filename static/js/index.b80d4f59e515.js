$(function(){
  
  $(window).scroll(function() {
    if ($(this).scrollTop() > 50 ) {
        $('.scrolltop:hidden').stop(true, true).fadeIn();
    } else {
        $('.scrolltop').stop(true, true).fadeOut();
    }
});
$(function(){$(".scroll").click(function(){$("html,body").animate({scrollTop:$(".thetop").offset() -100},"3000");return false})})


   $('hr').css({
       "background-color": "#f86b24",
        "width":"80%",
        "margin-left":"50px",
        "height":"1px"
   });
   const smallHeaderNav = $('.small-navs-wrapper ul ');

   smallHeaderNav.css({
    "margin":"0%",
   "margin-left": "35%",
   "font-size":"12px"
  })
  
  const smallHeaderNavLinks= $('.small-nav-item  ');

smallHeaderNavLinks.css({
  "font-size":"3e"
})

  const userNameOnDisplay = $('.user-logged');
  userNameOnDisplay.css({
    "margin":"1%",
    "padding-bottom":"2%"
  })
   

  const userNameOnDisplayLogo = $('.user-logged img');
  userNameOnDisplayLogo.css({
    "margin":"0.5%",
  })




  

   });


//    var textHolder = document.getElementsByClassName('.home-handler'),
//   text = textHolder.innerHTML,
// 	chars = text.length,
// 	newText = '',
// 	i;	

// for (i = 0; i < chars; i += 1) {
// 	newText += '<i>' + text.charAt(i) + '</i>';
// }

// textHolder.innerHTML = newText;

// var letters = document.getElementsByTagName('i'),
// 	flickers = [5, 7, 9, 11, 13, 15, 17],
// 	randomLetter,
// 	flickerNumber,
// 	counter;

// function randomFromInterval(from,to) {
// 	return Math.floor(Math.random()*(to-from+1)+from);
// }

// function hasClass(element, cls) {
//     return (' ' + element.className + ' ').indexOf(' ' + cls + ' ') > -1;
// }

// function flicker() {		
// 	counter += 1;
	
// 	if (counter === flickerNumber) {
// 		return;
// 	}

// 	setTimeout(function () {
// 		if(hasClass(randomLetter, 'off')) {
// 			randomLetter.className = '';
// 		}
// 		else {
// 			randomLetter.className = 'off';
// 		}

// 		flicker();
// 	}, 30);
// }

// (function loop() {
//     var rand = randomFromInterval(500,3000);

// 	randomLetter = randomFromInterval(0, 3);
// 	randomLetter = letters[randomLetter];
	
// 	flickerNumber = randomFromInterval(0, 6);
// 	flickerNumber = flickers[flickerNumber];

//     setTimeout(function() {
//             counter = 0;
//             flicker();
//             loop();  
//     }, rand);
// }());