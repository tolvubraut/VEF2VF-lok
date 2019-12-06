{% extends "base.html" %}
{% block title %} Verkefni7 {% endblock %}
{% block content %}
	<h1>Blog</h1>
		{% for y in blogs %}
			<div class="mminfo">
				<h3>{{ y[0] }}</h3>
				<p>{{ y[1] }}</p>
				<i>{{ y[2] }}</i>
			</div>
		{% endfor %}
		<form action="{{ url_for('update') }}" method="post" autocomplete="off">
			<h3> Update your blog </h3>
			<label>Title:
				<input type="text" name='title' required>
			</label>
			<label>New Content:
				<input type="text" name='content' required>
			</label>
			<h5>{{ msg }}</h5>
			<input type='submit' class="button" value="Submit">
			<a href="{{ url_for('blog') }}">Blog</a>
		</form>
{% endblock %}