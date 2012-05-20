drawResponseOverviewGraph = function(data, targetElement) {
  var respData = [{'data': data}];
  var graphOpts = {
      series: {
        lines: { show: true, lineWidth: 1, fill: true},
        shadowSize: 0
       },
      xaxis: { ticks: []},
      yaxis: { ticks: [], autoscaleMargin: 0.1 },
      'grid': {'borderWidth': 0}
  };

  $.plot(targetElement, respData, graphOpts);
};

drawResponseGraph = function(data, targetElement, label) {
  var respData = [{
      'data': data,
      'label': label}];
  var graphOpts = {
      'lines': {'show': true},
      'grid': {'borderWidth': 0}};
  $.plot(targetElement, respData, graphOpts);
};

updateResponseGraphs = function(freq, step, impulse) {
  drawResponseGraph(freq, $('#freq-resp-graph'), 'Frequency response');
  drawResponseOverviewGraph(freq, $('#graph-overview'));
  drawResponseGraph(step, $('#step-resp-graph'), 'Step response');
  drawResponseGraph(impulse, $('#impulse-resp-graph'), 'Impulse response');
};

gatherResponseData = function(responseUrl, lowFreq, highFreq) {
  var freqRespKey = 'freq_response',
      stepRespKey = 'step_response',
      impulseRespKey = 'impulse_response';

  var requestArgs = {
    'low': lowFreq,
    'high': highFreq};

  $.getJSON(responseUrl, requestArgs, function(response) {
    // TODO(almarinescu): Validate response data - check for hash key.
    freqResponse = response[freqRespKey];
    stepResponse = response[stepRespKey];
    impulseResponse = response[impulseRespKey];

    updateResponseGraphs(freqResponse, stepResponse, impulseResponse);
  });
};

sliderChangeState = function (value) {
  var freqs = value.split(';');
  var lowFreq = freqs[0],
      highFreq = freqs[1];

  gatherResponseData('/response', lowFreq, highFreq);
};

initUiBehaviour = function () {
  // Attach behaviour to slider.
  $("#freq-slider").slider({
    from: 0.025, 
    to: 0.975, 
    step: 0.025, 
    smooth: true, 
    round: 3, 
    dimension: "&nbsp;hz", 
    skin: "round_plastic", 
    callback: sliderChangeState});
};

initApp = function() {
  sliderChangeState($('#freq-slider').slider().getValue());
}

$(document).ready(function () {
  initUiBehaviour();
  initApp();
});
