$(document).ready(function () {
    $("#image-slider").slick({
      autoplay: true,
      autoplaySpeed: 2000,
      dots: true,
      arrows:true,
      prevArrow:'<button type="button" data-role="none" class="slick-prev">Previous</button>',
      nextArrow:'<button type="button" data-role="none" class="slick-next">Next</button>',
    });
  }); 

