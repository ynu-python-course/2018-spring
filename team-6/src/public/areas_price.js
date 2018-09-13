function aprice(res) {
  const data = res['fangs'];
  const city = res['city'];
  areas_price.hideLoading();
  let orientations = [];
  for (const d of data) {
    orientations = orientations.concat(d['orientations'])
  }
  orientations = orientations.sort().map(item => {
    const reItem = item.replace('（', '').replace('）', '');
    return reItem;
  });
  const orientations_data = [];
  for (let i = 0; i < orientations.length;) {
    let count = 0;
    for (let j = i; j < orientations.length; j++) {
      if (orientations[i] === orientations[j]) {
        count++;
      }
    }
    orientations_data.push({
      name: orientations[i],
      value: count
    });
    i += count;
  };
  orientations_data.sort(function (a, b) {
    return a.value - b.value;
  })
  const option = {
    backgroundColor: '#2c343c',

    title: {
      text: `${city}房屋朝向饼图`,
      left: 'center',
      top: 20,
      textStyle: {
        color: '#ccc'
      }
    },
    legend: {
      left: 0,
      top: '10%',
      orient: 'vertical',
      data: orientations_data.map(item => item.name),
      textStyle: {
        color: '#ccc'
      }
    },
    tooltip: {
      trigger: 'item',
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    series: [{
      type: 'pie',
      radius: '50%',
      center: ['50%', '50%'],
      data: orientations_data,
      roseType: 'radius',
      label: {
        normal: {
          textStyle: {
            color: 'rgba(255, 255, 255, 0.3)'
          }
        }
      },
      labelLine: {
        normal: {
          lineStyle: {
            color: 'rgba(255, 255, 255, 0.3)'
          },
          smooth: 0.2,
          length: 10,
          length2: 20
        }
      },
      itemStyle: {
        normal: {
          shadowBlur: 200,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      },

      animationType: 'scale',
      animationEasing: 'elasticOut',
      animationDelay: function (idx) {
        return Math.random() * 200;
      }
    }]
  };
  areas_price.setOption(option)
}