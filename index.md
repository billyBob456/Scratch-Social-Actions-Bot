<!doctype html>
<html lang="en">
	
<head>
	<style>
h1 {
	color: rgb(255, 255, 255);
}

body {
  background-color: rgb(0,0,0);
	font-family: monospace;
}

iframe {
  text-align: center;
}

.text {
  font-family: monospace;
  color: rgb(255, 255, 255);
  text-align: center;
}

nav {
  text-align: center;
  background-color: grey;
  padding: 10px;
}

nav a {
  text-decoration: none;
  padding-left: 7px;
  padding-right: 7px;
  width: 5px;
  height: 5px;
}

nav a:hover {
  background-color: rgb(0, 0, 0);
}

a {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
	</style>
  	<nav>
		<a href="https://scratch-view-bot.billybob456.repl.co" class="text">Home</a>
	</nav>
  	<title>Scratch Social Actions Bot</title>
</head>

<body>

	<div class="text">
    <h1><b>This is a bot for Scratch	developed by 348663451y with help from Joecooldoo.</b></h1>
		<br>
		<h2>Love/Favourite/View instructions:</h2>Simply enter your project ID below and the action you want to perform upon this project. 
		<br>Reload the page to continue adding views. 
		<br>Everytime the page loads it adds one view. 
		<br>This only loves and faves a project once but it can love and fave many projects. 
		<br>Your project ID is the big number in the URL of your project. 
		<br>
		<form>
  		<label>Choose an action:</label>
  		<select id="action"">
    	<option value="view">View</option>
    	<option value="love">Love</option>
    	<option value="favourite">Favourite</option>
  		</select>
		</form>
		Project ID:<input id="id" type=text><button onclick="redirect()">Go!</button>
		<script>
 function redirect()
  {
		var e = document.getElementById('action');
		var action = e.options[e.selectedIndex].value;
    var url = "/" + action + "/" + document.getElementById('id').value;
    window.location.href=url;
  }
  	</script>
		<br><br>
		<h2>Follow instructions: </h2>To follow simply put your username in the text box bellow and press "Follow!". 
		<br>
		Username:<input id="username" type=text><button onclick="follow_redirect()">Follow!</button>
		<script>
			function follow_redirect() {
    				var url = "/follow/" + document.getElementById('username').value;
    				window.location.href=url;
  			}
		</script>
		<br><br>
    <h2><b>To view the status of the page:</b></h2>Visit this link: <a href='https://stats.uptimerobot.com/6xqkWSPomQ'>Scratch Social Actions Bot Status</a>
	</div>
</body>
</html>
