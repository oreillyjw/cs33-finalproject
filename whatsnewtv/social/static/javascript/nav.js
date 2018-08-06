// value comaprision in handlebars in the template
// https://gist.github.com/pheuter/3515945
Handlebars.registerHelper("ifvalue", function(conditional, options) {
    if (conditional == options.hash.equals) {
        return options.fn(this);
    } else {
        return options.inverse(this);
    }
});

var searchHovered = false;

$(".navbar-nav > form > button").bind("mouseover",function() {
    searchHovered = true;
}).bind("mouseout",function() {
    searchHovered = false;
});

$('.navbar-nav > form > .search').on('focus', function(){
  $(this).next('button').removeClass('d-none');
});

$('.navbar-nav > form > .search').on('blur', function(){
  if(!searchHovered) {
       $(this).next('button').addClass('d-none');
  }
  else {
      $(".navbar-nav > form > .search").bind("mouseup",function() {
           $('.navbar-nav > form > button').addClass('d-none');
      })
  }
})

$('.nav-item > a.notification').on('click', function () {
  $("#notifcation-dropdown").html('<div class="dropdown-item text-center" ><i class="fa fa-spinner fa-spin fa-3x fa-fw"></i></div>');
});


$('div[data-href]').on('click', function(){
  console.log($(this).data('href'));
  let href = $(this).data('href');
  if (href.match(/^\/(movie|tv)\/(\d+)$/)){
    window.location = href;
  }
});
