<header class ="head">
	<div class="logo">
	{% if name == 'Administrator' %}
		<a href="{{ url_for('homeAd') }}"><img src="static/beta.svg" width="150" height="150"></a>
	{% elif name != 'Administrator' %}
		<a href="{{ url_for('home') }}"><img src="static/beta.svg" width="150" height="150"></a>
    {% endif %}
    </div>
    <div>
        <h1> VERKEFNI 8 </h1>
    </div>
</header>