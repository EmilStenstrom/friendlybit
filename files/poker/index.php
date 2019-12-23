<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
	<title>Poker Company - Play poker with us</title>
	<?php
	if (preg_match("/^[0-9a-z_]+$/", $_GET["style"]))
		echo "<link rel=\"stylesheet\" href=\"" . $_GET["style"] . ".css\" type=\"text/css\">";
	if (preg_match("/^[0-9a-z_]+$/", $_GET["style2"]))
		echo "<link rel=\"stylesheet\" href=\"" . $_GET["style2"] . ".css\" type=\"text/css\">";
	?>
</head>
<body>

<div id="header">
	<h1>Poker Company</h1>
	<p>Poker Company has been online since 1997 and is one of the biggest sites for 
	online poker. Every day over 40.000 people play, exchange tactics and talk about 
	poker on this site. Sounds like something you're interested in? Click the button 
	below to get started.</p>
	<ul>
		<li><strong>4.375</strong> users online</li>
		<li><strong>236</strong> tables</li>
		<li><strong>5</strong> tournaments</li>
	</ul>
	<a href="#play-poker.html">Play poker</a>
</div>
<div id="navigation">
	<h2>Navigation</h2>
	<ul>
		<li><a href="#play-poker.html">Play poker</a> |</li>
		<li><a href="#help/">Beginners guide</a> |</li>
		<li><a href="#news/">News</a> |</li>
		<li><a href="#forum/">Forum</a> |</li>
		<li><a href="#about/">About us</a></li>
	</ul>
	<form action="#search.php" method="get">
	<fieldset>
		<legend>Site search</legend>
		<label for="phrase">Search: </label>
		<input type="text" id="phrase">
		<input type="submit" value="search">
	</fieldset>
	</form>
</div>
<div id="adverts">
	<h2>Advertisement</h2>
	<a href="#url_to_advertisers_site.com">
		<img src="play-roulette-online.png" alt="Advertisement: Play roulette online">
	</a>
</div>
<div id="content">
	<div id="c_beginnersguide">
		<h2>Beginners guide</h2>
		<p>If you are a poker beginner you might want to start by reading 
		<a href="#help/rules-of-poker.html">the rules</a>. When you are done with that 
		you can <a href="#help/register.html">register an account</a> with us. Don't worry, 
		to join is free of charge and you can even win some money in our 
		<a href="#help/monthly-tournaments.html">monthly tournaments</a>.</p>
		<p class="more">More questions are answered in the 
		<a href="#help/frequently-asked-questions.html">frequently asked questions</a> section</p>
	</div>
	<div id="c_news">
		<h2>News</h2>
		<ul>
			<li>23 feb: <a href="#news/highest-prize-ever">Highest Prize Ever paid...</a></li>
			<li>5 jan: <a href="#news/caught-cheating">Top player caught cheating</a></li>
			<li>10 dec: <a href="#news/how-to-improve">How to improve your betting</a></li>
			<li>1 nov: <a href="#news/pokercompany-featured">PokerCompany featured on...</a></li>
			<li>30 okt: <a href="#news/murkus-baltomi">Murkus Baltomi the new...</a></li>
			<li>24 apr: <a href="#news/planned-downtime">Planned downtime on sunday</a></li>
		</ul>
		<p class="more">We maintain an <a href="#news/">archive</a> too.</p>
	</div>
	<div id="c_forum">
		<h2>Forum</h2>
		<ul>
			<li><a href="#forum/forum.php?topic=7">Best strategy with one...</a> - 124 repl.</li>
			<li><a href="#forum/forum.php?topic=572">Anyone know of a store...?</a> - 115 repl.</li>
			<li><a href="#forum/forum.php?topic=17">What's the name of the...</a> - 89 repl.</li>
			<li><a href="#forum/forum.php?topic=67">What your biggest pot?</a> - 51 repl.</li>
			<li><a href="#forum/forum.php?topic=23">There was this guy in...</a> - 49 repl.</li>
			<li><a href="#forum/forum.php?topic=325">Help me get my...</a> - 36 repl.</li>
		</ul>
		<p class="more"><a href="#forum/">Our forums</a> are always filled with people to answer your questions.</p>
	</div>
	<div id="c_aboutus">
		<h2>About us</h2>
		<p>PokerCompany has been in the business since 1997 and is...</p>
		<p class="more">Want to read <a href="#about/">more about us</a>?</p>
	</div>
</div>
<div id="footer">
	<p>You are looking at a template of a Poker site that is a part of the 
	<a href="/css/semantic-poker-template/">semantic poker template</a> article 
	on Friendly Bit. You are free to use this template as you wish.</p>
</div>
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