$(function() {
  // http://bl.ocks.org/mbostock/4061961
  // https://gist.github.com/d3noob/5886992
  var
    margin = { top: 10, right: 10, bottom: 20, left: 70 },
    width = 400 - margin.left - margin.right,
    height = 60 - margin.top -  margin.bottom,
    data_arr = [
      {
        "title": "battery",
        "subtitle": "%",
        "ranges": [30, 60, 100],
        "measures": [42],
        "markers": [100],
      }
    ];

  var chart = d3.bullet()
                .width(width)
                .height(height);

  var svg = d3.select("#battery")
                .selectAll("svg")
                .data(data_arr)
              .enter().append("svg")
                .attr("class", "bullet")
                .attr("font-size", "10px")
                .attr("font-family", "sans-serif")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
              .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
                .call(chart);

  var title = svg.append("g")
        .style("text-anchor", "end")
        .attr("transform", "translate(-6," + height / 2 + ")");

  title.append("text")
    .attr("class", "title")
    .attr("font-size", "14px")
    .attr("font-weight", "bold")
    .text(function(d) { return d.title; });

  title.append("text")
    .attr("class", "subtitle")
    .attr("fill", "#999")
    .attr("dy", "1.5em")
    .text(function(d) { return d.subtitle; });
});
