// source: http://stackoverflow.com/a/807194/669265

//detect change anywhere in html input
var somethingChanged = false;
$(document).ready(function() { 
   $(':input').change(function() { 
        somethingChanged = true; 
   }); 
});


//detect change of children of #myDiv in input
var somethingChanged = false;
$(document).ready(function() { 
   $('#myDiv > :input').change(function() { 
        somethingChanged = true; 
   }); 
});