$(function() {
  // http://www.h2.dion.ne.jp/~defghi/svgMemo/svgMemo_20.htm
  var
    width = 300,
    height = 300,
    data_arr = [
      {"name": "application", "score": 80},
      {"name": "video", "score": 100},
      {"name": "music", "score": 30},
      {"name": "others", "score": 15},
    ],
    color_arr = ["blue", "purple", "red", "orange"],
    get_sum = function(d) {return d.score},
    sum = d3.sum(data_arr, get_sum);

  var arc = d3.svg.arc()
              .startAngle(function(d) {return 0;})
              .endAngle(function(d) {return Math.PI * 2 * d.score/sum;})
              .outerRadius(function(d) {return 100;});

  var svg = d3.select("#harddisk")
              .append("svg")
              .attr("width", 300)
              .attr("height", 300);

  var g = svg.selectAll("path").data(data_arr).enter()
            .append("path")
              .attr("d", function(d,i) {return arc(d);})
              .attr("transform", function(d,i) {
                var sub_arr = (i == 0) ? [] : data_arr.slice(0,i);
                return "translate(" + width/2 + "," + height/2 + "), rotate(" + 360 * d3.sum(sub_arr, get_sum)/sum + ")";
              })
              .attr("stroke", "white")
              .attr("fill", function(d,i) {return color_arr[i % color_arr.length];})
  g.append("text")
    .attr("dy", ".35em")
    .style("text-anchor", "middle")
    .text(function(d) {return d.name});
});
