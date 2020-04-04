const url3 = "http://127.0.0.1:5000/emotions"

d3.json(url3).then(function(data){
    console.log(data)


    var anger = {
        x: data.dates,
        y: data.anger,
        type: 'line',
        name: "Anger"
      };

    var anticipation = {
        x: data.dates,
        y: data.anticipation,
        type: 'line',
        name: "Anticipation"
        };

    var disgust = {
        x: data.dates,
        y: data.disgust,
        type: 'line',
        name: "Disgust"
        };

    var fear = {
        x: data.dates,
        y: data.fear,
        type: 'line',
        name: "Fear"
        };
    var joy = {
        x: data.dates,
        y: data.joy,
        type: 'line',
        name: "Joy"
        };

    var negative = {
        x: data.dates,
        y: data.negative,
        type: 'line',
        name: "Negative"
        };

    var positive = {
        x: data.dates,
        y: data.positive,
        type: 'line',
        name: "Positive"
        };

    var sadness = {
        x: data.dates,
        y: data.sadness,
        type: 'line',
        name: "Sadness"
        };

    var surprise = {
        x: data.dates,
        y: data.surprise,
        type: 'line',
        name: "Surprise"
        };

    var trust = {
        x: data.dates,
        y: data.trust,
        type: 'line',
        name: "Trust"
        };


      var d = [anger,anticipation,disgust,fear,joy, negative, positive, sadness, surprise, trust];

      var layout = {
        title: 'Emotional Response Detected',
        width: 700,
        height: 500
    }
    Plotly.newPlot('bottom-middle', d, layout);



})