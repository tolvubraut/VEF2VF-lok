{% extends "base.html" %}
{% block title %} Verkefni7 {% endblock %}
{% block content %}
	<h1> Home Page </h1>
	<p> Hello {{ nafn }} </p>
	<table>
		<caption><h3>List of members</h3></caption>
		<tbody>
			<tr>
				<td><strong> User </strong></td>
				<td><strong> Name </strong></td>
			</tr>
		{% for x in users %}		
			<tr>
				<td>{{ x[0] }}</td>
				<td>{{ x[2] }}</td
			</tr>			
		{% endfor %}
		</tbody>
	</table>
	<a href="{{ url_for('logout') }}">Logout</a>
{% endblock %}	