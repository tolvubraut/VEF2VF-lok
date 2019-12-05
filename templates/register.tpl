{% extends "base.html" %}
{% block title %} Verkefni7 {% endblock %}
{% block content %}
	<div class="register">
		<h1>Register</h1>
		<form action="{{ url_for('register') }}" method="post" autocomplete="off">
			<label>User:
				<input type="text" name='user' required>
			</label>
			<label>Pass:
				<input type="password" name='passw'>
			</label>
			<label>Name:
				<input type="text" name='nafn' required>
			</label>
			<h5>{{ msg }}</h5>
			<input type='submit' class="button" value="Register">
			<a href="{{ url_for('login') }}">Login</a>
		</form>
	</div>
{% endblock %}	