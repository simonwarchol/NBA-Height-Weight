// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = 600 - margin.left - margin.right,
    height = 270 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%Y").parse;

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(5);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

// Define the line
var valueline1 = d3.svg.line()
    .x(function(d) { return x(d.Year); })
    .y(function(d) { return y(d.Weight); });
    
// Adds the svg canvas
var svg1 = d3.select("#weight")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("data/yearly.csv", function(error, data) {
    data.forEach(function(d) {
        d.Year = parseDate(d.Year);
        d.Weight = +d.Weight;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.Year; }));
    y.domain([ d3.min(data, function(d) { return d.Weight }) - 1, d3.max(data, function(d) { return d.Weight }) + 1]);
    //y.domain([0, d3.max(data, function(d) { return d.Height; })]);

    // Add the valueline path.
    svg1.append("path")
        .attr("class", "line")
        .attr("d", valueline1(data));

    // Add the X Axis
    svg1.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    
    // Add the Y Axis
    svg1.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    svg1.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x",0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Weight (lbs.)");

    
    //X Axis Label
    svg1.append("text") // text label for the x axis .attr("x", 265 )
            .attr("transform","translate(" + (width/2) + " ," + (height+margin.bottom) + ")")
            .style("text-anchor", "middle")
            .text("Year");

     svg1.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .text("NBA Average Weight");

});
