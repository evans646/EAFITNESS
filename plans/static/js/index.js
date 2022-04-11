$(function(){
    $(".content").slice(0, 4).show();
    $("#loadMore").on("click", function(e){
      e.preventDefault();
      $(".content:hidden").slice(0, 4).slideDown();
      if($(".content:hidden").length == 0) {
        $("#loadMore").text("No Content").addClass("noContent");
      }
    });
    

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


    // Show or hide the sticky footer button
    $(window).scroll(function() {
      if ($(this).scrollTop() > 200) {
        $('.go-top').fadeIn(200);
      } else {
        $('.go-top').fadeOut(200);
      }
    });
    
    // Animate the scroll to top
    $('.go-top').click(function(event) {
      event.preventDefault();
      $('html, body').animate({scrollTop: 0}, 300);
    })
   });


  