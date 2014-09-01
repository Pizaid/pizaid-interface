$(function() {
  // http://bl.ocks.org/mbostock/4061961
  var
    width = 250,
    height = 250,
    radius = Math.min(width, height) / 2,
    data_arr = [
      { "name": "application", "score": 80, "color": "blue" },
      { "name": "video", "score": 100, "color": "purple" },
      { "name": "music", "score": 30, "color": "red" },
      { "name": "others", "score": 15, "color": "orange" },
    ];

  var arc = d3.svg.arc()
              .innerRadius(0)
              .outerRadius(radius - 10);

  var pie = d3.layout.pie()
              .sort(null)
              .value(function(d) { return d.score });

  var svg = d3.select("#disk-usage").append("svg")
              .attr("width", width)
              .attr("height", height)
              .append("g")
              .attr("transform", "translate(" + width/2 + "," + height/2 + ")");

  var g = svg.selectAll(".arc").data( pie(data_arr) ).enter()
          .append("g")
          .attr("class", "arc");

  g.append("path")
    .attr("d", arc)
    .attr("stroke", "white")
    .style("fill", function(d) { return d.data.color; });

  g.append("text")
    .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
    .attr("dy", ".35em")
    .attr("fill", "white")
    .style("text-anchor", "middle")
    .text(function(d) { return d.data.name } );
});
