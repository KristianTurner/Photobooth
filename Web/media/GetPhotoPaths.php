<?php 
		$dir    = './';
		$files = array_diff(scandir($dir), array('..', '.'));
		echo json_encode($files);
 ?>