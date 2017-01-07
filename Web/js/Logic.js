$(document).ready(function(){

var pswpElement = document.querySelectorAll('.pswp')[0];
// build items array
var items = [
    {
        src: 'https://placekitten.com/600/400',
        w: 600,
        h: 400
    },
    {
        src: 'https://placekitten.com/1200/900',
        w: 1200,
        h: 900
    }
];

// define options (if needed)
var options = {
    // optionName: 'option value'
    // for example:
    index: 0 // start at first slide
};

// Initializes and opens PhotoSwipe
$.ajax({
  url: "../media/GetPhotoPaths.php",
  dataType: "json",  
  success: function( result ) {    
    var imageRegex =  new RegExp('\.png|jpg$');
    items = [];
    $.each( result ,function( index, value ) {
            if (imageRegex.test(value)){           
            var path = "../media/"+value;
            items.push({src: path ,w: 1920,h: 1080});    
            }        
    });
    var gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);
    gallery.init();
  },
  failed: function( result ) {
    console.log(result);
  }
});





});