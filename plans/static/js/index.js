$(function(){
  $(window).scroll(function() {
    if ($(this).scrollTop() > 50 ) {
        $('.scrolltop:hidden').stop(true, true).fadeIn();
    } else {
        $('.scrolltop').stop(true, true).fadeOut();
    }
});
$(function(){$(".scroll").click(function(){$("html,body").animate({scrollTop:parseInt($(".thetop")).offset().top},"1000");return false})})

// .animate({scrollTop:100}, 500, 'offset', function() { 
//   return false
// });

   $('hr').css({
       "background-color": "#f86b24",
        "width":"80%",
        "margin-left":"50px",
        "height":"1px"
   });
   const smallHeaderNav = $('.small-navs-wrapper ul ');

   smallHeaderNav.css({
    "margin":"0%",
   "margin-left": "35%"
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

