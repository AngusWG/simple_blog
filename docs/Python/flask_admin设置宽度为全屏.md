```    
{% extends 'admin/base.html' %}    
    
{% block head_tail %}    
    {{ super() }}    
    <link href="{{ url_for('static', filename='layout.css') }}" rel="stylesheet">    
    <style>    
        .container {    
            width: 100%;    
        }    
    </style>    
{% endblock %}    
```    
