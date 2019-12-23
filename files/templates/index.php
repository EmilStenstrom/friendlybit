<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
   <title>Your own page title</title>
	<?php
	if (preg_match("/^[0-9a-z_]+$/", $_GET["style"])) {
		$style = $_GET["style"];
		echo "<link rel=\"stylesheet\" href=\"" . $_GET["style"] . ".css\" type=\"text/css\">";
	}
	?>
</head>
<body>

<div id="header">
   <h1>The name of this page</h1>
</div>
<div id="navigation">
   <h2>Navigation</h2>
   <ul>
      <li><a href="#first">First</a></li>
      <li><a href="#second">Second</a></li>
      <li><a href="#third">Third</a></li>
   </ul>
</div>
<?php
$cols = 2;
if (preg_match("/^[2-9]$/", $_GET["cols"]))
	$cols = $_GET["cols"];
?>
<?php
$showed = false;
for ($i = 1; $i < $cols; $i++) { ?>
<div id="content<?php echo $i; ?>">
   <h2>Content <?php echo $i; ?></h2>
   <p>Some sample content, add your own here</p>
<?php if (!empty($style) && !$showed): $showed = true; ?>
	<p>You can have a look at the <a href="<?php echo $style ?>.css">CSS file</a> if you want.</p>
<?php endif; ?>
</div>
<?php } ?>
<?php if (!$_GET["nofooter"]) { ?>
<div id="footer">
   <p>This page is written by [Your name] and builds on a
	<a href="https://friendlybit.com">Friendlybit template</a>.</p>
</div>
<?php } ?>
<!-- Please remove the two script blocks below, I use them for tracking what people read on friendlybit! -->
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-67394-2"); pageTracker._initData(); pageTracker._trackPageview();
</script>
</body>
</html>
