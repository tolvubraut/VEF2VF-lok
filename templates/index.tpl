{% extends "base.html" %}
{% block title %} Verkefni7 {% endblock %}
{% block content %}
	<div class="login">
		<h1>Login</h1>
		<form action="{{ url_for('login') }}" method="post">
			<label>User:
				<input type="text" name='user' required>
			</label>
			<label>Pass:
				<input type="password" name='passw'>
			</label>

			<h5>{{ msg }}</h5>
			<input type='submit' class="button" value="Login">
			<a href="{{ url_for('register') }}">Register now</a>
		</form>
	</div>
{% endblock %}