<%inherit file="master.mako"/>

<%def name="head_tags()">
	<link type="text/css" rel="stylesheet/less" href="/static/css/main.less"/>
	<link type="text/css" rel="stylesheet" href="/static/css/jquery.slider.min.css"/>
  <script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script>
  <script type="text/javascript" src="/static/js/jquery.slider.min.js"></script>
  <script src="/static/js/flot/jquery.flot.js" type="text/javascript"></script>
  <script type="text/javascript" src="/static/js/main.js"></script>
</%def>

<div class="body-container">
  <div class="graph-container main-container">
    <div class="header-control-container">
      <div class="header-container">
        <h3 class="graph-header">Frequency response</h3>
      </div>
      <div class="slider-container">
        <input id="freq-slider" type="slider" name="freq" value="0.1;0.9"/>
        <div id="graph-overview"></div>
      </div>
    </div>

    <div id="freq-resp-graph" class="response-graph"></div>
  </div>

  <div class="graph-container secondary-container">
    <h3 class="graph-header">Step response</h3>
    <div id="step-resp-graph" class="response-graph"></div>
  </div>

  <div class="graph-container secondary-container">
    <h3 class="graph-header">Impulse response</h3>
    <div id="impulse-resp-graph" class="response-graph"></div>
  </div>
</div>
