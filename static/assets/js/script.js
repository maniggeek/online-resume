
$(window).scroll(function () {

  if ($(window).scrollTop() > 0 || $("html").scrollTop() > 0) {

    $('#navbar').addClass('scrolled');

  } else {

    $('#navbar').removeClass('scrolled');
  }
});

// AOS
AOS.init({
   duration: 800,
});

$(document).ready(function () {

  var pre = $("#preloader");
  if (pre) {
    setTimeout(() => {
      pre.addClass('loaded');
    },1000);
    setTimeout(() => {
      pre.remove();
    },2000);

  }

  $("#mobile_button").click(function () {
    $('#navbar').css('background-color','var(--c-dark);');
    $(".nav-link").css('padding-left','10px');

  });

});
