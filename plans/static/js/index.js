$(function () {
  $(".content").slice(0, 6).show();
  $("#loadMore").on("click", function (e) {
    e.preventDefault();
    $(".content:hidden").slice(0, 6).slideDown();
    if ($(".content:hidden").length == 0) {
      $("#loadMore").text("No Content").addClass("noContent");
    }
  });
  
  //Scroll to top
  $(window).scroll(function () {
    if ($(this).scrollTop() > 50) {
      $(".scrolltop:hidden").stop(true, true).fadeIn();
    } else {
      $(".scrolltop").stop(true, true).fadeOut();
    }
  });
  $(function () {
    $(".scroll").click(function () {
      $("html,body").animate(
        { scrollTop: $(".thetop").offset() - 100 },
        "3000"
      );
      return false;
    });
  });

  // Show or hide the sticky footer button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
      $(".go-top").fadeIn(200);
      $(".social-sidebar").addClass(".none")
    } else {
      $(".go-top").fadeOut(200);
    }
  });

  // Animate the scroll to top
  $(".go-top").click(function (event) {
    event.preventDefault();
    $("html, body").animate({ scrollTop: 0 }, 400);
  });
});
