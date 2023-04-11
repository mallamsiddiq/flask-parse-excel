
var mainbox = document.getElementById("mainbox")

var barColors = [
    "#b91d47",
    "#00aba9",
    "#2b5797",
    "#e8c3b9",
    "#1e7145",
    "#b93d47",
    "#02aba9",
    "#2b5797",
    "#e2c3b9",
    "#1e5145",
    "#10aba9",
    "#2b5757",
    "#e8c3b1",
    "#1e7148"
  ];

const title_text = "Years spent in Units by employess"

new Chart("myChart", {
  type: "bar",
  data: {
    labels: data_labels,
    datasets: [{
      backgroundColor: barColors,
      data: data_values
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: title_text + ' bar chart'
    }
  }
});

var xValues = data_labels;
var yValues = data_values;
// var barColors = barColors

new Chart("myChart2", {
  type: "doughnut",
  data: {
    labels: data_labels,
    datasets: [{
      backgroundColor: barColors,
      data: data_values
    }]
  },
  options: {
    title: {
      display: true,
      text: title_text + ' doughnut chart'
    }
  }
});
