{% extends "base.html" %}
{% block title %} Verkefni7 {% endblock %}
{% block content %}
	<h1>Blogs</h1>
		{% for y in blogs %}
			<div class="mminfo">
				<h3>{{ y[0] }}</h3>
				<p>{{ y[1] }}</p>
				<i>{{ y[2] }}</i>
			</div>
		{% endfor %}
		<a href="{{ url_for('logout') }}">Logout</a>
		<a href="{{ url_for('update') }}">Update</a>
		<a href="{{ url_for('delete') }}">Delete</a>
		<form action="{{ url_for('blog') }}" method="post" autocomplete="off">
			<h3> Write your blog </h3>
			<label>Title:
				<input type="text" name='title' required>
			</label>
			<label>Content:
				<input type="text" name='content'>
			</label>
			<label>User:
				<input type="text" name='user' required>
			</label>
			<h5>{{ msg }}</h5>
			<input type='submit' class="button" value="Submit">
		</form>
{% endblock %}	