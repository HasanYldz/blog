/*
   
    Template Name : Write - Simple Blog Template
    Author : UiPasta Team
    Website : https://www.uipasta.com/
    Support : https://www.uipasta.com/contact-us/
	
	
*/



/*
   
   Table Of Content
   
   1. Preloader
   2. Smooth Scroll
   3. Scroll To Top
   4. Ajaxchimp for Subscribe Form
   5. Search Modal
   6. Load More Post
 

*/


(function ($) {
    'use strict';

    jQuery(document).ready(function () {

        
       /* Preloader */
		
        $(window).load(function () {
            $('.preloader').delay(800).fadeOut('slow');
         });
		 		
		
		
       /* Smooth Scroll */

        $('a.smoth-scroll').on("click", function (e) {
            var anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $(anchor.attr('href')).offset().top - 50
            }, 1000);
            e.preventDefault();
        });
				 
		
		
		
       /* Scroll To Top */
		
        $(window).scroll(function(){
        if ($(this).scrollTop() >= 500) {
            $('.scroll-to-top').fadeIn();
         } else {
            $('.scroll-to-top').fadeOut();
         }
         });
	
	
        $('.scroll-to-top').click(function(){
          $('html, body').animate({scrollTop : 0},800);
          return false;
          });  
		  
		  
	   
       /* Ajaxchimp for Subscribe Form */
		
        $('#mc-form').ajaxChimp();
		
		

       /* Search Modal */
	   
         $(document).on("click", ".btn-header-search", function(event) {
                event.preventDefault();

                $(".header-search").addClass("open");
            });

            $(document).on("click", ".search-close", function(event) {
                event.preventDefault();
                $(".header-search").removeClass("open");
            });
	   
	   
	   
       /* Load More Post */	
	   	
        $("div.blog-post").slice(0, 4).show();
          $("#load-more-post").on('click', function (e) {
             e.preventDefault();
             $("div.blog-post:hidden").slice(0, 1).slideDown(300);
             if ($("div.blog-post:hidden").length == 0) {
             $('#post-end-message').html('<div class="end">End</div>').fadeIn(800);
             $("#load-more-post").fadeOut(100);
              }
             });
              
		   
            });

   })(jQuery);