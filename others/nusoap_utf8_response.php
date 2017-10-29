<?php 
$client = new nusoap_client(PATH_TO_WSDL_LOCATION, true); 
$client->soap_defencoding = 'UTF-8';
$client->decode_utf8 = false;
?>