// source: http://stackoverflow.com/a/807194/669265

//detect change anywhere in html input

//option 1:
var somethingChanged = false;
$(document).ready(function() { 
   $(':input').change(function() { 
        somethingChanged = true; 
   }); 
});

//option 2:
//detect change of children of #myDiv in input
var somethingChanged = false;
$(document).ready(function() { 
   $('#myDiv > :input').change(function() { 
        somethingChanged = true; 
   }); 
});



//option 3:
// source: https://stackoverflow.com/a/959679/669265
$.fn.extend({
    trackChanges: function() {
      $(":input",this).change(function() {
         $(this.form).data("changed", true);
      });
    }
    ,
    isChanged: function() { 
      return this.data("changed"); 
    }
});


$("#myform").trackChanges();

if ($("#myform").isChanged()) {
    // ...
 }