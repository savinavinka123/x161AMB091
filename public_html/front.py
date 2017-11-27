<html >
<head >
<title >ūAJAX:pakaya </title >
<meta charset= "UTf-8 "/>
</head >
<body >
<script type= "text/ javascript ">
// ---------------------------------------------
// ūStam īpieprasjumu datu āāāpiegdtjam
function xml_http_post (url , data , callback ) {
var req = new XMLHttpRequest ();
req.open ("POST", url , true);
req.onreadystatechange = function () {
if ( req.readyState == 4) {
callback (req);
}
}
req.send (data);
}
// ---------------------------------------------
// āāApstrdjam pogas spiedienu ūnostot īpieprasjumu uz pareizu URL
function button_press () {
var data = document.main_form.student_id.value;
var port = '10' + data.slice (-3);
xml_http_post (" http: //213.175.92.37: "+port , data , display_result )
}
// ---------------------------------------------
// ēAttlojam ārezulttu
function display_result (req) {
var elem = document.getElementById (' result_span ')
elem.innerHTML = req.responseText
}
</script >ū
Ldzu ievadi īapliecbas numuru:
<form name=main_form >
<input type= "text" name= " student_id " value= "0" size= "9">
<input type=button onClick= " button_press ();" value= " start " title= "start "
>
</form>
Studenta dati ir <span id=" result_span " style= " color:red "> - </span>
</body >
</html >
